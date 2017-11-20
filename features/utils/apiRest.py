import requests
header = {'Authorization':'Basic cWEudGVzdGluZy5kZ3NAZ21haWwuY29tOmRpZWdvMTk4Nw=='}
r = requests.get('https://Todo.ly/API/user.json', headers=header)

print("Values \n", r.json())
print("Context \n", r.content)
print("Code \n", r.status_code)
