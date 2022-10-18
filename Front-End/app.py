from bidict import bidict
from random import choice
from flask import (
    Flask, render_template, request,
    redirect, url_for, session
)
#from tensorflow import keras


ENCODER = bidict({
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
})

app = Flask(__name__)
app.secret_key = 'DBMhandwriting'

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route('/add-data', methods=['GET'])
def add_data_get():
    message = session.get('message', '')
    letter = choice(list(ENCODER.keys()))
    #image = "eleph.jpg"
    return render_template("addData.html", letter=letter, message=message)

@app.route('/add-data', methods=['POST'])
def add_data_post():
    label = request.form['letter']
    print(label)
    pixels = request.form['pixels']
    pixels = pixels.split(',')
    print(len(pixels))

    session['message'] = f'"{label}" added to the word'
    return redirect(url_for("add_data_get"))

if __name__ == '__main__':
    app.run(debug=True)