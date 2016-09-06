from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/request-counter')
def counter():
    
    return '1'

if __name__ == '__main__':
    app.run(debug=True)
