class UserApp(object):
    def __init__(self,mode):
        self.mode = mode
    def signup(self):
        return 'hello singup'
    def login(self):
        return "hello login"

###############################################################################
# Factory
###############################################################################
import re
def middleware_factory(name,mode):
    if re.match(name,'UserApp'):
        return UserApp(mode)
    else:
        return None
