import csv
from smallbusinessapp.models import BusinessData
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import time

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business_tool.settings')
class Command(BaseCommand):
    def handle(self, **options):
        data_path = Path("C:/WebDevelopment/businesslookup_research/data/business_data_percentile.csv")
        start_ind = 9700000
        end_ind = 10500000
        cur_ind = 0

        with open(data_path, 'r') as f:            
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                if cur_ind >= start_ind and cur_ind < end_ind:

                    BusinessData.objects.filter(business_name=row['BorrowerName'], zip_code=row['BorrowerZip'],
                        naics_code = row['code']
                    ).update(percentile_industry=round(self.try_convert_to_float(row['percentile']), 0))
                    
                    if cur_ind % 100 == 0:
                        print(cur_ind)
                        print(row['BorrowerName'] + ' and ' + row['BorrowerZip'])
                        #time.sleep(1)
                cur_ind +=1 

    def try_convert_to_float(self, val):
        if val == '':
            return 0
        else:
            return round(float(val), 2)