# -*- coding: utf-8 -*-
# vim:set ai et sts=2 sw=2:

from project import application
#from project.models.sub_module1 import toto

###############################################################################
#
# EXAMPLE
#
###############################################################################
@application.get('/sub_module1/:key')
def g_key(key):
    return __name__ + ' : ' + key

#@application.get('/sub_module1/toto')
#def g_toto():
#    return __name__ + ' : ' + toto
