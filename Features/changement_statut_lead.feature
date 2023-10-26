Feature: Changement de statut de lead

Scenario: Changer le statut d'un lead
    Given Cliquer sur le menu backoffice
    And Cliquer sur le menu répertoire de lead
    When Cliquer sur le menu Urne des leads
    Then Cliquer sur le bouton New
    And Cliquer sur la liste déroulante status
    And Choisir le statut "En cours"
    And Cliquer sur le bouton Enregistrer
    And Vérifier le changement de statut de lead
   
