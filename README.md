# Ollama API Base Example with Python

This project demonstrates how to interact with the [Ollama](https://ollama.com/) API using Python's `ollama` library to send prompts and receive AI-generated responses in a structured way.

---

## Requirements

- Python 3.8+
- [Ollama installed and running locally](https://ollama.com/download)
- A compatible model pulled (e.g. `gemma3:1b`)

Install dependencies:

```bash
pip install ollama

ollama pull <model>
```

## Usage

Run the script:

```bash
python chat_example.py
```

You'll be prompted to enter a message. The script will send it to the Ollama model and display the response.

## Example Code

```bash
from ollama import chat
from ollama import ChatResponse

content = input("Enter your prompt...\n")

print('Finding answer...')

response: ChatResponse = chat(model='gemma3:1b', messages=[
    {
        'role': 'user',
        'content': content,
    },
])

print(response.message.content)
```

## Example Output

```bash
Enter your prompt...
What is the capital of France?
Finding answer...
Paris is the capital of France.
```

## Advanced
To structure your conversation history:

```bash
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Explain quantum physics in simple terms.'}
]

response = chat(model='gemma3:1b', messages=messages)
```

## License
MIT – use freely and responsibly.
