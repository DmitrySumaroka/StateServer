#   Created by Dmitry Sumaroka - 2017
#   Contact dmitriy.sumaroka@gmail.com
#   Config file to Load up global stuff we might need.

import json

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 8080

state_data = None
try:
    with open("states.json") as json_state_data:
        state_data = json.load(json_state_data)
except EnvironmentError:
    print("State Data not available, please have states.json file in this dir.")
    sys.exit()