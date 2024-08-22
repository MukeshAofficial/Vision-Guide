from flask import Flask, render_template, request, jsonify,redirect, url_for
from gtts import gTTS
import google.generativeai as genai
import base64
import io
import os
import PIL.Image
from googletrans import Translator
import textwrap

app = Flask(__name__)
translator = Translator()
# Configure Generative AI
genai.configure(api_key="AIzaSyB4Go6j0e342y5l7mSvzyb4BWTDZFcW7oM")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/scan2')
def scan2():
    return render_template('scan2.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # Get the image data from the request
        data = request.json
        image_data = data.get('image')

        # Decode the base64 image data
        image_data = image_data.split(',')[1]
        image_binary = base64.b64decode(image_data)

        # Save the image to a file on your local PC
        img_path = 'captured_image.png'
        with open(img_path, 'wb') as img_file:
            img_file.write(image_binary)

        # Load the image
        img = PIL.Image.open(io.BytesIO(image_binary))

        # Use Generative AI model to generate text from the image
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(["Describe the scene in the image using beautiful and simple language", img], stream=True)
        response.resolve()

        # Generate speech from the extracted text
        tts = gTTS(text=response.text, lang='en')

        # Save the speech to a file
        audio_path = 'static/output.mp3'
        tts.save(audio_path)
        audio_url = f"/{audio_path}"
        
        return redirect(url_for('result'))

@app.route('/upload2', methods=['GET','POST'])
def upload2():
    if request.method == 'POST':
        # Get the image data from the request
        data = request.json
        image_data = data.get('image')

        # Decode the base64 image data
        image_data = image_data.split(',')[1]
        image_binary = base64.b64decode(image_data)

        # Save the image to a file on your local PC
        img_path = 'captured_image.png'
        with open(img_path, 'wb') as img_file:
            img_file.write(image_binary)

        # Load the image
        img = PIL.Image.open(io.BytesIO(image_binary))

        # Use Generative AI model to generate text from the image
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(["Describe the scene in the image using beautiful and simple language", img], stream=True)
        response.resolve()

        # Generate speech from the extracted text
        translated_text = translator.translate(response.text, dest='ta').text
        tts = gTTS(text=translated_text, lang='ta')

        # Save the speech to a file
        audio_path = 'static/output.mp3'
        tts.save(audio_path)
        audio_url = f"/{audio_path}"
        
        return redirect(url_for('result'))

@app.route('/gpt', methods=['GET', 'POST'])
def gpt():
    response_text = ""
    audio=''
    if request.method == 'POST':
        # Get transcribed text from the form
        transcribed_text = request.form.get('transcribed_text')
          
        # Generate response using the transcribed text
        if transcribed_text:
            # Generate response using Generative AI model
            model = genai.GenerativeModel('gemini-pro')
            rply = model.generate_content("explain in 3 lines"+ transcribed_text)
            response_text = rply.text
            print(response_text)
            # Convert response text to speech
            tts = gTTS(text=response_text, lang='en')
            tts.save('response.mp3')
            # Encode the audio file as base64
            with open("response.mp3", "rb") as audio_file:
                 encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')
        else:
            response_text = "No input provided."
            encoded_string = ""
        
        # Return the response to the client
        return render_template('gpt.html', response=response_text, audio=encoded_string)
    else:
        # If it's a GET request, render the form
        return render_template('gpt.html')
@app.route('/result')
def result():
    audio_url = "output.mp3"
    return render_template('result.html', audio=audio_url)

if __name__ == '__main__':
    app.run(debug=True)
