Feature: Connexion
  Scenario: Connexion
      Given Saisir l'url de la page
      When Saisir l'adresse mail
      And Saisir le mot de passe
      And Cliquer sur le bouton Login
      Then Vérifier la réussite de la connexion