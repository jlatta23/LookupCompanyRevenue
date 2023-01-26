from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from smallbusinessapp.models import State
import time
from django.db import transaction, connection
import csv
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def handle(self, **options):
        sitemaps_dir = Path('C:/WebDevelopment/businesslookup_research/data/sitemaps/') 
        sitemap_path = sitemaps_dir / 'sitemap_browse_by_state.txt'
        business_per_page = 99
        for state in State.objects.all():
            total_pages = int(state.num_businesses / business_per_page)
            cur_state_browse_urls = []
            base_url = 'https://lookupcompanyrevenue.com/browse/'
            with open(sitemap_path, 'a+') as f_sitemap:
                for i in range(0, total_pages):
                    url = base_url + state.abbreviation + '/' + str(i) + '/'
                    cur_state_browse_urls.append(url)
                for url in cur_state_browse_urls:
                    f_sitemap.write(url + '\n')  
