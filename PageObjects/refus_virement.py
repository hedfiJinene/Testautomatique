from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RefusVirementObject:

    def __init__(self, driver):
        self.driver = driver

    def cliquer_sur_le_menu_echange(self):
        echanges = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div/aside/aside/ul/li[3]/div")
        echanges.click()

    def cliquer_sur_le_menu_virement_bancaire1(self):
        virement_bancaires = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div/aside/aside/ul/li[3]/ul/li[1]/a/span")
        virement_bancaires.click()

    def cliquer_sur_le_menu_transaction_en_attente1(self):
        transaction_attente = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/button[1]")
        transaction_attente.click()

    def cliquer_sur_le_bouton_details_de_virement_d_un_client1(self):
        details = self.driver.find_element(By.XPATH, "//*[@id='invoice-list']/div[3]/div[2]/div/div/table/tbody/tr[1]/td[7]/span/button")
        details.click()

    def cliquer_sur_le_bouton_refuser(self):
        btn_refuser = self.driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div/div[1]/main/div/div[1]/div/div/div[2]/div[2]/span[2]/button")
        btn_refuser.click()

    def expliquer_le_motif_de_refus(self, motif):
        raison_refus = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/form/div[1]/div/div/div/div/div/div[3]/textarea")
        raison_refus.send_keys(motif)

    def cliquer_sur_enregistrer1(self):
        btn_enregistrer = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/form/div[2]/button[1]/span[3]")
        btn_enregistrer.click()

    def valider_le_refus(self):
        btn_valider = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[6]/button[1]")
        btn_valider.click()
        WebDriverWait(self.driver, 30).until(EC.url_to_be("https://test.dashboard.u-smile.app/exchanges"))
