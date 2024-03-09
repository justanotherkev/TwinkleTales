from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import sys
from storyGenerator import storyGen

# from ..storyGenerator.storyGen import story as story


nltk.download('punkt')
sys.path.insert('E:\IIT studies\2 ND YEAR MATERIAL\SDGP\TwinkleTales')  # Include the path to module_folder


# story to be summarized
story = storyGen.story

parser = PlaintextParser.from_string(story, Tokenizer("english"))

# LSA summarizer
summarizer = LsaSummarizer()

# Generate the summary
summary = summarizer(parser.document, sentences_count=6)  

# Output the sentences 
print("Summary:")
for sentence in summary:
    print(sentence)
