# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:25:16 2020

@author: Liqiong LIU
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

homo = np.zeros(0)
homo_pre = np.array([(1,0,0),(0,1,0),(0,0,1)])
UPDATE = 1
kernal_size = 20

img_original = cv2.imread("0.jpeg")
img0 = cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY)
cv2.imwrite(str(0)+'output.jpg', img0) 
# Create ORB detector with 5000 features. 
orb_detector = cv2.ORB_create(50) 
  
# Find keypoints and descriptors. 
# The first arg is the image, second arg is the mask 
#  (which is not reqiured in this case). 
kp1, d1 = orb_detector.detectAndCompute(img0, None) 
pt_this = np.zeros((len(kp1),2))
for i in range(len(kp1)):
    pt_this[i,:] = kp1[i].pt
    
range_start = 1
range_end = 100
for kk in range(range_start,range_end):
    # Open the image files. 
    
    img1_color = cv2.imread(str(kk-1)+"output"+".jpg")  # Image to be aligned. 
    img2_color = cv2.imread(str(kk)+".jpg")    # Reference image. 
      
    # Convert to grayscale. 
    img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY) 
    img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY) 
    height, width = img2.shape 
    
    count=0
    
    
    p1 = np.zeros((1,2))
    p2 = np.zeros((1,2))


    

        
    for i in range(len(kp1)):        
        c_index = int(pt_this[i,0])
        r_index = int(pt_this[i,1])  
        
      
    

        if r_index<height-kernal_size and c_index<width-kernal_size:
        
             # The keypoint block of original image
            
            kernal = img1[r_index-kernal_size:r_index+kernal_size+1,c_index-kernal_size:c_index+kernal_size+1]
            
            kernal_float = kernal.astype(np.float32)
            
            kernal_Gaussian = cv2.GaussianBlur(kernal_float, (3,3), 0)
            kernal_Laplacian = cv2.Laplacian(kernal_Gaussian,cv2.CV_32F) 

            # The keypoint block of current image
            im_temp = img2[r_index-kernal_size:r_index+kernal_size+1,c_index-kernal_size:c_index+kernal_size+1]
            im_temp_float = im_temp.astype(np.float32)
            
            im_temp_Gaussian = cv2.GaussianBlur(im_temp_float, (3,3), 0)
            im_temp_Laplacian = cv2.Laplacian(im_temp_Gaussian,cv2.CV_32F)
            hanning = cv2.createHanningWindow((kernal_size*2+1,kernal_size*2+1),cv2.CV_32F)
            
            shift,response = cv2.phaseCorrelate(kernal_Laplacian,im_temp_Laplacian)
            
                
                
            
            if response>0.5:
            
                homography = np.array([[1,0,shift[0]],[0,1,shift[1]],[0,0,1]])
                transformed_img = cv2.warpPerspective(kernal_float, 
                            homography, (kernal_size*2+1,kernal_size*2+1)) 
                
                im_temp_original = np.absolute(kernal_float-im_temp_float)
                im_temp_results = np.absolute(im_temp_float-transformed_img)
                
                find_1 = np.flatnonzero(kernal > 10)
                find_2 = np.flatnonzero(im_temp > 10)
                #print(str(len(find_1)),str(len(find_2)))
                
                
                p1 = np.append(p1,[[c_index,r_index]],axis=0)
                p2 = np.append(p2,[[c_index+shift[0],r_index+shift[1]]],axis=0)
                #print(shift[0],shift[1],response)
                
    p1 = np.delete(p1,0,axis=0)
    p2 = np.delete(p2,0,axis=0)
    p_shift = p2-p1
    p_shift_x = np.mean(p_shift[...,0])
    p_shift_y = np.mean(p_shift[...,1])
    
    # perspective transform compared with the previous registrated image
    homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC,5.0 ) 
    
    
    if np.absolute(homography[0,2])>(kernal_size) or np.absolute(homography[1,2])>(kernal_size):
        homography = np.array([(1,0,0),(0,1,0),(0,0,1)])

        print("corrected homography")
    
    # accumulated perspective transform    
    homo_current = np.dot(homo_pre,homography)
    # generate registrated image
    transformed_img = cv2.warpPerspective(img_original, 
                        homo_current, (width, height)) 
    cv2.imwrite(str(kk)+'output.jpg', transformed_img) 
    homo_pre = homo_current
    pt_this = np.array([pt_this])
    pt_this = cv2.perspectiveTransform(pt_this,homography)
    pt_this = pt_this.reshape(len(kp1),-1)
    
    
    
    