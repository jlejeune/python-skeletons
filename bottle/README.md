bottle
======

This skeleton uses bottle (0.12.8) library.
If you want a up-to-date version, download it on https://pypi.python.org/pypi/bottle and replace bottle.py file by new one in this folder.

The WS server supports multiple WSGI servers:
 - gevent
 - gunicorn
 - paste
 - tornado
 - uwsgi
 - wsgiref (default)

Note: the wsgiref is the only one installed by default
