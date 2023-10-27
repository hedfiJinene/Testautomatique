Feature: Changement de statut de lead
Background
    Given Saisir l'url de la page "https://test.dashboard.u-smile.app/login"
    When Saisir l'adresse mail"derouichewifek88@gmail.com"
    And Saisir le mot de passe "$2y$10$8JbJh84fJAOAer01mzFbPOpEuzw/n3eKmLiKdATT1fQvLFLWOucXq"
    And Cliquer sur le bouton Login
    Then Vérifier la réussite de la connexion "https://test.dashboard.u-smile.app/dashboards/analytics"
Scenario: Changer le statut d'un lead
    Given Cliquer sur le menu backoffice
    And Cliquer sur le menu répertoire de lead
    When Cliquer sur le menu Urne des leads
    Then Cliquer sur le bouton New
    And Cliquer sur la liste déroulante status
    And Choisir le statut "En cours"
    And Cliquer sur le bouton Enregistrer
    And Vérifier le changement de statut de lead
   
