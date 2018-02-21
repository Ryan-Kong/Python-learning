# -*- coding:utf-8 -*-
import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body = b'<h1>Awesome<h1>', headers = {'content-type':'text/html'})

@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server start at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



# Python一定要注意大小写，并保证拼写正确
# logging 模块的使用方法：http://blog.csdn.net/liuchunming033/article/details/39080457
