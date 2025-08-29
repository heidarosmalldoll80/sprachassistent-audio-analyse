from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Render index.html as the homepage
    return render_template('index.html')

@app.route('/api/audio', methods=['POST'])
def analyze_audio():
    # Function to handle audio file uploads and analysis
    # Check if an audio file has been uploaded
    if 'audio' not in request.files:
        return jsonify({'error': 'Keine Audiodatei hochgeladen!'}), 400
    audio_data = request.files['audio']
    # Check if the uploaded file is empty
    if audio_data.filename == '':
        return jsonify({'error': 'Die hochgeladene Audiodatei ist leer!'}), 400
    # TODO: Implement the audio analysis logic here
    # Currently, returning a dummy response
    # Debugging statement to log the uploaded file details
    print(f"Uploaded audio file: {audio_data.filename}")
    return jsonify({'message': 'Audio erfolgreich analysiert', 'feedback': 'Verbessere deine Aussprache!'}), 200

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)