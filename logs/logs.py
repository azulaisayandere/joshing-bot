import json
import pandas as pd

read_log = json.load(open("user_log.json", "r"))

userlist = read_log['users']
write_user = {"users": userlist}

async def log_data(message):

    # user data
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
        print(f"[{message.created_at.strftime('%H:%M:%S')}] Logged new user! {message.author}")

    # write to files
    with open('user_log.json', 'w') as userfile:
        json.dump(write_user, userfile, indent=2)
    pd.DataFrame(userlist, columns=['name', 'uid', 'dnm', 'cnt']).to_csv('user_log.csv')
