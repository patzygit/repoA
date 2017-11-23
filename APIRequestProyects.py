import requests

#if __name__ == '__main__':
urlToDo = 'https://todo.ly/api'
accessToken = {'Authorization':'Basic cWEudGVzdGluZy5kZ3NAZ21haWwuY29tOmRpZWdvMTk4Nw=='}

def CreateProyect():
    urlProyects = '/projects.json'
    url = urlToDo + urlProyects
    createParams = {"Content": "My New Project-dgs", "Icon": 4}
    response = requests.post(url,json=createParams, headers=accessToken)
    if response.status_code == 200:
        payload = response.json()
        print(payload)

def GetProyect():
    urlProyects = '/projects.json'
    url = urlToDo+urlProyects
    response = requests.get(url, headers=accessToken)
    if response.status_code== 200:
        payload = response.json()
        print(payload)

def GetProyectID(id):
    urlProyects = '/projects/'+id+'.json'
    url = urlToDo + urlProyects
    print(url)
    response = requests.get(url, headers=accessToken)
    if response.status_code == 200:
        payload = response.json()
        print(payload)

def UpdateProyectID(id):
    urlProyects = '/projects/' + id + '.json'
    url = urlToDo + urlProyects
    updateParams = {"Icon":2}
    print(url)
    response = requests.put(url, json=updateParams, headers=accessToken)
    if response.status_code == 200:
        payload = response.json()
        print(payload)

def DeleteProyectID(id):
    urlProyects = '/projects/' + id + '.json'
    url = urlToDo + urlProyects
    print(url)
    response = requests.delete(url, headers=accessToken)
    print(response.status_code)
    if response.status_code == 200:
        payload = response.json()
        print(payload)
    else:
        print("************************")

def getItemsInAProject(id):
    urlProyects = '/projects/' + id + '/items.json'
    url = urlToDo + urlProyects
    print(url)
    response = requests.get(url, headers=accessToken)
    if response.status_code == 200:
        payload = response.json()
        print(payload)


def GetDoneItemsOfAProject(id):
    urlProyects = '/projects/' + id + '/doneitems.json'
    url = urlToDo + urlProyects
    print(url)
    response = requests.get(url, headers=accessToken)
    if response.status_code == 200:
        payload = response.json()
        print(payload)






#CreateProyect()
#GetProyect()
#3662821
GetProyectID("3662854")
#UpdateProyectID("3662821")
#DeleteProyectID("3660943")
#getItemsInAProject("3660943")
#GetDoneItemsOfAProject("3660943")
