from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_reponse():
    userText = request.args.get('msg')
    return str(process(userText))
@app.route("/test")
def say_hi():
   
    return str("hi")

if __name__ == "__main__":
    app.run(debug=True)