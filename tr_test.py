from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageDraw
import uuid
"""Open and image and show it"""
# im = Image.open('app/static/imagenet_subset/n01498041_stingray.JPEG')
# print(im.format, im.size, im.mode)
# im.show()

"""Resize and rotate image"""
# out = im.resize((128, 128))
# out = im.rotate(45) # degrees counter-clockwise
# out.show()

"""Change color of the image"""
# with Image.open('app/static/imagenet_subset/n01498041_stingray.JPEG') as im:
# im = im.convert("L")
# im.show()

"""Filter"""
# out = im.filter(ImageFilter.DETAIL)
# out.show()

"""Applying point transforms"""
# multiply each pixel by 5
# out = im.point(lambda i: i * 5)
# out.show()






"""Image Enhance"""

# Reference: https://www.geeksforgeeks.org/python-pil-imageenhance-color-and-imageenhance-contrast-method/

im = Image.open('app/static/imagenet_subset/n01498041_stingray.JPEG')

"""Color"""
col = ImageEnhance.Color(im)
# col.enhance(5.0).show()


"""Brightness"""
brh = ImageEnhance.Brightness(im)
# brh.enhance(0.3).show()   # downgrade brightness


"""Contrast"""
con = ImageEnhance.Contrast(im)
# con.enhance(1.3).show("30% more contrast")


"""Sharpness"""
sharp = ImageEnhance.Sharpness(im)
# sharp.enhance(3.0).show() # upgrade sharpness



def transformation_image(image, path, color_factor=1.0, brightness_factor=1.0, contrast_factor=1.0,
                         sharpness_factor=1.0):  # default values
    img = Image.open(image)  # open the image
    col = ImageEnhance.Color(img)
    im_col = col.enhance(color_factor)  # set the color factor
    brh = ImageEnhance.Brightness(im_col)
    im_col_brh = brh.enhance(brightness_factor)  # set brightness factor to the previous modified image
    con = ImageEnhance.Contrast(im_col_brh)
    im_cal_brh_con = con.enhance(contrast_factor)  # set contrast factor to the previous modified image
    sharp = ImageEnhance.Sharpness(im_cal_brh_con)
    im_cal_brh_con_sharp = sharp.enhance(sharpness_factor)  # set sharpness factor to the previous modified image
    #im_cal_brh_con_sharp.show()
    im_cal_brh_con_sharp.save(path)
image_id = uuid.uuid4()
img_test = 'app/static/imagenet_subset/n02105056_groenendael.JPEG'
#img.show()
path_tr = f'app/static/img_transformation/transform_{image_id}.JPEG'
transformation_image(img_test, path_tr, color_factor=1.5, brightness_factor=1.9, contrast_factor=1.4, sharpness_factor=5.0)
# plt.savefig(f'app/static/imagenet_transform/trans_{img_transformed}')
