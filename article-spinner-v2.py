from __future__ import print_function, division
from future.utils import iteritems
from builtins import range

import nltk
import random

from bs4 import BeautifulSoup

# load the data
# data courtesy of http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html
negative_reviews = BeautifulSoup(open('data_input/negative.review').read())
negative_reviews = negative_reviews.findAll('review_text')

# extract trigrams and insert into dictionary
# (w1, w3) is the key, [ w2 ] are the values
trigrams = {}
for review in negative_reviews:
    text_article = review.text.lower()
    tokens = nltk.tokenize.word_tokenize(text_article)
    for i in range(len(tokens) - 2):
        key_word = (tokens[i], tokens[i+2])
        if key_word not in trigrams:
            trigrams[key_word] = []
        trigrams[key_word].append(tokens[i+1])

# turn each array of middle-words into a probability vector
trigram_probabilities = {}
for key_word, words in iteritems(trigrams):
    # create a dictionary of word -> count
    if len(set(words)) > 1:
        # only do this when there are different possibilities for a middle word
        d = {}
        n = 0
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
            n += 1
        for w, c in iteritems(d):
            d[w] = float(c) / n
        trigram_probabilities[key_word] = d


def random_sample(d):
    # choose a random sample from dictionary where values are the probabilities
    r = random.random()
    cumulative = 0
    for w, p in iteritems(d):
        cumulative += p
        if r < cumulative:
            return w


def test_spinner():
    review = random.choice(negative_reviews)
    text_article = review.text
    print("Original:", text_article)
    text_article = text_article.lower()
    # print("Lower Text:", text_article)
    tokens = nltk.tokenize.word_tokenize(text_article)
    for i in range(len(tokens) - 2):
        if random.random() < 0.2: # 20% chance of replacement
            key_word = (tokens[i], tokens[i+2])
            if key_word in trigram_probabilities:
                w = random_sample(trigram_probabilities[key_word])
                tokens[i+1] = w
    print("Spinner:")
    print(" ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))


if __name__ == '__main__':
    test_spinner()