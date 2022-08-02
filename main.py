# from dis import code_info
# import json
#
# import cv2
# import numpy as np
# import face_recognition
# import os
# from datetime import datetime
# from findEncodings import findEncodings
# from attendance import markAttendance
# import pymongo
# import dbConnection
# import time
# import schedule
# from event import unknown_person
#
#
# def attendance():
#     # paths
#     pathStaff = 'staffImgs'
#     pathChild = 'childImgs'
#     # pathStaff = '../EyeSAVE-master/EyeSAVE_attendance_python/staffImgs'
#     # pathChild = '../EyeSAVE-master/EyeSAVE_attendance_python/childImgs'
#     db = dbConnection.get_connection()
#     children_collection = db["children"]
#     staff_collection = db["staff"]
#     finishTime = datetime.now().replace(hour=23, minute=30, second=0, microsecond=0)
#     # arrays of images, names and roles(child or staff member)
#     images = []
#     id_list = []
#     role = []
#     childrenList = os.listdir(pathChild)
#     staffList = os.listdir(pathStaff)
#     # print(childrenList)
#     for cl in childrenList:
#         # read image from repository
#         Img = cv2.imread(f'{pathChild}/{cl}')
#         # add image to the array
#         images.append(Img)
#         # add the name to the array without .jpg
#         id_list.append(os.path.splitext(cl)[0])
#         role.append("child")
#     # print(id_list)
#     for cl in staffList:
#         Img = cv2.imread(f'{pathStaff}/{cl}')
#         images.append(Img)
#         id_list.append(os.path.splitext(cl)[0])
#         role.append("staff")
#     # print(id_list)
#
#     # encode the images
#     encodeListKnown = findEncodings(images)
#     print('Encoding Complete')
#
#     # rtsp://tapocamnum2:Ss321352387@192.168.0.8:554/stream1
#     # rtsp://tapocamnum1:Ss321352387@192.168.0.6:554/stream1
#     cap = cv2.VideoCapture(0)
#     # cap = cv2.VideoCapture("rtsp://tapocamnum2:Ss321352387@192.168.0.8:554/stream1")
#
#     while True:
#         success, img = cap.read()
#         # resize and change colour of the live stream
#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#         # locate and encode faces from the frame
#         facesCurFrame = face_recognition.face_locations(imgS)
#         encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
#
#         # compare the faces from the frame to the faces from the repositories
#         for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#             matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#             faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#             matchIndex = np.argmin(faceDis)
#
#             # if the faces match change the name to upper letters and draw the rectangle around the face
#             if matches[matchIndex]:
#                 idString = id_list[matchIndex]
#                 # print(id)
#                 y1, x2, y2, x1 = faceLoc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                 cv2.putText(img, idString, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 id = int(idString)
#                 # mark attendance
#                 if role[matchIndex] == "child":
#                     markAttendance(id, "child")
#                 else:
#                     markAttendance(id, "staff")
#             else:
#                 y1, x2, y2, x1 = faceLoc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                 cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 unknown_person()
#
#         cv2.imshow('Webcam', img)
#         cv2.waitKey(1)
#         if cv2.waitKey(1) & 0xFF == ord('q') or finishTime < datetime.now():
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# def main():
#     # schedule.every().day.at("07:30").do(attendance)
#     # while True:
#     #     schedule.run_pending()
#     #     print("sleeping")
#     #     time.sleep(1)
#     attendance()
#
#
# if __name__ == '__main__':
#     main()
# from dis import code_info
# import json

# import cv2
# import numpy as np
# import face_recognition
# import os
# from datetime import datetime
# from findEncodings import findEncodings
# from attendance import markAttendance
# import pymongo
# import dbConnection
# import time
# import schedule
# from event import unknown_person

