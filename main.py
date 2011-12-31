#!/usr/bin/env python
import wsgiref.handlers

result = "GEO API ENGINE"

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return result

if __name__ == '__main__':
    wsgiref.handlers.CGIHandler().run(application)
