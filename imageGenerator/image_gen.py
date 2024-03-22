import replicate

from pprint import pprint

image_URLs = []


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
    #  Return some backup images instead of no images at all
    


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
