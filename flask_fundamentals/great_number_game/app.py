from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'This is a wonderful game'

def increase(session, session_key):
  try:
    session[session_key] += 1
  except KeyError:
    session[session_key] = 1

@app.route('/', methods=['GET', 'POST'])
def index():
  error = None
  if request.method == 'GET':
    if 'random_number' in session:
      error='You cannot restart until you guess! This counts as an attempt :p'
      increase(session, 'attempts')
    else:
      from random import randint
      session['random_number'] = randint(1, 100)
    return render_template('index.html', error=error)
  else:
    try:
      guess = int(request.form['guess_input'])
    except ValueError:
      error = 'Invalid input!'
    increase(session, 'attempts')
    return render_template('index.html', guess=guess, error=error)

@app.route('/restart')
def restart():
  session.clear()
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)