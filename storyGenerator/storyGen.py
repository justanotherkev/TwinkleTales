import ast
from openai import OpenAI



def storyGenerator(story_data):
  
  my_data = ast.literal_eval(story_data)

  client = OpenAI(api_key="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")

  prompt = f"Generate a short story suitable for children aged 4 to 7 about a charcter named {my_data[0]} who lives in {my_data[1]} and loves {my_data[2]}.The story should take place in the {my_data[3]} on a {my_data[4]} day.This should incorporate a moral value."

  response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt={prompt},
    max_tokens= 2500,
    temperature=0
  )

  story = response.choices[0].text.strip()

  
  return story