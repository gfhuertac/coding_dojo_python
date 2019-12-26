from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults={'rows': 8, 'columns': 8, 'color1': 'black', 'color2': 'white'})
@app.route('/<int:columns>', defaults={'rows': 8, 'color1': 'black', 'color2': 'white'})
@app.route('/<int:rows>/<int:columns>', defaults={'color1': 'black', 'color2': 'white'})
@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def checker_board(rows, columns, color1, color2):
    return render_template('checker_board.html', rows=rows, columns=columns, color1=color1, color2=color2)

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