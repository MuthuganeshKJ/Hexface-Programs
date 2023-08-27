from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

search_string = input("Input the Medicine you want to search for:")

driver  = webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\chromedriver.exe')

for i in range(1):
    matched_elements = driver.get("https://www.dictionary.com/browse/" + search_string)

reviews = driver.find_elements_by_xpath('//*[@id="base-pw"]/main/section/section/div[1]/section[2]/div[2]/div/div[1]')