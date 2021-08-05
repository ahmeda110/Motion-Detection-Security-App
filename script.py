#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import cv2
from datetime import datetime


firstFrame = None
statusList = [None, None]
times = []
video = cv2.VideoCapture(0)


while True:
    status = 0
    (confirm, frame) = video.read()

    grayImg = cv2.cvtColor(
                            frame,
                            cv2.COLOR_BGR2GRAY
                        )

    grayImg = cv2.GaussianBlur(
                                grayImg, 
                                (21, 21), 
                                0
                            )
    if firstFrame is None:
        firstFrame = grayImg
        continue

    deltaFrame = cv2.absdiff(
                            firstFrame,
                             grayImg
                            )

    thresholdFrame = cv2.threshold(
                                    deltaFrame,
                                    30,
                                    255,
                                    cv2.THRESH_BINARY
                                   )[1]

    thresholdFrame = cv2.dilate(
                                thresholdFrame,
                                None,
                                iterations=2
                            )

    (contours, _) = cv2.findContours(
                                        thresholdFrame.copy(),
                                        cv2.RETR_EXTERNAL, 
                                        cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        if cv2.contourArea(i) < 10000:
            continue

        status = 1
        (x, y, width, height) = cv2.boundingRect(i)
        cv2.rectangle(
                        frame,
                        (x, y), 
                        (x + width, y + height), 
                        (0, 255,0),
                        3
                    )

    statusList.append(status)

    
    if statusList[-1] == 1 and statusList[-2] == 0:
        times.append(datetime.now())
    if statusList[-1] == 0 and statusList[-2] == 1:
        times.append(datetime.now())

    # cv2.imshow('Gray Frame', grayImg)
    # cv2.imshow('Delta Frame', deltaFrame)
    # cv2.imshow('Threshold Frame', thresholdFrame)
    cv2.imshow('Recording', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

video.release()
cv2.destroyAllWindows()

df = pd.DataFrame(columns=['START', 'END'])

for i in range(0, len(times), 2):
    df = df.append(
                    {
                        'START': times[i],
                        'END': times[i + 1]
                    },
                    ignore_index=True
                )

df.to_csv('Times.csv')
