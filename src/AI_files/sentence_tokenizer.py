from spacy.lang.en import English
import filepath as fp
import sys
sys.path.append('./src/Data_process')
import fetch_recent_conv as frc
def get_file_path():
    results = fp.run("results")
    return results
def fetch_recent_conversation(results):
    recent_conversation = frc.run(results)
    return recent_conversation
class sentence_tokenizer:
    def __init__(self, recent_conversation):
        pass
    def sentence_tokenizer(self):
        nlp = English()

        # Create the pipeline 'sentencizer' component
        sbd = nlp.create_pipe('sentencizer')

        # Add the component to the pipeline
        nlp.add_pipe(sbd)

        text = """When learning data science, you shouldn't get discouraged!
        Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

        #  "nlp" Object is used to create documents with linguistic annotations.
        doc = nlp(text)

        # create list of sentence tokens
        sents_list = []
        for sent in doc.sents:
            sents_list.append(sent.text)
        print(sents_list)
def run():
    results = get_file_path()
    recent_conversation = fetch_recent_conversation(results)
    sentence_tokenize = sentence_tokenizer(recent_conversation)