from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from .models import BusinessData, State, StateIndustryRevenueAverages, ZipCodeIndustryRevenueAverages, StateIndustryEmployeesAverages, ZipCodeIndustryEmployeesAverages
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.generic.detail import DetailView
from django.contrib.postgres.search import *
from django.core.mail import send_mail
from django.template.defaultfilters import slugify
import psycopg2
from django.conf import settings

from .forms import SignUpForm
from .tokens import account_activation_token
from users.models import User

import logging
import re
from random import randrange

logger = logging.getLogger(__name__)

def test(request, test_id):
    print('\n\n\n\n\n\nTest hit!, testid = ' + str(test_id))
    return redirect('index')

# Create your views here.
def index(request):
    logger.info('Lookup view')
    user = request.user
    if user is not None and user.is_anonymous == False:
        logger.info('user= ' + str(user.email) + ', last login = ' + str(user.last_login))
        logger.info(user.is_confirmed)
    else:
        logger.info('no user logged in')
    query_str = '''
    SELECT * FROM smallbusinessapp_businessdata
    TABLESAMPLE SYSTEM_ROWS(30)
    '''
    business_examples = BusinessData.objects.raw(query_str)
    for b in business_examples:
        b.slug_name = slugify(b.business_name)
    states = State.objects.all().order_by('abbreviation')
    context = {'businesses':business_examples, 'my_states':states}
    return render(request, 'smallbusinessapp/stats.html', context)

