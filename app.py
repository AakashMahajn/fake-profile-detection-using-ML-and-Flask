from flask import Flask, render_template, url_for,request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # Get form data
        profilepic = float(request.form ['profilepic'])
        username = float(request.form ['username'])
        words = float(request.form ['words'])
        fullname = float(request.form ['fullname'])
        equal = float(request.form ['equal'])
        description = float(request.form ['description'])
        external = float(request.form ['external'])
        private = float(request.form ['private'])
        posts = float(request.form ['posts'])
        followers = float(request.form ['followers'])
        following = float(request.form ['following'])
        
        print(request.form)
        
        features = [profilepic, username, words, fullname, equal, description, external, private, posts, followers, following]

        # Make prediction
        prediction = model.predict([features])
        
        if prediction[0] == 1:
            result = "Fake Profile"            
        else:
            result = "Real Profile"
            
        print("Features:", features)  # Check the features being passed to the model
        print("Prediction:", prediction)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)