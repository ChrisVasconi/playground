from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/play')
def box_one():
    return render_template("index.html", num=3, color="blue")


@app.route('/play/<int:num>')
def box_two():
    return render_template("index.html", num=num, color="blue")


@app.route('/play/<int:num>/<string:color>')
def box_three(num, color):
    return render_template("index.html", num=num, color="blue")


if __name__ == "__main__":
    app.run(debug=True)
