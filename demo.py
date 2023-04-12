import nltk
nltk.download('averaged_perceptron_tagger')
reviews = open('ice_cream_reviews.txt')

for review in reviews:
    print(review)
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    print(pos_tags)
    for token in pos_tags:
        if token[1] == 'JJ' or token[1] == 'NN':
            #print(token[0])
            print(token)
