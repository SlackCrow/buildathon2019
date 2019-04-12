from flask import Flask
from data import Articles
app = Flask(__name__)


# Main Web-page path
@app.route("/")
def inputPage():
    #return "Hello World!"
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
