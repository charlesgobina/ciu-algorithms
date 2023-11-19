# algorithm to convert points to rewards for an owner
import math

redeemables = {
    'voice_call': 100,
    'text_message': 50,
    'electricity': 1000,
    'data_bundle': 200,
}

eco_levels = {
    'entry': 1000,
    'gold': 3000,
    'platinum': 5000,
}

dummy_owner = {
    'name': 'John Doe',
    'overall_eco_points': 1000,
    'eco_points': 2000,
    'eco_level': "entry",
}

def redeem(owner, reward, count=1):
    eco_points = owner['eco_points']
    redeem_count = math.floor(eco_points / redeemables[reward])

    # ask user if they want to use all their points on this reward
    choice = input(f'Do you want to use all your {eco_points} eco points on this reward? (y/n)')
    if choice == 'y':
        count = redeem_count
    else:
        print(f'You can redeem {redeem_count} {reward}s')
        count_reward = input(f'How many {reward}s do you want to redeem?')
        count = int(count_reward)
    
    # update owner's eco points
    owner['eco_points'] -= count * redeemables[reward]

    # update owner's eco level
    match owner['eco_points']:
        case x if x < eco_levels['entry']:
            owner['eco_level'] = 'entry'
        case x if x < eco_levels['gold']:
            owner['eco_level'] = 'gold'
        case x if x < eco_levels['platinum']:
            owner['eco_level'] = 'platinum'
        case _:
            owner['eco_level'] = 'platinum'

    return {
        'owner': owner,
        'redeem_count': redeem_count,
        'reward': reward,
    }

print(redeem(dummy_owner, 'voice_call'))

    