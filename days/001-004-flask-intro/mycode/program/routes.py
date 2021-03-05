from program import app

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello Visitor</h1>"

@app.route("/help")
def help():
    return "Found you"
