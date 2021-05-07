from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')

def index():
    return render_template("index.html")

@app.route('/play/<int:num>')

def boxes(num):
    return render_template("index2.html", box_num = num)

@app.route('/play/<int:num>/<color>')

def colorBoxes(num, color):
    return render_template("index3.html", box_num = num, box_color = color)

if __name__=="__main__":
    app.run(debug=True)

