#!/usr/local/bin/python3

#   Created by Dmitry Sumaroka - 2017
#   Contact dmitriy.sumaroka@gmail.com

from HTTPRequestHandler import HTTPRequestHandler
from http.server import HTTPServer
import config

if __name__ == '__main__':
    server_address = (config.HOST_NAME, config.PORT_NUMBER)
    httpd = HTTPServer(server_address, HTTPRequestHandler)
    try:
        print("Serving at: " + config.HOST_NAME + ":" + str(config.PORT_NUMBER))
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server Stoped")
