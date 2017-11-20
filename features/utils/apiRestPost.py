payload = {'Email' : 'todo@jala.com', 'Password' : '123456', 'Fullname' : '123456'  }

r = request.post("https://Todo.ly/API/user.json", data = payload)
print(r.json)