import sounddevice as sd
import speech_recognition as sr
import speech_recognition.audio as audio_module
import edge_tts
import asyncio
import playsound3
import os
import json
from datetime import datetime


# ============================================================
# WINDOWS ARM64 FIX
# ============================================================

flac_path = os.path.join(
    os.path.dirname(audio_module.__file__),
    "flac-win32.exe"
)

audio_module.get_flac_converter = lambda: flac_path


# ============================================================
# SPEECH RECOGNIZER
# ============================================================

recognizer = sr.Recognizer()


# ============================================================
# TEXT TO SPEECH
# ============================================================

async def speak(text, filename):

    speech = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await speech.save(filename)

    playsound3.playsound(filename)


# ============================================================
# VOICE INPUT
# ============================================================

def listen():

    print("\n🎤 SERA is listening...")

    sample_rate = 16000
    duration = 5

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    print("✅ Recording finished!")

    audio_data = sr.AudioData(
        audio.tobytes(),
        sample_rate,
        2
    )

    try:

        text = recognizer.recognize_google(audio_data)

        print("You said:", text)

        return text.lower().strip()

    except sr.UnknownValueError:

        print("Sorry, I couldn't understand you.")
        return ""

    except sr.RequestError as e:

        print("Speech recognition service error:", e)
        return ""


# ============================================================
# GREETING
# ============================================================

def greet_user(name):

    print("=========================================")
    print("=========================================")
    print("          Project SERA v0.6")
    print("=========================================")
    print("=========================================")
    print(f"Hello, {name}")
    print("I am SERA.")
    print("Your personal AI assistant")


# ============================================================
# MAIN MENU
# ============================================================

def title():

    print("\n1. Study")
    print("2. Motivation")
    print("3. Information about me")
    print("4. Organizer")
    print("5. Voice Assistant")
    print("6. Exit")


# ============================================================
# STUDY MENU
# ============================================================

def study():

    print("\nLet's start learning.")
    print("1. Add Subjects")
    print("2. View Subjects")
    print("3. Remove Subjects")
    print("4. Back")


# ============================================================
# ORGANIZER MENU
# ============================================================

def organizer():

    print("\nLet's organize your day.")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Back")


# ============================================================
# MOTIVATION
# ============================================================

def motivation():

    print('KEEP LEARNING UNTIL "L" BECOMES SILENT')


# ============================================================
# ABOUT SERA
# ============================================================

def about_her():

    print("I am SERA.")
    print("Your new personal AI Assistant.")
    print("I am still growing.")


# ============================================================
# SUBJECT DISPLAY
# ============================================================

subjects = []


def subj():

    if len(subjects) == 0:
        print("No subjects found.")
    else:
        for i in range(len(subjects)):
            print(i + 1, subjects[i])


# ============================================================
# LOAD NAME
# ============================================================

try:

    with open("memory.txt", "r") as file:

        name = file.read()

        print("Welcome back,", name)

except FileNotFoundError:

    name = input("What is your name? ")

    with open("memory.txt", "w") as file:

        file.write(name)

    print("Nice to meet you.", name)


# ============================================================
# LOAD SUBJECTS
# ============================================================

try:

    with open("subjects.txt", "r") as file:

        for subject in file.readlines():

            subjects.append(subject.strip())

except FileNotFoundError:

    with open("subjects.txt", "w") as file:

        pass


# ============================================================
# LOAD TASKS
# ============================================================

try:

    with open("tasks.json", "r") as file:

        tasks = json.load(file)

        for task in tasks:

            task["due"] = datetime.strptime(
                task["due"],
                "%Y-%m-%d %H:%M"
            )

except FileNotFoundError:

    tasks = []


# ============================================================
# CHECK REMINDERS
# ============================================================

for task in tasks:

    if task["due"] <= datetime.now():

        print("⚠️ Task is due:", task["name"])


# ============================================================
# GREET USER
# ============================================================

greet_user(name)


# ============================================================
# MAIN LOOP
# ============================================================

main_running = True

speech_number = 1


