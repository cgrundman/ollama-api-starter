from ollama import chat
from ollama import ChatResponse

content = input("Enter your prompt...\n")

print('finding answer...')

response: ChatResponse = chat(model='gemma3:1b', messages=[
  {
    'role': 'user',
    'content': content,
  },
])

# or access fields directly from the response object
print(response.message.content)