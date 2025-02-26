

users: dict[int, str] = {0: 'First User', 1: 'Second User'}

if user := users.get(1):
    print(f'{user} exists!')
else:
    print("No user was found!")
