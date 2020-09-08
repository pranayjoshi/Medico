from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import nltk
nltk.download("popular", quiet=True)
from nltk.tokenize import word_tokenize
from get_data import get_final_file_path, csv_to_df
import sentence_tokenizer
import sys
import filepath as fp
sys.path.append("./src/Data_process")
import remove_punctuation as re_punc

def get_file_path():
    doc2vec_loc = fp.run("doc2vec")
    return doc2vec_loc

def csv2dataframe():
    data = get_final_file_path()
    data_frame = csv_to_df(data)
    return data_frame

def remove_punctuation(document):
    unpunctuated_doc=[]
    for sentence in document:
        unpunctuated_sentence = re_punc.run(sentence)
        unpunctuated_doc.append(unpunctuated_sentence)
    return unpunctuated_doc

def doc_to_sent(document, idx_no):
    for sentence in document:
        return document

class predict:

    def __init__(self, sentence):
        self.sentence = sentence
        self.model_loc = get_file_path()
        self.data_frame = csv2dataframe()

    def load_model(self):
        model = Doc2Vec.load(self.model_loc)
        self.model = model

    def tokenized_input_sent(self):
        sentence = self.sentence
        sentence_lower = sentence.lower()
        input_sentence = word_tokenize(sentence_lower)
        self.input_sentence = input_sentence

    def set_code_index(self):
        try:
            self.data_frame.set_index("code", inplace=True)
        except KeyError:
            pass

    def predictor(self):
        tokenized_sentence = []
        code_results=[]
        sureity_percentage=[]
        matched_sentence=[]
        model = self.model
        for _ in range(2):         
            best_result = model.docvecs.most_similar(positive=[model.infer_vector(self.input_sentence)],topn=1)
            best_matched_code = best_result[0][0]            
            sureity_percent = best_result[0][1]
            sureity_percent = "{:.2%}".format(sureity_percent)
            most_similar_sentence = self.data_frame.loc[int(best_result[0][0]), "display"]
            most_similar_sentence_lst = list(most_similar_sentence)
            best_matched_sentence = most_similar_sentence_lst[0]
            code_results.append(best_matched_code)
            matched_sentence.append(best_matched_sentence)
            tokenized_sentence.append(word_tokenize(best_matched_sentence))
            sureity_percentage.append(sureity_percent)
        self.tokenized_sentence = tokenized_sentence
        self.code_results = code_results
        self.matched_sentence = matched_sentence
        self.sureity_percentage = sureity_percentage

    def matched_words(self):
        sentence_iter1 = 0
        sentence_iter2 = 0
        for value in self.input_sentence:
            if value in self.tokenized_sentence[0]:
                sentence_iter1 += 1
            if value in self.tokenized_sentence[1]:
                sentence_iter2 += 1
        self.sentence_iter1 = sentence_iter1
        self.sentence_iter2 = sentence_iter2

    def get_minimum(self):
        minimum_len = min(len(self.tokenized_sentence[0]),len(self.tokenized_sentence[1]), len(self.input_sentence))
        self.minimum_len = minimum_len

    def check_medical_terms(self):   

        if self.minimum_len >3:
            mod = 3
        else:
            mod = 2

        if self.sentence_iter1 >= mod or self.sentence_iter2 >= mod:               
            self.check_med_terms = True
        else:
            self.check_med_terms = False

    def detect_code(self):
        if self.check_med_terms:
            if self.sentence_iter1 >= self.sentence_iter2: 
                detected_code = self.code_results[0]
                detected_sentence = self.matched_sentence[0]
            else: 
                detected_code = self.code_results[1]
                detected_sentence = self.matched_sentence[1]
        else:
            detected_code = 0
            detected_sentence = 0
        self.detected_code = detected_code
        self.detected_sentence = detected_sentence

    def returner(self):
        return self.detected_code, self.detected_sentence

    def printer(self):
        printing_acessories = ["1 Iteration", "2 Iteration: ", "   <-------->   ",
         "Best matched Code: ", "Sureity percentage: ", "Best matched sentence: ", "    -->   ","%", "\n",
          "                 ---------|||>>>>>>>>>>>>|||---------"]
        print("Input Setence: "+ self.sentence + printing_acessories[-2])
        print(printing_acessories[3] + self.detected_code + printing_acessories[-2])
        print(printing_acessories[0] + printing_acessories[2] +printing_acessories[-2] +
        printing_acessories[3] + printing_acessories[6] + self.code_results[0] +
        printing_acessories[-2] + printing_acessories[4] + printing_acessories[6] +
        str(self.sureity_percentage[0]) + printing_acessories[-2] + printing_acessories[5] +
        printing_acessories[6] + self.matched_sentence[0] + printing_acessories[-2])

        print(printing_acessories[-1]+printing_acessories[-2])

        print(printing_acessories[1] + printing_acessories[2] + printing_acessories[-2] +
        printing_acessories[3] + printing_acessories[6] + self.code_results[1] +
        printing_acessories[-2] + printing_acessories[4] + printing_acessories[6] +
        str(self.sureity_percentage[1]) + printing_acessories[-2] + printing_acessories[5] +
        printing_acessories[6] + self.matched_sentence[1] + printing_acessories[-2])

def run(printer=True):
    document = sentence_tokenizer.run()
    unpunctuated_doc = remove_punctuation(document)
    codes = []
    sentences = []
    for sentence in unpunctuated_doc:
        prediction = predict(sentence)
        prediction.load_model()
        prediction.tokenized_input_sent()
        prediction.set_code_index()
        prediction.predictor()
        prediction.matched_words()
        prediction.get_minimum()
        prediction.check_medical_terms()
        prediction.detect_code()
        detected_code, detected_sentence = prediction.returner()
        if detected_code !=0:
            prediction.printer()
            codes.append(detected_code)
            sentences.append(detected_sentence)
        else:
            continue

    return codes, sentences

if __name__ == "__main__":
    print(run())

