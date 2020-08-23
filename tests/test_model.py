import pandas as pd
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import nltk
from nltk.tokenize import word_tokenize

def load_model():
    model= Doc2Vec.load("./storage/doc2vec.model")
    ## Print model vocabulary
    model.wv.vocab
    return model

def test(model):
    test_doc = word_tokenize("so after reading everything i came to know that chronic tophaceous gout obtained due to renel impairment".lower())
    model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=5)
    best_result = model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=1)
    expected_result = "303921000119109"
    if best_result[0][0] == expected_result:
        print("Test passed")
    print("Best Result: " + best_result[0][0] + "    --->    " + "Expected Result: " + "303921000119109")
    print("Sureity percntage: ",best_result[0][1])

model = load_model()
test(model)