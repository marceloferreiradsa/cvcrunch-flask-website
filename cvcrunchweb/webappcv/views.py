import os
import uuid
import time
import json
import glob
from flask import (Blueprint, render_template, jsonify, flash, 
                   request, session, redirect, url_for)
from flask import current_app as app
from flask_login import login_user, current_user, login_required, logout_user
from flask_wtf.csrf import generate_csrf, CSRFProtect, CSRFError, validate_csrf
from openai import OpenAI
from werkzeug.utils import secure_filename
from .utils.parse import allowed_file, parse_file, ALLOWED_EXTENSIONS
from .utils.api_call import load_file, call_openai_api
from .utils.models import User, db
from .utils.forms import LoginForm, SignupForm, ResetRequestForm, ResetPasswordForm
from .utils.reset import get_reset_token, verify_reset_token, send_reset_email
from .utils.fetch_image import get_photo_url
from werkzeug.exceptions import BadRequest

main = Blueprint('main', __name__)

@main.route('/refresh-csrf', methods=['GET'])
def refresh_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@main.route('/')
def home():
    if current_user.is_authenticated:
        user_id = current_user.user_id
        existing_image = get_photo_url(user_id)
        print("autenticou", existing_image)
    else:
        print("não antenticado")
        existing_image = '../static/images/sillouete_1.webp'
    return render_template('index.html', profile_image = existing_image)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    
    if form.validate_on_submit():
        
        
        if user is None:
            
            flash('Confira email e/ou senha')
            return redirect(url_for('main.login'))
        
        elif user.check_password(form.password.data) and user is not None:
            
            login_user(user)
            show_dropdown = True 
            next = request.args.get('next')
            
            if next ==None or not next[0]=='/':
                next = url_for('main.home')

            return redirect(next)
    else:
        # Print errors to the terminal
        print("Form Errors:", form.errors)
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(f"Error in {fieldName}: {err}")
        
    # Handle form processing
    return render_template('login.html', form=form)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    existing_user = User.query.filter_by(email=form.email.data).first()
    if existing_user is not None:
        # If a user is found, flash an error message and redirect to the signup page
        flash('Verifique email e senha e tente novamente', 'error')
        return render_template('main.signup', form=form)
    elif form.validate_on_submit():
        user = User(email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Parabéns, registro com sucesso!")
        return redirect(url_for('main.login', form=form))
    else:
        app.logger.error('Validation errors occurred with the signup form:')
        for fieldName, errorMessages in form.errors.items():
            app.logger.error(f'{fieldName}: {", ".join(errorMessages)}')
    # Handle form processing
    return render_template('signup.html', form=form)

@main.route('/reset_request', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = ResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('main.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@main.route('/reset_token/<token>', methods=['GET', 'POST'])
def reset_token(token):
    print(f"reset_token route called with token: {token}")
    user_id = verify_reset_token(token)
    if user_id is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('main.reset_request'))
    user = User.query.get(user_id)
    form = ResetPasswordForm()
    if request.method=='POST':
        print('method post identified')
        if form.validate_on_submit():
            print("validou form resetpassword")
            user.set_password(form.password.data)
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('main.login'))
    return render_template('reset_token.html', title='Reset Password', form=form, token=token)

@main.route("/upload",methods=["POST","GET"])
def upload():
    success_message = False
    try:
        validate_csrf(request.form.get("csrf_token"))
    except BadRequest:
        return "CSRF token error", 400  # Or handle the error in a way that fits your application

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        
                     
        if file and allowed_file(file.filename):
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           unique_id = str(uuid.uuid4())
           session['unique_id'] = unique_id
           cv_path = os.path.join('webappcv', 'static', 'uploads', 'CV_' + unique_id + '_' + str(int(time.time())) + '.txt')
           session['session_cv'] = cv_path
           print(session['unique_id'])
           print(session['session_cv'])
           script_path = os.path.abspath(__file__)
           print("This script is located at:", script_path)
           new_text = parse_file(file, filename)
           with open(cv_path, 'w', encoding='utf-8') as file:
               file.write(new_text)
            
           success_message = True
           data = {"message": success_message} 
           
           print("executei")
        else:
           success_message = f'Invalid Upload. Only allowed {ALLOWED_EXTENSIONS} '
    message=success_message
    data = {"message": message}
    return jsonify(data)
 
@main.route('/textPaste', methods=['POST'])
def process_text():
    data = request.get_json()
    text_content = data['text']
    unique_id = session['unique_id']
    jd_path = os.path.join('webappcv', 'static', 'uploads', 'JD_'+ unique_id + '_' + str(int(time.time())) + '.txt')
    session['session_jd'] = jd_path
    # Write the text content to a .txt file
    with open(jd_path, 'w', encoding='utf-8') as file:
        file.write(text_content)
    return jsonify({'message': 'File saved successfully'})

@main.route('/apiCall', methods=['POST'])
def call_api():
    print("Entrou no código /apiCall")
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    folder = os.getcwd()
    unique_id = session['unique_id']
    cv = load_file(session['session_cv'])
    session_jd = session['session_jd']
    jd = load_file(session_jd)
    
    messages = call_openai_api(cv, jd, client)
    ms_path = os.path.join('webappcv', 'static', 'uploads', 'MS_'+ unique_id + '_' + str(int(time.time())) + '.json')
    session['api_report_path'] = messages[4]
    
    # Write the text content to a .txt file
    with open(ms_path, 'w', encoding='utf-8') as json_file:
        json.dump(messages, json_file, ensure_ascii=False)
    return jsonify({'message': 'File saved successfully'})

@main.route('/rollback', methods=['GET'])
def rollback():
    pass

@main.route('/report')
def step_four():
    
    return jsonify(session['api_report_path'])

@main.route('/test_db')
def test_db():
    # Query the first user in the database
    user = User.query.first()
    if user:
        print(f'User found: {user.user_name}, Email: {user.email}')
    else:
        print('No user found')
    return f'Check your terminal for output!'

@main.route('/profile')
def profile():
    if not current_user.is_authenticated:
       redirect(url_for('main.login'))
    else:
        existing_image = get_photo_url(current_user.user_id)
    return render_template('profile.html', profile_image=existing_image)
        
@main.route('/profile/picture', methods=['POST'])
def handle_upload():
    # Flask-WTF csrf_protect can be used here if CSRF is not validated globally
    file = request.files.get('file')
    if file:
        filename = secure_filename(file.filename)
        user_id = current_user.user_id
        ext = file_extension = os.path.splitext(filename)[1]
        file_path = os.path.join(os.path.dirname(__file__),'static', 'images', 'profiles', user_id + ext)
        print(os.path.dirname(__file__))
        file.save(file_path)
        # Optionally, save/update user profile image path in the database
        return redirect(url_for('main.profile'))  # Assuming 'main.profile' is a valid endpoint
    else:
        return redirect(url_for('main.profile'))

@main.errorhandler(CSRFError)
def handle_csrf_error(e):
    try:
        return render_template('csrf_error.html', reason=e.description), 400
    except :
        return 'CSRF error: ' + str(e.description), 400

      
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))