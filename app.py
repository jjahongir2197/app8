from flask import Flask, render_template, redirect

app = Flask(__name__)

likes = 0

@app.route("/")
def home():
    return render_template("like.html", likes=likes)

@app.route("/like")
def like():
    global likes
    likes += 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
