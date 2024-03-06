
import flask

app = flask.Flask(__name__)

@app.route("/health_check", methods=["GET"])
def health_check():
    return flask.Response("Endpoint is working", status=200) 
