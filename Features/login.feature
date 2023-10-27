Feature: Connexion
  Scenario: Connexion
      Given Saisir l'url de la page "https://test.dashboard.u-smile.app/login"
      When Saisir l'adresse mail"derouichewifek88@gmail.com"
      And Saisir le mot de passe "$2y$10$8JbJh84fJAOAer01mzFbPOpEuzw/n3eKmLiKdATT1fQvLFLWOucXq"
      And Cliquer sur le bouton Login
      Then Vérifier la réussite de la connexion""https://test.dashboard.u-smile.app/dashboards/analytics""