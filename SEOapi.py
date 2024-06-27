
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

prompt= f"Using this list of films watched by a user: {films} and a list of the ratings out of 10 of they gave these films: {ratings}. Can you give a movie recommendation and why?"

print(ask_ai(prompt))


# import os 
# import openai
# from openai import OpenAI

# # Set environment variables
# my_api_key = 'sk-proj-hF0EKYccdUjF3QSH0FeRT3BlbkFJz2kETFLdKZ3TYT5rNK3M'

# openai.api_key = my_api_key

# # Create an OpenAPI client using the key from our environment variable
# client = OpenAI(
#     api_key=my_api_key,
# )

# # # Function to interact with the chat API
# # def chat_with_gpt(prompt):
# #   response = client.chat.completions.create(
# #     engine="gpt-3.5-turbo",  # Specify the model to use
# #     prompt=prompt,
# #     max_tokens= float('inf'),  # Adjust the max tokens as needed
# #     n=1,  # Number of responses to generate
# #     stop=None,  # Stopping criteria for the response
# #     temperature=0.7  # Controls the randomness of the response
# #   )
# #   return response.choices[0].message.content


# # # Example variables
# # films= [] # taken from SQL
# # ratings = [] # taken from SQL

# # # Create a prompt with variables using f-string
# # user_prompt = f"Using this list of films: {films} and a list of the ratings out of 10 of these films: {ratings}. Can you recommend a film to this person?"

# # # Get response from GPT model
# # response = chat_with_gpt(user_prompt)
# # print("Chat response:", response)

# # # You can control the randomness of the response so when there is less data maybe make it more random?
# # #What if chat does not know the film?? Pull imdb API or some API to 
# # #get the genre and just recommed a film of some type, but how to know 
# # #if chat wont know the film,how can I process the response of chat


# '''Dummy Data'''
# films=['Toy Story',
# 'Finding Nemo',
# 'Monsters, Inc.',
# 'The Incredibles',
# 'Up']

# ratings=[8,9,7,8,10]


# # print(f"Using this list of films: {films} and a list of the ratings out of 10 of these films: {ratings}. Can you recommend a film to this person? and why")

# prompt= f"Using this list of films watched by a user: {films} and a list of the ratings out of 10 of they gave these films: {ratings}. Can you recommend another film to this user? and why"

# # Specify the model to use and the messages to send
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": prompt}
#     ]
# )
# print(completion.choices[0].message.content) 





# import os 
# import openai
# from openai import OpenAI


# # Set environment variables
# my_api_key = 'sk-proj-hF0EKYccdUjF3QSH0FeRT3BlbkFJz2kETFLdKZ3TYT5rNK3M'

# openai.api_key = my_api_key
# # WRITE YOUR CODE HERE
# client = OpenAI(
#     api_key=my_api_key,
# )

# print("hello")
# def ask_api(prompt):
# # Specify the model to use and the messages to send
#   completion = client.chat.completions.create(
#       model="gpt-3.5-turbo",
#       messages=[
#           {"role": "system", "content": "how do you make a cake?"}
#       ]
#   )
#   return(completion.choices[0].message.content)


# # while(True):
# #   question= input()
# #   if question:
# #     print(ask_api(question))

# '''Dummy Data'''
# films=['Toy Story',
# 'Finding Nemo',
# 'Monsters, Inc.',
# 'The Incredibles',
# 'Up']

# ratings=[8,9,7,8,10]


# ask_rec= True

# if ask_rec==True:
#   question= "Using this list of films: {films} and a list of the ratings out of 10 of these films: {ratings}. Can you recommend a film to this person? and why"
#   print(question)
#   print(ask_api(question))









