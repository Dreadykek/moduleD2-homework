import sentry_sdk
import os

from bottle import route, run, response
from sentry_sdk.integrations.bottle import BottleIntegration


sentry_sdk.init(
    dsn=os.environ['DSN_ENV'],
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
    <a href="/success">Успешный переход 200</a>
    <a href="/fail">Переход с ошибкой</a> 
  </body>
</html>
"""
    return html

@route('/success')
def index():
    return '{status}'.format(status=response.status)

@route('/fail')
def index():
    raise RuntimeError("There is an error!")


run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000)),
    server="gunicorn",
    workers=3,
)

