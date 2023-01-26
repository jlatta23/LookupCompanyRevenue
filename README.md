# LookupCompanyRevenue.com Project Showcase
This is a side project website I built that amassed over **120,000 monthly page views**, supported by ad revenue. The idea was to use publicly released PPP loan data combined with Burea of Labor Statistics (BLS) sector productivity data to provide company revenue estimates and headcount.

- [Background](#background)
- [Building the model](#building-the-model)
- [Acquiring Users](#acquiring-users)
  - [Viral Social Post](#viral-social-post)

# Background
There are over 12 million private companies in the US. Unlike public companies, which are required to post quarterly and annual reports, private companies are under no obligation to post any information. This makes it difficult to estimate the size of a private business. There are some tools out there that create estimates using all sorts of techniques but many of these are expensive B2B SaaS products.

The US Government instituted the Paycheck Protection Program (PPP) during the Coronavirus pandemic in 2020 to stave off massive layoffs when they forced small businesses to shut down. This program issued forgiveable loans accessible to essentially every small business in the US. The loan size was set based on the company's payroll size, with the idea to cover payroll expenses during the shutdown.

> Loan Size = 2.5 x Avg Monthly Payroll

The US Government released data on all of the companies that used the program, including their loan size and headcount. I realized I could create mathematical models and leverage this information to do research on many private companies. After weeks of Control-F searching the Excel files, I realized others would be interested in this content and decided to build a website.

# Building the model
I wanted to build revenue estimates of private businesses. PPP loan sizes could provide solid insights on a company's payroll and the BLS collects industry statistics about output, labor compensation, capital investment, etc. My goal was to calculate an accurate the ratio of a company's revenue to payroll costs based on BLS datasets. Since I could use the PPP data to estimate a company's payroll cost, I could multiply this to get the revenue estimate.

Like most data science projects, gathering and cleaning the data was the bulk of the work. There was a lot of manual downloading of csv files from Government websites and Python scripting to aggregate and handle missing data. Here's an example of some cleaned but still in process data:
![DataSnapshot](https://user-images.githubusercontent.com/90107864/214967855-43c1a501-31b2-4727-8afb-6e7cb209484c.jpg)

My goal was to divide the value of production (revenue) by labor compensation. Some industries are heavily reliant on worker productivity (think accounting firms, lawyers, consultants) while others are heavily reliant on capital productivity (think mining, airlines, oil & gas, anything that requires massive equipment investments). Here's the distribution of revenue to payroll ratios by sector for a subset of 650,000 small businesses:

![RevenueToPayroll](https://user-images.githubusercontent.com/90107864/214968611-35d8a6cc-a5ae-4661-a798-23d660d77e3b.jpg)

As you can see, most businesses have a revenue/payroll of between 1 and 4. While the long tail ones probably provide the least accurate revenue estimates, they are also significantly less occuring.


A key observation for model accuracy involved figuring out which BLS industry productivity rate to use for each business. The BLS had statistics for many industries but not all of them. "Industry" is a hierarchical concept and is defined by the BLS as such:

![Naics](https://user-images.githubusercontent.com/90107864/214922510-6f9c2946-ae04-46a3-aec1-386379ac7f8f.png)

BLS productivity metrics were available for an assortment of 2,3,4,5,6-digit codes. I matched businesses by find which available NAICS code was the closest "parent" of the provided business 6-digit NAICS code. Over 80% of businesses matched productivity data to the 3rd digit, implying solid accuracy. In the example above the difference between matching 2-3-4 digits is "Construction" vs "Construction of Buildings" vs "Residential Building Construction". Obviously different types of construction will have vastly different worker productivity rates. 

Multiplying the closest sector productivity (in $ terms) by the payroll gave an estimated revenue. Here's the distribution of the average estimated revenue of sectors. Some industries have high average revenues while the vast majority make less than $10,000,000.

![AvgRevSectors](https://user-images.githubusercontent.com/90107864/214973272-37ea57bd-a238-48bf-a08d-f5b095816da1.jpg)




# Acquiring Users
I hypothesized most users would come to LookupCompanyRevenue.com from long-tail search keywords, eg. "Bob's Coffee Shop revenue". 

My SEO Strategy:
- Pick a domain that matched the search terms I wanted to rank for (lookupcompanyrevenue.com)
- Make the URLs for each business page include the business name such as below:
![ImpressionsAndClicks](https://user-images.githubusercontent.com/90107864/214935376-9b5d83a0-21da-491a-a77a-f0b7767e06d6.jpg)

- Make sure each business's page inlcuded enough text (roughly 500 words) to increase the chances Google indexes it
- Submit sitemaps for each of the 12,000,000 business URLs
- Have links and graphs of similar businesses to increase engagement by users clicking on multiple pages

## Viral Social Post
Once I had the site built and tested, I decided to go find some users. I posted on a Reddit forum to let people know of my new creation.

See if you can spot when I had a viral Reddit post about the website.
![ViralPost](https://user-images.githubusercontent.com/90107864/214936027-c67de758-863d-4ab2-a143-ec07c4867a7d.jpg)

I went from having no users to to 2,5000 the day of posting. As you can see, usage sharply decreased shortly after but since my post was one of the top posts of the subreddit, I continued to have between 30-50 daily users. 

## SEO
I knew I needed to have a fully fuctional SEO funnel for this to scale. I worked hard to make sure the 12,000,000 pages were all set up correctly and that my Django + Postgresql setup was solid enough to not throw errors when Google was crawling. Because my site was so new, Google would only crawl a couple 100 pages per week. 

It took a lot of experimenting, submitting massive sitemaps, and building domain authority to get Google to start indexing my pages in any decent quantity. My hard work slowly started to pay off:

![SEO](https://user-images.githubusercontent.com/90107864/214975247-8b898540-4c37-4e22-83ab-5f05c936f339.jpg)

This increase of users can be directly correlated with Google increasingly indexing my website. Here's the graph of clicks from Google searches:

![SEO_SearchConsole](https://user-images.githubusercontent.com/90107864/214975550-856bae04-337c-4c3c-b899-e56327f79ec5.jpg)

There isn't that initial spike like in the user graph above, since that spike came from Reddit users clicking on the link rather than Google searches.






