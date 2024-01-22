from flask import Flask, render_template, url_for,request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app. route("/predict", methods=['POST'])
def predict():
    profilepic = int(request.form ['profilepic'])
    username = int(request.form ['username'])
    words = int(request.form ['words'])
    fullname = int(request.form ['fullname'])
    equal = int(request.form ['equal'])
    description = int(request.form ['description'])
    external = int(request.form ['external'])
    private = int(request.form ['private'])
    posts = int(request.form ['posts'])
    followers = int(request.form ['followers'])
    following = int(request.form ['following'])
    
    prediction = model.predict([[profilepic, username, words, fullname, equal, description, external, private, posts, followers, following]])
    output = round(prediction[0])
    return render_template('index.html',prediction_text=f'The account is {output}')


if __name__ == "__main__":
    app.run(debug=True)