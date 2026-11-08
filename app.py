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
    "koscheideathless": {
        "title": "Koschei the Deathless",
        "background": "page_template.jpg",
        "pages": [
            {"text":["Prince Ivan Tsarevish weds the warrior queen Marya Morevna.",
                     "Prior to Marya heading off to war, she warns Ivan about a specific closet, telling him not to open it."],
                     "image":"koschei.gif"},
            {"text":["Ivan does not heed Marya's warning and opens the closest, where he finds the emaciated skeletal sorcerer Koschei the Deathless chained inside."],
             "image":"koschei.gif"},
            {"text":["Koschei begs Ivan for water, and drinks three bucketfuls.", 
                     "Once he receives some, his strength recovers and he immediately frees himself from his chains."],
                     "image":"koschei.gif"},
            {"text":["Koschei then kidnaps Marya, and Ivan sets out to rescue her, but is killed and chopped to pieces by Koschei."],
             "image":"koschei.gif"},
            {"text":["Ivan's three magical bird brother-in-laws, a falcon, eagle and raven, sprinkle him with the Waters of Life and Death, resurrecting him."],
            "image":"koschei.gif"},
            {"text":["Ivan then visits the witch Baba Yaga to acquire a magical, lightning-fast horse, capable of outrunning Koschei.",
                     "With the help of the animals he'd spared along the way, Ivan succeeds."],
                     "image":"koschei.gif"},
            {"text":["Riding his new magic steed, Ivan confronts Koschei and finishes him off, rescuing Marya Morevna for good."],
             "image":"koschei.gif"} ]
    },
    "yuki-onna":{
        "title": "Yuki-Onna",
        "background": "page_template.jpg",
        "pages": [
            {"text":["Two woodcutters, an old man named Mosaku and a young apprentice named Minokichi, are caught in a severe mountain snowstorm in the Japanese alps, when they take shelter in an abandoned ferry hut."],
                      "image":"yukionna.gif"},
            {"text":["In the middle of the night, a tall, pale woman in a white kimono appears.", 
                     "She breathes her freezing, icy breath onto Mosaku, freezing him to death.",
                      "She turns to young Minokichi, ready to kill him too, but spares him because she finds him young and handsome.",
                      "She warns him that if he ever tells a single soul about what happened that night, she will end his life."],
                     "image":"yukionna.gif"},
            {"text":["Years later, Minokichi meets a beautiful, pale young woman named O-Yuki, during a snowy evening.",
                     "They marry, have several children, and live a happy life together while she remarkably never seems to age."],
                     "image":"yukionna.gif"},
            {"text":["One evening, while looking at O-Yuki by the lamplight, Minokichi is reminded of his strange encounter from his youth.", 
                     "After many years, he felt safe to tell her the story as a curious secret, noting how much she resembles the snow spirit."],
                     "image":"yukionna.gif"},
            {"text":["O-Yuki suddenly stands up, drops her disguise, and reveals that she was the Yuki-Onna who spared him.",
                     "She rebukes him for breaking his solemn promise, saying she would kill him if not for the sake of their children, and then melts into a cold, white mist that drifts up through the chimney and vanishes into the night forever."],
                     "image":"yukionna.gif"}]
    }
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