from openai import OpenAI
client = OpenAI()

story_data = ["Anne","America","park","stormy","Badminton"]
#prompt = f"Tell me a short children's bedtime story . {story_data[0]} loves to play {story_data[4] } in the {story_data[2]}. The weather that day was {story_data[3]}. Include moral values into this story."

prompt = f"Can you generate a short bedtime story suitable for children aged 4 to 7 about a charcter named {story_data[0]} who lives in {story_data[1]} and loves {story_data[4]}.The story should take place in a {story_data[2]} on a {story_data[3]} day.This should incorporate cultural factors and a moral value."

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

# print(completion.choices[0].message)