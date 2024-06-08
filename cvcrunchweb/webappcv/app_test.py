from flask import render_template, Flask
from utils.forms import LoginForm, SignupForm  # Adjust the import path based on your project structure
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)

Bootstrap(app)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Handle form processing
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # Handle form processing
    return render_template('signup.html', form=form)

if __name__ ==  "__main__":
    app.run(debug=True)
    
