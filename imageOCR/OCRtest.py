# coding=UTF-8

# from selenium import webdriver
# # from imageOCR import *
# import time

# driver = webdriver.Chrome()
# driver.get(urls)

# # 查找图片元素
# image_element = driver.find_element_by_tag_name('img')

# # 获取图片URL
# image_url = image_element.get_attribute('src')

# time.sleep(1)


import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = 'https://www.baidu.com/'
# urlregister = url + 'register.php'

# 创建Chrome浏览器选项
chrome_options = Options()
chrome_options.add_argument("--start-minimized")

# 创建Chrome浏览器驱动程序
driver = webdriver.Chrome(options=chrome_options)
# 打开网页
driver.get(url)

# 使用 find_element 方法定位图片元素
image_element = driver.find_element(By.ID, "s_lg_img")

# 展开验证码
# link_element = driver.find_element(By.ID, 'codeImgText')
# print(link_element)
# link_element.click()
# time.sleep(1)
# 获取图片的 src 属性值
image_src = url + image_element.get_attribute("src")
print(image_src)

location = image_element.location
size = image_element.size
driver.save_screenshot("screenshot.png")
x = location['x']
y = location['y']
width = size['width']
height = size['height']
captcha = Image.open("screenshot.png")
captcha = captcha.crop((x, y, x+width, y+height))

# 使用pytesseract进行字符识别
text = pytesseract.image_to_string(captcha)

# 打印识别结果
print(text)

# 关闭浏览器
driver.quit()
