# -*- coding: utf-8 -*-
# vim:set ai et sts=2 sw=2:

from project import application


###############################################################################
#
# EXAMPLE
#
###############################################################################
@application.get('/sub_module2/:key')
def g_key(key):
    return __name__ + ' : ' + key
