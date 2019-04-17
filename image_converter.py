import cv2
import numpy as np
import glob

a = 'C:/Users/hids/Desktop/test_images_for_compile'.replace('\\', '/')

img_array = []
for filename in glob.glob(a+'/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project2.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    for j in range(60):
        out.write(img_array[i])
        print(i, j)
out.release()
cv2.destroyAllWindows()
print('complite')