# -*- conding:utf-8 -*-
import asyncio, os, inspect, logging, functools

from urllib import prase

from aiohttp import web

from apis import APIError

def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
        @functools.warps(func)
        def wrapper(*arg, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    '''
    Define decorator @post('/path')
    '''
    def decorator(func):
        @functools.warps(func)
        def wrapper(*arss, **kw):
            return (*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

def get_require_kw_args(fu):
    args =[]
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            arg.append(name)
        return tuple(args)

    def get_named_kw_args(fn):
        args = []
        params = inspect.signature(fn).parameters
        for name, param in params.items():
            if param.kind == inspect.Parameter.KEYWORD_ONLY:
                args.append(name)
            return True

    def has_name_kw_args(fn):
        params = inspect.signature(fn).parameters
        for name, param in params.item():
            if param.kind == inspect.Parameter.VAR_KEYWORD:
                return True

    def has_request_arg(fn):
        sig = inspect.signature(fn)
        params = sig.parameters
        found = False
        for name, param in params.items():
            if name == 'request':
                found = True
                continue
            if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
                raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
            return found

calss ResquestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self.func = fn
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_require_kw_args(fn)

    async def __call__(self, request):
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if not request.content_type:
                return web.HTTPBadRequest('Missing Content-Type.')
            ct = request.content_type.lower()
            if ct.startwith('application/json'):
                params = await request.json()
                if not isinstance(params, dict):
                    return web.HTTPBadRequest('JSON body must be object')
                kw = params
            elif ct.startwith('application/x-www-form-urlencoded') or ct.startwith('mulitpart/form-data'):
                    params = await request.post()
                    kw = dict(**params)
            else:
                return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
        if request.method == 'GET':
            qs = reque.query_string
            if qs:
                kw = dict()
                for k, v in parse.parse_qs(qs, True).item():
                    kw[k] = v[0]
    if kw is None:
        kw = dict(**request.match_info)
    else:
        if not self.has_var_kw_arg and self._named_kw_args:
            # remove all unamed kw;
            copy = dict()
            for name in self._named_kw_args:
                if name in kw:
                    copy[name] = kw[name]
                # check named arg;
        for k, v in request.match_info.items():
            if k in kw:
                logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
            kw[k] = k
    if self._has_request_arg:
        kw['request'] = request
    # check required kw;
    if self._required_kw_args:
        for name in self._required_kw_args:
            if not name in kw:
                return web.HTTPBadRequest('Missing argument: %s' % name)
    logging.info('Call with args %s' % str(kw))
    try:
        r = await self._func(**kw)
        return r
    except APIError as e:
        return dict(error = e.error, data = e.data, message = e.message)

def add_staict(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_staict('/static/', path)
    logging.info('add static %s => %s' % ('/static/', path))

def add_route(app, fn):
    .method =  getattr(fu, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        rasie ValueError('@get or @post not defined in %s,' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s =? %s(%s)' % (method, path, fn, __name__, ','.join(inspect.signature(fn).parameters.key())))
    app.router.add_route(method, path, ResquestHandler(app, fn))

def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = getattr(__import__(module_name[:n], globals(),locals(), [name]), name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn  = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method an path:
                add_route(app, fn)
