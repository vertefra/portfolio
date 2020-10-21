from fastapi.templating import Jinja2Templates

import sys
import os


# router and app set up
views = Jinja2Templates(directory="views")


views = Jinja2Templates(directory="views")


class Config():

    def get_env(self):

        argv = sys.argv

        if len(argv) == 1:
            self.env = "dev"

        elif len(argv) == 2:
            opt = argv[1].split('=')[0]
            cmd = argv[1].split('=')[1]

            if opt == 'env':

                if cmd == 'dev' or cmd == 'prod' or 'test':
                    self.env = cmd

                else:
                    print(f'option {cmd} not foond setting env=dev')

        else:
            print('too many arguments')
            return False

    def def_setup(self, port=3000):

        if (self.env):

            if self.env == 'dev':

                self.PORT = port
                self.DB_URL = "postgresql:///projects"

            elif self.env == 'prod':

                self.PORT = os.environ['PORT']
                self.DB_URL = os.environ['DATABASE_URL']


project_config = Config()
project_config.get_env()
project_config.def_setup(port=5000)
