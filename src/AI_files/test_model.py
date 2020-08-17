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
    test_doc = word_tokenize("I can understand he is suffering from Chronic tophaceous gout of hand due to renal impairment".lower())
    model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=5)
    best_result = model.docvecs.most_similar(positive=[model.infer_vector(test_doc)],topn=1)
    print("Best Result: ",best_result[0][0])
    print("Sureity percntage: ",best_result[0][1])

model = load_model()
test(model)