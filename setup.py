from fastapi.templating import Jinja2Templates

import sys
import os


# router and app set up
views = Jinja2Templates(directory="views")


views = Jinja2Templates(directory="views")


class Config():

    def __init__(self):
        self.env = None
        self.DB_URL = None
        self.PORT = None

    def get_env(self):

        argv = sys.argv

        if len(argv) == 1:
            print("No environment spcified. setting to development")
            self.env = "dev"

        elif len(argv) == 2:
            opt = argv[1].split('=')[0]
            cmd = argv[1].split('=')[1]

            print("reading command options")
            print("option is => ", opt)
            print("cmd is    => ", cmd)
            if opt == '--env':

                if cmd == 'dev' or cmd == 'prod' or cmd == 'test':
                    self.env = cmd
<<<<<<< HEAD

=======
                    print("setting envionment to => ", self.env)
                    return self.env
>>>>>>> 1103f7fdba8bf8dc310cb520f8c47450708a7021
                else:
                    print(f'option {cmd} not foond setting env=dev')

        else:
            print('too many arguments')
            return False

    def def_setup(self, port=3000):

<<<<<<< HEAD
        if (self.env):

            if self.env == 'dev':

                self.PORT = port
                self.DB_URL = "postgresql:///projects"

            elif self.env == 'prod':
=======
        if self.env == 'dev':

            self.PORT = port
            self.DB_URL = "postgresql:///projects"
>>>>>>> 1103f7fdba8bf8dc310cb520f8c47450708a7021

        elif self.env == 'prod':

            self.PORT = os.environ['PORT']
            self.DB_URL = os.environ['DATABASE_URL']


print("===== SETTING EVIRONTMENT VARIABLES =====")
project_config = Config()
project_config.get_env()
<<<<<<< HEAD
=======

print("current config: ")
print("env = ", project_config.env)
>>>>>>> 1103f7fdba8bf8dc310cb520f8c47450708a7021
project_config.def_setup(port=5000)
