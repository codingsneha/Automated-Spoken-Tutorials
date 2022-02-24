import pyttsx3

#text for audio
string="""Hello\n
        this is a sample run"""

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

engine.say(string)

engine.save_to_file(string, 'female.mp3')

engine.runAndWait()