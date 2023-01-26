from django.contrib.postgres import indexes
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.indexes import GinIndex, HashIndex
from django.contrib.postgres.search import SearchVectorField


class BusinessData(models.Model):
    business_name = models.TextField()
    address = models.TextField()
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    zip_code = models.TextField(null=True)
    zip_code_int = models.IntegerField(null=True)
    naics_code = models.TextField(null=True)
    naics_name = models.TextField(null=True)
    revenue_estimate = models.FloatField(null=False)    

    business_type = models.TextField(null=True)
    loan_amount = models.FloatField(default=0)
    owner_race = models.TextField(null=True)
    owner_ethnicity = models.TextField(null=True)
    num_employees = models.IntegerField(default=0)
    payroll_proceed = models.FloatField(null=True)
    payroll_annual = models.FloatField(null=True)
    utilities_proceed = models.FloatField(default=0)
    mortgage_proceed = models.FloatField(default=0)
    rent_proceed = models.FloatField(default=0)
    health_care_proceed = models.FloatField(default=0)
    debt_interest_proceed = models.FloatField(default=0)
    servicing_lender_name = models.TextField(null=True)
    origination_lender_name = models.TextField(null=True)
    business_age = models.TextField(null=True)
    revenue_confidence = models.TextField(default='high') #high, low

    approximate_naics_code = models.TextField(null=False)
    revenue_to_payroll = models.FloatField(null=False)

    percentile_industry = models.FloatField(default=0)
    
    revenue_range = models.TextField(null=True)
    employee_range = models.TextField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['business_name',]),
            models.Index(fields=['business_name', 'naics_name','revenue_estimate', 'num_employees', 'naics_name', 'address', 'state',]),
            models.Index(fields=['revenue_estimate',]),
            models.Index(fields=['num_employees',]),
            models.Index(fields=['naics_name',]),
            models.Index(fields=['address',]),
            models.Index(fields=['state',]),
            models.Index(fields=['zip_code',]),
            models.Index(fields=['zip_code_int',]),
            models.Index(fields=['state','naics_code']),
            models.Index(fields=['zip_code','naics_code']),
            HashIndex(fields=['naics_code'])
        ]

class State(models.Model):
    name = models.TextField()
    abbreviation = models.TextField()
    num_businesses = models.IntegerField(default=0)

    change = models.TextField()

class StateIndustryRevenueAverages(models.Model):
    state = models.TextField(null=False)
    naics_code = models.TextField(null=False)
    avg_revenue = models.TextField(null=False)

    class Meta:
        indexes = [
            models.Index(fields=['naics_code', 'state']),
            models.Index(fields=['state']),
            models.Index(fields=['naics_code'])
            ]

class ZipCodeIndustryRevenueAverages(models.Model):
    zip_code = models.TextField(null=False)
    naics_code = models.TextField(null=False)
    avg_revenue = models.TextField(null=False)    

    class Meta:
        indexes = [
            models.Index(fields=['naics_code', 'zip_code']),
            models.Index(fields=['zip_code']),
            models.Index(fields=['naics_code'])
        ]    

class StateIndustryEmployeesAverages(models.Model):
    state = models.TextField(null=False)
    naics_code = models.TextField(null=False)
    avg_employees = models.FloatField(null=False)

    class Meta:
        indexes = [
            models.Index(fields=['naics_code', 'state']),
            models.Index(fields=['state']),
            models.Index(fields=['naics_code'])       
        ] 

class ZipCodeIndustryEmployeesAverages(models.Model):
    zip_code = models.TextField(null=False)
    naics_code = models.TextField(null=False)
    avg_employees = models.FloatField(null=False)    

    class Meta:
        indexes = [
            models.Index(fields=['naics_code', 'zip_code']),
            models.Index(fields=['zip_code']),
            models.Index(fields=['naics_code'])        
        ]