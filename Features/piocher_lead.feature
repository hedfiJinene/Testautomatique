Feature: Piocher un lead
  Scenario: Piocher un lead depuis le tableau de bord
    Given le télévendeur est sur la page du tableau de bord
    When le télévendeur se connecte avec l'adresse e-mail "votre_email" et le mot de passe "votre_mot_de_passe"
    And le télévendeur clique sur le bouton "Piocher un lead"
    Then le télévendeur vérifie que le lead a été pioché avec succès
