from fastapi.templating import Jinja2Templates
import sys
import os


# router and app set up

class Config():
    def __init__(self):
        self.views = Jinja2Templates(directory="views")

    def getPort(self, port=3000):

        argv = sys.argv

        if len(argv) == 1:
            return port

        if len(argv) == 2:

            opt = argv[1]
            opt_type = opt.split('=')[0]
            opt_cmd = opt.split('=')[1]

            if opt_type == "--env":

                if opt_cmd == "dev":
                    return port

                elif opt_cmd == "prod":

                    if os.environ["PORT"]:
                        return os.environ["PORT"]
                    else:
                        return port

                else:

                    # command not found
                    return port
