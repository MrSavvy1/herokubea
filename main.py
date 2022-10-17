import flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, this a web app created by Mr Savvy, please this is a test process, the real shit is coming!"
if __name__ == "__main__":
    app.run(host="127.0.0.1",port = 8080, debug= True)