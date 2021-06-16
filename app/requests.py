import urllib.request
import json
from .models import Movie

# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']


def get_movies(category):
    get_movies_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id, title, overview,
                                 poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview,
                                 poster, vote_average, vote_count)

    return movie_object

def watch_trailer(id):
    watch_movie_trailer = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US'.format(
        id, api_key)


    response = urllib.request.urlopen(watch_movie_trailer)
    content = response.read()
    data = json.loads(content.decode('utf-8'))
    # with urllib.request.urlopen(watch_movie_trailer) as url:
    #     search_trailer_data = url.read()
    #     search_trailer_response = json.loads(search_trailer_data)

        # search_trailer_results = None

        # if search_trailer_response['results']:
        #     search_trailer_list = search_trailer_response['results']
        #     search_trailer_results = process_results(search_trailer_list)

        # print(search_trailer_results) 
    return data
