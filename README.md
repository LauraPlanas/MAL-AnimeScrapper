# MAL Top Anime Scrapper
## Introduction
This project has been developed for an assignment on the subject "Tipologia i cicle de vida de les dades" from the Data Science Master's Degree on UOC (Open University of Catalonia). The goal is to apply web scrapping techniques with Python and to create a dataset. The extra information for the assignment can be seen in the <code>pdf</code> folder. 

The dataset extracted for this project contains information from the top 500 anime list on [MyAnimeList](https://myanimelist.net/). 

## Contributors
This project has been developed individually by Laura Planas Simón.

## Project structure
* <code>src/entities/Anime.py</code>: contains the class Anime, which is used to store the scrapped anime data in an object. It also contains a method to pretty print the object information.
* <code>src/anime_scrapper.py</code>: contains the class AnimeScrapper, that includes all the methods to scrap the information from an Anime given the URL. The fields extracted for each anime are ranking position, title, score, number of episodes, start and end airing date, emission status, synopsis, genres and timestamp. 
* <code>src/top_anime_scrapper.py</code>: contains the class TopAnimeScrapper, that includes the methods to scrape N animes from the top and return a list with all the URLs.
* <code>scr/main.py</code>: file that executes the program. It creates the necessary objects and stores the information in the CSV file. When executed, a CSV file with the top 500 anime information on that day will be stored in the <code>csv</code> folder.

## Dataset DOI
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4256843.svg)](https://doi.org/10.5281/zenodo.4256843)
