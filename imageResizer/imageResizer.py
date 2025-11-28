from PIL import Image

def resizeImage(input_img, output_img, size):
    orginal = Image.open(input_img)
    resized = orginal.resize(size)
    resized.save(output_img)


input_img = 'qwerty.jpg'


output_img = 'output.jpg'
new_size = (200,230)

resizeImage(input_img=input_img, output_img=output_img, size=new_size)
# import os
# from PIL import Image
#
# input_img = './DSDSSDSF.png'
# if not os.path.isfile(input_img):
#     print("Image not found at:", input_img)
# else:
#     try:
#         original = Image.open(input_img)
#         # Do resizing...
#     except Exception as e:
#         print("Error opening image:", e)