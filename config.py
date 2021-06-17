import os


class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GENRES_URL ='https://api.themoviedb.org/3/genre/movie/list?api_key={}'
    GENRE_MOVIES_URL = 'https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres={}'


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
