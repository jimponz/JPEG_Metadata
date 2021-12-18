from exif import Image
import os

for f in os.listdir(os.getcwd()):
    if ".jpg" in f:
        with open(f, 'rb') as image_file:
            my_image = Image(image_file)
            
            print(f + " has EXIF: " + str(my_image.has_exif))
            if my_image.has_exif():
                
            image_file.close()
