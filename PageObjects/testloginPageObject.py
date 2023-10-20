from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "src/test/ressources/chromedriver.exe"

# Options du pilote Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

# Ouvrir le navigateur Chrome avec les options
driver = webdriver.Chrome(options=chrome_options)

# Maximiser la fenêtre du navigateur
driver.maximize_window()

# Temps d'attente implicite
driver.implicitly_wait(5)

# Ouvrir l'URL
driver.get("https://dashboard.u-smile.app/login")

# Déclaration des variables
email, password, bouton = None, None, None

# Identification des éléments
email = (By.ID, 'input-3')
password = (By.ID, 'input-5')
bouton = (By.XPATH, "div/div/div/div/div/div[2]/div/div[3]/form/div/div[2]/button")
email = driver.find_element(By.ID, 'input-3')
password = driver.find_element(By.ID, 'input-5')
bouton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div[3]/form/div/div[2]/button')
# Actions
email.send_keys("derouichewifek88@gmail.com")
password.send_keys("$2y$10$8JbJh84fJAOAer01mzFbPOpEuzw/n3eKmLiKdATT1fQvLFLWOucXq")
print("Email et mot de passe saisis")
bouton.click()
# Afficher un message de débogage
print("Bouton cliqué")
# Fermer le navigateur
driver.quit()




