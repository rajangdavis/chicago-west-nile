# Project 4 Data Dictionary

## Weather:
### Heat
    Departure (in degrees) from 65 degree fahrenheit baseline
### Heat_roll_28
    Rolling mean of 'heat' column
### Cool
    Departure (in degrees) from 65 degree fahrenheit baseline
### PrecipTotal
    Amout of rainfall (in inches)
### PrecipTotal_roll
    Rolling average rainfall
### WetBulb
    Temperature recorded via wetbulb thermometer. Takes into account humidity and ambient temp. Similar to heat index.
### Tmin
    Minimum temperature for a given day (fahrenheit)
### Tmin
    Minimum temperature rolling mean
### Tmax
    Minimum temperature for a given day (fahrenheit)
### Tmax_roll
    Maximum temperature rolling mean
### Tavg
    Daily average temperature (fahrenheit)
### Depart
    Temperature departure from historical normal
### DewPoint
    The temperature at which water condensates. A factor in measuring relative humidity.
### DewPoint_roll
    Rolling mean of dew point column
### Sunrise
    Time of sunrise (CST). Calculated, not observed.
### Sunset
    Time of sunset (CST). Calculated, not observed.
### Depth
    Depth of snowfall (inches)
### Water1
    Level of snowmelt (in inches)
### SnowFall
    Amount of snowfall (inches)
### StnPressure
    Daily average atmospheric pressure (inches/HG)
### SeaLevel
    Daily average sea level (feet)
### ResultSpeed
    Resultant wind speed (vector sum of wind and direction)
### ResultSpeed_roll
    Rolling mean of resultant wind speed
### ResultDir
    Resultant wind direction (whole degress)
### AvgSpeed
    Daily average wind speed (MPH)


## Spatial/Temporal:
### Date
    Date in datetime format (YYYY-MM-DD)
### Street
    Street address of mosquito trap
### Trap
    Trap id
### Lat_int
    Latitude of trap rounded to nearest integer
### Long_int
    Longitude of trap rounded to nearest integer

## Epidemiological:
### Species
    Species of mosquito
