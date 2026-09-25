from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    # if request.method == "POST":
    #     distancia = request.form.get("distancia")
    #     dias = request.form.get("dias")
    #     transporte = request.form.get("transporte")

    # print(distancia)
    # print(dias)
    # print(transporte)


    return render_template("index.html")


@app.route("/equipe")
def equipe():
    return render_template("equipe.html")


if __name__ == "__main__":
    app.run(debug=True)
