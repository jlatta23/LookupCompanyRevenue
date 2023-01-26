# LookupCompanyRevenue.com Project Showcase
This is a side project website I built that amassed over 100,000 monthly page views, supported by ad revenue. The idea was to use publicly released PPP loan data combined with Burea of Labor Statistics (BLS) sector productivity data to estimate company revenues.

- [Background](#background)
- [Building the model](#building-the-model)

# Background
There are over 12 million private companies in the US. Unlike public companies, which are required to post quarterly and annual reports, private companies are under no obligation to post any information related to their size. This makes it difficult to estimate the size of a private business. There are some tools out there that create estimates using all sorts of techniques but many of these are expensive B2B SaaS products.

The US Government instituted the Paycheck Protection Program (PPP) during the Coronavirus pandemic in 2020 to stave off massive layoffs when they forced small businesses to shut down. This program issued forgiveable loans accessible to essentially every small business in the US. The loan size was set based on the company's payroll size, with the idea to cover payroll expenses during the shutdown.

> Loan Size = 2.5 x Avg Monthly Payroll

The US Government released data on all of the companies that used the program, including their loan size and headcount. I realized I could create mathematical models and leverage this information to do research on many private companies. After weeks of Control-F searching the Excel files, I realized others would be interested in this content and decided to build a website.

# Building the model



