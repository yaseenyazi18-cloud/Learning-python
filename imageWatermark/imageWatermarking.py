#IMASNGE WATERMARK

from PIL import Image, ImageDraw, ImageFont

def add_waterMark(input_image, output_image, text):
    orginal_image = Image.open(input_image)
    watermark_image = Image.new("RGBA", orginal_image.size)
    watermark_draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype('arial.ttf',100)
    width, height = orginal_image.size
    watermark_draw.text((0, height/2), text=text, fill=(255,255,255,140), font=font)
    
    watermarked = Image.alpha_composite(im1=orginal_image.convert("RGBA"), im2= watermark_image )
    watermarked.save(output_image,"PNG")
    print("watermark image generated.......!")

input_image = 'yazi.jpeg'
output_image = 'output.png'
text = input("Enter your watermark text: ")
add_waterMark(input_image, output_image, text)
