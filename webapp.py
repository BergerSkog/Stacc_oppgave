from flask import Flask, render_template, request
import main
import hent_info
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        google = request.form.get("google")
        wikipedia = request.form.get("wikipedia")
        kunde = request.form["kunde"]


        if kunde.isspace() or (len(kunde) == 0): #sjekker om stringen kun inneholder mellomrom eller er tom
            return render_template("index.html", content="")
        else:
            googleContent = ""
            wikipediaContent = ""
            content = main.hentData(kunde)
            if google == "on":
                googleContent = "Treff fra google: " + hent_info.hentInfoGoogle(kunde)
            if wikipedia == "on":
                wikipediaContent = "Treff fra wikipedia: " + hent_info.hentInfoWikipedia(kunde)
            return render_template("index.html", content=content, googleContent=googleContent, wikipediaContent=wikipediaContent)
    else:
        return render_template("index.html", content="")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)