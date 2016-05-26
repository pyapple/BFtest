from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Applications/chromedriver')
driver.get("https://booking.prod.movinga.com/lead_steps/addresses")


flex_time = driver.find_element_by_name("lead[flexible_move_date]")
flex_time.click()

from_address = driver.find_element_by_id("form-fromAddress")
from_address.send_keys("Leopoldstraße 175,  80804 München")

to_address = driver.find_element_by_id("form-fromAddress")
to_address.send_keys("Heidelberger Str. 69,  69436 Schönbrunn")

button_next = driver.find_element_by_class_name("button cta")
button_next.click()

assert "No results found." not in driver.page_source
#@driver.close()