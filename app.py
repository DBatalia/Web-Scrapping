# Import Dependencies
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from flask_pymongo import PyMongo
import scrape_mars
import os


# Hidden authetication file
#import config

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up connection through mLab
# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017")
client = MongoClient("mongodb://localhost:27017")
db = client.mars_db
coll = db.mars_info


# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
        if(db.coll.find_one() is None):
                mars_info = []
        else:
                mars_info = db.coll.find_one()

    # Return template and data
        return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape():

    # Run scrapped functions
   
    mars_data = scrape_mars.return_scrape()
    db.coll.update({}, mars_data, upsert=True)

    return redirect("/", code=302)
if __name__ == "__main__":
        app.run(debug=True)
