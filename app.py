from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "26e22b8361674245cead27043c7dab8a8d074ab348413f9c69c926b096550532"

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

@app.route("/layout.html",methods=['GET','POST'])
def layout():
   if request.method == 'GET':
      return
   else:
    return render_template("layout.html")
