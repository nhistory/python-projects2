from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.amazon.ca/Best-Sellers-Electronics-Computer-Accessories/zgbs/electronics/1235983011/ref=zg_bs_nav_electronics_2_2404990011')

time.sleep(1)

# elem_list = browser.find_element(By.CSS_SELECTOR, "div.p13n-gridRow._cDEzb_grid-row_3Cywl")

items = browser.find_elements(By.XPATH, '//*[@id="gridItemRoot"]')

for item in items:
  title = item.find_element(By.CSS_SELECTOR, "._cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
  print("Title: ",title.text)

