import anthropic

client = anthropic.Anthropic(api_key = "Ihr_API_key",)

message = client.messages.create(
    model = "claude-3-5-sonnet-20240620",
    max_tokens = 1000,
    temperature = 0.7,
    system="Du bist ein hilfreicher KI-Assistent.",
    messages=[
        {"role": "user", "content": "Hallo Claude, wie kann ich dich in Python nutzen?"}
    ]
)
print(message.content[0].text)