from flask import *
from model import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/request-counter')
def counter():
    number = Counter()
    # c = number.counter

    return render_template('counter.html', number = number)


if __name__ == '__main__':
    app.run(debug=True)
