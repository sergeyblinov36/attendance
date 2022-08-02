import requests
from datetime import datetime

global status
status = 0
global startTime
staff = requests.get("https://eyesave.herokuapp.com/staff")

def unknown_person(flag):
    global status
    global startTime
    global staff
    url = "https://eyesave-noitfications.herokuapp.com/escort/send/"
    if status == 0 and flag == 0:
        url = "https://eyesave.herokuapp.com/events/"
        now = datetime.now()
        startTime = now.strftime("%H:%M")
        date = now.strftime("%Y-%m-%d")
        data1 = {'_date': date,
                 '_startTime': startTime,
                 '_endTime': '',
                 '_duration': '',
                 '_eventType': 'Stranger',
                 '_child1': '',
                 '_child2': '',
                 '_videoUrl': ''}
        request = requests.post(url, json=data1)
    for el in staff.json():
        if "_telegramID" in el:
            if status == 0 or flag == 0:
                data = {"userId": el["_telegramID"],
                        "msg": "Warning !!!! \n A suspicious person was identified!"}
                request = requests.post(url, json=data)
                status = 1
                startTime = datetime.now()
                print("started")
            elif status == 1 and flag == 1:
                curr_time = datetime.now()
                duration = curr_time - startTime
                print(duration)
                if duration.total_seconds() > 60:
                    status = 0
                    print("ended")
