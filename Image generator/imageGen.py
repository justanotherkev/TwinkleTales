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

prompts = [
    "a crocodile reading a book 3d animated",
    "a fox on a roof 3d",
    "a swan in a lake 3d",
    "a bunny eating carrots 3d",
    "a bird is flying in the sky 3d"
]

directory = r"C:\Users\94768\OneDrive\Desktop\IIT\L5\SDGP\image-gen-react\image-gen-react\src\assets\images"  # Change this to your desired directory

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


