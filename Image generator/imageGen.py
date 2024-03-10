import os
import requests
import replicate
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def download_image(image_url, directory, filename):
    # Ensure the directory exists, create if it doesn't
    os.makedirs(directory, exist_ok=True)

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(os.path.join(directory, filename), 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to load image from {image_url}")

ending = "in a colourful children's story animation style with out any texts."

prompts = [
    
    f"Ming was a little koala who lived in the Australian jungle {ending}",
    f"One sunny day, Ming woke up early and couldn't wait to go play cricket with his friends {ending}",
    f"He quickly ate his eucalyptus leaves for breakfast and headed out to the jungle clearing where they always played {ending}",
    f"He quickly grabbed some leaves and carefully removed the thorns from Joey's fur {ending}",
    f"They had so much fun playing together, and Joey even scored a few runs! {ending}",
    f"Soon, they were all playing cricket together, and Ming was so happy that he could share his love for the game with his friends and a new friend like Joey {ending}"
]

directory = r"E:\IIT studies\2 ND YEAR MATERIAL\SDGP\IMAGES"  # Change this to your desired directory

for i, prompt in enumerate(prompts):
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": prompt}
    )

    pprint(output)

    # Download image
    if output:
        download_image(output[0], directory, f"output_{i}.jpg")
    else:
        print(f"No image generated for prompt: {prompt}")


