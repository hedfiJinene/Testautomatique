Feature: Refuser un virement bancaire
  Je veux refuser un virement bancaire

  Background:
    Given Saisir le lien "https://test.dashboard.u-smile.app/login"
    When Saisir E-mail "derouichewifek88@gmail.com"
    And Saisir le mot de passe1 "$2y$10$8JbJh84fJAOAer01mzFbPOpEuzw/n3eKmLiKdATT1fQvLFLWOucXq"
    And Cliquer sur le bouton login.login

  @tag1
  Scenario: Refuser un virement bancaire
    Given Cliquer sur le menu Echange
    And Cliquer sur le menu Virement bancaire1
    When Cliquer sur le menu Transaction en attente1
    And Cliquer sur le bouton détails de virement d'un client1
    And Cliquer sur le bouton refuser
    And Expliquer le motif de refus "refus"
    And Cliquer sur enregistrer1
    And valider le refus
    And Vérifier l'URL obtenu "https://test.dashboard.u-smile.app/exchanges"
