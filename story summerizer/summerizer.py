from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import sys
import storyGenerator

nltk.download('punkt')
sys.path.append('https://github.com/justanotherkev/TwinkleTales/blob/Story-generation-changes-to-openai.py/storyGenerator')  # Include the path to module_folder


# story to be summarized
story = storyGenerator.story

parser = PlaintextParser.from_string(story, Tokenizer("english"))

# LSA summarizer
summarizer = LsaSummarizer()

# Generate the summary
summary = summarizer(parser.document, sentences_count=6)  

# Output the sentences 
print("Summary:")
for sentence in summary:
    print(sentence)
