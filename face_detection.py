# importing libraries
import cv2
import numpy as npy
import face_recognition as face_rec
# function
def resize(img,size):
    width=int(img.shape[1]*size)
    height=int(img.shape[0]*size)
    dimension=(width,height)
    return cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
# img declaration
praneeth=face_rec.load_image_file('sample_images\praneeth.jpg')
praneeth=cv2.cvtColor(praneeth,cv2.COLOR_BGR2RGB)
praneeth=resize(praneeth,0.50)
praneeth_test=face_rec.load_image_file('sample_images\elonmusk.jpeg')
#praneeth_test=resize(praneeth_test,0.50)
praneeth_test=cv2.cvtColor(praneeth_test,cv2.COLOR_BGR2RGB)

# finding face location

faceLocation_praneeth=face_rec.face_locations(praneeth)[0]
encode_praneeth=face_rec.face_encodings(praneeth)[0]
cv2.rectangle(praneeth,(faceLocation_praneeth[3],faceLocation_praneeth[0]),(faceLocation_praneeth[1],faceLocation_praneeth[2]),(255,0,255),3)

faceLocation_praneeth_test=face_rec.face_locations(praneeth_test)[0]
encode_praneeth_test=face_rec.face_encodings(praneeth_test)[0]
cv2.rectangle(praneeth_test,(faceLocation_praneeth_test[3],faceLocation_praneeth_test[0]),(faceLocation_praneeth_test[1],faceLocation_praneeth_test[2]),(255,0,255),3)

results=face_rec.compare_faces([encode_praneeth],encode_praneeth_test)
print(results)
cv2.putText(praneeth_test,f'{results}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('main_img',praneeth)
cv2.imshow('test_img',praneeth_test)
cv2.waitKey(0)
cv2.destroyAllWindows()