from flask import Flask, render_template, request
import socket
import datetime
from pymongo import MongoClient
import os 

app = Flask(__name__)
print("Mongodb HOSTNAME: ", os.environ.get("MONGO_HOSTNAME"))
print("Mongodb PORT: ", os.environ.get("MONGO_PORT"))
print("Mongodb ADMIN: ", os.environ.get("MONGO_ADMIN"))
print("Mongodb ADMIN_PASSWORD: ", os.environ.get("MONGO_ADMIN_PASSWORD"))

try: 
  mongo_uri = "".join([
    "mongodb://",
    os.environ.get("MONGO_ADMIN"), 
    ":", 
    os.environ.get("MONGO_ADMIN_PASSWORD"),
    "@",
    os.environ.get("MONGO_HOSTNAME"),
    ":",
    str(os.environ.get("MONGO_PORT")),
    "/"
  ])
  print("mongo uri:", mongo_uri)
  client = MongoClient(mongo_uri)
except:
  print("Error: Cannot connect to mongodb missing environement variables")

@app.route("/")
def Hello():
  try:
    db = client.web
    collection = db.web
  except:
    return "Error with the mongodb Database"
  
  hostname = socket.gethostname()
  now = datetime.datetime.now() # current date and time
  date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
  ip = request.environ['REMOTE_ADDR']
  dbrecords = collection.find()
  # create db record 
  record = {"date": date_time, "hostname": hostname, "ip":ip }
  collection.insert_one(record)
  print("create record in db: ", record)
  return render_template('index.html', hostname=hostname, date=date_time, dbrecords=dbrecords)

if __name__ == "__main__":
  app.run(debug=True)
