# Analysis of City Bike Data
The data are all individual CitiBike trips taken during September 2020. For plots that consider gender or age, rows that had no gender specified were excluded because they all had '1969' as the birth year ... this seems improbable.

## Map of Stations
The first sheet in the workbook is a map of all station locations in New York City, where station marker size is based on the number of trips originating from that station in September of 2020. We can see that stations in Manhattan see the most significant usage within the network because their markers are larger than markers elsewhere.

## Phenomena 1: Men tend to take more unique trips than women
The second sheet in this workbook shows the number of trips taken on CitiBikes by men (blue) and women (red) as a function of birth year. We can see that men have more distinct trips than women, but both curves follow a similar distribution.

However, we notice some usage differences when we look at the average age of riders by location, by gender. The map, "Median Age, female," shows the average birth year of female CitiBike users at each station. We can see that while some stations have slightly younger female users (areas in the Bronx, Bushwick), and some have older (Lower East Side, Carrol Gardens), we see that female riders are, on average, usually born in the late 80s or early 90s. On the other hand, male riders do not have as uniform a distribution across the city. In Brooklyn, Harlem and the Bronx, male riders tend to be born in the late 80s or early 90s, but in Manhattan, male riders are on average ten years older than their female counterparts.


## Phenomena 2: Rider Distance
Next, we look at the distance of each trip. Each trip's distance was calculated as the linear distance in meters from start station to end station. In the first sheet (Trip Distance by Birth Year), we see that trip distance as a function of rider age roughly follows the same distribution as the number of riders by rider age. This phenomenon makes intuitive sense for two reasons. First, the more riders of a given age, the more likely some of those riders are to take longer trips. Second, the older riders are, the shorter their trips may be. 

Now, let's see if there are weekly usage trends. Namely, do people ride further to commute or for leisure? If we look at the Maps "Median Trip Distance by Station - Weekend" and "Median Trip Distance by Station - Weekday," we see that on average through September, rides taken on Saturdays and Sundays were longer. Stations up and down the west side highway are more used on the weekends, stations around the southern tip of Central Park, and Brooklyn's Broadway.