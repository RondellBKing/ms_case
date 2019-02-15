from flask import Flask, render_template, request
app = Flask(__name__)

""" 
Rondell King - Morgan Stanley Case study Part 2.

To run this simple app do run below in cmd/terminal. Then open -> http://127.0.0.1:5000/
---> python case_study_part_2.py
"""


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form  # Input data from webpage
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
