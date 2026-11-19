# tiny_predictor.py: a toy "next word" predictor for Lesson 1.2.1.
# It "trains" by counting which word follows which in a few sentences,
# then "generates" by repeatedly picking a likely next word.
# It only reads the text below and prints. It changes no files.
import random
from collections import Counter, defaultdict

# The "training data": all the text this toy model will ever see.
text = """
the market opened higher today . the market closed lower today .
the video got more views today . the video got more likes .
the product sold out today . the market opened lower .
"""

# Training: count which word comes after each word.
words = text.split()
follows = defaultdict(Counter)
for current, nxt in zip(words, words[1:]):
    follows[current][nxt] += 1

print("After 'the', it has seen:", dict(follows["the"]))
print("After 'market', it has seen:", dict(follows["market"]))

# Generating: start with 'the', then keep picking a next word.
# Words seen more often are more likely to be picked, but it's still a random pick.
word = "the"
sentence = [word]
for _ in range(8):
    options = follows[word]
    if not options:
        break
    word = random.choices(list(options), weights=list(options.values()))[0]
    sentence.append(word)
    if word == ".":
        break
print("Generated:", " ".join(sentence))
