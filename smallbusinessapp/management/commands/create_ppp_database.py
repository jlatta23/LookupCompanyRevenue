import csv
from smallbusinessapp.models import BusinessData
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import time

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_tool.settings')
class Command(BaseCommand):
    def handle(self, **options):
        in_mem_data = []
        start_ind = 0
        end_ind = 1000000000
        cur_ind = 0
        num_cur_interval = 0
        write_interval = 200
        file_name = 'DjangoModelBusinessData_up_to_150_12.csv' #BusinessData.csv
        #BusinessData.objects.all().delete()
        with open(Path('C:/WebDevelopment/smallbusinesslookup/smallbusinessapp/data/' + file_name), 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                if cur_ind >= start_ind and cur_ind < end_ind:
                    num_cur_interval +=1
                    if num_cur_interval > write_interval:
                        print('hit current interval, cur_ind = ' + str(cur_ind))
                        BusinessData.objects.bulk_create(in_mem_data)
                        print('finished bulk create')
                        time.sleep(0.65)
                        num_cur_interval = 0
                        in_mem_data = []
                    obj = BusinessData(business_name = row["BorrowerName"],
                    address = row['BorrowerAddress'],
                    city=row['BorrowerCity'],
                    state=row['BorrowerState'],
                    zip_code = row['BorrowerZip'],
                    naics_code = row['NAICSCode'],
                    naics_name = row['industry_name'],
                    revenue_estimate = self.try_convert_to_float(row['revenue_estimate']),
                    business_type = row['BusinessType'],
                    loan_amount = self.try_convert_to_float(row['InitialApprovalAmount']),
                    owner_race = row['Race'],
                    owner_ethnicity = row['Ethnicity'],
                    num_employees = self.try_convert_to_int(row['JobsReported']),
                    payroll_proceed = self.try_convert_to_float(row['PAYROLL_PROCEED']),
                    payroll_annual = self.try_convert_to_float(row['payroll_annual']),
                    utilities_proceed = self.try_convert_to_float(row['UTILITIES_PROCEED']),
                    mortgage_proceed = self.try_convert_to_float(row['MORTGAGE_INTEREST_PROCEED']),
                    rent_proceed = self.try_convert_to_float(row['RENT_PROCEED']),
                    health_care_proceed = self.try_convert_to_float(row['HEALTH_CARE_PROCEED']),
                    debt_interest_proceed = self.try_convert_to_float(row['DEBT_INTEREST_PROCEED']),
                    servicing_lender_name = row['ServicingLenderName'],
                    origination_lender_name = row['OriginatingLender'],
                    business_age = row['BusinessAgeDescription'],
                    revenue_confidence = row['revenue_confidence'],
                    approximate_naics_code = row['naics_code_approximate'],
                    revenue_to_payroll = self.try_convert_to_float(row['revenue_to_payroll'])
                    )
                    in_mem_data.append(obj)
                    if cur_ind % 500 == 0:
                        print(cur_ind)
                cur_ind+=1
                
        BusinessData.objects.bulk_create(in_mem_data)

    def try_convert_to_float(self, val):
        if val == '':
            return 0
        else:
            return round(float(val), 2)

    def try_convert_to_int(self, val):
        if val =='':
            return 0
        else:
            return int(float(val))
