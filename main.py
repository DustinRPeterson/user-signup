from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_signup.html', title="User Signup")

@app.route("/user-signup", methods=['POST', 'GET'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    email = request.form['email']

    valid_username = validate_username(username)
    valid_password = validate_password(password)
    match_password = passwords_match(password, confirm_password)
    valid_email = validate_email(email)

    if valid_username == True and valid_password == True and match_password == True and valid_email == True:
        return render_template('welcome.html', username=username)
    else:
        if valid_username == False:
            username = ''
        if valid_email == False:
            email = ''
        return render_template('user_signup.html', username = username, valid_username=valid_username, valid_password=valid_password, match_password=match_password, email = email, valid_email=valid_email)


def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        return False
    elif username.isalnum() == False:
        return False
    else:
        return True

def validate_password(password):
    if len(password) < 3 or len(password) > 20:
        return False
    elif password.isalnum() == False:
        return False
    else:
        return True

def passwords_match(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False

def validate_email(email):

    check_string = email.split('@')
    if len(email) < 3 or len(email) > 20:
        return False
    elif ' ' in email:
        return False
    elif '@' in check_string[0]:
        return False
    elif '.' in check_string[0]:
        return False
    else:
        return True




app.run()
    