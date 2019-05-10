from functools import wraps
from flask import request, abort
# Apply Aspect Oriented Programming to server routes using roles

# e.g. we want to specify the role, perhaps supplied
# by the request or a jwt token, using a decorator
# to abstract away the authorization


# possible decorator implementation
def roles_required(roles):
    def decorator(func):
        # can't skip this @wraps function 
        # or error 'View function mapping is overwriting an existing endpoint function
        # stackoverflow.com/questions/19964079
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(roles, 'required')
            print(args, kwargs, 'provided')
            if (kwargs['role']):
                print(kwargs['role'])
                if (kwargs['role'] not in roles):
                    print('unauthorised')
                    return abort(401)
                else:
                    print('authorised')
                    return func(*args, **kwargs)
                #return abort(401)
            #func()
        return wrapper
    return decorator
            

# can in theory use jwt token parsing to check role here
