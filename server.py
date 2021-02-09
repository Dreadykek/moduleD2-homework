import sentry_sdk
import os

from bottle import route, run, response
from sentry_sdk.integrations.bottle import BottleIntegration


sentry_sdk.init(
    "https://15a319e2297841a99692954feb794a20@o519025.ingest.sentry.io/5628790",
    traces_sample_rate=1.0,
    integrations=[BottleIntegration()]
)

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Module_D2</title>
  </head>
  <body>
    <label>Выберите то, что вам нужно</label>
    <a href="/succes">Успешный переход 200</a>
    <a href="/fail">Переход с ошибкой</a> 
  </body>
</html>
"""
    return html

@route('/succes')
def index():
    return 'HTTP статус - {status}'.format(status=response.status)

@route('/fail')
def index():
    raise RuntimeError("There is an error!")


run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)),
    server="gunicorn",
    workers=3,
)

