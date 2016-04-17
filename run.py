from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/api/service")
def test():
    return "Web application 1.0"

flask_app.run(port=8082)