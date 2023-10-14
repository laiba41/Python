users = []
new_user = {
    'last': 'laiba',
    'first': 'noor',
    'username': 'fiza',
 }

users.append(new_user)

new_user = {
    'last': 'laiba',
    'first': 'noor',
    'username': 'fiza',
 }
users.append(new_user)

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
        print("\n")