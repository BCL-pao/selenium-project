import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Inicializar el driver de Chrome
driver = webdriver.Chrome()

# Navegar a la página de inicio de sesión
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Esperar a que el campo de correo electrónico esté presente antes de interactuar
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("testuser13@tripleten.com")
driver.find_element(By.ID, "password").send_keys("00000000")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Esperar a que la página se cargue y aparezca el feed de publicaciones
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "places__list")))

# Guardar el título de la publicación más reciente
title_before = driver.find_element(By.XPATH, "//li[@class='places__item card'][1]//h2[@class='card__title']").text

# Hacer clic en el botón que agrega una nueva publicación
driver.find_element(By.CLASS_NAME, "profile__add-button").click()

# Generar el nuevo nombre de la publicación y almacenarlo en new_title
new_title = f"Tokio{random.randint(100, 999)}"

# Insertar el valor de new_title en el campo Nombre
driver.find_element(By.NAME, "name").send_keys(new_title)

# Insertar el enlace de la imagen en el campo Enlace
image_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg"
driver.find_element(By.NAME, "link").send_keys(image_url)

# Guardar los datos haciendo clic en el botón 'Guardar'
save_button_xpath = ".//form[@name='new-card']/button[text()='Guardar']"
driver.find_element(By.XPATH, save_button_xpath).click()

# Esperar a que aparezca el botón Eliminar de la nueva publicación
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//li[@class='places__item card'][1]//button[@class='card__delete-button card__delete-button_visible']"))
)

# Verificar que la nueva tarjeta tiene el título correcto
title_after = driver.find_element(By.XPATH, "//li[@class='places__item card'][1]//h2[@class='card__title']").text
assert new_title == title_after

# Guardar la cantidad de tarjetas antes de eliminar la nueva
cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))

# Eliminar la nueva tarjeta
delete_button_xpath = "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']"
driver.find_element(By.XPATH, delete_button_xpath).click()

# Esperar a que el título de la tarjeta más reciente sea igual al de antes (title_before)
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']"), title_before)
)

# Comprobar que ahora hay una tarjeta menos
cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
assert cards_before - 1 == cards_after

# Cerrar el navegador
driver.quit()