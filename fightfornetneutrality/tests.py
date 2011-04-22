# -*- coding: utf-8 -*-
import unittest
from fightfornetneutrality import NetNeutrality
from webob import Response
from webtest import TestApp

def application(environ, start_response):
    resp = Response('OK')
    return resp(environ, start_response)

class Tests(unittest.TestCase):

    def setUp(self):
        self.app = TestApp(NetNeutrality(application))

    def test_autorized(self):
        resp = self.app.get('/', extra_environ={'REMOTE_ADDR': '127.0.0.2'})
        resp.mustcontain('OK')

    def test_not_autorized(self):
        resp = self.app.get('/', status=403, extra_environ={'REMOTE_ADDR': '62.160.71.50'})
        resp.mustcontain('Ressource inaccessible')

    def test_proxy_not_autorized(self):
        resp = self.app.get('/', status=403, extra_environ={'REMOTE_ADDR': '127.0.0.1', 'HTTP_X_FORWARDED_FOR': '62.160.71.50'})
        resp.mustcontain('Ressource inaccessible')


