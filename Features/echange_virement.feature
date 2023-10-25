@tag
Feature: Valider le virement bancaire d'un client
 @tag
Feature: Valider le virement bancaire d'un client
  Background:
    Given Saisir le lien "https://test.dashboard.u-smile.app/login"
    When Saisir E-mail "derouichewifek88@gmail.com"
    And Saisir le mot de passe1 "$2y$10$8JbJh84fJAOAer01mzFbPOpEuzw/n3eKmLiKdATT1fQvLFLWOucXq"
    And Cliquer sur le bouton login.login

  @tag1
  Scenario: Valider le virement bancaire d'un client
    Given Cliquer sur le menu Echanges
    And Cliquer sur le menu Virement bancaire
    And Cliquer sur le menu Transaction en attente
    And Cliquer sur le bouton détails de virement d'un client
    When Cliquer sur le bouton valider la transaction
    And Cliquer sur le bouton oui pour confirmer la transaction

 
   