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
            content = main.hentDataCsv(kunde)
            if google == "option1":
                googleContent = "Treff fra google: " + hent_info.hentInfoGoogle(kunde)
            if wikipedia == "option2":
                wikipediaContent = "Treff fra wikipedia: " + hent_info.hentInfoWikipedia(kunde)
            return render_template("index.html", content=content, googleContent=googleContent, wikipediaContent=wikipediaContent)
    else:
        return render_template("index.html", content="")


if __name__ == "__main__":
    app.run(debug=True)