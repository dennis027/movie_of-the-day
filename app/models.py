class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Genres:
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Trailer:
    def __init__(self,key):
        # self.id = id
        # self.name = name
        self.key = key