from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app. route("/predict", methods=['POST'])
def predict():
    profilepic = int(request.form ['profilepic'])
    username = int(request.form ['username'])
    fullname = int(request.form ['fullname'])
    equal = int(request.form ['equal'])
    description = int(request.form ['description'])
    private = int(request.form ['private'])
    posts = int(request.form ['posts'])
    followers = int(request.form ['followers'])
    following = int(request.form ['following'])
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)