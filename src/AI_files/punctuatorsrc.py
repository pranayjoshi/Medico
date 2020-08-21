from punctuator import Punctuator
import sys
sys.path.append('./src/Data_process')
import fetch_recent_conv as frc
import filepath

def get_filepath():
    results_loc = filepath.run("results")
    punctuator_model_loc = filepath.run("punctuator_model")
    return results_loc, punctuator_model_loc

def punctuate_conversation(conversation, loc):
    p = Punctuator(loc)
    punctuated_converse = p.punctuate(conversation)
    return punctuated_converse
def run():
    results_loc, punctuator_model_loc = get_filepath()
    conversation = frc.run(results_loc)
    location = "./src/AI_files/punctuator/Demo-Europarl-EN.pcl"
    punctuate_conv = punctuate_conversation(conversation, loc=location)
    return punctuate_conv
if __name__ == "__main__":   
    print(run())

