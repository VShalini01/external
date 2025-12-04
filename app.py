from flask import Flask, request,render_template
app = Flask(__name__)
@app.route('/')
def register():
    return render_template('register.html')
@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name']
    location = request.form['location']
    return render_template('greet.html',name=name, location=location)
app.run(debug = True)