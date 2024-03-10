from openai import OpenAI
# from storySummerizer.summerizer import storySummerizer

client = OpenAI(api_key="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")

story_data = ["Nina","Paris","Underground","rainy","Frisbee throwing"]

prompt = f"Generate a short story suitable for children aged 4 to 7 about a charcter named {story_data[0]} who lives in {story_data[1]} and loves {story_data[4]}.The story should take place in the {story_data[2]} on a {story_data[3]} day.This should incorporate a moral value."

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt={prompt},
  max_tokens= 2500,
  temperature=0
)

story = response.choices[0].text.strip()
print(story)

# sentences = storySummerizer(story)
