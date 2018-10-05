#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import logging
import inspect
import functools


class APIError(Exception):
    """
    """
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    """
    """
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResoureNotFoundError(APIError):
    """
    """
    def __init__(self, field, message=''):
        super(APIResoureNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    """
    """
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)