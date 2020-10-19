

class Anime:
    def __init__(self, title, synopsis, score, n_episodes, genres_list, ranked_top):
        self.title = title
        self.synopsis = synopsis
        self.score = score
        self.n_episodes = n_episodes
        self.genres_list = genres_list
        self.ranked_top = ranked_top
        self.reviews_list = []

    def add_reviews(self):
        # TODO: get reviews from scrapping
        pass
