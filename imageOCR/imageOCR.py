# coding=UTF-8

import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from pytesseract import *
from PIL import Image
from PIL import ImageEnhance  
from PIL import ImageFilter  
import traceback

threshold = 140 
table = []  

