import replicate
# from dotenv import load_dotenv
from pprint import pprint


# ending = "in a colourful 3D children's story animation style with out any texts."

# prompts = [
    
#     f"Nina was a little girl who lived in the beautiful city of Paris {ending}",
#     f"One rainy day, Nina woke up to the sound of raindrops tapping on her window {ending}",
#     f"She explained that sometimes in life, things may not go as planned, but if we work together and support each other, we can still have fun and achieve our goals {ending}",
#     f"Nina understood the importance of teamwork and was grateful for her grandmother's lesson {ending}",
#     f"They continued playing until it was time for Nina's mother to pick her up {ending}",
#     f"Nina was happy and thanked her grandmother for the fun day they had {ending}"
# ]

def generateImages(prompts):
    image_URLs = []
    for prompt in prompts:
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt}
        )
        image_URLs.append(output[0])
        # pprint(output)
    return image_URLs        


