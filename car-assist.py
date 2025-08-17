
import SpeechRecognition as sr, pyttsx3, time, random
r = sr.Recognizer(); tts = pyttsx3.init()

def say(x): tts.say(x); tts.runAndWait()

def fatigue_detector():
    return random.random() < 0.08

def listen():
    with sr.Microphone() as src:
        audio = r.listen(src, phrase_time_limit=5)
    try: return r.recognize_google(audio).lower()
    except: return ""

if __name__ == "__main__":
    say("Car assistant online.")
    last_check = time.time()
    while True:
        if time.time() - last_check > 15:
            if fatigue_detector(): say("Alert. Please take a short break and hydrate.")
            last_check = time.time()
        cmd = input("Command (say/play/exit): ").strip().lower()
        if cmd == "exit": say("Drive safe."); break
        elif cmd.startswith("play"):
            song = cmd.replace("play","").strip() or "music"
            say(f"Playing {song}.")
        elif cmd.startswith("navigate"):
            dest = cmd.replace("navigate","").strip()
            say(f"Starting route guidance to {dest}.")
        else:
            say("I can play music or start navigation.")
