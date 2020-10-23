from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

import sys
import os


class Config():

    def __init__(self):
        self.env = None
        self.DB_URL = None
        self.PORT = None
        self.PSW = None
        self.views = None
        self.ADMIN_NAME = None
        self.SECRET_KEY = None

    def get_env(self):

        argv = sys.argv
        load_dotenv('./.env')

        self.PSW = os.getenv("ADMIN_PSW")
        self.ADMIN_NAME = os.getenv("ADMIN_NAME")
        self.SECRET_KEY = os.getenv("SECRET_KEY")

        self.views = Jinja2Templates(directory="views")

        if(self.PSW):
            print("Setted admin password")
        else:
            print("failed to set admin password")

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
                    print("setting envionment to => ", self.env)
                    return self.env
                else:
                    print(f'option {cmd} not foond setting env=dev')

        else:
            print('too many arguments')
            return False

    def def_setup(self, port=3000):

        if self.env == 'dev':

            self.PORT = port
            self.DB_URL = "postgresql:///projects"

        elif self.env == 'prod':

            self.PORT = os.environ['PORT']
            self.DB_URL = os.environ['DATABASE_URL']


print("===== SETTING EVIRONTMENT VARIABLES =====")
project_config = Config()
project_config.get_env()

print("current config: ")
print("env = ", project_config.env)
project_config.def_setup(port=5000)
