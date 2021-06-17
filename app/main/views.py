from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_genre_movies, get_genres, get_movies, get_movie, watch_trailer

@main.route('/')
def index():

    genres = get_genres()
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('main.search', movie_name=search_movie))
    else:
        return render_template('index.html', title=title, popular=popular_movies, upcoming=upcoming_movie, now_showing=now_showing_movie, genres= genres)

@main.route('/trailer/<int:id>')
def trailer(id):
    trailer = watch_trailer(id)
    trailer_url = 'https://www.youtube.com/watch?v='+trailer
    return redirect(trailer_url)
    
@main.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title=title, movie=movie)

@main.route('/genres/<int:id>/movies')
def genre_movies(id):
    movies = get_genre_movies(id)
    return render_template('genre.html',movies = movies)