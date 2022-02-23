from flask import Flask, render_template

app = Flask("Super Scrapper")

@app.route("/")
def home():
  return render_template("potato.html")

app.run(host = "0.0.0.0")
