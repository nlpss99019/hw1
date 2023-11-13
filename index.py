from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
  homepage = "<h1>王梓芸個人網頁</h1>"
  homepage += "<a href=/hw>簡介</a><br>"
  homepage += "<a href=/holland>何倫碼</a><br>"
  homepage += "<a href=/dcard>公司</a><br>"
  return homepage


@app.route("/hw")
def hw():
    now = datetime.now()
    return render_template("hw.html")

@app.route("/holland")
def holland():
    now = datetime.now()
    return render_template("holland.html")

@app.route("/dcard")
def dcard():
    now = datetime.now()
    return render_template("dcard.html")

#if __name__ == "__main__":
    #app.run()

