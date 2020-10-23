import re
from time import strptime
import datetime
import requests
from bs4 import BeautifulSoup

airing_dates_regex = re.compile(r'\s*(.{3})\s*(\d+),\s*(\d+)\s*to\s*(?:\?|(.{3})\s*(\d+),\s*(\d+))\s*')


class AnimeScrapper:

    def __init__(self, subdomain):
        self.domain = "https://myanimelist.net/anime"
        self.subdomain = subdomain

        self.title = None
        self.synopsis = None
        self.score = 0.0
        self.n_episodes = 0
        self.aired_date_start = 0
        self.aired_date_end = 0
        self.status = None
        self.genres_list = []

        self._scrape_anime()

    def _scrape_title(self, bs):
        self.title = str(bs.find("h1", class_="title-name").get_text())

    def _scrape_synopsis(self, bs):
        self.synopsis = str(bs.find("p", itemprop="description").get_text())

    def _scrape_score(self, bs):
        self.score = float(bs.find("div", class_="score-label").get_text())

    def _scrape_n_episodes(self, bs):
        episodes_span = bs.find("span", string="Episodes:")
        episodes_parent_text = str(episodes_span.parent.get_text())
        self.n_episodes = int(re.sub(r'\D', "", episodes_parent_text))

    def _scrape_aired_dates(self, bs):
        aired_span = bs.find("span", string="Aired:")
        aired_parent_text = str(aired_span.parent.get_text())
        split_dates = airing_dates_regex.search(aired_parent_text)

        # Getting groups from regex search
        month_start = split_dates.group(1)
        day_start = int(split_dates.group(2))
        year_start = int(split_dates.group(3))

        month_end = split_dates.group(4)
        day_end = int(split_dates.group(5))
        year_end = int(split_dates.group(6))

        month_start = strptime(month_start, '%b').tm_mon
        self.aired_date_start = datetime.date(year=year_start, month=month_start, day=day_start)

        if month_end is None: # if Anime is still Airing
            self.aired_date_end = None
        else:
            month_end = strptime(month_end, '%b').tm_mon
            self.aired_date_end = datetime.date(year=year_end, month=month_end, day=day_end)

    def _scrape_status(self, bs):
        status_span = bs.find("span", string="Status:")
        status_parent_text = str(status_span.parent.get_text())
        self.status = re.search(r'Status:\s+(.*?)\s*$', status_parent_text).group(1)

    def _scrape_genres_list(self, bs):
        genres_span = bs.find_all("span", itemprop="genre")
        for genre in genres_span:
            genre_text = str(genre.get_text())
            self.genres_list.append(genre_text)

    def _scrape_anime(self):
        print("Scraping anime from " + self.domain + self.subdomain)

        # Get page content in HTML
        page = requests.get(self.domain + self.subdomain)
        b_soup = BeautifulSoup(page.content, 'html.parser')

        # Get basic anime information
        self._scrape_title(b_soup)
        self._scrape_synopsis(b_soup)
        self._scrape_score(b_soup)
        self._scrape_n_episodes(b_soup)
        self._scrape_aired_dates(b_soup)
        self._scrape_status(b_soup)
        self._scrape_genres_list(b_soup)

    def get_anime_data(self):
        # TODO: Return information inside Anime object
        return self.title, self.synopsis, self.score, self.n_episodes, self.aired_date_start, self.aired_date_end, self.status, self.genres_list


if __name__ == "__main__":

    an_s = AnimeScrapper("/5114/Fullmetal_Alchemist__Brotherhood")
    print(an_s.get_anime_data())

    #bs = an_s._scrape_anime()





