import os
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'  # Change to your SMTP server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_CVCRUNCH_USERNAME')  # Change to your email
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_CVCRUNCH_PASSWORD')  # Change to your email password
app.config['MAIL_DEFAULT_SENDER'] = "no-reply@cvcrunch.com"  # Optional

mail = Mail(app)

@app.route('/')
def index():
    msg = Message("Hello from Flask-Mail",
                  recipients=["marcelo.ferreira.dsa@gmail.com"])  # Change to recipient's email
    msg.body = "This is a test email sent from a Flask application using Flask-Mail."
    mail.send(msg)
    return "Email sent!"

if __name__ == '__main__':
    app.run(debug=True)
