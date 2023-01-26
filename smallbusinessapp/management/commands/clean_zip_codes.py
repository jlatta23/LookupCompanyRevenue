from smallbusinessapp.models import BusinessData
from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import time
from django.db import transaction, connection

class Command(BaseCommand):
    def handle(self, **options):
        start_ind = 6449550
        end_ind = 11800000
        write_interval = 250
        with connection.cursor() as cursor:
            for i in range(start_ind, end_ind, write_interval):
                print('Writing at index ' + str(i))
                cur_end = i + write_interval
                query_str = f'''
                UPDATE smallbusinessapp_businessdata
        SET zip_code = split_part(zip_code, '-', 1)
        WHERE id >= {i} AND id <= {cur_end}
                '''
                #BusinessData.objects.raw(query_str)
                #with connection.cursor() as cursor:
                cursor.execute(query_str)
                    
                
                
                time.sleep(3)