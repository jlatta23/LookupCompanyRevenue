
from pathlib import Path
import csv
#url = 'https://lookupcompanyrevenue.com/business/cotoia-electric-company/9534414/'
#url = 'https://lookupcompanyrevenue.com/business/keli-ellis-land-services-inc/10690088/'
url = 'https://lookupcompanyrevenue.com/business//7103844/'
ind = 0
write_interval = 49000
num_maps = 1
sitemaps_dir = Path('C:/WebDevelopment/businesslookup_research/data/sitemaps/') 
i = 0

for i in range(1, 211):
    sitemap_name = 'sitemap_' + str(i) + '.txt'
    sitemap_path = sitemaps_dir / sitemap_name
    with open(sitemap_path, 'r') as f_sitemap:
        csv_reader = csv.reader(f_sitemap)
        for row in csv_reader:
            if row[0] == url:
                print('Found it')
                print(sitemap_name)

