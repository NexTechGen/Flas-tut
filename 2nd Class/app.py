from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

''' Fillters!!!!
safe
capitalize
lower
upper
title
trim
striptags
'''

# Create a route decorator
@app.route("/")

def index():
    firts_name = "Rusaid"
    #stuff = "This is <strong>Bold</strong> Text"
    stuff = "This is bold Text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushroom"]
    return render_template("index.html", first_name = firts_name,
                           stuff= stuff,
                           pizza = favorite_pizza)

# localhost:5000/user/Rusaid
@app.route('/<name>')

def user(name):
    return render_template("user.html", user_name = name)

if __name__ == "__main__":
    app.run(debug=True)