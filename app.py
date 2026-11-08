from flask import Flask, render_template, request, redirect

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
  return render_template("intro.html")


# When using hrefs, make the @app.route the name of the html file if not that shit aint working :((
@app.route("/menu.html")
def menu():
  return render_template("menu.html")

@app.route("/anansi.html")
def anansi():
   return render_template("anansi.html")

@app.route("/layout.html")
def layout():
   return render_template("layout.html")
