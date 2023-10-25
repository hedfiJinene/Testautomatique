from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EchangeObject:
    def __init__(self, driver):
        self.driver = driver

    def cliqueEchanges(self):
        element = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/aside/aside/ul/li[3]/div")
        element.click()

    def cliqueVirement_bancaires(self):
        element = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/aside/aside/ul/li[3]/ul/li[1]/a/span")
        element.click()

    def cliquetransaction_attente(self):
        element = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/button[1]")
        element.click()

    def cliqueDétails(self):
        element = self.driver.find_element(By.XPATH, "//*[@id=\"invoice-list\"]/div[3]/div[2]/div/div/table/tbody/tr[1]/td[7]/span/button")
        element.click()

    def cliquevalider_boutton(self):
        element = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/div[1]/main/div/div[1]/div/div/div[2]/div[2]/span[1]/button/span[4]")
        element.click()

    def cliqueoui(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[6]/button[1]")
        element.click()

