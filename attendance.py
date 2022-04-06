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
    departureTime = now.replace(hour=12, minute=0, second=0, microsecond=0)
    # the jsons are saved in different repositories
    if role == "child":
        # path = children_collection
        url = "http://localhost:8000/childrenAttendance/"
        query = "_childId"
        path = requests.get("http://localhost:8000/childrenAttendance/")
    else:
        # path = staff_collection
        url = "http://localhost:8000/staffAttendance/"
        query = "_employeeId"
        path = requests.get(url)
        print(path.text)
    # DBelements = path.find()
    found = False
    for element in path.json():
        # print(query)
        if element[query] == id:
            found = True
            print(element[query])
            if element["_date"] == dString:
                if departureTime < now:
                    # path.update_one(
                    #     {query: int(element[query])},
                    #     {
                    #         "$set": {
                    #             "_departureTime": tString
                    #         },
                    #         "$currentDate": {"lastModified": True}
                    #
                    #     }
                    # )
                    url = "http://localhost:8000/childrenAttendance/"
                    url1 = f'{url }{element["_id"]}'
                    # url1 ="%s%s" % (url, id)
                    # print(type(url1))
                    data = {
                        "_departureTime": tString
                    }
                    param = {"_childId": id}
                    request = requests.put(url1, json=data)
                    print(request.text)
            else:
                createData(id, role, path)
    if found == False:
        createData(id, role, path)


def createData(id, role, path):
    now = datetime.now()
    dString = now.strftime("%Y-%m-%d")
    tString = now.strftime("%H:%M:%S")

    if role == "child":
        # path.insert_one(
        #     {"_childId": int(id),
        #      "_date": dString,
        #      "_arrivalTime": tString,
        #      "_departureTime": "",
        #      "_absence": '',
        #      "_childDelay": False,
        #      "_escortDelay": False}
        # )
        url = "http://localhost:8000/childrenAttendance/"
        data = {"_childId": int(id),
                "_date": dString,
                "_arrivalTime": tString,
                "_departureTime": "",
                "_absence": '',
                "_childDelay": False,
                "_escortDelay": False}
        request = requests.post(url, json=data)
        print(request.text)
    if role == "staff":
        # path.insert_one(
        #     {
        #         "_employeeId": int(id),
        #         "_date": dString,
        #         "_arrivalTime": tString,
        #         "_departureTime": "",
        #     }
        # )
        url = "http://localhost:8000/staffAttendance/"
        data = {"_employeeId": int(id),
                "_date": dString,
                "_arrivalTime": tString,
                "_departureTime": "",
                }
        request = requests.post(url, json=data)
        print(request.text)

