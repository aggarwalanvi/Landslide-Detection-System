import cv2 as cv
import numpy as np

# from picamera import PiCamera
# from time import sleep

# camera = PiCamera()
# camera.start_preview()
# sleep(5)
# for i in range(6):
#     sleep(0.5)
#     camera.capture('/home/raspberry/Desktop/Landslide Prediction/image%s.jpg' % i)    
# camera.stop_preview()

# li = []


# # for i in range(5):
A = cv.imread("test1.jpg")
B = cv.imread("test2.jpg")
C=cv.imread("test3.jpg")
D=cv.imread("test4.jpg")
E=cv.imread("test5.jpg")

height = 312
width = 312
delta = cv.norm(C , E, cv.NORM_L2 )
v = delta / ( height * width )
# avg = 0
# for i in li:
#     avg +=i

# avg /=5

# if avg>0.5:
#     print('Alert landslide is coming')
if v>0.4 :
    print('Image Variance = ',v)
    print("Threat!!")
else:
    print('No threat')

cv.waitKey(0)
