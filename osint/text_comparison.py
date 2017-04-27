# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer

files = ['path/to/file1',
        'path/to/file2', 'path/to/file3'
        ]

docs = [open(f) for f in files]
        
tfidf = TfidfVectorizer().fit_transform(docs)

pairwise_similarity = tfidf * tfidf.T

print pairwise_similarity