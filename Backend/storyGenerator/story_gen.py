import ast
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


def story_generator(story_data):

    story_data_list = ast.literal_eval(story_data)

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"Generate a short story suitable for children aged 4 to 7 about a charcter named {story_data_list[0]} who lives in {story_data_list[1]} and loves {story_data_list[2]}.The story should take place in the {story_data_list[3]} on a {story_data_list[4]} day.This should incorporate a moral value."

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct", prompt={prompt}, max_tokens=2500, temperature=0
    )

    story = response.choices[0].text.strip()

    return story
