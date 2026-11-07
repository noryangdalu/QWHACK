from flask import Flask, render_template, request, redirect

app = Flask(_name_)

if _name_ == "_main_":
    app.run(debug=True)

@app.route("/")
def index():
  return render_template("intro.html")

@app.route("/layout")
def layout():
  return render_template("layout.html")
