from flask import Flask , render_template, redirect, request
from collections import Counter 
app = Flask(__name__)

data = []
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        song = request.form['song']
        if song == "":
            return redirect("index.html")
        else:
            print(song)
            a = data.append(song)
            print(data)
            return render_template("success.html",song=song)
    return render_template("index.html")


@app.route("/admin")
def rank_songs():
    global data
    b = Counter(data)
    k = dict(sorted(b.items(),reverse=True))
    
    print(k)
    return render_template("rank.html",data=k)


if __name__ == "__main__":
    app.run(debug=True)
