from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
driver.get("https://test.dashboard.u-smile.app/login")
driver.implicitly_wait(10)

# Identification des éléments
email = driver.find_element(By.ID, 'input-3')
password = driver.find_element(By.ID, 'input-5')
bouton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div/div[3]/form/div/div[2]/button')
element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/aside/aside/ul/li[1]/a')
element2 =driver.find_element(By.XPATH, 'div/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/button[1]')
element3=driver.find_element(By.XPATH, 'div/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/button[1]/span[3]')
element4=driver.find_element(By.XPATH, '//*[@id=\"invoice-list\"]/div[3]/div[2]/div/div/table/tbody/tr[1]/td[7]/span/button')
element5=driver.find_element (By.XPATH, 'div/div/div/div/div[1]/main/div/div[1]/div/div/div[2]/div[2]/span[1]/button/span[4]')
element6=driver.find_element(By.XPATH, '/html/body/div[5]/div/div[6]/button[1]')

# Actions
email.send_keys("derouichewifek88@gmail.com")
password.send_keys("$2y$10$8JbJh84fJAOAer01mzFbPOpEuzw/n3eKmLiKdATT1fQvLFLWOucXq")
print("Email et mot de passe saisis")
bouton.click()
element.click()
element2.click()
element3.click()
element4.click()
element5.click()
element6.click()
# Afficher un message de débogage
print("Bouton cliqué")

 

 




        