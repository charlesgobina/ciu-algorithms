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
# def calculate_volume(category, quantity):
#     sizes = { "Bucket": 10, "Trashbag": 27, "Wheelbarrow": 80  }
#     volume = (sizes[category] / 1000)* quantity
#     return int(volume)


# # check if agent is available
# def agent_availability(agent):
#     current_day = datetime.now().weekday()
#     agent_shift = agent.agent_shift[current_day]

#     if (agent_shift == None  or len(agent_shift) == 0 or agent.agent_availability == False):
#         return False
    
#     # get current hour
#     current_hour = datetime.now().hour
#     if (
#     (7 <= current_hour < 12 and "morning" in agent_shift) or
#     (13 <= current_hour < 19 and "afternoon" in agent_shift)):
#         return True
    
#     return False


# def agent_assination(request, agent_list):
#     request_coordinantes = {
#         "lat": request.localisation.latitude,
#         "lon": request.localisation.longitude
#     }

#     available_agents = [free_agents for free_agents in agent_list if agent_availability(free_agents)]
#     if (len(available_agents) == 0):
#         return "No available agent"
    
#     # get the available_agent location
#     agent_locations_with_closest_proximity_to_request = []
#     for agent in available_agents:
#         agent_location = {
#             "lat": agent.localisation.latitude,
#             "lon": agent.localisation.longitude
#         }
#         distance = haversine(request_coordinantes["lat"], request_coordinantes["lon"], agent_location["lat"], agent_location["lon"])
#         agent_locations_with_closest_proximity_to_request.append({
#             "agent": agent,
#             "distance": distance
#         })

#         # sort the list by distance
#         agent_locations_with_closest_proximity_to_request.sort(key=lambda x: x["distance"])

#     return agent_locations_with_closest_proximity_to_request[0]

    

# # OOP version

class AgentAvailability:
    def __init__(self, agent):
        self.agent = agent
    
    def is_available(self):
        current_day = datetime.now().weekday()
        agent_shift = self.agent.agent_shift[current_day]

        if (agent_shift == None  or len(agent_shift) == 0 or self.agent.agent_availability == False):
            return False
        
        # get current hour
        current_hour = datetime.now().hour
        if (
        (7 <= current_hour < 12 and "morning" in agent_shift) or
        (13 <= current_hour < 19 and "afternoon" in agent_shift)):
            return True
        
        return False
    
    def get_agent(self):
        return self.agent


# doing this assunimg that the backend team merged the user location and their booking to form a request object

class AgentAssignation:
    def __init__(self, request, agent_list):
        self.request = request
        self.agent_list = agent_list
    
    def get_request_coordinates(self):
        return {
            "lat": self.request.localisation.latitude,
            "lon": self.request.localisation.longitude
        }
    
    def get_available_agents(self):
        available_agents = [free_agents for free_agents in self.agent_list if AgentAvailability(free_agents).is_available()]
        return available_agents
    
    def get_agent_locations_with_closest_proximity_to_request(self):
        request_coordinantes = self.get_request_coordinates()
        available_agents = self.get_available_agents()

        agent_locations_with_closest_proximity_to_request = []
        for agent in available_agents:
            agent_location = {
                "lat": agent.localisation.latitude,
                "lon": agent.localisation.longitude
            }
            distance = haversine(request_coordinantes["lat"], request_coordinantes["lon"], agent_location["lat"], agent_location["lon"])
            agent_locations_with_closest_proximity_to_request.append({
                "agent": agent,
                "distance": distance
            })

            # sort the list by distance
            agent_locations_with_closest_proximity_to_request.sort(key=lambda x: x["distance"])

        return agent_locations_with_closest_proximity_to_request
    
    def get_agent_with_closest_proximity_to_request(self):
        agent_locations_with_closest_proximity_to_request = self.get_agent_locations_with_closest_proximity_to_request()
        return agent_locations_with_closest_proximity_to_request[0]["agent"]
  
