# Pharmaceutical Sales Prediction

# Business Overview

The finance team at Rossmann Pharmaceuticals wants to **forecast sales** in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales. 
The data team identified factors such as **promotions, competition, school and state holidays, seasonality, and locality** as necessary for predicting the sales across the various stores.
# Objective
Our job is to build and serve an end-to-end product that delivers this prediction to analysts in the finance team.

# Field Description

This is a brief description of what data columns represent:

* Id : an Id that represents a (Store, Date) duple within the test set  <br />
* Store : a unique Id for each store  <br />
* Sales : the turnover for any given day (this is what you are predicting)  <br />
* Customers : the number of customers on a given day  <br />
* Open : an indicator for whether the store was open: 0 = closed, 1 = open <br />
* StateHoliday : indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None <br />
* SchoolHoliday : indicates if the (Store, Date) was affected by the closure of public schools <br />
* StoreType : differentiates between 4 different store models: a, b, c, d <br />
* Assortment : describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here <br />
* CompetitionDistance : distance in meters to the nearest competitor store <br />
* CompetitionOpenSince[Month/Year] : gives the approximate year and month of the time the nearest competitor was opened <br />
* Promo : indicates whether a store is running a promo on that day <br />
* Promo2 : Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating <br />
* Promo2Since[Year/Week] : describes the year and calendar week when the store started participating in Promo2 <br />
* PromoInterval : describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store <br />
