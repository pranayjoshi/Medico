import sys
sys.path.append("./src/AI_files")
sys.path.append("./src/Speech_process")
import speech_to_text 
import detector

speech_to_text.run()
print(detector.run())