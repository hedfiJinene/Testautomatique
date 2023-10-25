from behave import *
from behave import given, when, then
import time


@given("Saisir l'url de la page")
def step_impl(context):
    context.authentification.load()

@when("Saisir l'adresse mail")
def step_impl(context, email):
    time.sleep(5)
    context.authentification.usernameSendKeys(email)

@step("Saisir le mot de passe")
def step_impl(context, password):
    time.sleep(5)
    context.authentification.passwordSendKeys(password)

@step("Cliquer sur le bouton Login")
def step_impl(context):
    time.sleep(5)
    context.authentification.loginButtonClick()

@then("Vérifier la réussite de la connexion")
def step_impl(context):
  time.sleep(5)
print("Email et mot de passe saisis")