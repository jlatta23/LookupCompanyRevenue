
from pathlib import Path
import csv
#url = 'https://lookupcompanyrevenue.com/business/cotoia-electric-company/9534414/'
#url = 'https://lookupcompanyrevenue.com/business/keli-ellis-land-services-inc/10690088/'
url = 'https://lookupcompanyrevenue.com/browse/'

total_sitemaps = 115229
sitemaps_dir = Path('C:/WebDevelopment/businesslookup_research/data/sitemaps/') 
sitemap_path = sitemaps_dir / 'sitemap_browse.txt'
sitemaps = []
for i in range(0, total_sitemaps):
    sitemaps.append(url + str(i) + '/')

with open(sitemap_path, 'a+') as f_sitemap:
    for u in sitemaps:
        f_sitemap.write(u + '\n')