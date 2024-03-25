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
    # images = [
    #     "https://replicate.delivery/pbxt/3kDtTlgo2CILA5FHkcSXZe2pHZwX0LIZjFY9qVotcfp3DgjSA/out-0.png",
    #     "https://replicate.delivery/pbxt/2ewrv40HB6xSS6OrukTWufaiBdhqyQ5ET9I9Y717K5KFEgjSA/out-0.png",
    #     "https://replicate.delivery/pbxt/ZeavYRHTmsSCCCRGpOmkuAtUJYJSGuf9cRMCecKpuQ5kIAHlA/out-0.png",
    #     "https://replicate.delivery/pbxt/Yh8nvPmHhuKHFR9V5BfmfYUVVDEDf8Js6st2aApS798jJAHlA/out-0.png",
    #     "https://replicate.delivery/pbxt/quQ0c6uJrxJCABCFnweGXzcbM4cKQc6VlLyU3obc8pHiCwRJA/out-0.png",
    #     "https://replicate.delivery/pbxt/AGzQ3pI4OxKYPJGE4SL0TJggbyYUwfvg4WcRPfD7YNPhfAHlA/out-0.png",
    # ]

    # for image in images:
    #     image_URLs.append(image)


def return_urls():
    global image_URLs
    final_image_list = image_URLs
    image_URLs = []
    return final_image_list
