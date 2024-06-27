from imdb import Cinemagoer


def search_movie(title):
    ia = Cinemagoer()
    movies = ia.search_movie(title)
    if movies:
        return movies[0]
    else:
        return None


def get_movie_details(movie):
    ia = Cinemagoer()
    movie_id = movie.movieID
    movie = ia.get_movie(movie_id)
    details = {
        'title': movie['title'],
        'year': movie['year'],
        'genres': movie['genres'],
        'directors': [d['name'] for d in movie['directors']],
        'cast': [a['name'] for a in movie['cast'][:10]],  # First 10 cast members
        'plot': movie['plot'][0] if 'plot' in movie else 'No plot available'
    }
    return details