def search_businesses(request):
    logger.info('search businesses\n')
    company_name = request.GET.get("companyName", None)
    revenue_range = request.GET.get("revenueRange", None)
    industry = request.GET.get("industry", None)
    zip_code = request.GET.get("zipCode", None)
    employee_range = request.GET.get("employeeRange", None)
    state = request.GET.get("state", None)
    start_index = int(request.GET.get("start_index", None))
    order_dir = request.GET['order_dir']
    order_by = request.GET['order_by']
    if order_dir == 'desc':
        order_str = '-' + order_by.split('-')[0]
    else:
        order_str = order_by.split('-')[0]
    results_multiple = 30
    start = start_index * results_multiple
    end = start_index * results_multiple + results_multiple

    rev_lower_bound = 0
    rev_upper_bound = 1000000000000
    if revenue_range == 'over':
        rev_lower_bound = 300000000
    elif '-' in revenue_range:
        r = revenue_range.split('-')
        rev_lower_bound = int(r[0])
        rev_upper_bound = int(r[1])
    elif revenue_range == 'below':
        rev_upper_bound = 1000000

    employee_lower_bound = 0
    employee_upper_bound = 10000000000
    if employee_range == 'over':
        employee_lower_bound = 300000000
    elif '-' in employee_range:
        r = employee_range.split('-')
        employee_lower_bound = int(r[0])
        employee_upper_bound = int(r[1])
    elif employee_range == 'below':
        employee_upper_bound = 1

    #instantiate postgresql ready variables        
    stripped_company_name = company_name.strip() #remove leading and trailing whitespace
    
    business_name_words = re.sub(' +', ' ', stripped_company_name).split(' ') #remove consecutive whitespaces
    business_str = business_name_words[0]
    if len(stripped_company_name) > 0:
        if '&' in business_str: #ampersand is somewhat common business name, breaks the ts_query, need to surround with double quote, cant wildcard a double quote term
            business_str = '"' + business_str + '"'
        else:
            if len(business_str) > 3: #only do wild card matching for sufficiently long words, "A* B*" queries take forever
                business_str = business_name_words[0] + ':*'
            else:
                business_str = business_name_words[0]
    if len(business_name_words) > 1:
        for word in business_name_words[1:]:
            if '&' in word:
                word = '"' + word + '"' #surround word with double quotes
                business_str += ' <-> ' + word
            else:
                if len(word) > 3:
                    business_str += ' <-> ' + word + ':*'
                else:
                    business_str += ' <-> ' + word
    
    stripped_industry = industry.strip()
    industry_str_words = re.sub(' +', ' ', stripped_industry).split(' ')
    industry_str = industry_str_words[0]
    if len(stripped_industry) > 0:
        industry_str = industry_str_words[0]
        if len(industry_str) > 4: #only do wild card matching for sufficiently long words, "A B" queries take forever
            industry_str += ':*'
    if len(industry_str_words) > 1:
        for word in industry_str_words[1:]:
            if len(word) > 4:
                industry_str += ' <-> ' + word + ':*'
            else:
                industry_str += ' <-> ' + word

    if False: #Free user or unsigned in user
        #Must have some sort of filter in the search
        #
        query_str = f'''SELECT * FROM smallbusinessapp_businessdata WHERE'''
        if business_str != '':
            query_str += f" ts_simple @@ to_tsquery('simple', '{business_str}') "
        if zip_code != '':
            if business_str != '':
                query_str += ' AND '
            query_str += f''' zip_code LIKE '{zip_code_str}' '''
        if state != 'Any':
            if zip_code != '' or business_str != '':
                query_str += ' AND '
            query_str += f''' state = '{state}' '''
        if business_str != '':
            query_str += f'''ORDER BY ts_rank(ts_simple, to_tsquery('simple', '{business_str}'))'''
        query_str += f' LIMIT {results_multiple} OFFSET {start}'
        businesses = BusinessData.objects.raw(query_str)
    else:
        #        SET statement_timeout TO 20s;
        #business_str = '"J&P:*" <-> PAPPAS:*'
        query_str = f'''
        SELECT * FROM smallbusinessapp_businessdata WHERE'''
        where_filter = False
        if business_str != '':
            query_str += " ts_simple @@ to_tsquery('simple', %(business_str)s) "
            where_filter = True
        if zip_code != '':
            if where_filter:
                query_str += ' AND '
            where_filter = True
            zip_code_int = int(zip_code)
            query_str += f''' zip_code_int = {zip_code_int} '''
        if state != 'Any':
            if where_filter:
                query_str += ' AND '
            where_filter = True
            query_str += f''' state = '{state}' '''
        if stripped_industry != '':
            if where_filter:
                query_str += ' AND '
            where_filter = True
            query_str += " ts_simple_industry @@ to_tsquery('simple', %(industry_str)s) "
        if revenue_range != 'Any':
            if where_filter:
                query_str += f" AND revenue_estimate >= {rev_lower_bound} AND revenue_estimate <= {rev_upper_bound}"
            else:
                where_filter = True
                query_str += f" revenue_estimate >= {rev_lower_bound} AND revenue_estimate <= {rev_upper_bound}"
        if employee_range != 'Any':
            if where_filter:
                query_str += f" AND num_employees >= {employee_lower_bound} AND num_employees <= {employee_upper_bound}"
            else:
                where_filter = True
                query_str += f" num_employees >= {employee_lower_bound} AND num_employees <= {employee_upper_bound}"
        


        if business_str != '':
            print('business_str = ' + business_str)
            query_str += '''ORDER BY ts_rank(ts_simple, to_tsquery('simple', %(business_str)s))'''
        elif stripped_industry != '':
            query_str += '''ORDER BY ts_rank(ts_simple_industry, to_tsquery('simple', %(industry_str)s))'''
        
        query_str += f' LIMIT {results_multiple} OFFSET {start}'

        if where_filter is False: #No filters applied
            query_str = f'''
    SELECT * FROM smallbusinessapp_businessdata
    TABLESAMPLE SYSTEM_ROWS({results_multiple})
    '''
        logger.info(query_str)
        businesses = BusinessData.objects.raw(query_str, {'business_str':business_str, 'industry_str':industry_str})
        for b in businesses:
            b.slug_name = slugify(b.business_name)
    num_businesses =1
    logger.info(businesses.query)
    states = State.objects.all().order_by('abbreviation')
    context = {'businesses':businesses, 'my_states':states}
    t = get_template('search_businesses.html')
    logger.info('right before response')
    return HttpResponse(t.render(context))

def pricing(request):
    print('pricing')
    return render(request, 'smallbusinessapp/pricing.html', {})

def faq(request):
    logger.info('FAQ visited')
    return render(request, 'smallbusinessapp/faq.html', {})

def terms_and_conditions(request):
    logger.info('Terms and Conditions visited')
    return render(request, 'smallbusinessapp/terms_and_conditions.html', {})

def privacy_policy(request):
    logger.info('Privacy policy visited')
    return render(request, 'smallbusinessapp/privacy_policy.html', {})

