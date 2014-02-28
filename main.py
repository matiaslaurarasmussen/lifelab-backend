import sys
sys.path.insert(0, 'modules')
from bottle import route, run, template, Bottle, debug

bottle = Bottle()

debug(True)




@bottle.route('/', method="GET")
def index():
    return 'API index'

@bottle.route('/activity/<name:re:[a-z]+>', method="GET")
def activity(name):
    return 'GET activity'

@bottle.route('/activity/<name:re:[a-z]+>', method="PUT")
def activity(name):
    return 'PUT activity'

@bottle.route('/activity/<name:re:[a-z]+>', method="POST")
def activity(name):
    return 'POST activity'

@bottle.route('/activity/<name:re:[a-z]+>', method="DELETE")
def activity(name):
    return 'DELETE activity'







#run(host='localhost', port=8080)
