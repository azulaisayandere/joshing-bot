import json

read_log = json.load(open("user_log.json", "r"))

masslist = read_log['guilds']
write = {"guilds": masslist}

async def log_data(message):

    #guild data
    g = False
    for guilds in masslist:
        if guilds['guid'] == message.guild.id:
            userlist = guilds['users']
            g = True
        elif guilds['name'] == message.guild:
            guilds['name'] == f'{message.guild}'
            print("[{}] {} has changed their guild name to {}, updating entry in file.".format(message.created_at.strftime('%H:%M:%S'), guilds['name'], message.guild))
            g = True
        else:
            pass

    if g == True: # user data
        u = False
        for users in userlist:
            if users['name'] == f'{message.author}':
                u = True
                user = users
            elif (users['uid'] == message.author.id) and (users['name'] != f'{message.author}'):
                print("[{}] User {} has changed their tag to {}, updating entry in file.".format(message.created_at.strftime('%H:%M:%S'), users['name'], message.author))
                users['name'] = f'{message.author}'
                u = True
                user = users

        if u == True: # update msg count
            user['cnt'] += 1

        else: # log users
            userlist.append({
                'name': f'{message.author}',
                'uid': message.author.id,
                'dnm': 40,
                'cnt': 1})
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Logged new user in {message.guild}! {message.author}")
    else:
        masslist.append({
            "name": f'{message.guild}', "guid": int(f'{message.guild.id}'), 'users': []})
        for guilds in masslist:
            if guilds['guid'] == message.guild.id:
                guilds['users'].append({
                        'name': f'{message.author}',
                        'uid': message.author.id,
                        'dnm': 40,
                        'cnt': 1})
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Logged new user in {message.guild}! {message.author}")
            else:
                pass

    # write to files
    with open('user_log.json', 'w') as userfile:
        json.dump(write, userfile, indent=2)