# def attendance():
#     # paths
#     pathStaff = '../EyeSAVE-master/EyeSAVE_attendance_python/staffImgs'
#     pathChild = '../EyeSAVE-master/EyeSAVE_attendance_python/childImgs'
#     db = dbConnection.get_connection()
#     children_collection = db["children"]
#     staff_collection = db["staff"]
#     finishTime = datetime.now().replace(hour=22, minute=59, second=0, microsecond=0)
#     # arrays of images, names and roles(child or staff member)
#     images = []
#     id_list = []
#     role = []
#     childrenList = os.listdir(pathChild)
#     staffList = os.listdir(pathStaff)
#     # print(childrenList)
#     for cl in childrenList:
#         # read image from repository
#         Img = cv2.imread(f'{pathChild}/{cl}')
#         # add image to the array
#         images.append(Img)
#         # add the name to the array without .jpg
#         id_list.append(os.path.splitext(cl)[0])
#         role.append("child")
#     # print(id_list)
#     for cl in staffList:
#         Img = cv2.imread(f'{pathStaff}/{cl}')
#         images.append(Img)
#         id_list.append(os.path.splitext(cl)[0])
#         role.append("staff")
#     # print(id_list)

#     # encode the images
#     encodeListKnown = findEncodings(images)
#     # print('Encoding Complete')

#     cap = cv2.VideoCapture("rtsp://tapocamnum2:Ss321352387@192.168.0.8:554/stream1")
#     # cap = cv2.VideoCapture("rtsp://tapocamnum1:Ss321352387@176.229.235.86:554/stream1")

#     while True:
#         success, img = cap.read()
#         # resize and change colour of the live stream
#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#         # locate and encode faces from the frame
#         facesCurFrame = face_recognition.face_locations(imgS)
#         encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

#         # compare the faces from the frame to the faces from the repositories
#         for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#             matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#             faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#             matchIndex = np.argmin(faceDis)

#             # if the faces match change the name to upper letters and draw the rectangle around the face
#             if matches[matchIndex]:
#                 idString = id_list[matchIndex]
#                 # print(id)
#                 y1, x2, y2, x1 = faceLoc
#                 y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#                 cv2.putText(img, idString, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#                 id = int(idString)
#                 # mark attendance
#                 if role[matchIndex] == "child":
#                     markAttendance(id, "child")
#                 else:
#                     markAttendance(id, "staff")
#         # img = imutils.resize(img, width = 600)
#         #cv2.imshow('Webcam', img)
#         cv2.waitKey(1)
#         if cv2.waitKey(1) & 0xFF == ord('q') or finishTime < datetime.now():
#             break

#     cap.release()
#     cv2.destroyAllWindows()


# def main():
#     # schedule.every().day.at("22:42").do(attendance)
#     # while True:
#     #     schedule.run_pending()
#     #     print("sleeping")
#     #     time.sleep(1)
#     attendance()


# # if __name__ == '__main__':
# #     main()

from dis import code_info
import json

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from findEncodings import findEncodings
from attendance import markAttendance, escortArrival
import pymongo
import dbConnection
import time
import schedule
from event import unknown_person
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
import json
import numpy as np
import urllib.request as urllib
import base64


