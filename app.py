from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import io
import os

from config import host, port, ffmpeg_bin_folder

os.environ["PATH"] += os.pathsep + ffmpeg_bin_folder
from pydub import AudioSegment

AudioSegment.converter = ffmpeg_bin_folder + r"\ffmpeg.exe"
AudioSegment.ffmpeg = ffmpeg_bin_folder + r"\ffmpeg.exe"
AudioSegment.ffprobe = ffmpeg_bin_folder + r"\ffprobe.exe"

app = Flask(__name__)
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        audio_file = request.files['file']
        
        # Read the raw browser audio (WebM/MP4) using pydub
        audio_segment = AudioSegment.from_file(audio_file)
        
        # Export it in-memory as a true PCM WAV
        wav_io = io.BytesIO()
        audio_segment.export(wav_io, format="wav")
        wav_io.seek(0) # Reset the file pointer to the beginning
        
        # Pass the valid WAV data to speech_recognition
        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)
            
        # Convert to text
        text = recognizer.recognize_google(audio_data)
        print(f"User said: {text}")
        
        return jsonify({"status": "success", "text": text})

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return jsonify({"status": "error", "message": "Could not understand audio. Try speaking clearer."})
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return jsonify({"status": "error", "message": "API unavailable."})
    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)