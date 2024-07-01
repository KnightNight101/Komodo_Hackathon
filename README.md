# Komodo - Hackathon

## Project Spec 
Initially, this project is a 2 week project, with the possibility of another week depending on outcomes of the hackathon. The project is based on ‘best-effort’ - we do not expect you to commit to a specific number of hours, but we do hope you use the opportunity to show what you can do.

This is a remote-working project (apart from the 2 days at the hackathon itself). 
If you are unable to attend the hackathon, please let us know so we can prepare for the event appropriately. If you are able to attend, we will pay for travel fares.

## Project
We will be working towards an ‘energy flexibility calculator’ in the hackathon. The basic idea is to show how much carbon savings can be made using energy storage assets.

The first week (24th-28th March), will be about examining the data and preparing some simple jupyter notebooks (or similar) for us to be able to access and manipulate on the day. We would like you to have a look through the data that has been shared below, and share ideas, insights or interesting things you find - in particular around energy storage, carbon emissions and renewable energy.

The second week will consist of the hackathon Mon-Tues (if you can attend) and then round up and completing any work that has been started during those first two days. 

If there is a third week, it will be building on the work completed either on the backend calculations or in the data visualisations.
## Things to Think about

Some of the most common problems Tech Zero companies have told us about are:
- How do we find the carbon footprint of our company’s data storage?
- How do we know Carbon Offsets are legit, impactful, and well-managed?
- Lots of emissions data are behind paywalls! 
- Leadership doesn’t understand how to implement sustainability plans
- Employees don’t understand how they can help with sustainability plans

- Can we use market data (e.g. pricing) to understand when is the best time to flex?
- Can we work out the current carbon emission given the realtime generation mix?
- Can we historical data to understand the impact flexibility would have had? 
- What is the carbon footprint of using energy at peak times vs a different time of the day?
- What are the characteristics of energy storage assets (capacity, charging profiles, user expectations etc) that can be tweaked to provide flexibility? 
- etc.




 
# Data and API breakdown


## Octopus Energy Open API
### Links
[Octopus Energy Open API](https://octopus.energy/blog/agile-smart-home-diy/#AgileAPI)
[Guide to the Octopus Energy Open API - GUYLIPMAN](https://www.guylipman.com/octopus/api_guide.html)
[Generic API Tool](https://www.guylipman.com/octopus/generic.html)
## Breakdown
- Each customer has an account number, which will be of the form A-AAAA1111
- each each account will have one or more meter points, each with an mpan (meter point administration number). 
- If you are paid for the electricity you export (as opposed to being on a Feed-in Tariff), you will have a second mpan for your export. 
- Each mpan will generally be populated a meter, and each meter will have a meter serial number. 
- There may be multiple meters for a single mpan, and the same meter may populate multiple The same meter can apply to multiple mpans
- For gas, it works similarly, but instead of mpans there are mprns (meter point reference numbers) and you can't export. 
- Each mpan is in a region, and has a region code, which is a letter from A to P. You can lookup the region code from the first two digits of the mpan [in this table](https://www.wikiwand.com/en/Meter_Point_Administration_Number#Distributor_ID)
- Each mpan/mprn will be be subject to a single tariff code at a time (though you can change tariff codes over time). 
- Each tariff will have defined standing charges and usage charges, though these can change over time. 
- To identify the product code for a particular tariff, you can usually take off the first few letters of the tariff (E-1R-, E-2R- or G-1R) which indicate if it is electricity single register, electricity dual register (eg economy7) or gas single register, and the letter at the end (eg -A) which indicates the region code
- Electricity is typically measured in kwh (kilowatt hour), which is the amount of electricity you get if you use 1 kilowatt for an hour. 
- We typically quote the price of electricity in pence/kwh. Wholesale electricity is typcially measured in mwh (megawatt hour), and priced in £/mwh. £10/mwh is equivalent to 1p/kwh

