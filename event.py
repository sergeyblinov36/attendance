import requests
from datetime import datetime
global status
status = 0
global startTime

def unknown():
    global status
    global startTime
    url = "http://localhost:8000/events/"
    if status == 0:
        data = {}
        # request = requests.post(url, data=data)
        status = 1
        startTime = datetime.now()
        print("started")
    else:
        curr_time = datetime.now()
        duration = curr_time - startTime
        print(duration)
        if duration.total_seconds() > 5:
            status = 0
            print("ended")
