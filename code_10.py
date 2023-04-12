import nltk
reviews = open('ice_cream_reviews.txt')

for review in reviews:
    tokens = nltk.word_tokenize(review)
    print(tokens)
