import cv2
import numpy as np

#######################################
def color_avg(lists, rgb):
	total = 0
	for i in lists:
		total += i[rgb]
	if len(lists) > 0:
		return total/len(lists)
	else:
		return 0

##############################################################
def sqaure_calc(img, i, j):
	#if(i < (img.shape[0] -1) and j < (img.shape[1] -1)):
		#print(img[i+1,j+1])
	lists = []
	lists.append(_square_calc(img, i, j))
	lists.append(_square_calc(img, i, j+1))
	lists.append(_square_calc(img, i, j+2))

	lists.append(_square_calc(img, i+1, j))
	lists.append(_square_calc(img, i+1, j+2))

	lists.append(_square_calc(img, i+2, j))
	lists.append(_square_calc(img, i+2, j+1))
	lists.append(_square_calc(img, i+2, j+2))

	#list comprehension 
	#lists = [ x for x in lists if x != -100]
	lists = list(filter((-100).__ne__, lists))
	#print(lists)

	if(i < (img.shape[0] -1) and j < (img.shape[1] -1)):
		img[i+1,j+1][0] = color_avg(lists,0)
		img[i+1,j+1][1] = color_avg(lists,1)
		img[i+1,j+1][2] = color_avg(lists,2)
		#print("changed avg")
		#print(img[i+1,j+1])

######################################################
#this function returns -100 if x or y are out of bounds
#Else it will return the pixel RBG
def _square_calc(img, i ,j):
	if(i > img.shape[0] -1 or j > img.shape[1] -1):
		return -100
	else:
		return img[i,j]

################################################################
#this function gets the rows and columns 
#then loops through every pixel and runs the calculation on each
def gaussian_blur(img):  
	img_rows = img.shape[0]
	img_cols = img.shape[1]

	for i in range(0,img_rows):
		for j in range(0, img_cols):
			sqaure_calc(img,i,j)




###################### M A I N #############################

img = cv2.imread('tiedye.jpg')

#running blur 3 times, very obvious blur
gaussian_blur(img)
gaussian_blur(img)
gaussian_blur(img)
print("done")


#this shows what we did to the pic
cv2.imwrite('blurr.jpg',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


