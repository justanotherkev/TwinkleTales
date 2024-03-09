from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages = [
    {"role": "user", "content": {prompt}},
]

)

print(completion.choices[0].message)
