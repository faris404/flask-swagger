from models import *
from resources.user import *


# api register
api.add_resource(Users,'/users')


# swagger register
docs.register(Users)

if __name__ == '__main__':
   app.run(debug=True)