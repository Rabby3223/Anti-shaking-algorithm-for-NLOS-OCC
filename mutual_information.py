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



def mutual_information(hgram):
     """ Mutual information for joint histogram
     """
     # Convert bins counts to probability values
     pxy = hgram / float(np.sum(hgram))
     px = np.sum(pxy, axis=1) # marginal for x over y
     py = np.sum(pxy, axis=0) # marginal for y over x
     px_py = px[:, None] * py[None, :] # Broadcast to multiply marginals
     # Now we can do the calculation using the pxy, px_py 2D arrays
     nzs = pxy > 0 # Only non-zero pxy values contribute to the sum
     return np.sum(pxy[nzs] * np.log(pxy[nzs] / px_py[nzs]))


infor_array_ref = np.zeros(100)
infor_array = np.zeros(100)


    
range_start = 1
range_end = 100
for kk in range(range_start,range_end):
    # Open the image files. 
    

    img1_color = cv2.imread(str(kk)+"output"+".jpg")  # Image to be aligned. 
        
    img2_color = cv2.imread(str(kk)+".jpg")    # Reference image. 
    img3_color = cv2.imread("0.jpeg")
      
    # Convert to grayscale. 
    img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY) 
    img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY) 
    img3 = cv2.cvtColor(img3_color, cv2.COLOR_BGR2GRAY) 
    height, width = img2.shape 

    
    hist_2d, x_edges, y_edges = np.histogram2d(img2.ravel(),img3.ravel(),bins=100)
    mutual_info = mutual_information(hist_2d)
    infor_array_ref[kk-1] = mutual_info
    
    hist_2d, x_edges, y_edges = np.histogram2d(img2.ravel(),img1.ravel(),bins=100)
    mutual_info = mutual_information(hist_2d)
    infor_array[kk-1] = mutual_info
    

a1 = np.mean(infor_array_ref)
a2 = np.mean(infor_array)
print('Mutual information for low-exposure image and long-exposure image: '+str(a1))
print('Mutual information for low-exposure image and corrected long-exposure image: '+str(a2))

