from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk


nltk.download('punkt')

# story to be summarized
story = """
Once upon a sunny day in the peaceful countryside, there lived two friends named Molly the Mouse and Robbie the Rabbit.
They lived in a cozy burrow nestled under the big oak tree near the meadow. The sky was a bright shade of blue, and fluffy clouds drifted lazily overhead.
Molly and Robbie loved to play catch with a soft ball made of leaves in the meadow. It was their favorite game to play together.
The meadow was their special place, where flowers bloomed in every color imaginable, and the tall grass swayed gently in the breeze.
One day, as they were playing catch, Robbie noticed that Molly's little mouse hole was looking a bit messy. Leaves and twigs were scattered around, making it difficult for Molly to come in and out comfortably.
"Hey, Molly," said Robbie, hopping over to her side. "Your home looks a bit messy. Would you like some help tidying up?"Molly smiled gratefully, touched by Robbie's kindness.
"That would be wonderful, Robbie. Thank you!"Together, they gathered twigs and leaves, sweeping them away from Molly's burrow.
Robbie hopped around energetically, while Molly scurried back and forth, organizing her cozy home.As they worked, dark clouds began to gather in the sky, and the wind started to pick up.
Robbie looked up worriedly, noticing the weather changing rapidly."Molly, I think there's a storm coming," he said, concern evident in his voice.
Molly nodded, her whiskers twitching with apprehension. "You're right, Robbie. We should find shelter before it gets too windy.
"They hurried back to Robbie's burrow, which was sturdier and more sheltered from the storm. Together, they huddled inside, listening to the rain pattering against the ground outside.
As the storm raged on, Molly and Robbie felt safe and warm inside the burrow, grateful for each other's company.
The rain eventually stopped, and the sun peeked out from behind the clouds, casting a warm glow over the meadow once again."Thank you for helping me tidy up, Robbie," said Molly, her eyes shining with gratitude.
"And thank you for keeping me safe during the storm."Robbie smiled, his heart full of happiness. "Anytime, Molly. That's what friends are for."And so, in the meadow where the sun always shines after the storm, Molly and Robbie learned that true friendship means helping each other through both sunny days and stormy nights.
"""

parser = PlaintextParser.from_string(story, Tokenizer("english"))

# LSA summarizer
summarizer = LsaSummarizer()

# Generate the summary
summary = summarizer(parser.document, sentences_count=6)  

# Output the sentences 
print("Summary:")
for sentence in summary:
    print(sentence)


# The sky was a bright shade of blue, and fluffy clouds drifted lazily overhead.
# Molly and Robbie loved to play catch with a soft ball made of leaves in the meadow.
# One day, as they were playing catch, Robbie noticed that Molly's little mouse hole was looking a bit messy.
# "Molly, I think there's a storm coming," he said, concern evident in his voice.
# "They hurried back to Robbie's burrow, which was sturdier and more sheltered from the storm.
# "Thank you for helping me tidy up, Robbie," said Molly, her eyes shining with gratitude.