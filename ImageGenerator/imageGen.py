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

image_URLs = []

def generateImages(prompts):
    print("\n[imageGen.py] - Received prompts:")
    global image_URLs
    for prompt in prompts:
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={"prompt": prompt},
        )
        image_URLs.append(output[0])
        pprint(output)

def return_urls():
    return image_URLs

    # image_URLs = [
    #     "https://replicate.delivery/pbxt/oNZuusE1FNpvDFuGUYGASOXP6hMPqySWadBKgOPGTAgSdtoE/out-0.png",
    #     "https://replicate.delivery/pbxt/RUkVneea9eHjipkSzCbyWypY5lnFIPzOazm2dlZTGEquqrFlA/out-0.png",
    #     "https://replicate.delivery/pbxt/nlrmxM6TDnZwHp8rGw4NfQK75ExxN1K16RVUNR6V0Sox6aRJA/out-0.png",
    #     "https://replicate.delivery/pbxt/n8701TPRefjSfprYWk1yeQzOWV9rI7pehF2DTNbb3ufXcdtoE/out-0.png",
    #     "https://replicate.delivery/pbxt/VeW1tZxb9M3Dcak62Z3VZZZzfbKehd4Pa86oOyDyzqE8rrFlA/out-0.png",
    #     "https://replicate.delivery/pbxt/amXw8ytaDwI5MFQkEVHZUfUtCfP3XuoCXqSNm6pP2hbN21iSA/out-0.png",
    # ]

    # return image_URLs
