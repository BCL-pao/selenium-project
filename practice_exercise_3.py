from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Esperar a que el campo de correo electrónico esté presente antes de interactuar
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("testuser13@tripleten.com")
driver.find_element(By.ID, "password").send_keys("00000000")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Buscar la tarjeta y desplazarla a la vista
element = driver.find_element(By.CSS_SELECTOR, ".places__list .places__item")
driver.execute_script("arguments[0].scrollIntoView();", element)


driver.quit()
