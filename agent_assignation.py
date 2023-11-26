import datetime
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

# volume calculator
def calculate_volume(category, quantity):
    sizes = { "Bucket": 10, "Trashbag": 27, "Wheelbarrow": 80  }
    volume = (sizes[category] / 1000)* quantity
    return int(volume)


# check if agent is available
def agent_availability(agent):
    current_day = datetime.now().weekday()
    agent_shift = agent.agent_shift[current_day]

    if (agent_shift == None  or len(agent_shift) == 0 or agent.agent_availability == False):
        return False
    
    # get current hour
    current_hour = datetime.now().hour
    if (
    (4 <= current_hour < 12 and "morning" in agent_shift) or
    (13 <= current_hour < 19 and "afternoon" in agent_shift)):
        return True

  
