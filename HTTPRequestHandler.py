#   Created by Dmitry Sumaroka - 2017
#   Contact dmitriy.sumaroka@gmail.com

from http.server import BaseHTTPRequestHandler
from searchState import search_state
from urllib.parse import urlparse, parse_qs

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query_string = urlparse(self.path).query
        if query_string:
            query_params = parse_qs(query_string)
            if 'latitude' in query_params and 'longitude' in query_params:
                self.send_response(200)
                points = []
                points.append(float(query_params['longitude'][0]))
                points.append(float(query_params['latitude'][0]))
                state = search_state(points)
                if state:
                    self.wfile.write(bytes(state, "utf8"))
                else:
                    self.wfile.write(bytes("No state found", "utf8"))
                return
            else:
                self.send_response(400)
                self.wfile.write(bytes("Lat or Long missing", "utf8"))
        else:
            self.send_response(400)
            self.wfile.write(bytes("Lat and Long params missing", "utf8"))
