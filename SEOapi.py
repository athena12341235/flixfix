import os
import openai
from openai import OpenAI

# Set environment variables
my_api_key = 'sk-proj-hF0EKYccdUjF3QSH0FeRT3BlbkFJz2kETFLdKZ3TYT5rNK3M'

openai.api_key = my_api_key

# Create an OpenAPI client using the key from our environment variable
client = OpenAI(
    api_key=my_api_key,
)

def ask_ai(prompt):
  # Specify the model to use and the messages to send
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": prompt}
      ]
  )
  return(completion.choices[0].message.content) 

def get_movie_recommendation(films, ratings, genre, age_rating, year_range):
    prompt = (f"Using this list of films watched by a user: {films} and the ratings out of 5 they gave these films: {ratings}, "
              f"can you give a movie recommendation? The user prefers {genre} genre, with an age rating of {age_rating}, "
              f"and movies released in the years {year_range} inclusive."
              f"Please only output a numbered list of 5 movies and a sentence-long plot summary for each.")
    return ask_ai(prompt)

'''Dummy Data'''
# films=['Toy Story',
# 'Finding Nemo',
# 'Monsters, Inc.',
# 'The Incredibles',
# 'Up']

# ratings=[8,9,7,8,10]

films=['Pulp Fiction',
'The Shawshank Redemption',
'Fight Club',
'Forrest Gump',
'The Matrix'
]

ratings=[8,10,7,9,6]


# print(ask_ai(prompt))
# #prompt= f"Using this list of films watched by a user: {films} and a list of the ratings out of 10 of they gave these films: {ratings}. Can you give a movie recommendation? Just return the name of the movie."











