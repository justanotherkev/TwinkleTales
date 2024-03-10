from textblob import TextBlob
import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

test_string = "Kevin is playing football"
blob = TextBlob(test_string)
print(blob.noun_phrases)