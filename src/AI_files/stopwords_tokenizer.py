from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import get_data
def stop_words_tokenizer(feature_list):
    nlp = English()
    filtered_sentence=[]
    for line in feature_list:
        sentence = ""
        doc = nlp(line)
        for word in doc:
            if word.is_stop==False:
                sentence = sentence + " " + str(word)
        filtered_sentence.append(sentence)
    return filtered_sentence
def retrive_data():
    data = get_data.run()
    return data
def get_feature(data):
    feature = data["display"]
    return feature
def run():
    data = retrive_data()
    feature = get_feature(data)
    feature_list = list(feature)
    tokenized_features = stop_words_tokenizer(feature_list)
    return tokenized_features
if __name__ == "__main__":
    tokenized_features = run()
    print(tokenized_features[:5])