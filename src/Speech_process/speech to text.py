import speech_recognition as sr     #Recognition Module
import pyttsx3                      #Speaking package
import json
import series_counter as s_c

engine = pyttsx3.init()             #initialising pyttsx value

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak('hi user')

def Voice_recognize(wait_time, noice_duration):
    #listens to commands

    r = sr.Recognizer()             #assigning recognize value

    with sr.Microphone() as source:

        speak('i am ready for your command')
        r.pause_threshold = wait_time                  # Check when the user takes the pause for 5 second
        r.adjust_for_ambient_noise(source, duration=noice_duration)
        audio = r.listen(source)

    try:
        #Using google's api, 
        output = r.recognize_google(audio).lower()  #Well I want to use the default language so I am leaving the language field
        speak('you said:' + output)        # use this before using "language" attribute <lang = langs["Hindi"]>

    
    except sr.UnknownValueError:            #loop back to continue to listen for commands if unrecognizable speech is received
        speak("Your last command couldn\'t be heard")
        output = Voice_recognize();        # runs the code again
    
    return output
class speech_to_text:
    def __init__(self,count, output, results_loc):
        self.count = count
        self.output = output
        self.results_loc = results_loc

    def counter(self):
        self.present_count = self.count

    def result_formatter(self):
        self.final_result = self.present_count + " "
        self.final_result += self.output + " \n"

    def result_to_txt(self):
        with open(self.results_loc, "a+",  encoding='utf8') as mfopener:
            mfopener.write(self.final_result)

    def result_returner(self):
        return self.final_result

# this class will act as a test printer
class test_printer:
    def __init__(self, actual):
        self.actual = actual
    def test_input(self):
        self.expected = "so after reading your report i came to know that you have been suffering from diarrhoea and here are some medicine for you crocin 650 paracetamol and Acetaminophen"
    def printer(self):
        out = (f"Actual: {self.actual}\nExpected: {self.expected}")
        return out   
class run_utils:
# returns the path required
    def __init__(self, present_count):
        self.present_count = present_count
    def file_paths(self):
        with open("./storage/path.json", "r+") as file:       #for mailing system
            data = json.load(file)
        results_loc = data["results"]
        self.results_loc = results_loc
 
    #runs the Voice_recognize function
    def run_Vr(self):
        wait_time,duration=5,0.5
        Voice_recog = Voice_recognize(wait_time, duration)
        self.output = Voice_recog

    # run all the functions in the speech_to_text class
    def run_all_s2t(self):
        s2t = speech_to_text(self.present_count, self.output, self.results_loc)
        s2t.counter()
        s2t.result_formatter()
        s2t.result_to_txt()             
        self.return_result = s2t.result_returner()

    def run_printer(self):
        tst_print = test_printer(self.output)
        tst_print.test_input()
        self.printer = tst_print.printer
    
    def printer(self):
        return self.printer
#this script will run all
def run_all(present_count):
    r_utils = run_utils(present_count)
    r_utils.file_paths()
    r_utils.run_Vr()
    r_utils.run_all_s2t()
    r_utils.run_printer()
    printer = r_utils.printer()
    return printer
# finally run the script
def run():
    present_count = s_c.run()
    printer = run_all(present_count)
    print(printer)
if __name__ == "__main__":
    run()
    