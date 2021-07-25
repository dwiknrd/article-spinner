import re
import random
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import regexp_tokenize
import nltk.data
from nltk.stem.porter import *

class spinner(object):

    def spin(self, s):
        while True:
            s, n = re.subn('{([^{}]*)}',
                lambda m: random.choice(m.group(1).split("|")), s)

            if n == 0: break

        return s.strip()


    def splitToSentences(self, content):

        tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

        return tokenizer.tokenize(content)

    
    # get all synonyms of a word from the wordnet database
    def getSynonyms(self, word):

    #include the original word
        synonyms = [word]
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.name != word:
                    # since wordnet lemma.name will include _ for spaces, we'll replace these with spaces
                    w, n = re.subn("_", " ", lemma.name())
                    synonyms.append(w)
            s = list(set(synonyms))

        return len(s), s

    
    """
    Transform text into spintax with the folowing steps
    1. split the text to sentences
    2. loop through the sentences and tokenize it
    3. loop thorugh each token, find its stem and assemble all the synonyms of it into the spintax
    """

    def getSpintax(self, text):
        sentences = self.splitToSentences(text)
        stemmer = PorterStemmer()
        spintax = ""

        for sentence in sentences:
            tokens = regexp_tokenize(sentence, "[\w']+")

            for token in tokens:
                stem = token
                n, syn = self.getSynonyms(stem)
                spintax += "{"
                spintax += token
                spintax += "|"

                for x in range(n):
                    spintax += syn[x]
                    if x < n-1:
                        spintax += "|"
                    else:
                        spintax += "} "
                
        return spintax


if __name__ == '__main__':
# Assign the object for the class
    s = spinner()
    st = "Machine learning is a field of computer science that gives computer systems the ability to learn"
    spintax = s.getSpintax(st)

    print(spintax)

    spun = s.spin(spintax)

    print(spun)
