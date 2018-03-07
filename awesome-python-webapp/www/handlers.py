# -*- coding:utf-8 -*-

import re, time, json, logging, hashlib, base64, asyncio

import markdown2


from aiohttp import web

from coroweb import get, post
from api import APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id
from config import configs

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret

def user2cookie(user, max_age):
    '''
    Generate cookie str by user.
    '''
    # build cookie string by: id-expires-sha1
    expires =  str(int(time.time() + max_age))
    s = '%s - %s - %s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

@asyncio.coroutine
def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = yeild from User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user, passwd, expires _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None

@get('/')
def index(request):
    summary = 'Lorem ipsun dolor sit amet, consectetur adipisicing elitm, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id = '1', name = 'Test Blog', summary = summary, created_at = time.time()-120),
        Blog(id = '2', name = 'Something New', summary = summary, created_at = time.time()-3600),
        Blog(id = '3', name = 'Learn Swift', summary = summary, created_at = time.time()-7200),
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/api/users')
def api_get_users():
    users = yield from User.findAll(orderBy = 'created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users = users)
