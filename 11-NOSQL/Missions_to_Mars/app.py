from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.nasa_db

@app.route("/scrape")
def scrape():
    db.mars_facts.drop()
    mars_dict = scrape_mars.scrape()
    db.mars_facts.update({}, mars_dict, upsert=True)
    return redirect("/")

@app.route('/')
def main():
    # db.mars_facts.drop()
    # mars_dict = scrape_mars.scrape()
    # db.mars_facts.update({}, mars_dict, upsert=True)
    # Find one record of data from the mongo database
    destination_data = db.mars_facts.find_one()
    # Return template and data
    return render_template("index.html", mars=destination_data)

if __name__ == '__main__':
    app.run(debug=True)