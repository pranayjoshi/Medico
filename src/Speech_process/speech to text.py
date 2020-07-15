import speech_recognition as sr     #Recognition Module
import pyttsx3                      #Speaking package

engine = pyttsx3.init()             #initialising pyttsx value

def speak(text):
    engine.say(text)
    engine.runAndWait()
#testing
speak('hi user')


def Voice_recognize(api_key, wait_time=5):
    #listens for commands

    r = sr.Recognizer()             #assigning recognize value

    with sr.Microphone() as source:

        speak('i am ready for your command')
        r.pause_threshold = wait_time                  # Check when the user takes the pause for 5 second
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()         #Using google's api
        speak('you said:' + command)

    
    except sr.UnknownValueError:            #loop back to continue to listen for commands if unrecognizable speech is received
        speak("Your last command couldn\'t be heard")
        command = Voice_recognize();        # runs the code again
    
    return command

def result(command):
    result = ">> " + command + "." + " \n"
    expected = "so after reading your report i came to know that you have been suffering from diarrhoea and here are some medicine for you crocin 650 paracetamol and Acetaminophen"
    print(f"Actual: {result}\nExpected: {expected}")
    mfopener = open("./Data_store/results.txt", "a+")
    mfopener.write(result)
    mfopener.close()

def run():
    api_key="GOOGLE_SPEECH_RECOGNITION_API_KEY"
    result(Voice_recognize(api_key=api_key))
    