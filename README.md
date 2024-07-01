# project1
RUN THE PYTHONSCRIPT FILE TO USE PROGRAM

CREATE/USE YOUR OWN API KEY


Database Schema Design:
Users Table:

UserID (Primary Key): Unique identifier for each user.
Username: User's chosen name or handle.
Email: User's email address.
SignUpDate: When the user joined the service.


Movies Table:

MovieID (Primary Key): Unique identifier for each movie.
Title: The title of the movie.
Genre: Primary genre of the movie.
ReleaseYear: Year the movie was released.
Director: Director of the movie.


UserPreferences Table:

PreferenceID (Primary Key): Unique identifier for each record.
UserID (Foreign Key): Links to the Users table.
MovieID (Foreign Key): Links to the Movies table.
Rating: User's rating for the movie.
Favorite: Boolean indicating if this is one of their favorite movies.

MovieDiscussions Table:

DiscussionID (Primary Key): Unique identifier for each discussion session.
UserID (Foreign Key): Links to the Users table.
MovieID (Foreign Key): Links to the Movies table.
Timestamp: When the discussion/comment was made.
Comment: The user's comment or discussion input.
