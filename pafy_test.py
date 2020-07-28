from flask import Flask,render_template,request
import pafy
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        link=str(request.form.get("link"))
        video=pafy.new(link)
        vid=video.getbest().url
        aud=video.getbestaudio().url
        return render_template("index2.html",vid=vid,aud=aud)
    else:
        return render_template("index1.html")
@app.route("/about")
def about():
    return render_template("about.html")
app.run(debug=True)
