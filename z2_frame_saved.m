% clc;clear all;close all
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %对拍摄的视频进行帧提取
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
head=VideoReader('1618059714404.mp4');
frame_num=floor(head.Duration*head.FrameRate);
for i=1:200%1163:frame_num
  frame = read(head, i);
  imwrite(frame,strcat(num2str(i),'.jpg'));
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
