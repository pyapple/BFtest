from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Applications/chromedriver')
driver.get("https://booking-stg.movinga.com/lead_steps/addresses")


flex_time = driver.find_element_by_class_name("std")
flex_time.click()

from_address = driver.find_element_by_id("form-fromAddress")
from_address.send_keys("Leopoldstraße 175,  80804 München")

to_address = driver.find_element_by_id("form-toAddress")
to_address.send_keys("Heidelberger Str. 69,  69436 Schönbrunn")

button_next = driver.find_element_by_id("s-next-mobile")
#button_next.click()

assert "No results found." not in driver.page_source
#driver.close()
