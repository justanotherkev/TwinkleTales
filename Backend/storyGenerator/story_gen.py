import ast
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


### PROMPT MUST BE CHANGED BASED ON THE THEME SELECTED
def story_generator(theme, story_data):

    print(type(story_data))
    print(story_data)

    story_data_list = ast.literal_eval(story_data)
    # story_data_list = ["Drax", "laser", "boho", "hydrogen", "miami"]

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Integrates the answers from the user to generate a prompt

    prompt = f""

    if theme.lower() == "superhero":
        print(theme.lower() + " theme selected")
        prompt = f"Write a short superhero story suitable for children aged 4 to 7 about a superhero named {story_data_list[0]} whose strongest power is {story_data_list[1]}. Their arch-nemesis is {story_data_list[2]}, who has a diabolical plan to take over the city of {story_data_list[4]}. {story_data_list[2]}'s weakness is {story_data_list[3]}, which {story_data_list[0]} exploits to save the day. The story should include an exciting battle, clever strategies, and a moral value teaching the importance of courage and perseverance."

    elif theme.lower() == "adventure":
        print(theme.lower() + " theme selected")
        prompt = f"Write a short adventure story suitable for children aged 4 to 7 about a brave adventurer named {story_data_list[0]} who starts their journey in {story_data_list[1]}. Early in the adventure, {story_data_list[0]} faces a challenging {story_data_list[2]} and meets a wise guide ({story_data_list[3]}) along the way. Together, they embark on a quest to find the legendary {story_data_list[4]}. The story should include thrilling encounters, clever problem-solving, and a moral value teaching the importance of bravery, friendship, and determination."

    elif theme.lower() == "fairy tale":
        print(theme.lower() + " theme selected")
        prompt = f"Write a short fairy tale suitable for children aged 4 to 7 about a character ({story_data_list[0]}) who lives in {story_data_list[1]}. One day, {story_data_list[0]} discovers a magical creature, a {story_data_list[2]}, in {story_data_list[1]}. Together with their loyal companion, a {story_data_list[3]}, {story_data_list[0]} sets out on an epic quest to {story_data_list[4]}. The story should include magical adventures, enchanting discoveries, and a moral value teaching the importance of kindness, teamwork, and perseverance."

    elif theme.lower() == "sports":
        print(theme.lower() + " theme selected")
        prompt = f"Write a short sports story suitable for children aged 4 to 7 about a star athlete named {story_data_list[0]} who lives in {story_data_list[1]} and loves to play {story_data_list[2]}. {story_data_list[0]}'s biggest rival is {story_data_list[3]}. {story_data_list[0]} dreams of winning the {story_data_list[4]}, which would be a chance for {story_data_list[0]} to be remembered forever. The story should include exciting matches, personal growth, and a moral value teaching the importance of sportsmanship, hard work, and determination."

    print("\n\nPROMPT:\n" + prompt)
    # prompt is used by the openai API to generate a story script
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct", prompt={prompt}, max_tokens=2500, temperature=0
    )

    story = response.choices[0].text.strip()

    print("\n\nSTORY:\n" + story)

    return story
