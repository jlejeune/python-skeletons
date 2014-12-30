# -*- coding: utf-8 -*-

from project import application


###############################################################################
#
# EXAMPLE
#
###############################################################################
@application.get('/module1/:key')
def g_key(key):
    return __name__ + ' : ' + key
