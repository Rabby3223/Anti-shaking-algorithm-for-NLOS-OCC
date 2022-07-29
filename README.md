# Anti-shaking-algorithm-for-NLOS-OCC
## Description
The NLOS OCC system using reflected light exhibits its advantages, such as (i) reduced requirement on alignment and (ii) the expanded received rolling shutter pattern to achieve a larger data rate. However, there are few investigations and solutions to the effect of unconcise handshaking in the NLOS OCC system. This 

## Anti-shaking algorithm

The challenge is to realize image registration between the long-exposure image and the corrupted short-exposure images.  
### Feature-based image registration algorithm
Match the key points based on their features.
The features may be corrupted by the stripes.
### Phase correlation algorithm
Estimate relative translative offset between two similar images.
Exhibit robust performance for noisy and corrupted images.
The perspective transformation cannot be derived. 
### Proposed anti-shaking algorithm
Step 1: Find key points from the long-exposure image.
Step 2: i) Apply phase correlation algorithm to the image blocks with key points at the center. ii) Calculate perspective transformation matrix based on the positions of key point pairs. iii) Generate transformed long-exposure image.
  
[https://github.com/Rabby3223/Anti-shaking-algorithm-for-NLOS-OCC/blob/main/algorithm.jpg](https://github.com/Rabby3223/Anti-shaking-algorithm-for-NLOS-OCC/blob/main/algorithm.jpg)

## Getting started

Anaconda 3  
Matlab 2021b  
  
0.jpeg: Image captured with long exposure time  
1618053369425.mp4：Video captured with low expsoure time  
z2_frame_saved.m: Convert video to images  
anti_shaking.py: Anti-shaking algorithm
mutual_information.py: Calculate mutual information between the low=exposure image and long-exposure image  


## Authors

Liqiong Liu, Department of Information Engineering, The Chinese University of Hong Kong

## License

Distributed under the MIT License.
