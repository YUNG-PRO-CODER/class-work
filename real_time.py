import datetime
import random
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
current_voice = 0  

def speak(text):
    engine.setProperty('voice', voices[current_voice].id)
    engine.say(text)
    engine.runAndWait()

fun_facts = [
    "Honey never spoils.",
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries aren't.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus."
]

name = input("Enter your name: ")

def greet():
    return f"Hello {name}, how can I help you today?"

def get_date():
    today = datetime.date.today()
    return f"Today's date is {today.strftime('%B %d, %Y')}"

def random_fact():
    return random.choice(fun_facts)

def change_voice():
    global current_voice
    choice = input("Choose voice (male/female): ").lower()

    if choice == "male":
        current_voice = 0
        return "Switched to male voice"
    elif choice == "female":
        current_voice = 1
        return "Switched to female voice"
    else:
        return "Invalid choice. Try again."

def assistant():
    print(greet())
    speak(greet())

    while True:
        try:
            command = input("\nEnter command: ").lower()

            if command == "date":
                response = get_date()

            elif command == "greet":
                response = greet()

            elif command == "fun fact":
                response = random_fact()

            elif command == "voice":
                response = change_voice()

            elif command == "exit":
                response = "Goodbye!"
                print(response)
                speak(response)
                break

            else:
                response = "Sorry, I didn't understand that command."

            print(response)
            speak(response)

        except Exception as e:
            print("Something went wrong:", e)

assistant()