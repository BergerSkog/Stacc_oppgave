from flask import Flask, render_template, request
import hent_csv
import hent_info

app = Flask(__name__)


# Flask html side
@app.route("/", methods=["POST", "GET"])
def index():
    # Starter index.html på localhost


    # Sjekker om knappen er trykket
    if request.method == "POST":

        # Sjekker om knappene til google og wikipedia ekstra info er huket av
        # og henter teksten fra input feltet
        google = request.form.get("google")
        wikipedia = request.form.get("wikipedia")
        kunde = request.form["kunde"]


        if kunde.isspace() or (len(kunde) == 0):  # sjekker om stringen kun inneholder mellomrom eller er tom
            return render_template("index.html", content="")
        else:
            googleContent = ""
            wikipediaContent = ""
            content = hent_csv.hentDataCsv(kunde)

            # Henter dataen fra de relevante kildene
            if google == "option1":
                googleContent = "Treff fra google: " + hent_info.hentInfoGoogle(kunde)
            if wikipedia == "option2":
                wikipediaContent = "Treff fra wikipedia: " + hent_info.hentInfoWikipedia(kunde)

            # Viser siden
            return render_template("index.html", content=content, googleContent=googleContent,
                                   wikipediaContent=wikipediaContent)
    else:
        # Viser siden uten data
        return render_template("index.html", content="")


if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)
