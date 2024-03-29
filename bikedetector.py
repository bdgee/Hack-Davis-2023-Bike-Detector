import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os
import takepicture

def count_bikes():
    takepicture.picture_capture()
    img = cv2.imread('bike.png')

    box, label, count = cv.detect_common_objects(img, confidence = 0.3)
    bikebox = [box[i] for i in range(len(box)) if label[i] == "bicycle"]
    bikelabel = [label[i] for i in range(len(label)) if label[i] == "bicycle"]
    bikecount = [count[i] for i in range(len(count)) if count[i] == "bicycle"]
    print(label)
    # output = draw_bbox(img, bikebox, bikelabel, bikecount)

    # output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    # plt.figure(figsize=(12,12))
    # plt.imshow(output)
    # plt.axis('off')
    # plt.show()

    print("Number of objects in this image are " +str(len(label)))
    print("Number of bicycles in this image are " +str(len([bicycle for bicycle in label if bicycle == "bicycle"])))

    if os.path.exists("bike.png"):
        os.remove("bike.png")
    else:
        print("The file does not exist") 

    return len([bicycle for bicycle in label if bicycle == "bicycle"])