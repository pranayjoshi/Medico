import pandas as pd
import os
from get_data import get_final_file_path, csv_to_df
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import nltk
from nltk.tokenize import word_tokenize
import filepath as fp

# CSV to DataFrame
def get_file_path():
    doc2vec_loc = fp.run("doc2vec")
    return doc2vec_loc
def csv2dataframe():
    data = get_final_file_path()
    data_frame = csv_to_df(data)
    return data_frame
# Trainable Formats
def trainable_data(data_frame):
    X_train = data_frame["display"]
    Y_train = data_frame["code"]

    doc = X_train.values.tolist()
    features = Y_train.values.tolist()
    return doc, features

# Word tokenizer
def word_tokenizer(doc):
    tokenized_doc = []
    for val in range(len(doc)):
        word = str(doc[val]).lower()
        tokenized_doc.append(word_tokenize(word))
    print(tokenized_doc[:5])
    return tokenized_doc

# Tagged documents
def tagged_docs(tokenized_doc, features):
    tagged_data = []
    for value in range(len(tokenized_doc)):
        feature = features[value]
        tokenized_sent = str(tokenized_doc[value])
        tagged_sentence = TaggedDocument(tokenized_sent, [str(feature)])
        tagged_data.append(tagged_sentence)
    print("First 5 taggd sentences: ",tagged_data[:5])
    return tagged_data

# Building Model
def model(tagged_data, doc2vec_loc, max_epochs=30, vec_size=20, alpha=0.025):

    model = Doc2Vec(vec_size=vec_size,
                    alpha=alpha, 
                    min_alpha=0.00025,
                    min_count=1,
                    dm =1)
    print("build started")
    model.build_vocab(tagged_data)
    print("build end")
    for epoch in range(max_epochs):
        print(f'iteration {epoch}/{max_epochs}')
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)
        # decrease the learning rate
        model.alpha -= 0.0002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    model.save(doc2vec_loc)
    print("Model Saved")

def run():
    data_frame= csv2dataframe()
    doc, features = trainable_data(data_frame)
    tokenized_doc = word_tokenizer(doc)
    tagged_data = tagged_docs(tokenized_doc, features)
    doc2vec_loc = get_file_path()
    model(tagged_data=tagged_data, doc2vec_loc = doc2vec_loc)

if __name__ == "__main__":
    run()
