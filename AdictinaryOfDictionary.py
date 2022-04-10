


users = {
    'aeinstein': {
        'first':'abbert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username, user_dict in users.items():
    print('\nUsername: ' + username)
    full_name = user_dict['first'] + ' '
    full_name += user_dict['last']
    location = user_dict['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())