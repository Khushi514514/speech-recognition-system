import speech_recognition as sr


# Initialize the recognizer
recognizer = sr.Recognizer()

print("Say something! (Press Ctrl+C to stop)\n")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"{text}\n")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.\n")

    except sr.RequestError as e:
        print(f"Could not request results; check your internet. Error: {e}\n")

    except KeyboardInterrupt:
        print("Exiting... Bye!")
        break



