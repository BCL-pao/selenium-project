from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Buscar el título
driver.find_element(By.CSS_SELECTOR, '.auth-form__title')

# Cerrar el navegador
driver.quit()
