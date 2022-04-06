from datetime import datetime
import dbConnection
import requests

db = dbConnection.get_connection()
children_collection = db["children_attendance"]
staff_collection = db["staff_attendance"]


def markAttendance(id, role):
    now = datetime.now()
    dString = now.strftime("%Y-%m-%d")
    tString = now.strftime("%H:%M")
    departureTime = now.replace(hour=15, minute=30, second=0, microsecond=0)
    # the jsons are saved in different repositories
    if role == "child":
        # path = children_collection
        url = "https://eyesaveserver.herokuapp.com/childrenAttendance/"
        query = "_childId"
        path = requests.get("https://eyesaveserver.herokuapp.com/childrenAttendance/")
    else:
        # path = staff_collection
        url = "https://eyesaveserver.herokuapp.com/staffAttendance/"
        query = "_employeeId"
        path = requests.get(url)

    # DBelements = path.find()
    found = False
    for element in path.json():
        if element[query] == id:
            found = True
            if element["_date"] == dString:
                if departureTime < now:
                    url = "https://eyesaveserver.herokuapp.com/childrenAttendance/"
                    url1 = f'{url }{element["_id"]}'
                    data = {
                        "_departureTime": tString
                    }
                    param = {"_childId": id}
                    request = requests.put(url1, json=data)
            else:
                createData(id, role, path)
    if found == False:
        createData(id, role, path)


def createData(id, role, path):
    now = datetime.now()
    dString = now.strftime("%Y-%m-%d")
    tString = now.strftime("%H:%M")

    if role == "child":
        url = "https://eyesaveserver.herokuapp.com/childrenAttendance/"
        data = {"_childId": int(id),
                "_date": dString,
                "_arrivalTime": tString,
                "_departureTime": "",
                "_absence": '',
                "_childDelay": False,
                "_escortDelay": False}
        request = requests.post(url, json=data)
    if role == "staff":
        url = "https://eyesaveserver.herokuapp.com/staffAttendance/"
        data = {"_employeeId": int(id),
                "_date": dString,
                "_arrivalTime": tString,
                "_departureTime": "",
                }
        request = requests.post(url, json=data)

