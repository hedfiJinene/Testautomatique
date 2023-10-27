from behave import *
from selenium.webdriver.common.by import By
from time import sleep 

@given("le télévendeur est sur la page du tableau de bord")
def step_impl(context):
    context.browser.get("https://dashboard.u-smile.app/televendeurs")

@when("le télévendeur se connecte avec l'adresse e-mail "{email}" et le mot de passe "{password}"')
def step_impl(context, email, password):
    email_input = context.browser.find_element(By.ID, "email")
    email_input.send_keys(email)

    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys(password)

@when("le télévendeur clique sur le bouton Login")
def step_impl(context):
    login_button = context.browser.find_element(By.ID, "login-button")
    login_button.click()
    
 
@then("le télévendeur vérifie que le lead a été pioché avec succès")
def step_impl(context):
    # Insérez ici le code pour vérifier que le lead a été pioché avec succès
    pass
