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

# localhost:5000/user/Rusaidf
@app.route('/user:<name>')

def user(name):
    return render_template("user.html", user_name = name)

# Creat Custom Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)