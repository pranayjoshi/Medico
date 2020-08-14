import pandas as pd
import os
from get_data import get_final_file_path, csv_to_df
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import nltk
from nltk.tokenize import word_tokenize

# CSV to DataFrame
data = get_final_file_path
data_frame = csv_to_df(data)

# Trainable Formats
X_train = data_frame["display"]
Y_train = data_frame["code"]

doc = X_train.values.tolist()
features = Y_train.values.tolist()

# Word tokenizer
def word_tokenize(doc):
    tokenized_doc = []
    for d in doc:
        d = str(d)
        tokenized_doc.append(word_tokenize(d.lower()))
    print("First 10 toknized sentences: ", tokenized_doc[:10])
    return tokenized_doc

# Tagged documents
def tagged_docs(tokenized_doc, features):
    features = Y_train.values.tolist()
    tagged_data = []
    for value in range(len(doc)):
        feature = features[value]
        tokenized_sent = tokenized_doc[value]
        taggd_sentence = TaggedDocument(tokenized_sent, [str(feature)])
        tagged_data.append(tagged_sentence)
    print("First 5 taggd sentences: ",tagged_data[:5])
