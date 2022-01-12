import time
from time import sleep
import json
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(
    executable_path = r'repository/driver/chromedriver',
    chrome_options = options
)

  
def TryMakeCheck(value):

  data_dict={}
  driver.get("http://www.cne.gob.ve/web/index.php")
  sleep(1)
  driver.set_window_size(1280, 962)
  driver.execute_script("window.scrollTo(0,318)")
  driver.find_element(By.NAME, "cedula").click()
  sleep(1)
  driver.find_element(By.NAME, "cedula").send_keys(f"{value}")
  driver.find_element(By.CSS_SELECTOR, "td:nth-child(3) > input").click()
  sleep(1)
  data = driver.find_element(By.ID,"datos_registro_electoral")
  element = driver.find_element(By.NAME, "cedula")
  actions = ActionChains(driver)
  actions.move_to_element(element).click_and_hold().perform()
  
  if  'V-0' in data.text:

    data_dict={
    'Cédula': 'No Disponible',
    'Nombre': 'No Disponible',
    'Estado': 'No Disponible',
    'Municipio': 'No Disponible',
    'Parroquia': 'No Disponible',
    'Centro': 'No Disponible'
    }
  elif 'objeción' in data.text:
    data_dict={
    'Cédula': 'No Disponible por objección',
    'Nombre': 'No Disponible por objección',
    'Estado': 'No Disponible por objección',
    'Municipio': 'No Disponible por objección',
    'Parroquia': 'No Disponible por objección',
    'Centro': 'No Disponible por objección'
    }

  else:

    for line in data.text[57:].splitlines():
      mark = line.split(":")
      if len(mark)==2:
        data_dict[mark[0]]=mark[1]
      else:
        pass

  return data_dict
  
  
  