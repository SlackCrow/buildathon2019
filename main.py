from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


# Main Web-page path
@app.route("/")
def main():
    return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect("home.html")
    return render_template("login.html")


@app.route("/home", methods=['GET','POST'])
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
