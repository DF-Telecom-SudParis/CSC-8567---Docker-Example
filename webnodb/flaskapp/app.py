from flask import Flask, render_template
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def Hello():
  hostname = socket.gethostname()
  now = datetime.datetime.now() # current date and time
  date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
  return render_template('index.html', hostname=hostname, date=date_time)

if __name__ == "__main__":
  app.run(debug=True)
