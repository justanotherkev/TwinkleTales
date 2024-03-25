import replicate

from pprint import pprint

image_URLs = []


# Uses the Replicate API to generate 6 images
def generate_images(prompts):
    count_break = 0
    while count_break < 5:
        try:
            print("\n[imageGen.py] - Received prompts:")
            global image_URLs
            for prompt in prompts:
                output = replicate.run(
                    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                    input={"prompt": prompt},
                )
                image_URLs.append(output[0])
                pprint(output)
            break
        except Exception as e:
            count_break += 1
            print("\n[image_gen.py] - Error generating images", e)
            continue

# Returns all the image URLs
def return_urls():
    global image_URLs
    final_image_list = image_URLs
    image_URLs = []
    return final_image_list
