'''
test_ROI.py
https://stackoverflow.com/questions/47857141/attributeerror-module-cv2-has-no-attribute-imread
imread installation issues: https://stackoverflow.com/questions/47857141/attributeerror-module-cv2-has-no-attribute-imread
'''
import cv2
import numpy as np

if __name__ == '__main__':
    #Read Image
    im = cv2.imread("test.jpg")
    print (im.shape)
    #Select ROI
    try:
    	r = cv2.selectROI("selection_window",im,False, False)
    	print (r)
    except:
    	exit()

#https://learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/
#https://stackoverflow.com/questions/47857141/attributeerror-module-cv2-has-no-attribute-imread
