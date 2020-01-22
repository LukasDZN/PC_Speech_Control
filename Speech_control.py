# Voice activated computer functions

# Importing modules
import speech_recognition as sr # For recognizing speech
import pyaudio # For audio input
import os # For pc control

# Set the text to '', because otherwise it'll bring up 'name undefined' error
text = ""

# Creating a recognizer instance
r = sr.Recognizer()

# # Recognize the microphone (1 is the USB microphone, which is not primary (0))
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

with sr.Microphone(device_index=1) as source:

    # Automatically adjust for how sensitive sounds the microphone should listen to
    r.adjust_for_ambient_noise(source, duration=5) # duration added for longer adjustment period for added accuracy. (recommended 1 sec)
    
    def ContinueListening(source):
        
        # Indicate to the user to begin speaking
        print('Speak anything: ')
        # Set the threshold manually
        # r.energy_threshold = 50
        
        # Listen to the audio
        audio = r.listen(source)
        
        # Attempt to transcribe the audio
        try:
            text = r.recognize_google(audio)
            print(f'You said: {text}')
            
            # Phrases to comprehend
            # Music to play
            if text == 'music':
                os.startfile('https://www.youtube.com/watch?v=K9mNaZRDhUk')
            elif text == 'rick roll':
                os.startfile('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            elif text == 'relax':
                os.startfile('https://www.youtube.com/watch?v=Ws6xaVnusbc&list=PLL4ISqWNFxSEAykkmvLWEHZwf5wCfx68I&index=2&t=0s')
            elif text == 'epic': # Theoden's speech LOTR
                os.startfile('https://youtu.be/POdknqszMDY?t=145')
            elif text == 'good music': # baisi realybe 
                os.startfile('https://www.youtube.com/watch?v=fzVe_0l1EaM')
            # PC control
            elif text == 'sleep':
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        # Print the error message if voice is not recognized
        except:
            print('Could not recognize your voice')
        
        # Indicating the end of one listening cycle
        print('\nDone')
        
        # Reinitiate the listening cycle
        ContinueListening(source)
    
    # Initiate the program
    ContinueListening(source)

# Thourough documentation
# https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
