from flask import Flask, request, render_template, redirect, session
from random import randint, random
from datetime import datetime

app =  Flask(__name__)
app.secret_key = 'Ninja Gold Secret Key'

@app.route('/')
def index():
  if not 'gold' in session:
    session['gold'] = 0
  if not 'activities' in session:
    session['activities'] = ''
  return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
  session.clear()
  return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
  building = request.form['building']
  min = int(request.form['min'])
  max = int(request.form['max'])
  color = 'green'
  now = datetime.now().strftime('%Y/%m/%d %H:%M %p')
  sign = 1
  if building == 'casino':
    sign = -1 if random() < 0.5 else 1
    
  amount = randint(min, max)
  session['gold'] += sign * amount
  if sign == 1:
    message = f'<div style="color:{color};">Earned {amount} golds from the {building} ({now})'
  else:
    color = 'red'
    message = f'<div style="color:{color};">Entered a {building} and lost {amount} golds ... Ouch ... ({now})'
  session['activities'] = message + session['activities']
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)