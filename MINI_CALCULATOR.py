import sys
sys.path.append('/calculator_modules/')
import calculator_modules
from calculator_modules.calculator import *
print(responses[0])
print(responses[1])
while True:
    print()
    import speech_recognition as sr

    r=sr.Recognizer()

    with sr.Microphone() as source:
        text=print("Say something")
        audio=r.listen(source)
        try:
            print("you said "+r.recognize_google(audio))
            text=r.recognize_google(audio)
        except:
            pass
        for word in text.split(' '):
            if word.upper() in operations.keys():
                try:
                    l=extract_numbers_from_text(text)
                    r=operations[word.upper()](l[0],l[1])
                    print(r)
                except:
                    print("something is wrong please try again")
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
        else:
            sorry()
            

