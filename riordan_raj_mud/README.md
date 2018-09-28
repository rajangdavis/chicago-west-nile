# Project 4 - West Nile Virus in the City of Chicago
by Mudassir Mayet, Rajan Davis and Riordan Tenney

## Our final project is located in the [`completed`](https://git.generalassemb.ly/mudassirmayet/rrm/tree/master/completed) directory.

## Data Science Problem/ Mission Statement
In this group project, we set out to determine which factors most heavily influenced West Nile Virus in mosquito populations in the city of Chicago.

Relying on datasets from a Kaggle competition and some outside research, we were able to determine which factors contributed to the likelihood of WNV appearing in a given trap. We hypothesized that there would be a strong correlation between the number of mosquitos in a given trap and the presence of WNV.  Moreover, we were able to were able to determine, with some degree of accuracy, whether or not the virus would be present. This information would be extremely valuable to the CDC as well as the Chicago Department of Environmental Health, which jointly manage the problem of WNV in the city.

## Process
We began by cleaning the three datasets on which we would base all of our models--weather data, mosquito spray data and our training data.  The weather data contained detailed weather information from the years 2007-2014; spray data contained spatial and temporal information from the years 2011 and 2013; training data contained spatial and temporal information from the even years of 2008-2014.

After reducing features and filling in missing values, we combined these dataframes in order to model. We each developed our initial models independently, with varying degrees of success. We then built on our strongest model, which used a RandomForestClassifier, by feature engineering rolling means of weather data and by using Principal Component Analysis. These are the scores of all of our models:

---------------------------------------------
| **Model**             | **ROC/AUC Score** |
|:---------------------:|:-----------------:|
| ExtraTreesClassifier  |  0.53299          |
| LogisticRegression    | 0.64892           |
| RandomForestClassifier| 0.71922           |
| RandomForest w/ PCA   | 0.71974           |
---------------------------------------------

## Conclusion
In our final model, these were the features with the greatest weights:
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Feature</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Species</td>
      <td>0.008183</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Street</td>
      <td>0.343346</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Trap</td>
      <td>0.389918</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Lat_int</td>
      <td>0.014845</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Long_int</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ResultSpeed_21</td>
      <td>0.044472</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PrecipTotal_15</td>
      <td>0.030347</td>
    </tr>
    <tr>
      <th>7</th>
      <td>DewPoint_16</td>
      <td>0.047255</td>
    </tr>
    <tr>
      <th>8</th>
      <td>AvgSpeed_19</td>
      <td>0.034524</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Heat_28</td>
      <td>0.030297</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Tmax_4</td>
      <td>0.029762</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Tmin_8</td>
      <td>0.027050</td>
    </tr>
  </tbody>
</table>

# Recommendations/Cost-Benefit Analysis
Chicago's department of Environmental Health and Safety, which oversees mosquito abatement, spent ~$1m attacking the problem of WNV in 2014, the last year that we have information on:

https://www.cityofchicago.org/content/dam/city/depts/obm/supp_info/2014%20Budget/2014Overview.pdf

In 2017, the budget of this department has grown to over $2 million.

https://www.cityofchicago.org/content/dam/city/depts/obm/supp_info/2017%20Budget/2017BudgetOverviewFinal.pdf

We think that this money would be better spent early in the mosquito season, rather than spraying insecticide after adult mosquito populations peak.

In fact, we want to rethink the spraying approach entirely. In 2013, for instance, WNV already appears in late June whereas spraying doesn't begin until July 17th, well after a sizable mosquito population was established in the city. For spraying to be at all effective, it must begin earlier in the season--we recommend the first week of August.

We've also noticed that each year, mosquito populations begin to appear at around the area of ORD--this may be due to a topographic feature of the landscape or some other factor, but in any case populations seem to "begin" at around this point and "spread" east to the areas immediately adjacent to Lake Michigan. Focusing our initial spraying at this location would make sense.

Looking at the mosquito population alone doesn't give us the best insight into the spread of WNV. We also need to take into account the sparrow population--this species of invasive bird is involved in a cyclical transmission of WNV to mosquitos and vice versa. Mitigating the sparrow population might reduce impact of WNV on human populations.

# Long-Term Goals

https://www.wired.com/story/heres-the-plan-to-end-malaria-with-crispr-edited-mosquitoes/

Given the recent advancements in CRISPR technologies, we feel that there is a strong case to be made for further research and development in this area. This is a great deal more expensive in the short term, (something along the lines of $100m instead of $1m) but would save money in the long run after implementation. We also expect the cost of these technologies to come down significantly in the coming years/decades.
