
import os
import platform
import subprocess
from gtts import gTTS
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# 1. Load Environment Variables
load_dotenv()
ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY") # Make sure this matches your .env file exactly

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    
    play_audio(output_filepath)

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    
    # Save the audio file safely
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
            
    play_audio(output_filepath)

def play_audio(file_path):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', file_path])
            
        elif os_name == "Windows":  # Windows
            # We use ffplay because the default Windows player crashes with MP3s
            # -nodisp: No graphical window
            # -autoexit: Close when finished
            subprocess.run(['ffplay', '-nodisp', '-autoexit', file_path])
            
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', file_path])  
            
        else:
            raise OSError("Unsupported operating system")
            
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Testing line (comment out when running the full app)
# text_to_speech_with_elevenlabs("Testing the new player.", "test.mp3")