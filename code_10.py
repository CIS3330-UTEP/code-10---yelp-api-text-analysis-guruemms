import nltk
from nltk.corpus import stopwords
from yelpapi import YelpAPI
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

stop_words = set(stopwords.words('english'))
analyzer = SIA()

api_key = 'NclPqNJ86OBRq0Y5cfLU5ch7BxPop6oHLJ7LwzJCqPqFAvmPaM2jxRa-qcNPDhKmZXqMEhsXz3rsBgwt9SopTmynTRsV3QuWg5FQUcxz3UE0Lzi5VeFFUa6aM6Q1ZHYx'
yelp_api = YelpAPI(api_key)

#search query
search_term = "coffee"
search_location = "El Paso, TX"
search_sort_by = "rating" #best_match, rating, review_count, distance
search_limit = 20
search_results = yelp_api.search_query(term=search_term,location = search_location, sort_by = search_sort_by, limit = search_limit)
#use offset = ___ to move further down list of resturants

for business in search_results['businesses']:
    print(business['name'])
    print(business['alias'])
    print("\n")

id_for_reviews = ("proof-and-press-el-paso")
reviews_result = yelp_api.reviews_query(id = id_for_reviews)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
for review in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

id_for_reviews = ("sand-dust-coffee-el-paso")
reviews_result = yelp_api.reviews_query(id = id_for_reviews)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
for review in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

id_for_reviews = ("vyable-coffee-el-paso")
reviews_result = yelp_api.reviews_query(id = id_for_reviews)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
for review in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

id_for_reviews = ("global-coffee-el-paso")
reviews_result = yelp_api.reviews_query(id = id_for_reviews)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
for review in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')

id_for_reviews = ("perks-coffee-el-paso")
reviews_result = yelp_api.reviews_query(id = id_for_reviews)
reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
for review in reviews_df['text']:
    sentiment_score = analyzer.polarity_scores(review)
    print(review)
    print(sentiment_score)
    print('\n')