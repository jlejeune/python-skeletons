import bottle


###############################################################################
# 1st method
#import application.module1
#import application.module2
#import application.views.sub_module1
#import application.views.sub_module2

#application = bottle.default_app()


###############################################################################
# 2nd method
#bottle.default_app.push()

#import application.module1
#import application.module2
##from application.views.sub_module1 import *
##from application.views.sub_module2 import *
#import views.sub_module1
#import views.sub_module2

#application = bottle.default_app.pop()


###############################################################################
# 3rd method
#import application.module1
#import application.module2
#from application.views.sub_module1 import routes as sub_module1_routes
##from application.views.sub_module2 import routes as sub_module2_routes
#application = bottle.default_app()

#application.merge(sub_module1_routes)
#application.merge(sub_module2_routes)

#from application.views.sub_module1 import submodule1
#from application.views.sub_module2 import submodule2

#application.mount('/', submodule1)
#application.mount('/', submodule2)
##application.mount(submodule1, '/')
##application.mount(submodule2, '/')


###############################################################################
# 4th method : WORK !!!!
application = bottle.default_app()

# Import views
import project.module1
import project.module2
import project.views.sub_module1
import project.views.sub_module2
