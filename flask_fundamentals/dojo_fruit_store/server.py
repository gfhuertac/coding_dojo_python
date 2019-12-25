from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    from datetime import datetime
    when = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    fruits = dict(request.form)
    del fruits['first_name']
    del fruits['last_name']
    del fruits['student_id']
    fruits = { key:int(val) for key,val in fruits.items() }
    print(f'Charging {first_name} {last_name} for {sum(fruits.values())} fruits')
    return render_template("checkout.html", fruits=fruits, first_name=first_name, last_name=last_name, student_id= student_id, when=when)

@app.route('/fruits')         
def fruits():
    from pathlib import Path
    images = ['apple.png', 'blackberry.png', 'raspberry.png', 'strawberry.png']
    fruits = [ {'name': Path(i).stem, 'src': i} for i in images]
    return render_template("fruits.html", fruits=fruits)

if __name__=="__main__":   
    app.run(debug=True)    
