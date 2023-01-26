from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_businesses, name='search'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/',  login_required(UserView.as_view()), name='profile'),
    path('activate/<str:email_encoded>/<str:token>',  views.activate, name='activate'),
    path('terms/', views.terms_and_conditions, name='terms'),
    path('privacy/', views.privacy_policy, name='privacy'),
    path('test/<str:test_id>', views.test, name='test'),
    path('business/<slug:slug_name>/<int:business_id>/', views.business_detail, name='business_detail'),
    path('c24ad4b95aeb5e3cc183d32c61b9a351.html', views.propellarads_verify),
    path('ads.txt', google_adsense, name='adsense'),
    path('business//<int:business_id>/', views.business_not_found, name='business_not_found'),
    # path('browse/<str:state>/<int:page>/', views.browse_by_state, name='browse'),
    path('browse/<int:page>/', views.browse_overall, name='browse')
]