from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)
app.secret_key = "26e22b8361674245cead27043c7dab8a8d074ab348413f9c69c926b096550532"

STORIES = {
    "anansi": {
        "title": "Anansi and the Box of Stories",
        "background": "page_template.jpg",
        "pages": [
            {"text": ['There was once a time with no stories.',
                      "Children sat at fireplaces in silence, only able to listen to the crackling of flames.",
                    "So where were the stories?",],
                    "image": "anansi1.gif"},
            {"text": ["The one who held the stories was Nyame, the god of the Sky, and the chief of gods.",
                      "Nyame kept all the stories in a box in the sky, all to himself.",
                      "So, a small but egotistical spider, Anansi, asked to buy them from him."],"image": "anansitalk.gif"},
            {"text": ["Nyame responded with a seemingly impossible price for Anansi to pay.", 
                      "Nyame wanted Anansi to bring him Onini the python"],
                        "image": "snake.gif"},  
            {"text": ["Osebo the leopard,"],
                      "image": "leopard.gif"},
            {"text": ["and the Mmboro hornets."],
                      "image": "trapbee.gif"},     
            {"text": ["Anansi used his wit instead of his strength to capture all 3.", 
                      "He tricked the python into tying himself to a pole, trapped the leopard in a pit and lured the hornets into a gourd"], 
                      "image": "victims.gif"},
            {"text": ["Anansi impressed Nyame, and the Sky God held up his end of the deal and gave Anansi the stories.", 
                      "Anansi then scattered them across the world for everyone to share."], 
                      "image": "vsskygod.jpeg"},
        ],
    },
}


def make_spreads(pages):
    return [pages[i:i + 2] for i in range(0, len(pages), 2)]


@app.route("/")
def index():
    return render_template("intro.html")


@app.route("/menu.html")
def menu():
    return render_template("menu.html")


@app.route("/story/<slug>", methods=["GET", "POST"])
def story(slug):
    data = STORIES.get(slug)
    if data is None:
        abort(404)

    spreads = make_spreads(data["pages"])
    key = f"counter_{slug}"
    flag = f"turning_{slug}"

    if request.method == "POST":
        step = request.form.get("incre")
        if step in ("1", "-1"):
            session[key] = (session.get(key, 0) + int(step)) % len(spreads)
        session[flag] = True              # tells the next GET "this came from a button"
        return redirect(url_for("story", slug=slug))

    if session.pop(flag, False):          # came from Next/Back: keep the position
        counter = session.get(key, 0) % len(spreads)
    else:                                 # fresh arrival: start at page 1
        counter = 0
        session[key] = 0

    return render_template(
        "layout.html",
        story=data,
        slug=slug,
        spread=spreads[counter],
        counter=counter,
        total=len(spreads),
    )


if __name__ == "__main__":
    app.run(debug=True)
