import pyttsx3

#text for audio
string="""Hello\n
        this is a sample run"""

# Initialize the converter
converter = pyttsx3.init()
  
# Set properties
# Set speed 150
converter.setProperty('rate', 150)
# Set volume 0.7
converter.setProperty('volume', 0.7)

converter.say(string)
  
converter.save_to_file(string, 'male.mp3')

converter.runAndWait()

