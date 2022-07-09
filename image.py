import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

hr = np.array(cv2.imread("./image/hr1.png"))
# fsrcnn = np.array(cv2.imread('/fsrcnn1.png'))
srcnn = np.array(cv2.imread('./image/srcnn1.png'))
bicubic = np.array(cv2.imread('./image/bicubic1.png'))
print(srcnn.shape)

def crop(image, left_top, x=200, y=200):
  	return image
# interpolation된 이미지와 고해상도 이미지의 동일한 부분을 각각 잘라냅니다.
left_top = (0,0)
crop_bicubic = crop(bicubic, left_top)
crop_hr = crop(hr, left_top)
# crop_fsrcnn = crop(fsrcnn, left_top)
crop_srcnn = crop(srcnn, left_top)


# 잘라낸 부분을 시각화합니다.
plt.figure(figsize=(15,50))
plt.subplot(1,2,1); plt.imshow(crop_hr); plt.title("HR", fontsize=30)
plt.subplot(1,2,1); plt.imshow(crop_srcnn); plt.title("SRCNN", fontsize=30)
plt.subplot(1,2,1); plt.imshow(crop_bicubic); plt.title("Bicubic", fontsize=30)
