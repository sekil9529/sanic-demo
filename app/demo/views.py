# coding: utf-8

from sanic.response import json
from sanic.views import HTTPMethodView


async def hello(request):
    return json({'message': 'hello world!'})


class HelloView(HTTPMethodView):
    """cbv"""

    async def get(self, request):
        return json({'message': 'hello world!'})
