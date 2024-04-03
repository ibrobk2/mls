from flask import Flask, render_template, request, redirect
import pyttsx3

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for displaying learning modules
@app.route('/modules', methods=["GET"])
def modules():
    # Logic to retrieve and display learning modules
    return render_template('modules.html')

# Route for displaying individual lessons
# @app.route('/lesson/<lesson_id>')
# def lesson(lesson_id):
#     # Logic to retrieve and display lesson content
#     return render_template('lesson.html', lesson_id=lesson_id)


# Route for displaying individual lessons
# @app.route('/lesson1')
# def lesson1():
#     # Logic to retrieve and display lesson content
#     return render_template('lesson1.html')


def t2s(lesson):
    
    modified = []
    file = open(lesson, "r")
    reader = file.readlines() 
        
    for line in reader:
        if line[-1] == '\n':
            modified.append(line[:-1])
        else:
            modified.append(line)
    
    text = modified
    # print(text)
    
    # initialize pyttsx3
    engine = pyttsx3.init()

    # Initialize and configure the pyttsx3 engine
   
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # Adjust the volume level (0.0 to 1.0)
   
    """VOICE"""
    voice = voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    print(voice[0])
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
    
    if engine._inLoop:
        engine.endLoop()




@app.route('/lesson', methods=['POST', 'GET'])
def lesson():
    if request.method == 'POST':
      
        t2s('lesson1.txt')
        
        return render_template('/lesson.html')
    return render_template('/lesson.html')


@app.route('/lesson1', methods=['POST', 'GET'])
def lesson1():
    if request.method == 'POST':
      
        t2s('lesson1.txt')
        
        return render_template('/lesson1.html')
    return render_template('/lesson1.html')


@app.route('/lesson2', methods=['POST', 'GET'])
def lesson2():
    if request.method == 'POST':
        t2s('lesson2.txt')

        return render_template('/lesson2.html')
    return render_template('/lesson2.html')


@app.route('/lesson3', methods=['POST', 'GET'])
def lesson3():
    if request.method == 'POST':
        t2s('lesson3.txt')

        return render_template('/lesson3.html')
    return render_template('/lesson3.html')


@app.route('/lesson4', methods=['POST', 'GET'])
def lesson4():
    if request.method == 'POST':
        t2s('lesson4.txt')

        return render_template('/lesson4.html')
    return render_template('/lesson4.html')


@app.route('/lesson5', methods=['POST', 'GET'])
def lesson5():
    if request.method == 'POST':
        t2s('lesson5.txt')

        return render_template('/lesson5.html')
    return render_template('/lesson5.html')


@app.route('/lesson6', methods=['POST', 'GET'])
def lesson6():
    if request.method == 'POST':
        t2s('lesson6.txt')

        return render_template('/lesson6.html')
    return render_template('/lesson6.html')


@app.route('/lesson7', methods=['POST', 'GET'])
def lesson7():
    if request.method == 'POST':
        t2s('lesson7.txt')

        return render_template('/lesson7.html')
    return render_template('/lesson7.html')



@app.route('/lesson8', methods=['POST', 'GET'])
def lesson8():
    if request.method == 'POST':
        t2s('lesson8.txt')

        return render_template('/lesson8.html')
    return render_template('/lesson8.html')



@app.route('/lesson9', methods=['POST', 'GET'])
def lesson9():
    if request.method == 'POST':
        t2s('lesson9.txt')

        return render_template('/lesson9.html')
    return render_template('/lesson9.html')


@app.route('/lesson10', methods=['POST', 'GET'])
def lesson10():
    if request.method == 'POST':
        t2s('lesson10.txt')

        return render_template('/lesson10.html')
    return render_template('/lesson10.html')

# Problem Based Section
@app.route('/pb1', methods=['POST', 'GET'])
def pb1():
    if request.method == 'POST':
        t2s('pb1.txt')

        return render_template('/pb1.html')
    return render_template('/pb1.html')



@app.route('/pb2', methods=['POST', 'GET'])
def pb2():
    if request.method == 'POST':
        t2s('pb2.txt')

        return render_template('/pb2.html')
    return render_template('/pb2.html')



@app.route('/pb3', methods=['POST', 'GET'])
def pb3():
    if request.method == 'POST':
        t2s('pb3.txt')

        return render_template('/pb3.html')
    return render_template('/pb3.html')



@app.route('/pb4', methods=['POST', 'GET'])
def pb4():
    if request.method == 'POST':
        t2s('pb4.txt')

        return render_template('/pb4.html')
    return render_template('/pb4.html')


@app.route('/pb5', methods=['POST', 'GET'])
def pb5():
    if request.method == 'POST':
        t2s('pb5.txt')

        return render_template('/pb5.html')
    return render_template('/pb5.html')


@app.route('/pb6', methods=['POST', 'GET'])
def pb6():
    if request.method == 'POST':
        t2s('pb6.txt')

        return render_template('/pb6.html')
    return render_template('/pb6.html')



@app.route('/pb7', methods=['POST', 'GET'])
def pb7():
    if request.method == 'POST':
        t2s('pb7.txt')

        return render_template('/pb7.html')
    return render_template('/pb7.html')


@app.route('/pb8', methods=['POST', 'GET'])
def pb8():
    if request.method == 'POST':
        t2s('pb8.txt')

        return render_template('/pb8.html')
    return render_template('/pb8.html')


@app.route('/pb9', methods=['POST', 'GET'])
def pb9():
    if request.method == 'POST':
        t2s('pb9.txt')

        return render_template('/pb9.html')
    return render_template('/pb9.html')


@app.route('/pb10', methods=['POST', 'GET'])
def pb10():
    if request.method == 'POST':
        t2s('pb10.txt')

        return render_template('/pb10.html')
    return render_template('/pb10.html')
# End of PB section

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
