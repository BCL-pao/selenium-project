from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Esperar a que el campo de correo electrónico esté presente antes de interactuar
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))


# Iniciar sesión
# Buscar el campo Correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("testuser13@tripleten.com")

# Buscar el campo Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("00000000")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))


# Hacer clic en la foto de perfil
driver.find_element(By.CSS_SELECTOR, ".profile__image").click()

# Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Guardar la nueva foto
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Guardar']").click()

# Agregar una espera para que la nueva imagen de perfil se actualice
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_attribute(
    (By.CLASS_NAME, "profile__image"), "style", avatar_url
))

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
profile_image = driver.find_element(By.CLASS_NAME, "profile__image")
style = profile_image.get_attribute("style")

# Comprobar que style contiene el enlace a la foto de perfil
assert avatar_url in style, "La imagen de perfil no se actualizó correctamente."


driver.quit()