def calculate_random_matching_business_range(count, num_sample):
    if count > num_sample:
        start = randrange(count - num_sample)
    else:
        start = 0
    return start

def business_detail(request, slug_name, business_id):    
    try:
        business = BusinessData.objects.get(pk=business_id)
    except Exception as e:
        logger.info('Business not found exception: ' + str(e))
        return HttpResponse('Business not found.')
        

    logger.info('business detail view, business_name = ' + business.business_name)
    #similar_businesses_zip_code = BusinessData.objects.filter(zip_code_int=business.zip_code_int, naics_name=business.naics_name).order_by('?')[:5]
    
    try:
        num_samples = 10

        all_matching_businesses_state = BusinessData.objects.filter(state=business.state, naics_code=business.naics_code)
        num_matching_state = all_matching_businesses_state.count()
        start_ind = calculate_random_matching_business_range(num_matching_state, num_samples)
        similar_businesses_state = all_matching_businesses_state[start_ind:start_ind + num_samples]
        
        for b in similar_businesses_state:
            b.slug_name = slugify(b.business_name)

        state_ind_avg = StateIndustryRevenueAverages.objects.filter(state=business.state, naics_code=business.naics_code)

        logger.info('len state ind avg = ' + str(len(state_ind_avg)))
        if len(state_ind_avg) == 0:
            state_ind_rev_avg_num = 1
        else:
            state_ind_rev_avg_num = state_ind_avg[0].avg_revenue

        state_ind_avg_employees = StateIndustryEmployeesAverages.objects.filter(state=business.state, naics_code=business.naics_code)
        if len(state_ind_avg_employees) == 0:
            state_ind_avg_employees_num = 1
        else:
            state_ind_avg_employees_num = state_ind_avg_employees[0]


        all_matching_businesses_zip = BusinessData.objects.filter(zip_code=business.zip_code, naics_code=business.naics_code)
        num_matching_zip = all_matching_businesses_zip.count()
        start_ind_zip = calculate_random_matching_business_range(num_matching_zip, num_samples)
        similar_businesses_zip = all_matching_businesses_zip[start_ind_zip:start_ind_zip + num_samples]
        for b in similar_businesses_zip:
            b.slug_name = slugify(b.business_name)
        zip_ind_avg = ZipCodeIndustryRevenueAverages.objects.filter(zip_code=business.zip_code, naics_code=business.naics_code)
        logger.info('len zipcode ind avg = ' + str(len(zip_ind_avg)))
        if len(zip_ind_avg) == 0:
            zip_ind_rev_avg_num = 1
        else:
            zip_ind_rev_avg_num = zip_ind_avg[0].avg_revenue

        zip_ind_avg_employees = ZipCodeIndustryEmployeesAverages.objects.filter(zip_code=business.zip_code, naics_code=business.naics_code)
        print(len(zip_ind_avg_employees))
        if len(zip_ind_avg_employees) == 0:
            zip_ind_avg_employees_num = 1
            print('Len zip in zero')
        else:
            zip_ind_avg_employees_num = zip_ind_avg_employees[0].avg_employees

        all_matching_businesses_country = BusinessData.objects.filter(naics_code=business.naics_code)
        num_matching_country = 69 #all_matching_businesses_country.count()
        logger.info('after count matching industry country')
        start_ind_country = calculate_random_matching_business_range(num_matching_country, num_samples)
        similar_businesses_country = all_matching_businesses_country[start_ind_country:start_ind_country + num_samples]
        for b in similar_businesses_country:
            b.slug_name = slugify(b.business_name)

        if business.num_employees == 0:
            rev_per_employee = business.revenue_estimate
        else:
            rev_per_employee = business.revenue_estimate / business.num_employees
        states = State.objects.all().order_by('abbreviation')
        context = {
            'business':business, 
            'state_industry_businesses':similar_businesses_state,
            'state_industry_businesses_count': num_matching_state,
            'state_ind_rev_avg': state_ind_rev_avg_num,
            'zip_ind_rev_avg': zip_ind_rev_avg_num,
            'zip_industry_businesses': similar_businesses_zip,
            'zip_industry_businesses_count':num_matching_zip,
            'revenue_per_employees':rev_per_employee,
            'country_industry_businesses' : similar_businesses_country,
            'country_industry_businesses_count': num_matching_country,
            'percentile_industry': int(business.percentile_industry), 
            'state_ind_employees_avg': state_ind_avg_employees_num,
            'zip_ind_employees_avg': zip_ind_avg_employees_num,
            'my_states': states
        }
        logger.info('right before render')
        return render(request, 'smallbusinessapp/business_detail.html', context)
    except Exception as e:
        logger.info('Exception in the entire business detail view, exception = ' + str(e))
        return HttpResponse('Error retrieving business.')

