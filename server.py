from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/") ## python annotation, app.route() is a function that returns a function
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name)