import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.utils.data import Dataset, DataLoader
import random

# Define a custom dataset class to load stories from the text file
class StoriesDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_length):
        self.stories = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                self.stories.append(tokenizer.encode(line.strip()[:max_length], add_special_tokens=True))

    def __len__(self):
        return len(self.stories)

    def __getitem__(self, idx):
        return torch.tensor(self.stories[idx])

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Path to your text file containing stories
file_path = "C:\Users\94768\Downloads\Stories.txt"

# Hyperparameters
max_length = 512  # Maximum length of input sequences
batch_size = 4
epochs = 5

# Create dataset and dataloader
dataset = StoriesDataset(file_path, tokenizer, max_length)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Training loop
model.train()
for epoch in range(epochs):
    total_loss = 0
    for batch in dataloader:
        inputs = batch[:, :-1].to(model.device)
        labels = batch[:, 1:].to(model.device)

        # Forward pass
        outputs = model(inputs, labels=labels)
        loss = outputs.loss

        # Backward pass
        loss.backward()
        total_loss += loss.item()

        # Update parameters
        optimizer.step()
        optimizer.zero_grad()

    print(f'Epoch {epoch + 1}, Loss: {total_loss / len(dataloader)}')

# Save the trained model
model.save_pretrained('trained_model')
tokenizer.save_pretrained('trained_model')
