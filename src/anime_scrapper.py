import re
import requests
from bs4 import BeautifulSoup


class AnimeScrapper:

    def __init__(self, subdomain):
        self.domain = "https://myanimelist.net/anime"
        self.subdomain = subdomain

        self.title = None
        self.synopsis = None
        self.score = 0.0
        self.n_episodes = 0

        self.scrape_anime()

    def scrape_title(self, bs):
        self.title = str(bs.find("h1", class_="title-name").get_text())

    def scrape_synopsis(self, bs):
        self.synopsis = str(bs.find("p", itemprop="description").get_text())

    def scrape_score(self, bs):
        self.score = float(bs.find("div", class_="score-label").get_text())

    def scrape_n_episodes(self, bs):
        episodes_span = bs.find("span", string="Episodes:")
        episodes_parent_text = str(episodes_span.parent.get_text())
        self.n_episodes = int(re.sub(r'\D', "", episodes_parent_text))

    def scrape_anime(self):
        print("Scraping anime from " + self.domain + self.subdomain)

        # Get page content in HTML
        page = requests.get(self.domain + self.subdomain)
        b_soup = BeautifulSoup(page.content, 'html.parser')

        # Get basic anime information
        self.scrape_title(b_soup)
        self.scrape_synopsis(b_soup)
        self.scrape_score(b_soup)
        self.scrape_n_episodes(b_soup)

    def get_anime_data(self):
        # TODO: Return information inside Anime object
        return self.title, self.synopsis, self.score, self.n_episodes


if __name__ == "__main__":

    an_s = AnimeScrapper("/5114/Fullmetal_Alchemist__Brotherhood")
    print(an_s.get_anime_data())
