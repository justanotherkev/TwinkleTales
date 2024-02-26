import warnings
from transformers import XLNetTokenizer, XLNetLMHeadModel

# Suppress warnings
warnings.filterwarnings("ignore")

# Load XLNet tokenizer and model
tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
model = XLNetLMHeadModel.from_pretrained('xlnet-base-cased')

# Prompt for generating a story
prompt = "In a faraway kingdom, there was a brave knight"

# Tokenize the prompt
inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=True)

# Generate story
output = model.generate(
    inputs.input_ids,
    max_length=150,  # Adjust maximum length to a reasonable value
    num_return_sequences=1,
    num_beams=5,  # Adjust number of beams for beam search
    early_stopping=True if 5 > 1 else False,  # Enable early stopping only for beam search
    no_repeat_ngram_size=2,  # Avoid repetition of n-grams
    pad_token_id=tokenizer.eos_token_id  # Set pad token ID for padding
)

# Decode and print the generated story
generated_story = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_story)

