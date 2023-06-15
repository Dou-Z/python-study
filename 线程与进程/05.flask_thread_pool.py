import time

import flask
import json
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor()

def read_file():
    time.sleep(0.1)
    return "file data"


def read_DB():
    time.sleep(0.2)
    return "DB data"


def read_API():
    time.sleep(0.3)
    return "API data"


@app.route("/")
def index():
    result_file = pool.submit(read_file)
    result_DB = pool.submit(read_DB)
    result_API = pool.submit(read_API)

    return json.dumps({
        "read_file": result_file,
        "result_DB": result_DB,
        "result_API": result_API,
    })

app.run()
