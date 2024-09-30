import itertools
from time import sleep
import math
import pandas as pd

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

from selenium import webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://neal.fun/perfect-circle/')

from selenium.webdriver.common.by import By
driver.find_element(By.XPATH, '//button[@class="on"]').click()
sleep(1)

section_canvas = driver.find_element(By.TAG_NAME, 'section')
canvas = section_canvas.find_element(By.TAG_NAME, 'svg')

canvas_width = section_canvas.size['width']
canvas_height = section_canvas.size['height']

center_x = 0
center_y = 0
radius = 200

from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)

start_x = center_x + radius * math.cos(0)
start_y = center_y + radius * math.sin(0)
actions.move_to_element_with_offset(canvas, start_x, start_y).click_and_hold()

for angle in range(0, 363, 13):
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    actions.move_by_offset(int (x - start_x),int (y - start_y))
    start_x, start_y = x, y

actions.release().perform()

sleep(5)
driver.quit()