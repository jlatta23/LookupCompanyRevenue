import xml.etree.cElementTree as ET

sitemapindex = ET.Element("sitemapindex", mlns = "http://www.sitemaps.org/schemas/sitemap/0.9")

for i in range(1, 211):

    ET.SubElement(ET.SubElement(sitemapindex, "sitemap"), "loc").text = 'https://www.lookupcompanyrevenue.com/static/sitemap_' + str(i) + '.txt'

tree = ET.ElementTree(sitemapindex)
tree.write('sitemap_index.xml', encoding='UTF-8')