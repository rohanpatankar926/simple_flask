from flask import Flask

app=Flask(__name__)

@app.route("/hello/<name>/<float:age>",methods=["GET"])
def index(name,age):
    return f"<h1>HElloo {name} and my age is {age}</h1>"

if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=8000)