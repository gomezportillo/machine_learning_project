#Machine learning techniques project

This repository is devoted to the project part of this subject. In this project, an accidents dataset from [Euskadi OpenData](http://opendata.euskadi.eus/w79-home/es/) will be set onto clusters by means of different algorithims.

* First milestone is a touchdown with the data format. It was asked to perform a parsing from the XML file downloaded from the website to a CSV file storing only the accidents befallen on a single province, in our case Gipuzkoa.
* Second milestone was aimed to plot the accidents by its latitude and longitude, cluster that data by means of the [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) algorithim trying to get an optiman [silhouette coefficient](https://en.wikipedia.org/wiki/Silhouette_(clustering))

<p align="center">
  <img src="Milestone2/out/figure_3.png?raw=true" alt="DBSCAN"/>
</p>
