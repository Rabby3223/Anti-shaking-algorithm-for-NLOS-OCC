% clc;clear all;close all
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %���������Ƶ����֡��ȡ
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
head=VideoReader('1618059714404.mp4');
frame_num=floor(head.Duration*head.FrameRate);
for i=1:200%1163:frame_num
  frame = read(head, i);
  imwrite(frame,strcat(num2str(i),'.jpg'));
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
