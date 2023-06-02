from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Housekeeper",
    'location': "Roxas Isabela",
    'salary': "P 12,000.00"
  },
  {
    'id': 2,
    'title': "Cook",
    'location': "Roxas Isabela",
    'salary': "P 10,000.00"
  },
  {
    'id': 3,
    'title': "Security Guard",
    'location': "Roxas Isabela",
    'salary': "P 14,000.00"
  },
  {
    'id': 4,
    'title': "Watcher",
    'location': "Roxas Isabela",
    'salary': "P 9,000.00"
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True )