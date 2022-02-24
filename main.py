from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Super Scrapper")

db = {}

@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  print(jobs[0])
  return render_template("report.html",
    searchingBy = word,
    resultsNumber = len(jobs),
    resultJobs = jobs)

app.run(host = "0.0.0.0")
