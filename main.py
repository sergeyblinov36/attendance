from dis import code_info
import json

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from findEncodings import findEncodings
from attendance import markAttendance
import pymongo
import dbConnection
import time
import schedule
from event import unknown


def attendance():
    # paths
    pathStaff = 'staffImgs'
    pathChild = 'childImgs'
    # pathStaff = '../EyeSAVE-master/EyeSAVE_attendance_python/staffImgs'
    # pathChild = '../EyeSAVE-master/EyeSAVE_attendance_python/childImgs'
    db = dbConnection.get_connection()
    children_collection = db["children"]
    staff_collection = db["staff"]
    finishTime = datetime.now().replace(hour=23, minute=30, second=0, microsecond=0)
    # arrays of images, names and roles(child or staff member)
    images = []
    id_list = []
    role = []
    childrenList = os.listdir(pathChild)
    staffList = os.listdir(pathStaff)
    # print(childrenList)
    for cl in childrenList:
        # read image from repository
        Img = cv2.imread(f'{pathChild}/{cl}')
        # add image to the array
        images.append(Img)
        # add the name to the array without .jpg
        id_list.append(os.path.splitext(cl)[0])
        role.append("child")
    # print(id_list)
    for cl in staffList:
        Img = cv2.imread(f'{pathStaff}/{cl}')
        images.append(Img)
        id_list.append(os.path.splitext(cl)[0])
        role.append("staff")
    # print(id_list)

    # encode the images
    encodeListKnown = findEncodings(images)
    # print('Encoding Complete')

    # rtsp://tapocamnum2:Ss321352387@192.168.0.8:554/stream1
    # rtsp://tapocamnum1:Ss321352387@192.168.0.6:554/stream1
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("rtsp://tapocamnum2:Ss321352387@192.168.0.8:554/stream1")

    while True:
        success, img = cap.read()
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

            # if the faces match change the name to upper letters and draw the rectangle around the face
            if matches[matchIndex]:
                idString = id_list[matchIndex]
                # print(id)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, idString, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                id = int(idString)
                # mark attendance
                if role[matchIndex] == "child":
                    markAttendance(id, "child")
                else:
                    markAttendance(id, "staff")
            else:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                unknown()

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q') or finishTime < datetime.now():
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    # schedule.every().day.at("07:30").do(attendance)
    # while True:
    #     schedule.run_pending()
    #     print("sleeping")
    #     time.sleep(1)
    attendance()


if __name__ == '__main__':
    main()
