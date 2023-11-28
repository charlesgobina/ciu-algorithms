import math

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance


class ClosestLandfield:
    def __init__(self, request, landfields):
        self.request = request
        self.landfields = landfields
    
    def get_closest_landfield(self):
        closest_landfield = None
        closest_distance = float('inf')

        for landfield in self.landfields:
            distance = haversine(self.request.lat, self.request.lon, landfield.geopoint.latitude , landfield.geopoint.longitude)
            if distance < closest_distance:
                closest_landfield = landfield
                closest_distance = distance

        return closest_landfield
        