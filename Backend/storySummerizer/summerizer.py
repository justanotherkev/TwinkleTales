from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def story_summerizer(story):
    
    parser = PlaintextParser.from_string(story, Tokenizer("english"))

    # LSA summarizer
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentences_count=6)  

    # Output the sentences 
    # print("Summary:")
    # for sentence in summary:
    #     print(sentence)

    return summary



