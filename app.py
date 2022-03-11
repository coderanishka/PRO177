from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
  {
      'inputs': '7',
      'word': 'Anishka',
      'clue': 'My Name!'
  },     
  {
      'inputs': '6',
      'word': 'Laptop',
      'clue': 'You use me to code!'
  }, 
  {
      'inputs': '5',
      'word': 'India',
      'clue': 'Place of huge cultural diversity'
  }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-template')
def get_template():
    return jsonify({
        'status': 'success',
        'word': random.choice(templates)
    })
if __name__ == '__main__':
    app.run()