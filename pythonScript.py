import sqlite3
from datetime import datetime

def make_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email: ")
    signup_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        #need to add to table created
        print("You've made a new account!")
    except sqlite3.IntegrityError: #Error that is caught, when that information, or any exists.
        print("Username already exists. You need to login.")
        return None

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    #from Table get USER and PASS fiels
    
    if user:
        print("Login successful!")
    else:
        print("Invalid credentials. Please try again.")
        return None

def review_movie(user_id):
    title = input("Enter the movie title you want to submit a review for: ")
    if is_horror_movie(title): #ADD CHECKING MOVIE API FOR HORROR FILM OR NOT
        rating = int(input("Rate the movie out of 5 stars: "))
        description = input("Add some comments about the movie.")
        #ADD TO USER FIELDS REVIEW
        print("Review submitted!")
    else:
        print("The movie is not a horror movie. Please try again.")

def main():
    user_id = None
    while not user_id:
        print("****** Welcome to our Horror Movie Recommendar ******", end='\n')
        action = input("Do you want to (1) Register or (2) Login? Enter 1 or 2: ")
        if action == '1':
            user_id = make_user()
        elif action == '2':
            user_id = login_user()
    
    while True:
        action = input("Do you want to (1) Review a Movie or (2) Get a Recommended Movie? Enter 1 or 2: ")
        if action == '1':
            review_movie(user_id)
        elif action == '2':
           #CALL CHATGPT FUNCTION
            if recommendation:
                print(f"We recommend you to watch: {recommendation}")
            else:
                print("No horror movie recommendations available at the moment. Please try to submit more reviews 🎅")
