eco_levels = {
    'entry': 1000,
    'gold': 3000,
    'platinum': 5000,
}

dummy_owner = {
    'name': 'John Doe',
    'overall_eco_points': 0,
    'eco_points': 0,
    'eco_level': "entry",
}


def earn_ecopoints(price, owner):
    # GET OWNER PRICE USED FOR PURCHASE

    # GET OWNER ECO LEVEL
    eco_level = owner['eco_level']
    ecopoints = owner['eco_points']
    overall_eco_points = owner['overall_eco_points']

    if price > 0:
        # convert price to ecopoints; 10 price = 1 ecopoint
        ecopoints = price / 10
    else:
        print("Price is invalid")
        return None
    
    print(f"Eco points earned: {ecopoints}")
    # UPDATE OWNER ECO POINTS
    dummy_owner['eco_points'] = ecopoints
    dummy_owner['overall_eco_points'] = ecopoints

    # CHECK OWNER ECO LEVEL BASED ON ECO POINTS GAINED
    if overall_eco_points >= eco_levels['gold']:
        dummy_owner['eco_level'] = "gold"
    elif overall_eco_points >= eco_levels['platinum']:
        dummy_owner['eco_level'] = "platinum"
    else:
        dummy_owner['eco_level'] = "entry"
    
    return dummy_owner

print(earn_ecopoints(2100, dummy_owner))