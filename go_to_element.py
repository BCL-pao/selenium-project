from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Esperar a que el campo de correo electrónico esté presente antes de interactuar
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("testuser13@tripleten.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("00000000")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "card__image")))


# Buscar el pie de página
element = driver.find_element(By.TAG_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", element)

# Comprobar que el pie de página contiene el string 'Around'
assert 'Around' in element.text

driver.quit()
