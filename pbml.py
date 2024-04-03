# app.py

from flask import Flask, render_template, request, jsonify
import pyttsx3 as pt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pb1.html')

@app.route('/test')
def test():
    return render_template('test1.html')

@app.route('/read_text')
def read_text():
    filename = request.args.get('filename')
    # Replace this with code to read text from the file
    # For demonstration, just returning a dummy text
    text = "This is a dummy text for demonstration purposes."
    engine = pt.init()
    
    engine.say(text)
    engine.runAndWait()
    return jsonify(text)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
