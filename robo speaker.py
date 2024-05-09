import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Pathik")
    while True:
        x = input("Enter what you want me to Speak:")
        if x == 'q':
            print("Bye Bye freind")
            break
    # Initialize the text-to-speech engine
        engine = pyttsx3.init()
    
    # Say the input text
        engine.say(x)
    
    # Wait for the speech to finish
        engine.runAndWait()

