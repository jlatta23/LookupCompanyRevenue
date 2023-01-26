from smallbusinessapp.models import BusinessData
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import time
from django.db import transaction, connection
import csv

class Command(BaseCommand):
    def handle(self, **options):
        start_ind = 0
        end_ind = 12000000
        read_interval = 200000
        file_name = Path('C:/WebDevelopment/businesslookup_research/data/' + 'BusinessDataTable.csv')
        # with connection.cursor() as cursor:
        for i in range(start_ind, end_ind, read_interval):
            print('Writing at index ' + str(i))
            cur_end = i + read_interval
            query_str = f'''
            SELECT * FROM smallbusinessapp_businessdata
    WHERE id >= {i} AND id <= {cur_end}
            '''
            businesses = BusinessData.objects.raw(query_str)
            with open(file_name, 'a', newline='') as f:
                writer = csv.writer(f)
                for ele in businesses:
                    business = [ele.business_name, ele.id, ele.zip_code, ele.naics_code
                    ]
                    writer.writerow(business)
            #cursor.execute(query_str)
                
            
            
            time.sleep(3)