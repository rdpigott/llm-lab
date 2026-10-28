import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

with open("data/sample.txt", encoding="utf-8") as f:
    text = f.read()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    system="You summarize documents for a busy executive. Be concise.",
    messages=[{"role": "user", "content": text}],
)
print(response.content[-1].text)
print(response.usage)  # check token usage and cost on every call