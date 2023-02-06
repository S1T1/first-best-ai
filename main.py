import openai
import pyttsx3
import speech_recognition as sr
from api_key import API_KEY

openai.api_key = API_KEY

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Shrey"
bot_name = "Mark"

while True:
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("No longer listening.")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = f"{user_name}: {user_input}\n{bot_name}: "
    conversation += prompt

    response = openai.Completion.create(
        engine='text-davinci-003', prompt=conversation, max_tokens=100
    )
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(f"{user_name}: ", 1)[0].split(f"{bot_name}: ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()