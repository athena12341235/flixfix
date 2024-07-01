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
