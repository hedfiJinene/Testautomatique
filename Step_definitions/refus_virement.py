from behave import *
from selenium.webdriver.common.by import By
from refus_virement import RefusVirementObject

# Importez la classe RefusVirementObject si elle se trouve dans un autre module.

refus_virement = RefusVirementObject(context.driver)

@given("Cliquer sur le menu Echange")
def cliquer_sur_le_menu_echange(context):
    refus_virement.cliquer_sur_le_menu_echange()

@given("Cliquer sur le menu Virement bancaire1")
def cliquer_sur_le_menu_virement_bancaire1(context):
    refus_virement.cliquer_sur_le_menu_virement_bancaire1()

@when("Cliquer sur le menu Transaction en attente1")
def cliquer_sur_le_menu_transaction_en_attente1(context):
    refus_virement.cliquer_sur_le_menu_transaction_en_attente1()

@when("Cliquer sur le bouton détails de virement d'un client1")
def cliquer_sur_le_bouton_détails_de_virement_d_un_client1(context):
    refus_virement.cliquer_sur_le_bouton_détails_de_virement_d_un_client1()

@when("Cliquer sur le bouton refuser")
def cliquer_sur_le_bouton_refuser(context):
    refus_virement.cliquer_sur_le_bouton_refuser()

@then("Expliquer le motif de refus {motif}")
def expliquer_le_motif_de_refus(context, motif):
    refus_virement.expliquer_le_motif_de_refus(motif)

@then("Cliquer sur enregistrer1")
def cliquer_sur_enregistrer1(context):
    refus_virement.cliquer_sur_enregistrer1()

@then("valider le refus")
def valider_le_refus(context):
    refus_virement.valider_le_refus()

@then("vérifier l'url obtenu {url}")
def vérifier_l_url_obtenu(context, url):
    refus_virement.vérifier_l_url_obtenu(url)
