from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/audio', methods=['POST'])
def analyze_audio():
    # Placeholder für die Audioanalyse-Logik
    audio_data = request.files['audio']
    # Dummy-Response
    return jsonify({'message': 'Audio erfolgreich analysiert', 'feedback': 'Verbessere deine Aussprache!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
