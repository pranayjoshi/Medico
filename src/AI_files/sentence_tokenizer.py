from spacy.lang.en import English
import filepath as fp
import sys
sys.path.append('./src/Data_process')
import punctuatorsrc as prc

def fetch_recent_conversation():
    recent_conversation = prc.run()
    return recent_conversation

class sentence_tokenizer:

    def __init__(self, recent_conversation):
        self.recent_conversation = recent_conversation

    def sentence_tokenizer(self):
        nlp = English()

        # Create the pipeline 'sentencizer' component
        sbd = nlp.create_pipe('sentencizer')

        # Add the component to the pipeline
        nlp.add_pipe(sbd)
        nlp.add_pipe(set_custom_boundaries, before="sentencizer")

        #  "nlp" Object is used to create documents with linguistic annotations.
        text = self.recent_conversation
        doc = nlp(text)

        # create list of sentence tokens
        sents_list = []      
        for sent in doc.sents:
            sents_list.append(sent.text)
        return sents_list

def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text in ("’s", "'s"):
            doc[token.i].is_sent_start = False
        if token.text in (",", ","):
            doc[token.i].is_sent_start = True
    return doc

def run():
    recent_conversation = fetch_recent_conversation()
    sentence_tokenize = sentence_tokenizer(recent_conversation)
    sent_tokenize = sentence_tokenize.sentence_tokenizer()
    return sent_tokenize

if __name__ == "__main__":
    print(run())