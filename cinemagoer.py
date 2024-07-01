from imdb import Cinemagoer


def search_movie(title):
    ia = Cinemagoer()
    movies = ia.search_movie(title)
    if movies:
        return movies[0]
    else:
        return None


def get_movie_id(title):
    movie = search_movie(title)
    if movie:
        return movie.movieID
    else:
        return None


def is_horror_movie(title):
    ia = Cinemagoer()
    movie_id = get_movie_id(title)
    movie = ia.get_movie(movie_id)
    genres = movie.get('genres', [])
    return 'Horror' in genres


def get_movie_details(movie):
    ia = Cinemagoer()
    movie_id = movie.movieID
    movie = ia.get_movie(movie_id)
    details = {
        'title': movie['title'],
        'year': movie['year'],
        'genres': movie['genres'],
        'directors': [d['name'] for d in movie['directors']],
        # First 10 cast members
        'cast': [a['name'] for a in movie['cast'][:10]],
        'plot': movie['plot'][0] if 'plot' in movie else 'No plot available'
    }
    return details
