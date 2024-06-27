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

prompt= f"Using this list of films watched by a user: {films} and a list of the ratings out of 10 of they gave these films: {ratings}. Can you give a movie recommendation? Just return the name of the movie."

print(ask_ai(prompt))










