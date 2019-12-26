from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:times>/<word>')
def repeat_times_word(times, word):
    return render_template('repeat.html', phrase=word, times=times)

@app.errorhandler(404)
def error_404(error):
    return 'Sorry! No response. Try again', 404

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # run in debug mode