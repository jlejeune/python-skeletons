# -*- coding: utf-8 -*-

from project import application
import time


###############################################################################
#
# EXAMPLE
#
###############################################################################
@application.get('/module2/gettime')
def g_time():
    return str(int(time.time()))

@application.get('/module2/:key')
def g_key(key):
    return __name__ + ' : ' + key
