from flask import Flask, render_template
import os

app = Flask(__name__)

def get_interests():
    interests = [
        'computer science',
        'coffee'
        'yoga',
        'pure math',
        'RuPaul\'s Drag Race',
        'the color orange'
    ]
    return interests


@app.route('/')
def home():
    return render_template('index.html', interests=get_interests())


if __name__ == "__main__":
    app.run(debug=True)