from flask import Flask

app = Flask(__name__)

#init session
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = '3fH4uQS1pG4MMSm2xXk'


from flask import redirect, url_for, render_template


@app.route('/')
def app_index():
  from util import hasLoggedIn

  #has logged in -> view user home
  if hasLoggedIn():
    return redirect(url_for('app_home'))

  #not logged in yet -> view log-in page
  else:
    return redirect(url_for('app_signin'))


@app.route('/signin')
def app_signin():
  view = 'app/signin.html'
  return render_template(view)


@app.route('/auth/signin')
def auth_signin():
  from util import markAsLoggedIn
  markAsLoggedIn()
  return 'Finish called auth_signin'


@app.route('/home')
def app_home():
  view = 'app/home.html'
  return render_template(view)


@app.route('/signout')
def app_signout():
  #unset session authInfo
  #mark as logged out
  from flask import session
  if 'authInfo' in session:
    del session['authInfo']

  #redirect to app_home
  return redirect(url_for('app_home'))
