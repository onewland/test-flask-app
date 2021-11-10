from flask import Flask
from flask.wrappers import Request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://d7e6a5e37601417db2324d8ff3aba5cb@o1.ingest.sentry.io/6058569",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 1 / 0

@app.route("/test")
def test():
    raise NotImplementedError