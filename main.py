from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/validate-time')
def display_time_form():
    return render_template('time_form.html')




@app.route('/', methods=['GET', 'POST']) 
def user_registration():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        username_error = ''
        password_error = ''
        verify_password_error = ''
        email_error = ''

        if not username:
            username_error = 'Please enter a username'
            username = ''
        else: 
            if ' ' in username:
                username_error = 'Username may not contain any spaces'
            else:                   
                if len(username) < 3 or len(username) > 20:
                    username_error = 'Username length out of range (3-20)'
       
        if not password:
            password_error = 'Please enter a password'            
        else: 
            if ' ' in password :
                password_error = 'Password may not contain any spaces'
            else:                   
                if len(password) < 3 or len(password) > 20:
                    password_error = 'Password length out of range (3-20)'

        if not verify_password:
            verify_password_error = 'Please enter your password into the verify password field'            
        else: 
            if verify_password != password:
                verify_password_error = 'Your password inputs do not match'

        if email:
            if ' ' in email or email.count('@') != 1 or email.count('.') != 1:
                email_error = """Please enter a valid e-mail address 
                ( A valid e-mail address has no spaces and exactly (1)'@' and exactly (1)'.'"""
            else:                   
                if len(username) < 3 or len(username) > 20:
                    username_error = 'Username length out of range (3-20)'               
        
        if (not username_error and not password_error 
        and not verify_password_error and not email_error):
            
            return redirect('/welcom?username={0}'.format(username))
        else:        
            return render_template('user_registration.html',
            css = '.error {color:red}',
            username_error=username_error,
            password_error=password_error,
            verify_password_error=verify_password_error,
            email_error=email_error,
            username=username,
            password='',
            verify_password='',
            email=email)
    
    return render_template('user_registration.html', title='Signup')   

@app.route('/welcom')
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome {0}!!! Thanks for creating an account!</h1>'.format(username)
app.run()    