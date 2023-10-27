from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Chemin du pilote Chrome
chrome_driver_path = "src/test/ressources/chromedriver.exe"

# Configuration du pilote Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximise la fenêtre du navigateur
chrome_driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

# Définition d'un temps d'attente implicite
chrome_driver.implicitly_wait(5)  # Attente implicite de 5 secondes

# Ouvrir l'URL
chrome_driver.get("https://dashboard.u-smile.app/televendeurs")

# Déclaration de la variable
production = None

