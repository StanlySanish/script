"""This is a script to add signature into pictures which is also known as watermark This project consist of two main folders
    those are:
    1--> Input Output Images: Where we keep the input images and also get the signed new processed image.
    2--> WaterMark Images: Where we store our signatures.
"""


import glob
from PIL import Image
import sys

images = []
"""Make sure that you change both the below directory paths as per your computers paths.
    Also don't forget to add "/*" at last of the path in order to get all the images present in the location. """

input_image_path = output_image_path = "/home/sanish/Documents/Image Process Script/Input Output Images/*"
watermark_image_path = "/home/sanish/Documents/Image Process Script/signature/*"


# This function combines the image and watermark together
def watermark_photo(input_image_path, watermark_image_path):
    output_image_path = input_image_path
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)

    position = get_image_size(input_image_path, watermark_image_path)
    base_image.paste(watermark, position)
    base_image.save(output_image_path)
    # To show the new saved images as pop-up uncomment the next line.
    #base_image.show()


# This function is used to get the size of the image inorder to allign the watermark at the right-bottom.
def get_image_size(input_image_path, watermark_image_path):
    image = Image.open(input_image_path)
    width, height = image.size

    image2 = Image.open(watermark_image_path)
    image2_w, image2_h = image2.size

    pos = ((width - image2_w), (height - image2_h))
    return pos


# This function help to get all images present in the specific location
def get_all_images(input_image_path):
    for img in glob.glob(input_image_path):
        images.append(img)
    return images


"""This function is used to get watermark. But in this function the user can set watermark in backend as his needs.
    This function also works fine so if you want to know the images you wanted to enter just use this code"""
# def get_watermark_image(choice):
#     if choice == 1:
#         watermark_image_path = "/home/anoop/Image Process Script/Watermark Images/123456.jpg"
#     elif choice == 2:
#         watermark_image_path = "/home/anoop/Image Process Script/Watermark Images/1234.jpg"
#     elif choice == 3:
#         watermark_image_path = "/home/anoop/Image Process Script/Watermark Images/12345.jpg"
#     else:
#         print("Please enter a proper choice")
#     return watermark_image_path


"""Below function is also used to get watermark. But in this function the user cannot set watermark in backend as his needs."""


def get_watermark_image(choice):
    for img in glob.glob(watermark_image_path):
        images.append(img)
    if images[choice]:
        water_mark_image_path = images[choice]
    else:
        print("Please enter a proper number for your signature")
    return water_mark_image_path


# This function allows to upload images as one by one.
def image_uploader(water_mark):
    input_image_path = "/home/sanish/Documents/Image Process Script/Input Output Images/*"

    watermark_image_path = get_watermark_image(water_mark) #Here we get the watermark image which the user selected.
    obj = get_all_images(input_image_path) #Here we get list of images inside our Input Output folder.

    for input_image_path in obj:
        watermark_photo(input_image_path, watermark_image_path)


#Assigning Values and also calling the function(Please delete this after you understand sanish).
"""In the below lines a= list(sys.argv) implies :
    Example
    If we enter script as "Python3 script.py 1" 
    the output of a is ["script.py","1"]
    so we took a[1] as the water mark image we wanted to input
    we have a number of choice for water_mark as: 1,2,3....
     but make sure the user have a proper count of no of watermark he has added."""


a = list(sys.argv)
if len(a) > 2:
    print("Only one number can be entered after the .py file")
else:
    water_mark = int(a[1])

#This is where the water_marking process starts.
image_uploader(water_mark)
