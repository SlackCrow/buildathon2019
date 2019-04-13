from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


# Main Web-page path
@app.route("/")
def main():
    return redirect(url_for('login'))


# Route to login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    # Check for re-direct from login
    if request.method == 'POST':
        return redirect("home.html")
    return render_template("login.html")


# Route for home page
@app.route("/home", methods=['GET', 'POST'])
def home():
    # Verification of blockchain history to determine...
    # If there are: outstanding liens, unpaid taxes, or outstanding judgements, then return failure_page
    # Else Return success page
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
