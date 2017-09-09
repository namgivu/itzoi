from flask import Flask

app = Flask(__name__)


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


@app.route('/home')
def app_home():
  view = 'app/home.html'
  return render_template(view)
