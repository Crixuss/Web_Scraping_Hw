from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape__mars as sm
from splinter import Browser
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
@app.route("/")
def index():
    mars_dict = mongo.db.mars_app.find_one()
    return render_template("index.html", mars_dict=mars_dict)
    


@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_app
    mars_info_scraped = sm.scrape()
    mars_info.update({}, mars_info_scraped, upsert=True)
    return redirect("/", code=302)
    
    


if __name__ == "__main__":
    app.run(debug=True)



