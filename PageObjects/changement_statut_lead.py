from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class ChangementStatutLeadObject:
    def __init__(self, driver):
        self.driver = driver

    def clique_backoffice(self):
        backoffice = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/aside/aside/ul/li[2]/div/span")
        backoffice.click()

    def clique_repertoire_lead(self):
        repertoire_lead = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/aside/aside/ul/li[2]/ul/li[2]/a/span")
        repertoire_lead.click()

    def clique_urne(self):
        urne = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/button[2]")
        urne.click()

    def clique_action(self):
        action = self.driver.find_element(By.XPATH, "//*[@id=\"invoice-list\"]/div[3]/div[2]/div/div/table/tbody/tr[1]/td[10]/button/span[3]/svg")
        action.click()

    def clique_nouveau_lead(self):
        nouveau_lead = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/div[1]/main/div/div/div[2]/span[3]/div/button/span[3]")
        if nouveau_lead.text == "New":
            nouveau_lead.click()
        else:
            maj_btn = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/div[1]/main/div/div/div[2]/span[2]/div/button/span[3]")
            maj_btn.click()

    def clique_liste_deroulante(self):
        liste_deroulante = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/form/div[1]/div[1]/div/div/div/div/div[3]/div/div")
        liste_deroulante.click()

    def choisir_le_statut_en_cours(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN)  # Nouveau
        actions.send_keys(Keys.DOWN)  # SPAM
        actions.send_keys(Keys.DOWN)  # SPAM
        actions.send_keys(Keys.DOWN)  # SPAM
        actions.send_keys(Keys.SPACE)  # Valider la sélection
        actions.perform()

    def cliquer_enregistrer(self):
        enregistrer = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/form/div[2]/button[1]")
        enregistrer.click()

    def verifier_changement_statut_lead(self):
        time.sleep(2)  # Attendre quelques secondes pour que la page se mette à jour
        nouveau_lead = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div/div/div[1]/main/div/div/div[2]/span[2]/div/button/span[3]")
        assert nouveau_lead.text == "En cours"
        print("lead en cours")
    
        
