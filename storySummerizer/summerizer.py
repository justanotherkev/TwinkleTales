from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
# from textblob import TextBlob

# story ='''
# Once upon a time, in the heart of Africa, there lived a young boy named Kevin. He lived in a small village surrounded by a dense jungle. Kevin was a curious and adventurous boy who loved to explore the jungle and all its wonders.

# One day, as Kevin was playing with his friends, a big storm suddenly hit their village. The sky turned dark and the wind howled fiercely. The rain poured down heavily, making it difficult for anyone to go outside. But Kevin was determined to have some fun, even on a stormy day.

# He remembered that his father had told him about a special place in the jungle where the trees were tall and the ground was flat. It was the perfect place to play basketball. Kevin loved basketball and he had always dreamed of playing in a real court.

# Without hesitation, Kevin grabbed his basketball and ran into the jungle. The rain was pouring down harder now, but Kevin didn't mind. He was too excited to play basketball in the jungle. As he ran deeper into the jungle, he could hear the sound of drums and singing. He followed the sound and soon came across a group of children from a nearby village.

# They were playing a traditional African game called "Mbube". Kevin was fascinated by the game and asked if he could join in. The children welcomed him with open arms and taught him how to play. They used a small ball made out of leaves and played on a small court made out of mud.

# Kevin had so much fun playing with the children. They laughed and danced together, forgetting all about the storm outside. As the rain started to ease up, the children invited Kevin to their village to continue playing. Kevin was amazed by their village, it was so different from his own. He learned about their culture, their food, and their way of life.

# As the storm passed and the sun came out, Kevin realized that he had made new friends and had learned so much about a different culture. He also learned that you don't need fancy equipment or a big court to have fun playing basketball. All you need is a ball and some friends to play with.

# From that day on, Kevin and the children from the village played basketball together every time it rained. They even taught Kevin some new moves and tricks. Kevin was grateful for the storm that brought him to the village and for the new friends he made.
# and play basketball with his friends. But then he had an idea, he could play basketball in the jungle!

# Kevin quickly put on his raincoat and grabbed his basketball. He ran out into the jungle, jumping over puddles and dodging fallen branches. As he made his way deeper into the jungle, he found a clearing where he could play.

# He started to dribble the ball and shoot hoops, but then he heard a loud cry for help. Kevin followed the sound and found a group of animals huddled together under a tree. They were scared and shivering in the rain.

# Kevin knew he had to help them. He invited the animals to join him in playing basketball. At first, they were hesitant, but Kevin showed them how to play and they soon started to have fun. They forgot all about the storm and their fears.

# As they played, Kevin noticed that one of the animals, a monkey, was very good at shooting hoops. He asked the monkey to join his team and they became the best players in the jungle. The other animals were amazed and cheered them on.

# After the storm passed, the animals thanked Kevin for helping them and teaching them how to play basketball. They all became good friends and promised to play together every day.

# Kevin learned an important lesson that day. He realized that even in the midst of a storm, there is always something good that can come out of it. He also learned that by helping others and sharing his love for basketball, he could make new friends and bring joy to others.

# From that day on, Kevin and his animal friends played basketball together every day, rain or shine. And the jungle was filled with laughter and the sound of bouncing basketballs. Kevin's love for basketball had brought the animals together and taught them the value of friendship and teamwork.

# And so, Kevin and his animal friends lived happily ever after, playing basketball and spreading joy in the jungle. The end.
# '''

def storySummerizer(story):
    
    parser = PlaintextParser.from_string(story, Tokenizer("english"))

    # LSA summarizer
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentences_count=6)  

    # Output the sentences 
    print("Summary:")
    for sentence in summary:
        print(sentence)

    return summary

# summary = storySummerizer(story=story)

