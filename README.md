# Article Spinner AI
<hr>

## 📌 Background
Content marketing is a great technique to boost the brand’s web presence and attract potential customers or clients. When using blog posts or articles as an online marketing tool however, many companies can begin to feel like they’re being stretched thin. After all, even if you hire a skilled writer, quality content takes time and effort to produce.<br>

Even though there are numerous methods that one can use to maximize on online visibility, spinning articles is one of the most effective ways to go about it. Article spinning involves creating new and unique articles from an original one. However, what matters most, in this instance, is to come up with unique and valuable content, and this boils down to the kind of software used.

## 🙋 Audiences
For blogger, SEO, digital marketer, website operator, or a writer that always lookout for unique content to post on your website. Benefit using article spinner: Cheap or zero cost, Time-saving, Unique output, and Improve search engines ranking.

## 📝 AI Article Spinner Idea:
1. NLP (Natural Language Processing)
2. Emulated Natural Language
3. NLTK wordnet
4. NLTK Rephrasing

## Article Spinner:
### Data
In this project, we will use data from scraping negative reviews of electronic goods provided by customers on Amazon. Data courtesy of http://www.cs.jhu.edu/~mdredze/datasets/sentiment/index2.html.

Because the data are in the format of negatif.review, we open it using `BeautifulSoup` library.

```
negative_reviews = BeautifulSoup(open('data_input/negative.review').read())
negative_reviews = negative_reviews.findAll('review_text')
```

### N-Grams Probabilities
The important thing to note, as for any other artificial intelligence or machine learning model, we neew to train the model with a huge corpus data. Once we do that, the system, or the NLP model will have a pretty good idea of the “probability” of the occurrence of a word after a certain word. So hoping that we have trained our model with a huge corpus of data, we’ll assume that the model gave us the correct answer.

N-gram probabilities are used to predict the next word given a sequence of words in a sentence. N-gram probabilities are calculated and associated models to give the most possible word fill in the next word.

**Intuitive Formulation**
Let’s start with equation `P(w|h)`, the probability of word `w`, given some history, `h`. 

Steps:
1. Label our words into: `w(1), w(2), w(3), ..., w(N)`
2. Model `w(i)` using `w(1), ..., w(i-1)` and `w(i+1), ..., w(N)`
3. Probabilistic `P{w(i)|w(1), ..., w(i-1), w(i+1), ..., w(N)}`

#### Trigrams
We will specific instance of "N-grams", where N=3. So the probabilities model is `P{w(i)|w(i-1), w(i+1)}`. We will use dictionary with `{w(i-1), w(i+1)}` as the key, and lookup `w(i)`. It is sort of like Markov model where `P{w(i)|w(i-1)}`. This are "unsupervised learning" because the are no labels.

We will extract trigrams and insert into dictionary. Where `(w1, w3)` is the key, `[w2]` are the values:

```
trigrams = {}
tokens = nltk.tokenize.word_tokenize(text_article)
    for i in range(len(tokens) - 2):
        key_word = (tokens[i], tokens[i+2])
        if key_word not in trigrams:
            trigrams[key_word] = []
        trigrams[key_word].append(tokens[i+1])
```

#### Trigram Probabilities
Next, we will turn each array of middle-words into probability vector
```
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
```

#### Random Sample
Choose a random sample from dictionary where values are the probabilities:
```
r = random.random()
    cumulative = 0
    for w, p in iteritems(d):
        cumulative += p
        if r < cumulative:
            return w
```

## Reference
- https://web.stanford.edu/~jurafsky/slp3/3.pdf
- http://www.phon.ox.ac.uk/jcoleman/old_SLP/Lecture_6/trigram-modelling.html
- https://towardsdatascience.com/introduction-to-language-models-n-gram-e323081503d9
- https://towardsdatascience.com/understanding-word-n-grams-and-n-gram-probability-in-natural-language-processing-9d9eef0fa058
- 