def business_not_found(request, business_id):
    return HttpResponse('Busienss not found')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.is_active = True
            user.is_confirmed = False
            user.save()
            raw_password = form.cleaned_data.get('password1')
            email_url_safe = urlsafe_base64_encode(force_bytes(user.email))
            token = default_token_generator.make_token(user)
        
            message = f"Please confirm your email by clicking below:\n http://127.0.0.1:8000/activate/{email_url_safe}/{token}"
            send_mail('Subject here', 
            message,
            'smallbusinesslookup@gmail.com',
            [user.email])
 
            
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'smallbusinessapp/registration/signup.html', {'form': form})

def activate(request, email_encoded, token):
    try:
        email = force_text(urlsafe_base64_decode(email_encoded))
        print('Activate email = ' + str(email))
        user = User.objects.get(email=email)
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    check = default_token_generator.check_token(user, token)
    print('activation token check token = ' + str(check))
    print('user = ' + str(user))
    if user is not None and default_token_generator.check_token(user, token):
        print('lets activate')
        user.is_confirmed = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    # else:
    return HttpResponse('Activation link is invalid!')

def browse_overall(request, page):
    num_per_page = 100
    id_start = num_per_page * page
    id_end = num_per_page * page + num_per_page
    query_str = f'''
    SELECT * FROM smallbusinessapp_businessdata
    WHERE id > {id_start} AND id < {id_end}
    '''    
    print('before')
    businesses = BusinessData.objects.raw(query_str)
    print('after')
    for b in businesses:
        print(b.business_name)
        b.slug_name = slugify(b.business_name)
    print('\n\n\n\n\n we here\n\n\n\n')
    next_page = page+1
    prev_page = page-1
    is_last_page = False
    if next_page > int(11522900 / num_per_page):
        is_last_page = True
    context = {
        'businesses': businesses,
        'page': page,
        'next_page': next_page,
        'prev_page': prev_page,
        'is_last_page': is_last_page,
    }
    return render(request, 'smallbusinessapp/browse_overall.html', context)

def serve_sitemap(num):
    #with open('/static/')
    pass

def browse_by_state(request, state, page):
    num_per_page = 99
    offset = num_per_page * page
    query_str = f'''
    SELECT * FROM smallbusinessapp_businessdata
    WHERE state='{state}'
    ORDER BY business_name
    LIMIT {num_per_page}
    OFFSET {offset}
    '''    

    print('before')
    businesses = BusinessData.objects.raw(query_str)
    print('after')
    for b in businesses:
        print(b.business_name)
        b.slug_name = slugify(b.business_name)
    print('\n\n\n\n\n we here\n\n\n\n')
    next_page = page+1
    prev_page = page-1
    state = State.objects.get(abbreviation=state)
    is_last_page = False
    if next_page > state.num_businesses / num_per_page:
        is_last_page = True
    states = State.objects.all().order_by('abbreviation')
    context = {
        'businesses': businesses,
        'page': page,
        'next_page': next_page,
        'prev_page': prev_page,
        'is_last_page': is_last_page,
        'state': state,
        'my_states': states
    }
    context = {}
    return HttpResponse('Hi')
    # return render(request, 'smallbusinessapp/browse_by_state.html', context)

def propellarads_verify(request):
    return render(request, 'smallbusinessapp/c24ad4b95aeb5e3cc183d32c61b9a351.html')

def google_adsense(request):
    line = 'google.com, pub-4889187939045480, DIRECT, f08c47fec0942fa0'
    return HttpResponse(line)

class UserView(DetailView):
    template_name = 'smallbusinessapp/profile.html'

    def get_object(self):
        return self.request.user
