from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import time
from django.db import transaction, connection
import csv
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def handle(self, **options):
        ind = 0
        write_interval = 49000
        num_maps = 1
        file_name = Path('C:/WebDevelopment/businesslookup_research/data/' + 'BusinessDataTable.csv')
        sitemaps_dir = Path('C:/WebDevelopment/businesslookup_research/data/sitemaps/') 
        i = 0
        with open(file_name, 'r', newline='') as f:
            csv_reader = csv.reader(f)
            sitemap_name = 'sitemap_' + str(num_maps) + '.txt'
            sitemap_path = sitemaps_dir / sitemap_name
            base_url = 'https://lookupcompanyrevenue.com/business/'
            in_mem_data = []
            for row in csv_reader:
                i+=1
                if ind % 500 == 0:
                    print(i)
                if ind > write_interval:     
                    print('writing to sitemap file in 1 go')
                    with open(sitemap_path, 'a+') as f_sitemap:
                        for ele in in_mem_data:
                            f_sitemap.write(ele + '\n')      
                    ind = 0
                    num_maps +=1
                    sitemap_name = 'sitemap_' + str(num_maps) + '.txt'
                    sitemap_path = sitemaps_dir / sitemap_name
                    in_mem_data = []
                    
                slug = slugify(row[0])
                business_id = row[1]
                url = base_url + slug + '/' + business_id + '/'
                in_mem_data.append(url)
                # 'https://lookupcompanyrevenue.com/business/cross-rhoades-inc/1602350/'

                ind +=1
            
            
