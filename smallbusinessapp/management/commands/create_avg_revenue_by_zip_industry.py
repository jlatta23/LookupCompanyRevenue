import csv
from smallbusinessapp.models import ZipCodeIndustryRevenueAverages
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import time

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_tool.settings')
class Command(BaseCommand):
    def handle(self, **options):
        data_path = Path("C:/WebDevelopment/businesslookup_research/data/avg_revenue_by_zip_and_industry.csv")
        start_ind = 0
        end_ind = 3200000
        cur_ind = 0
        num_cur_interval = 0
        write_interval = 20000
        in_mem_data = []
        ZipCodeIndustryRevenueAverages.objects.all().delete()
        with open(data_path, 'r') as f:            
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                if cur_ind >= start_ind and cur_ind < end_ind:
                    num_cur_interval +=1
                    if num_cur_interval > write_interval:
                        print('hit current interval, cur_ind = ' + str(cur_ind))
                        ZipCodeIndustryRevenueAverages.objects.bulk_create(in_mem_data)
                        print('finished bulk create')
                        time.sleep(0.65)
                        num_cur_interval = 0
                        in_mem_data = []
                    obj = ZipCodeIndustryRevenueAverages(
                        zip_code = row['BorrowerZip'],
                        naics_code = row['code'],
                        avg_revenue = self.try_convert_to_float(row['revenue_estimate'])
                    )
                    in_mem_data.append(obj)
                    if cur_ind % 1000 == 0:
                        print(cur_ind)
                cur_ind +=1 
        ZipCodeIndustryRevenueAverages.objects.bulk_create(in_mem_data)

    def try_convert_to_float(self, val):
        if val == '':
            return 0
        else:
            return round(float(val), 2)