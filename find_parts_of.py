import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sagan_quote = """ If you wish to make an apple pie from scratch, you must first invent the universe."""

tags = {}
for e in tagged_list:
    if(e[1] not in tags.keys()):
        tags[e[1]] = []
    tags[e[1]].append(e[0])

question = "Identify the "

print(tags)