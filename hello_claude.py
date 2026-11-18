from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello to Shah in one short sentence."}
    ],
)

print(message.content[0].text)