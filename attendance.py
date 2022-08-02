from datetime import datetime
import requests


def markAttendance(id, role):
    now = datetime.now()
    dString = now.strftime("%Y-%m-%d")

    # the jsons are saved in different repositories
    if role == "child":
        # path = children_collection
        url = "https://eyesave.herokuapp.com/childrenAttendance/"
        query = "_childId"
        path = requests.get(url)
    else:
        # path = staff_collection
        url = "https://eyesave.herokuapp.com/staffAttendance/"
        query = "_employeeId"
        path = requests.get(url)
        print(path.text)
    IDfound = False
    dateFound = False
    for element in path.json():
        # print(query)
        if element[query] == id:
            IDfound = True
            if element["_date"] == dString:
                dateFound = True
    if not IDfound:
        createData(id, role, path)
    if IDfound and not dateFound:
        createData(id, role, path)


def createData(id, role, path):
    now = datetime.now()
    dString = now.strftime("%Y-%m-%d")
    tString = now.strftime("%H:%M")

    if role == "child":
        url = "https://eyesave.herokuapp.com/childrenAttendance/"
        data = {"_childId": int(id),
                "_date": dString,
                "_arrivalTime": tString,
                "_departureTime": "",
                "_absence": False,
                "_childDelay": False,
                "_escortDelay": False}
        request = requests.post(url, json=data)
        print(request.text)
    if role == "staff":
        url = "https://eyesave.herokuapp.com/staffAttendance/"
        data = {"_employeeId": int(id),
                "_date": dString,
                "_arrivalTime": tString,
                "_departureTime": "",
                }
        request = requests.post(url, json=data)
        print(request.text)


def escortArrival(id):
    url = f'https://eyesave.herokuapp.com/escorts/{id}'
    escortData = requests.get(url)
    print(escortData.text)
    data = {
        "_escortArrival": True
    }
    date = datetime.now()
    dateSTR = date.strftime("%Y-%m-%d")
    escort = escortData.json()
    for element in escort["_children"]:
        query = f'https://eyesave.herokuapp.com/childrenAttendance/{dateSTR}/children/{element}'
        req = requests.put(query, json=data)
        print(req.text)
