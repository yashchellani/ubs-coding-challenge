from flask import Flask, request
from question1 import solve_question

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

#endpoint for the api where the request body contains a string
@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        #get the string from the request body
        string = request.data
        #return the string in the response body
        return solve_question(string)


if __name__ == '__main__':
    app.run(debug=True)