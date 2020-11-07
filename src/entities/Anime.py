
class Anime:
    def __init__(self, ranking_position, title, synopsis, score, n_episodes, aired_date_start, aired_date_end, status,
                 genres_list, timestamp):
        self.ranking_position = ranking_position
        self.title = title
        self.synopsis = synopsis
        self.score = score
        self.n_episodes = n_episodes
        self.aired_date_start = aired_date_start
        self.aired_date_end = aired_date_end
        self.status = status
        self.genres_list = genres_list
        self.timestamp = timestamp

    def pretty_print(self):
        print("RANKING POSITION: " + str(self.ranking_position))
        print("TITLE: " + self.title)
        print("SCORE: " + str(self.score))
        print("SYNOPSIS: " + self.synopsis)

        print("NUM OF EPISODES: " + str(self.n_episodes))
        print("START AIRED DATE: " + str(self.aired_date_start))
        print("END AIRED DATE: " + str(self.aired_date_end))
        print("STATUS: " + self.status)
        print("GENRES: " + str(self.genres_list))

    def get_anime_info_list(self):
        anime_data = [self.ranking_position,
                      self.title,
                      self.score,
                      self.n_episodes,
                      self.aired_date_start,
                      self.aired_date_end,
                      self.status,
                      self.synopsis,
                      self.genres_list,
                      self.timestamp
                      ]

        return anime_data
