#   Created by Dmitry Sumaroka - 2017
#   Contact dmitriy.sumaroka@gmail.com

import config
from shapely.geometry import Polygon, Point

LONGITUDE = 0;
LATITUDE = 1;

def search_state(cordiantes=None):
    if cordiantes:
        point = Point(cordiantes[LONGITUDE], cordiantes[LATITUDE])
        for state in config.state_data:
            # Create a simple polygon based on the border cordinates given
            polygon = Polygon(state['border'])
            if polygon.contains(point):
                return state['state']
        return None
    else:
        return None