def attendance():
    # paths
    pathStaff = 'staffImgs'
    pathChild = 'childImgs'
    pathEscort = 'escortImgs'
    settings = requests.get("https://eyesave.herokuapp.com/settings/")
    finishTime = settings[0]["_endMorning"]
    # arrays of images, names and roles(child or staff member)
    images = []
    id_list = []
    role = []
    # paths to children, staff and escorts information
    children = requests.get("https://eyesave.herokuapp.com/children/")
    staff = requests.get("https://eyesave.herokuapp.com/staff/")
    escorts = requests.get("https://eyesave.herokuapp.com/escorts/")
    print(children.text)
    # add the children images to the images array, their ids to the id list and their role "child" to the role array
    for cl in children.json():
        print(cl['_imageUrl'])
        Img = None
        try:
            resp = urllib.urlopen(cl['_imageUrl'])
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            Img = cv2.imdecode(image, cv2.IMREAD_COLOR)
            # Img = base64.b64decode(cl['_imageUrl'].encode('ascii'))
            images.append(Img)
            id_list.append(cl['_id'])
            role.append("child")
        except Exception as e:
            print(e)

    # add the staff images to the images array, their ids to the id list and their role "staff" to the role array
    for employee in staff.json():
        # read image from repository
        # newpath = pathChild + cl
        # Img = mpimg.imread(cl)
        # Img = cv2.imread(f'{pathChild}/{cl}')
        print(employee['_imageUrl'])
        Img = None
        try:
            resp = urllib.urlopen(employee['_imageUrl'])
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            Img = cv2.imdecode(image, cv2.IMREAD_COLOR)
            # Img = base64.b64decode(cl['_imageUrl'].encode('ascii'))
            images.append(Img)
            id_list.append(employee['_id'])
            role.append("staff")
        except Exception as e:
            print(e)

    # add the escorts images to the images array, their ids to the id list and their role "escort" to the role array
    for escort in escorts.json():
        # read image from repository
        # newpath = pathChild + cl
        # Img = mpimg.imread(cl)
        # Img = cv2.imread(f'{pathChild}/{cl}')
        print(escort['_imageUrl'])
        Img = None
        try:
            resp = urllib.urlopen(escort['_imageUrl'])
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            Img = cv2.imdecode(image, cv2.IMREAD_COLOR)
            # Img = base64.b64decode(cl['_imageUrl'].encode('ascii'))
            images.append(Img)
            id_list.append(escort['_id'])
            role.append("escort")
        except Exception as e:
            print(e)
        # Img = cv2.imread(cl['_imageUrl'])
        # add image to the array

        # add the name to the array without .jpg
        # id_list.append(os.path.splitext(cl)[0])

    # # print(id_list)
    # for cl in staffList:
    #     Img = mpimg.imread(f'{pathStaff}/{cl}')
    #     images.append(Img)
    #     id_list.append(os.path.splitext(cl)[0])
    #     role.append("staff")
    # for cl in escortList:
    #     Img = mpimg.imread(f'{pathEscort}/{cl}')
    #     images.append(Img)
    #     id_list.append(os.path.splitext(cl)[0])
    #     role.append("escort")
    # print(id_list)

    # encode the images
    print(len(images))
    print(id_list)
    encodeListKnown = findEncodings(images)
    # print('Encoding Complete')


    camera = settings.json()
    cam = camera[0]['_cameraUrl1']
    # cap = cv2.VideoCapture(cam)
    cap = cv2.VideoCapture(0)

    flag = 0
    while True:
        success, img = cap.read()
        if success:
            # resize and change colour of the live stream
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            # locate and encode faces from the frame
            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            # compare the faces from the frame to the faces from the repositories
            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                # if the faces match draw the rectangle around the face
                if matches[matchIndex]:
                    idString = str(id_list[matchIndex])
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, idString, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    id = int(idString)
                    if flag == 1:
                        flag = 0
                    # mark attendance
                    if role[matchIndex] == "child":
                        markAttendance(id, "child")
                    elif role[matchIndex] == "staff":
                        markAttendance(id, "staff")
                    elif role[matchIndex] == "escort":
                        escortArrival(id)
                else:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    unknown_person(flag)
                    flag = 1
            img = cv2.resize(img, (600, 500))
            cv2.imshow('Webcam', img)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('q') or finishTime < datetime.now():
                break
        else:
            cap.release()
            time.sleep(60)
            cap = cv2.VideoCapture(cam)

    cap.release()
    cv2.destroyAllWindows()


def main():
    settings = requests.get("https://eyesave.herokuapp.com/settings/")
    schedule.every().sunday.at(settings[0]["_startMorning"]).do(attendance)
    schedule.every().monday.at(settings[0]["_startMorning"]).do(attendance)
    schedule.every().tuesday.at(settings[0]["_startMorning"]).do(attendance)
    schedule.every().wednesday.at(settings[0]["_startMorning"]).do(attendance)
    schedule.every().thursday.at(settings[0]["_startMorning"]).do(attendance)
    # schedule.every().day.at("22:58").do(attendance)
    # while True:
    #     schedule.run_pending()
    #     print("sleeping")
    #     time.sleep(1)
    attendance()


if __name__ == '__main__':
    main()
