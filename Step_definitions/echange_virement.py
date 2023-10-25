from behave import *
from echange_virement import EchangeObject
from Setup import Setup

# Initialisation du pilote WebDriver
driver = Setup.initialize_driver()

valider_echange = EchangeObject(driver)

@given("Cliquer sur le menu Echanges")
def step_impl(context):
    valider_echange.cliqueEchanges()    

@given("Cliquer sur le menu Virement bancaire")
def step_impl(context):
    valider_echange.cliqueVirement_bancaires()

@given("Cliquer sur le menu Transaction en attente")
def step_impl(context):
    valider_echange.cliquetransaction_attente()

@given("Cliquer sur le bouton détails de virement d'un client")
def step_impl(context):
    valider_echange.cliqueDétails()

@when("Cliquer sur le bouton valider la transaction")
def step_impl(context):
    valider_echange.cliquevalider_boutton()

@when("Cliquer sur le bouton oui pour confirmer la transaction")
def step_impl(context):
    valider_echange.cliqueoui()




