import calendar
from datetime import datetime

agent = {
  "_id": {
    "$oid": "6499923c2937ad6e5d431c3d"
  },
  "agent_id": 1,
  "agent_shift": {
    "Monday": [
      "morning"
    ],
    "Tuesday": [
      "afternoon"
    ],
    "Wednesday": [
      "morning",
      "afternoon"
    ],
    "Thursday": [
      "afternoon"
    ],
    "Friday": [
      "morning",
      "afternoon"
    ],
    "Saturday": [
      "morning"
    ],
    "Sunday": []
  },
  "availability": True,
  "first_name": "Peter",
  "last_name": "Djami",
  "location_information": {
    "address": [
      "yaoundé",
      "Cameroon",
      "Simbock"
    ],
    "location": {
      "latitude": 3.8384765,
      "longitude": 11.5006256
    },
    "quater": "Simbock"
  },
  "account_status": "active"
}

agent = {
    "_id": {
        "$oid": "6499923c2937ad6e5d431c3d"
    },
    "agent_id": 1,
    "agent_shift": {
        "Monday": ["morning"],
        "Tuesday": ["afternoon"],
        "Wednesday": ["morning", "afternoon"],
        "Thursday": ["afternoon"],
        "Friday": ["morning", "afternoon"],
        "Saturday": ["morning"],
        "Sunday": []
    },
    "availability": True,
    "first_name": "Peter",
    "last_name": "Djami",
    "location_information": {
        "address": ["yaoundé", "Cameroon", "Simbock"],
        "location": {
            "latitude": 3.8384765,
            "longitude": 11.5006256
        },
        "quater": "Simbock"
    },
    "account_status": "active"
}

def weekdays_in_month(year, month):
    weekdays = [day for day in range(0, 7) if day < 5]  # Monday to Friday
    _, last_day = calendar.monthrange(year, month)
    weekdays_in_month = [calendar.day_name[calendar.weekday(year, month, day)] for day in range(1, last_day + 1) if calendar.weekday(year, month, day) in weekdays]
    return weekdays_in_month

# get all agent shift for a particular month
def agent_shift_count(agent):
    agent_shift = agent["agent_shift"]
    agent_shift_count = 0

    current_month = datetime.now().strftime('%B')
    all_weekdays = weekdays_in_month(datetime.now().year, datetime.now().month)
        

    print(all_weekdays);
    
    # Loop through all weekdays in the month
    for day in all_weekdays:
        # Check if the day is in the agent's shift schedule
        if day in agent_shift:
            if len(agent_shift[day]) == 0:
                continue
            elif len(agent_shift[day]) == 1:
                agent_shift_count += 1
            else:
                agent_shift_count += 2
    

    print(f'Agent shift count: {agent_shift_count}')
    return agent_shift_count

def calculate_bonus(bookings):
    # Get all the bookings done by the agent for the month
    current_month = datetime.now().strftime('%B')
    agent_bookings = [booking for booking in bookings if booking["booking_start_at"].startswith(current_month)]

    # Separate residence and commercial bookings
    residence_bookings = [booking for booking in agent_bookings if not booking["is_commercial"]]
    commercial_bookings = [booking for booking in agent_bookings if booking["is_commercial"]]

    # Calculate bonuses
    result1 = len(residence_bookings) // 20
    remainder1 = len(residence_bookings) % 20

    if remainder1 > 0:
        result2 = remainder1 // 10
        remainder2 = remainder1 % 10

        if remainder2 > 0:
            result3 = remainder2 // 5
            remainder3 = remainder2 % 5

    # Calculate total bonus
    total_bonus = (result1 * 20) + (result2 * 10) + (result3 * 5) + (remainder3 * 50)

    # Get all shifts done by agent
    total_shifts = agent_shift_count(agent)

    print(f'Total shifts: {total_shifts}; Total bonus: {total_bonus}')

    # Calculate total salary
    total_salary = (total_shifts * 500) + total_bonus

    return total_salary

# Sample booking list
bookings = [
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "November 14, 2023 at 17:23:33 UTC1:00:00.000000",
    },
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "November 13, 2023 at 17:23:33 UTC1:00:00.000000",
    },
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "November 13, 2023 at 17:23:33 UTC1:00:00.000000",
    },
    {
        "_id": {"$oid": "649b0a4d77cb44c555f672f9"},
        "owner_amount": 2000,
        "owner_id": "6495afc32937ad6e5d431c2f",
        "request_status": "Completed",
        "service_type": "pickup",
        "system_price": 1500,
        "description": "the second blue trash bin on the street",
        "localisation": {"latitude": 14.2437, "longitude": 118.2437},
        "trash_bin_image_url": "",
        "is_commercial": False,
        "booking_start_at": "November 13, 2023 at 17:23:33 UTC1:00:00.000000",
    },
]

total_salary = calculate_bonus(bookings)

print("Total Salary:", total_salary)