while main_running:

    print("\nHow can I help you today?")

    title()

    choice = input("Enter your choice: ")


    # ========================================================
    # STUDY
    # ========================================================

    if choice == "1":

        study_running = True

        while study_running:

            study()

            choice1 = input("Enter your choice: ")


            # Add subject
            if choice1 == "1":

                add = input("Enter your subject: ")

                subjects.append(add)

                with open("subjects.txt", "w") as file:

                    file.write("\n".join(subjects))

                print("Your subject is added!")

                subj()


            # View subjects
            elif choice1 == "2":

                print("Your subjects are:")

                subj()


            # Remove subject
            elif choice1 == "3":

                print("Which subject do you want to remove?")

                subj()

                try:

                    remove = int(
                        input("Enter subject number: ")
                    )

                except ValueError:

                    print("Please enter a valid subject number.")
                    continue

                if 1 <= remove <= len(subjects):

                    removed_subject = subjects.pop(remove - 1)

                    print(
                        removed_subject,
                        "is removed!"
                    )

                    with open("subjects.txt", "w") as file:

                        file.write("\n".join(subjects))

                else:

                    print("Enter a valid number.")


            # Back
            elif choice1 == "4":

                study_running = False


            else:

                print(
                    "Invalid choice!"
                    "\nPlease select between 1 to 4."
                )


    # ========================================================
    # MOTIVATION
    # ========================================================

    elif choice == "2":

        motivation()


    # ========================================================
    # ABOUT SERA
    # ========================================================

    elif choice == "3":

        about_her()


    # ========================================================
    # ORGANIZER
    # ========================================================

    elif choice == "4":

        organizer_running = True

        while organizer_running:

            organizer()

            choice2 = input("Enter your choice: ")


            # Add task
            if choice2 == "1":

                task_name = input("Enter your task: ")

                task_date = input(
                    "Enter the date (DD-MM-YYYY): "
                )

                task_time = input(
                    "Enter the time (HH:MM): "
                )

                try:

                    due = datetime.strptime(
                        task_date + " " + task_time,
                        "%d-%m-%Y %H:%M"
                    )

                except ValueError:

                    print("Invalid date and time.")
                    continue

                task = {
                    "name": task_name,
                    "due": due
                }

                tasks.append(task)


                # Convert datetime to string for JSON
                tasks_to_save = []

                for task in tasks:

                    tasks_to_save.append({
                        "name": task["name"],
                        "due": task["due"].strftime(
                            "%Y-%m-%d %H:%M"
                        )
                    })


                with open("tasks.json", "w") as file:

                    json.dump(
                        tasks_to_save,
                        file,
                        indent=4
                    )


                print("Task added successfully!")


            # View tasks
            elif choice2 == "2":

                if len(tasks) == 0:

                    print("No task found.")

                else:

                    for i in range(len(tasks)):

                        print(
                            i + 1,
                            tasks[i]["name"],
                            "-",
                            tasks[i]["due"]
                        )


            # Remove task
            elif choice2 == "3":

                if len(tasks) == 0:

                    print("No tasks to remove.")
                    continue


                for i in range(len(tasks)):

                    print(
                        i + 1,
                        tasks[i]["name"]
                    )


                try:

                    remove = int(
                        input(
                            "Enter task number to remove: "
                        )
                    )

                except ValueError:

                    print(
                        "Please enter a valid task number."
                    )

                    continue


                if 1 <= remove <= len(tasks):

                    remove_task = tasks.pop(remove - 1)


                    tasks_to_save = []

                    for task in tasks:

                        tasks_to_save.append({
                            "name": task["name"],
                            "due": task["due"].strftime(
                                "%Y-%m-%d %H:%M"
                            )
                        })


                    with open("tasks.json", "w") as file:

                        json.dump(
                            tasks_to_save,
                            file,
                            indent=4
                        )


                    print(
                        "Task removed:",
                        remove_task["name"]
                    )

                else:

                    print("Enter a valid number.")


            # Back
            elif choice2 == "4":

                organizer_running = False


            else:

                print(
                    "Invalid choice!"
                    "\nPlease select between 1 to 4."
                )


    # ========================================================
    # VOICE ASSISTANT
    # ========================================================

    elif choice == "5":

        print("\n===================================")
        print("       🎤 SERA VOICE MODE")
        print("===================================")
        print("Say 'hello'")
        print("Say 'how are you'")
        print("Say 'stop' to leave voice mode")


        voice_running = True

        while voice_running:

            text = listen()


            if text == "":

                continue


            # Hello
            if text == "hello":

                response = "Hello! How can I help you?"


            # How are you
            elif text == "how are you":

                response = (
                    "I am doing great! "
                    "Thank you for asking."
                )


            # Stop voice mode
            elif text == "stop":

                response = "Leaving voice mode."

                voice_running = False


            # Unknown command
            else:

                response = (
                    "I heard you, but I don't "
                    "know that command yet."
                )


            print("SERA:", response)


            filename = f"speech{speech_number}.mp3"

            asyncio.run(
                speak(
                    response,
                    filename
                )
            )

            speech_number += 1


        print("\n🎤 Voice mode ended.")


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "6":

        print(f"Goodbye, {name}!")
        print("See you soon.")
        print("I am shutting down.")

        main_running = False


    # ========================================================
    # INVALID MAIN MENU CHOICE
    # ========================================================

    else:

        print(
            "Invalid choice!"
            "\nPlease select between 1 to 6."
        )


# ============================================================
# SERA STOPPED
# ============================================================

print("\n🛑 SERA has stopped.")