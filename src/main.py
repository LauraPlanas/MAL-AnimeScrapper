import pandas as pd
from time import sleep
from datetime import datetime
from top_anime_scrapper import TopAnimeScrapper
from anime_scrapper import AnimeScrapper


# Scrapping the Top N Anime subdomain URLs
n_anime = 500
top_an_sc = TopAnimeScrapper(n_anime)
subdomains_list = top_an_sc.get_top_subdomains_urls()

# Scrapping Anime information for each url
anime_list = []
for subdomain in subdomains_list:
    an_sc = AnimeScrapper(subdomain)
    anime_obj = an_sc.get_anime_data()
    anime_info = anime_obj.get_anime_info_list()
    anime_list.append(anime_info)
    sleep(1)  # Sleep 1 second to not overflow the web

# Creating a pandas df to save the data in CSV
df_col_names = ['ranking_position', 'title', 'score', 'n_episodes', 'start_aired_date', 'end_aired_date',
                'status', 'synopsis', 'genres', 'scrape_timestamp']
df = pd.DataFrame(anime_list, columns=df_col_names)

file_timestamp = datetime.now().date()

filename = "TopAnime_" + str(file_timestamp) + ".csv"
df.to_csv("../csv/" + filename, sep="|", index=False)

