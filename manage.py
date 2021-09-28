# coding: utf-8

import os

from sanic import Sanic

from app import create_app

app: Sanic = create_app(os.environ.get("ENV", "DEV"))


if __name__ == '__main__':
    app.run(workers=2, port=8000, auto_reload=False)
