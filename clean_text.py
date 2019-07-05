#!/usr/bin/env python
# coding: utf-8

# # Create NLP pipeline to Clean Data
# 
#     - Load Input and read Reviews
#     - Tokenize 
#     - Remove stop words 
#     - Perform Stemimg
# 	  - Write cleaned data to output file
# In[1]:


sample_text = "I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."


# # NLTK
#     - for a single review string

# In[2]:


from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

import system as sys


# In[3]:


tokenizer = RegexpTokenizer(r'\w+')
# import nltk
# nltk.download('stopwords')
en_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


# In[4]:


def getCleanReview(review):
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    #Tokenize
    tokens = tokenizer.tokenize(review)
    new_tokens = [token for token in tokens if token not in en_stopwords]
    stemmed_token = [ps.stem(token) for token in new_tokens]
    
    cleanned_review = ' '.join(stemmed_token)
    return cleanned_review