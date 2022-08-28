import cv2
import glob #used for processing multiple images
import os #used for finding path of files

#--------------------------Face detection ---------------------------------


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

this_folder = os.path.dirname(os.path.abspath(__file__))    #variable to find absolute path location
my_file = os.path.join(this_folder, "bryan.jpg")   #Path to file


img = cv2.imread(my_file)
    #Second Command means 0 = Black and White, 1 = Color, -1 = means transparency capabilities

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV_IYUV)
    #Taking the image and editing out the color to become gray

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.01, minNeighbors = 5)
    #passing face_cascade object to call function, 1st parameter is used for image name
    #second parameter is the scaling factor. Everytime the image processes it shrinks the image each time
    #until it can find a face object. 3rd parameter is the minimal amount of neighbors, how many other
    #faces it can detect around the main face.

for x, y, w, h, in faces:
    img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)
    #rectangle accepts multiple parameters, 1st being file being passed, 2nd is the first
    #coordinates of the rectangle and where it starts, 3rd is used to map the rectangle providing
    #the coordinates of the next to points x + width, and y + height. 4th is used for the color scale
    #current is green. 5th parameter is how thick the line is.

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape([0]/3))))

cv2.imshow("Gray", resized)   
cv2.waitKey(0)
cv2.destroyAllWindows()

#--------------------------Basic image processing-----------------------------------
    #When using glob use for loop, to loop through image folder container file name

images = glob.glob(".jpg")

for image in images:

    print(type(img))
    print(img) 
    #Print the arrays of the image, extensive list

resized_img = cv2.resize(img, (500, 700)) 
    #Python is using the cv2.resize() to resize the img, takes two arguments, The image that needs to be resized
    #and the tuple of the two parameters that state the new size of said image.
    #To keep a healthy image, use the dimensions ratio provided when using the img.shape function
    #such as cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imwrite("Bryan_resized.jpg", resized_img)
    #Creates new file image of Bryan that is resized and saves it to the computer

cv2.imshow("Bryan", resized_img) #Displays an image in a window named the first argument, the image is provided in the second argument
cv2.waitKey(0) #How long it takes a commond to be issued, 0 means first key hit, and is measured in milliseconds
cv2.destroyAllWindows() #The command that proceeds after waitkey() function has timed out
