from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

prompt = "Once upon a time, in a lush forest, there lived a friendly fox named Freddie and his best friend, Robbie the rabbit. They loved playing soccer together in the clearing near their cozy burrows. One sunny day, as they kicked the ball back and forth, they noticed something strange lurking in the bushes..."

# Putting truncation from true to false to see if the story length is different 
res = generator(prompt, truncation=False, max_length=400, do_sample=True, temperature=0.9)

generated_text = res[0]['generated_text']

print("Generated Story:")
print(generated_text)

with open('gpttext.txt', 'w') as f:
    f.write(generated_text)
