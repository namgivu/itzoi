from flask import Flask

app = Flask(__name__)


@app.route('/')
def app_index():
  view = 'app/index.html'

  from flask import render_template
  return render_template(view)
