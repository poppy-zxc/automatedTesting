'''
@Filename: automatedTesting -> common
@Author: AnnieZhang
@Date: 2023/2/2 17:39
'''
from PIL import Image
from pytesseract import pytesseract

def pillow_test():
    image = Image.open("verification_code.png")
    image_new = image.convert("L") # 将彩色图像转化为灰度图像
    im_new = image_new.point(lambda x:0 if x<143 else 255) # 二值化处理
    get_result = pytesseract.image_to_string(im_new)
    print(get_result)

if __name__ == '__main__':
    pillow_test()