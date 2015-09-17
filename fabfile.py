from fabric.api import *

def push(message='updates'):
    local('git add .')
    local('git commit -m "%s"' % message)
    local('git push')


