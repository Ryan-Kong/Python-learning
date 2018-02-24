# -*- conding:utf-8 -*-
'''
JSON API definition
'''

import json, logging, inspect, functools

class APIError(exception):
    '''
    the base APIError which contains error(required), data(optional), and message(optional),
    '''
    def __init(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indecate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message = ''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(object):
            """Indicate the resource was not found. The date specifies the resource name."""
            def __init__(self, field, message = ''):
                super(APIResourceNotFoundError, self).__init__('valeu:notfound', field, message)
                self.arg = arg


class APIPermissionError(APIError):
    """Indicate the api has no permission."""
 def __init__(self, message = ''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)

