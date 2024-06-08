from itsdangerous import URLSafeTimedSerializer as Serializer, BadSignature, SignatureExpired
from flask_mail import Message
from flask import url_for
from .. import mail
from flask import current_app


def get_reset_token(user_id, expires_sec=1800):
    print(type(current_app.config['SECRET_KEY']), current_app.config['SECRET_KEY'])
    print(type(user_id), user_id)
    s = Serializer(secret_key=current_app.config['SECRET_KEY'], salt='reset' )
    token = s.dumps({'user_id': str(user_id)})
    print("Generated token:", token)
    return token

def verify_reset_token(token):
    s = Serializer(current_app.config['SECRET_KEY'], salt='reset')
    try:
        data = s.loads(token, max_age=1800)
    except (BadSignature, SignatureExpired):
        return None
    user_id = data.get('user_id')
    return user_id

def send_reset_email(user):
    token = get_reset_token(user.user_id)
    msg = Message('Password Reset Request',
                  sender='no-reply@cvcrunch.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: 
                {url_for('main.reset_token', token=token, _external=True)}
                If you did not make this request then simply ignore this email and no changes will be made.'''
    mail.send(msg)