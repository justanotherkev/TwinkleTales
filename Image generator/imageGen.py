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
    # "The sky was a bright shade of blue, and fluffy clouds drifted lazily overhead."
    # "Molly and Robbie loved to play catch with a soft ball made of leaves in the meadow."
    # "One day, as they were playing catch, Robbie noticed that Molly's little mouse hole was looking a bit messy."
    # "Molly, I think there's a storm coming, he said, concern evident in his voice."
    # "They hurried back to Robbie's burrow, which was sturdier and more sheltered from the storm."
    # "Thank you for helping me tidy up, Robbie, said Molly, her eyes shining with gratitude."
    
    f"The sky was a bright shade of blue, and fluffy clouds drifted lazily overhead {ending}",
    f"Molly the mouse and Robbie the rabbit loved to play catch with a soft ball made of leaves {ending}",
    f"One day, as they were playing catch, Robbie noticed that Molly's little mouse hole was looking a bit messy {ending}",
    f"Molly, I think there's a storm coming, he said, concern evident in his voice {ending}",
    f"They hurried back to Robbie's burrow, which was sturdier and more sheltered from the storm. children story book animation style.",
    f"Thank you for helping me tidy up, Robbie, said Molly, her eyes shining with gratitude children story book animation style."
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


