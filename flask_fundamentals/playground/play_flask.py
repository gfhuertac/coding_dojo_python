from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play', defaults={'times': 3, 'color': 'blue'})
@app.route('/play/<int:times>', defaults={'color': 'blue'})
@app.route('/play/<int:times>/<color>')
def play(times, color):
    return render_template('play.html', times=times, color=color)

@app.errorhandler(404)
def error_404(error):
    return 'Sorry! No response. Try again', 404

if __name__=="__main__":
    app.run(debug=True)