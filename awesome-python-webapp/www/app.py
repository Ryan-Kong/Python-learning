# -*- coding:utf-8 -*-
import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web

from jinjia2 import Enviroment, FileSystemLoader

import orm

from coroweb import add_route, add_static

from handlers import cookie2user, COOKIE_NAME

def init_jinjia2(app, **kw):
    logging.info('init jinjia2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinjia2 template path: %s' % path)
    env = Enviroment(loader = FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.item():
            env.fi[name] = f
    app['__templating__'] = env

@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # yield from asyncio.sleep(0.3)
        return (yield from handler(request))
    return logger

@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.methodm, request.path))
        request.__user__ = None
        cookie_str = request.cookie.get(COOKIE_NAME)
        if cookie_str:
            user  = yield from cookie2user(cookie_str)
            if user:
                loggin.info('set current user: %s ' % user.email)
                request.__user__ = user
        if request.path.startswith('/manage') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth

@asyncio.coroutine
def data_factory(app, handler):
    @asyncio.coroutine
    def parse_data(request):
        if request.method = 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__  = yield from request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = yield from request.post()
                logging.info('request form: %s' % str(request.__data__))
            return (yield from handler(request))
        return parse_data

@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r =  yield from handler(request)
        if isinstance (r, web.StreamReaponse):
            return r
        if isinstance(r, bytes):
            resp = web.Respinse(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body = r.encode('utf-8'))
            resp.content_type = 'text/html;charset = utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body = json.dumps(r, ensure_ascii = False, default = lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json; charset = utf-8'
                return resp
            else:
                r['__user__'] = request.__user__
                resp = web.Response(body = app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'application/json; charset = utf-8'
                return resp
        if isinstance(r, int) and t >= 100 and t < 600:
            return web.Response(t)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body = str(r).encode('utf-8'))
        resp.content_type = 'text/plain; charset = utf-8'
        return resp
    return response

def datatime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datatime.fromtimestamp(t)
    return u'%s年%s月%s天' % (dt.year, dt.month, dt.day)

'''
def index(request):
    return web.Response(body = b'<h1>Awesome<h1>', headers = {'content-type':'text/html'})
'''

@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop = loop, **configs,db)
    app = web.Application(loop = loop, middlewares = [
        logger_factory, auth_factory, response_factory
        ])
    init_jinjia2(app, filters = dict(datatime = datatime_filter))
    app.router(app, 'handler')
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server start at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



# Python一定要注意大小写，并保证拼写正确
# logging 模块的使用方法：http://blog.csdn.net/liuchunming033/article/details/39080457
