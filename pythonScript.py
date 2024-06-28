import sqlite3
from datetime import datetime
import APIClient
import SEOapi


conn = sqlite3.connect('user_reviews.db')
c = conn.cursor()

try:
    with open('Database.sql', 'r') as f:
        c.executescript(f.read())
    conn.commit()
except sqlite3.OperationalError:
    pass


def make_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email: ")
    signup_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        c.execute("INSERT INTO users (username, password, email, sign_up_date) VALUES (?, ?, ?, ?)",
                  (username, password, email, signup_date))
        conn.commit()
        print("Successfully Made a New Account!")
        return c.lastrowid
    except sqlite3.IntegrityError:  # Error that is caught, when that information, or any exists.
        print("Username already exists. You need to login.")
        return None

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Seeing if username and password is existent in the table from Users table
    
    c.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    if user:
        print("Login successful!")
        return user[0]  # Getting id of user table
    else:
        print("Invalid credentials. Please try again.")
        return None

def review_movie(user_id):
    title = input("Enter the movie title you want to submit a review for: ")

    if APIClient.search_movie(title):
        rating = int(input("Rate the movie out of 5 stars: "))
        comment = input("Add some comments about the movie: ")
        review_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        movie_id = APIClient.get_movie_id(title)

        # Check if the movie is already in the movies table
        c.execute("SELECT id FROM movies WHERE title = ?", (title,))
        result = c.fetchone()

        if result:
            movie_id = result[0]
        else:
            c.execute("INSERT INTO movies (title) VALUES (?)", (title,))
            conn.commit()
            movie_id = c.lastrowid

        c.execute("INSERT INTO reviews (user_id, movie_id, rating, comment, review_date) VALUES (?, ?, ?, ?, ?)",
        (user_id, movie_id, rating, comment, review_date))
        conn.commit()
        print("Review submitted!")
    else:
        print("The movie title does not exist in the Cinemagoer API. Please enter a valid movie title.")

def recommendation_made(user_id):
    c.execute("SELECT COUNT(*) FROM reviews "
              "WHERE user_id = ?", (user_id,))
    count = c.fetchone()[0]
    return count > 0

def fetch_reviews(user_id):
    c.execute("""
            SELECT reviews.rating, reviews.comment, reviews.review_date, movies.title
            FROM reviews
            JOIN movies ON reviews.movie_id = movies.id
            WHERE reviews.user_id = ?
        """, (user_id,))
    reviews = c.fetchall()
    movies = []
    ratings = []
    for review in reviews:
        rating, comment, review_date, movie_title = review
        movies.append(movie_title)
        ratings.append(rating)
    return movies, ratings

def print_reviews(user_id):
    movies, ratings = fetch_reviews(user_id)
    for movie, rating in zip(movies, ratings):
        print(f"Movie: {movie}, Rating: {rating}")
    return movies, ratings

def get_recommendation(user_id):
    genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller"]
    age_ratings = ["G", "PG", "PG-13", "R"]
    year_ranges = ["2000-2010", "2011-2015", "2016-2020", "2021-present"]

    genre = input(f"Select a genre from the following list: {', '.join(genres)}: ")
    age_rating = input(f"Select an age-appropriateness rating from the following list: {', '.join(age_ratings)}: ")
    year_range = input(f"Select a recency range from the following list: {', '.join(year_ranges)}: ")

    if recommendation_made(user_id):
        movies, ratings = fetch_reviews(user_id)
        recommendation = SEOapi.get_movie_recommendation(movies, ratings, genre, age_rating, year_range)
        print(f"We recommend you to watch: \n{recommendation}\n")
    else:
        print("No movie recommendations available at the moment. Must submit a movie review 🎅")

def main():
    user_id = None
    while not user_id:
        print("****** Welcome to FlixFix, Your Personalized Movie Recommender ******", end='\n')
        action = input("Do you want to (1) Register or (2) Login? Enter 1 or 2: ")
        if action == '1':
            user_id = make_user()
        elif action == '2':
            user_id = login_user()
    
    while True:
        action = input("Do you want to (1) Review a Movie, (2) Get a Recommended Movie, (3) Get a List of Your Reviews, or (4) Quit? Enter 1, 2, 3, or 4: ")
        if action == '1':
            review_movie(user_id)
        elif action == '2':
            get_recommendation(user_id)
        elif action == '3':
            if recommendation_made(user_id):
                print_reviews(user_id)
            else:
                print("You have not made any recommendations yet")
        elif action == '4':
            print("Thank you for using our Horror Movie Recommender. Goodbye!")
            break

if __name__ == "__main__":
    main()