from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import scispacy
import spacy
from get_data import csv_to_df
import filepath as fp

def stop_words_tokenizer(feature_list):
    nlp = spacy.load("en_core_sci_sm")
    filtered_sentence=[]
    for line in feature_list:
        doc = nlp(line)
        entity = doc.ents
        lst_entity = list(entity)
        sentence= ""
        for ele in lst_entity:
            sentence = sentence + str(ele) + " "
        filtered_sentence.append(sentence)
    return filtered_sentence

def get_data_loc():
    initial_data_loc = fp.run("initial_data")
    return initial_data_loc

def retrive_data(initial_data_loc):
    data = csv_to_df(initial_data_loc)
    return data

def get_feature(data):
    feature = data["display"]
    return feature

def run():
    initial_data_loc = get_data_loc()
    data = retrive_data(initial_data_loc)
    feature = get_feature(data)
    feature_list = list(feature)
    tokenized_features = stop_words_tokenizer(feature_list)
    return tokenized_features

if __name__ == "__main__":
    tokenized_features = run()
    print(tokenized_features[:5])