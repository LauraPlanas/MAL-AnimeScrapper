import re
import requests
from bs4 import BeautifulSoup


class TopAnimeScrapper:

    def __init__(self, n_anime):
        self.top_url = "https://myanimelist.net/topanime.php"
        self.n_anime = n_anime
        self.top_subdomains_urls = []

        self._scrape_top_anime()

    def _scrape_top_anime(self):
        # Pages are limited to show 50 anime
        pages_limit = range(0, self.n_anime, 50)

        count_anime = 0
        for limit in pages_limit:
            limit_url = "?limit=" + str(limit)

            # Get page content in HTML
            page = requests.get(self.top_url + limit_url)
            bs = BeautifulSoup(page.content, 'html.parser')

            table_rows = bs.find_all("tr", class_="ranking-list")

            for row in table_rows:
                row_href = row.find("a", class_="hoverinfo_trigger")['href']
                subdomain = re.sub(r'.+/anime', "", row_href)
                self.top_subdomains_urls.append(subdomain)
                count_anime += 1

                if count_anime >= self.n_anime:
                    break

    def get_top_subdomains_urls(self):
        return self.top_subdomains_urls



