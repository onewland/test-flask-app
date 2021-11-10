from flask import Flask
from flask.wrappers import Request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://7d07608112824d008d166d8ef7809eb8@o1066102.ingest.sentry.io/6058608",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

@app.route("/inverse/<float:divisor>")
def hello_world(divisor):
    return 1 / divisor

@app.route("/test")
def test():
    raise NotImplementedError