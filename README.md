# portfolio

fastAPI postrgresql and jinja2

## Isomorphic server side rendering with Python fastAPI and jinja2

- **v0.0.2** Oct 17 2020 Normalize added, added default "not found page", media queries for responsivness added.
  class Config with **view** as instance of Jinja2Templates
  getPort(port) if launch the server with

`python3 server.py --env=dev` will use as a port the port argument in getPort or **3000** as default

`python3 server.py --env=prod` will load the port from the environment