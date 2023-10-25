from behave import *
from behave import given, when, then
from changement_statut_lead import changementstatutleadObject
import time

@given("Cliquer sur le menu backoffice")
def step_cliquer_sur_le_menu_backoffice(context):
    context.changement_lead = changementstatutleadObject(context.driver)
    context.changement_lead.clique_backoffice()

@given("Cliquer sur le menu répertoire de lead")
def step_cliquer_sur_le_menu_repertoire_de_lead(context):
    context.changement_lead.clique_repertoire_lead()

@when("Cliquer sur le menu Urne des leads")
def step_cliquer_sur_le_menu_urne_des_leads(context):
    context.changement_lead.clique_urne()

@then("Cliquer sur le bouton New")
def step_cliquer_sur_le_bouton_new(context):
    context.changement_lead.clique_nouveau_lead()

@then("Cliquer sur la liste déroulante status")
def step_cliquer_sur_la_liste_deroulante_status(context):
    context.changement_lead.clique_liste_deroulante()

@then('Choisir le statut "{statut}"')
def step_choisir_le_statut(context, statut):
    context.changement_lead.choisir_le_statut(statut)

@then("Cliquer sur le bouton Enregistrer")
def step_cliquer_sur_le_bouton_enregistrer(context):
    context.changement_lead.cliquer_enregistrer()

@then("Vérifier le changement de statut de lead")
def step_verifier_le_changement_de_statut_de_lead(context):
    context.changement_lead.verifier_changement_statut_lead()
