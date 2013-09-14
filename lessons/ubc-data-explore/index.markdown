---
layout: lesson
root: ../..
title: Data Exploration with Python
---

##Planning Notes
<ul>
  <li>manually get hourly and daily YVR weather data CSV files from climate.weather.gc.ca - participant work in pairs to get different days and months so that we have a bunch of data to work with for git collaboration later</li>
  <li>intro NumPy and read data into arrays</li>
  <li>explore data with descriptive statistics</li>
  <li>intro Matplotlib and visualize data with plots</li>
</ul>


## Learning Goals
{% include ubc-data-explore/goals.markdown %}


The IPython notebooks for this lesson are in [data-explore.zip](data-explore.zip).
Please download that archive,
unzip it in your bootcamp repo,
then add and commit the files.

##First, We Need Data...

* Work in pairs
* Use your browser to go to [http://climate.weather.gc.ca/](http://climate.weather.gc.ca/) and work your way through to the "Hourly Data Report" for yesterday at the `VANCOUVER INTL A` station
* Download the August 2013 hourly data as a CSV file
* Use your shell skills to confirm that:
  * You really got a CSV file
  * It's for the `VANCOUVER INTL A` station
  * It contains hourly data for the whole month of August 2013
* Move or copy the CSV file into the `data-explore/` directory in your repo and commit it
* Back on the web page and use the "Nearby Stations with Data" link to get to the "Daily Data Report" for the `POINT ATKINSON` station
* Download a different year's daily data as a CSV file at the `POINT ATKINSON` station (We'll map out who gets which year on the whiteboard)
* Confirm that the file contains the data you expect, and commit it into your repo

Each member of each pair should end up with a hourly data report for YVR in August 2013 in their repo,
and a daily data report from Point Atkinson for a different year.


##Now for Exploration

Launch Ipython notebook in your `data-explore/` directory and create a new notebook.
We're going to interactively work through the following notebooks:

* [data-explore-0-numpy](http://nbviewer.ipython.org/url/douglatornell.github.io/2013-09-26-ubc/lessons/ubc-data-explore/data-explore-0-numpy.ipynb): an introduction to [NumPy][numpy]
* [data-explore-1-csv](http://nbviewer.ipython.org/url/douglatornell.github.io/2013-09-26-ubc/lessons/ubc-data-explore/data-explore-1-csv.ipynb): reading CSV data into [NumPy][numpy] arrays and manipulating it
* [data-explore-2-matplotlib](http://nbviewer.ipython.org/url/douglatornell.github.io/2013-09-26-ubc/lessons/ubc-data-explore/data-explore-2-matplotlib.ipynb): an introduction to [Matplotlib][matplotlib]

[numpy]: http://numpy.scipy.org/
[matplotlib]: http://matplotlib.org/


[Back to Topics](../../index.html#topics)
