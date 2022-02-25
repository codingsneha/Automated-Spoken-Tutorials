import pyttsx3
import fileinput

#text for audio
file=open("data.txt")
data = file.read()
file.close()


# Initialize engine
engine = pyttsx3.init()
  
# Set properties
# Set speed percent 150
engine.setProperty('rate', 150)
# Set volume 0.7
engine.setProperty('volume', 0.7)

# Convert to female voice
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)

engine.save_to_file(data, 'tts.mp3')

engine.runAndWait()