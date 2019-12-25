from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET', 'POST'])
def index():
  """ Renders the counter display page

    Returns: the rendered page
  """
  counter = 1
  if request.method == 'POST':
    try:
      counter = int(request.form.get('times_input', 1))
    except ValueError:
      counter = 1
  if 'counter' in session:
    session['counter'] += counter
  else:
    session['counter'] = 1
  if 'visits' in session:
    session['visits'] += 1
  else:
    session['visits'] = 1
  return render_template('counter.html', counter=session['counter'], visits=session['visits'])

@app.route('/destroy_session')
def destroy_session():
  """ Destroy the session data, only for counter.

    Returns: redirect to the index
  """
  session.pop('counter')
  # or
  # session.clear()
  return redirect('/')

if __name__=="__main__":   
  app.run(debug=True)