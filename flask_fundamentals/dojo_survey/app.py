from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)

locations = [
  {'id': 1, 'name': 'San Jose'},
  {'id': 2, 'name': 'Seattle'},
  {'id': 3, 'name': 'LA'},
  {'id': 4, 'name': 'Dallas'},
  {'id': 5, 'name': 'Arlington'},
  {'id': 6, 'name': 'Chicago'},
  {'id': 7, 'name': 'Tulsa'},
  {'id': 8, 'name': 'Oakland'},
  {'id': 9, 'name': 'Boise'},
  {'id': 10, 'name': 'OC'},
]

languages = [
  {'id': 1, 'name': 'Javascript'},
  {'id': 2, 'name': 'Python'},
  {'id': 3, 'name': 'Java'},
  {'id': 4, 'name': 'C'},
  {'id': 5, 'name': 'C++'},
  {'id': 6, 'name': 'PHP'},
  {'id': 7, 'name': 'Swift'},
  {'id': 8, 'name': 'C#'},
  {'id': 9, 'name': 'Ruby'},
  {'id': 10, 'name': 'Objective-C'},
]

@app.route('/', methods=['GET'])
def index():
  global languages, locations
  return render_template('index.html', languages=languages, locations=locations)

@app.route('/result', methods=['POST'])
def result():
  global languages, locations
  print(request.form)
  name = request.form['name_input']
  location_id = int(request.form['location_select'])
  location_name = locations[location_id-1]['name']
  language_id = int(request.form['language_select'])
  language_name = languages[language_id-1]['name']
  comments = request.form['comments_input']
  contact = 'Yes' if 'contact_checkbox' in request.form else 'No'
  return render_template('results.html', name=name, location=location_name, language=language_name, comments=comments, contact=contact)

if __name__ == '__main__':
  app.run(debug=True)