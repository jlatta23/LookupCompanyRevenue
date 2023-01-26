# LookupCompanyRevenue.com Project Showcase
This is a side project website I built that amassed over 100,000 monthly page views, supported by ad revenue. The idea was to use publicly released PPP loan data combined with Burea of Labor Statistics (BLS) sector productivity data to estimate company revenues.

- [Background](#background)
- [Building the model](#building-the-model)
- [Acquiring Users](#acquiring-users)

# Background
There are over 12 million private companies in the US. Unlike public companies, which are required to post quarterly and annual reports, private companies are under no obligation to post any information related to their size. This makes it difficult to estimate the size of a private business. There are some tools out there that create estimates using all sorts of techniques but many of these are expensive B2B SaaS products.

The US Government instituted the Paycheck Protection Program (PPP) during the Coronavirus pandemic in 2020 to stave off massive layoffs when they forced small businesses to shut down. This program issued forgiveable loans accessible to essentially every small business in the US. The loan size was set based on the company's payroll size, with the idea to cover payroll expenses during the shutdown.

> Loan Size = 2.5 x Avg Monthly Payroll

The US Government released data on all of the companies that used the program, including their loan size and headcount. I realized I could create mathematical models and leverage this information to do research on many private companies. After weeks of Control-F searching the Excel files, I realized others would be interested in this content and decided to build a website.

# Building the model
I wanted to build revenue estimates of private businesses. PPP loan sizes could provide solid insights on a company's payroll and the BLS collects industry statistics on worker productivity (how much revenue is produced by each payroll dollar or employee).

Like most data science projects, gathering and cleaning the data was the bulk of the work. There was a lot of manual downloading of csv files from Government websites and Python scripting to aggregate and handle missing data.

A key observation for model accuracy involved figuring out which BLS industry productivity rate to use for each business. The BLS had statistics for many industries but not all of them. "Industry" is a hierarchical concept and is defined by the BLS as such:

![Naics](https://user-images.githubusercontent.com/90107864/214922510-6f9c2946-ae04-46a3-aec1-386379ac7f8f.png)

I matched businesses with the BLS NAICS code that was the closest "parent" of the listed business 6-digit NAICS code. The best case scenario is the BLS has 6-digit level NAICS productivity data, but they have a mixture of 2,3,4,5,6 digit stats. There were approximately 20% of companies that only matched he general 2-digit sector classification but the rest matched to at least the 3rd digit, meaning increased accuracy.

Multiplying the closest sector productivity (in $ terms) by the payroll gave an estimated revenue.


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
See if you can spot when I had a viral Reddit post about the website.
![ViralPost](https://user-images.githubusercontent.com/90107864/214936027-c67de758-863d-4ab2-a143-ec07c4867a7d.jpg)



