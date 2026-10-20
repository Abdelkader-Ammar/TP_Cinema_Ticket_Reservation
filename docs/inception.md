# Enoncé — TP Cinéma (Inception / Étude préliminaire)

## 1. Vision (5 lignes)

**Problème :** Les clients doivent se déplacer au cinéma pour réserver une place et il est difficile de consulter les films et les séances en temps réel.

**Utilisateurs :** Client, Administrateur, Service de paiement.

**Valeur :** Réserver une place de cinéma en ligne rapidement, consulter les films et séances disponibles, et payer sans se déplacer.

## 2. Acteurs

- Client
- Administrateur
- Service de paiement

## 3. Liste des cas d'utilisation (UC)

1. Consulter les films
2. Consulter les séances
3. Réserver une place
4. Annuler une réservation
5. Effectuer le paiement
6. Gérer les séances

## 4. Priorisation des UC

Critères : valeur métier, risque, impact sur l'architecture.

| Cas d'utilisation | Valeur métier | Risque | Impact architecture | Priorité |
|---|---|---|---|---|
| Effectuer le paiement | Haute | Haute | Haute | 1 (en premier) |
| Réserver une place | Haute | Moyenne | Moyenne | 2 |
| Consulter les films | Haute | Basse | Basse | 3 |
| Consulter les séances | Haute | Basse | Basse | 3 |
| Annuler une réservation | Moyenne | Basse | Basse | 4 |
| Gérer les séances | Moyenne | Moyenne | Moyenne | 5 |

**Cas d'utilisation à traiter en premier :** Effectuer le paiement (c'est le cas à risque technique).

## 5. Plan des 3 itérations et des 4 phases

### Itération 1 (Inception + début Élaboration)
- Rédiger la vision (5 lignes) et identifier les acteurs
- Lister et prioriser les cas d'utilisation
- Créer le diagramme de cas d'utilisation (PlantUML)
- Architecture de base pour le paiement : controller -> service -> accès aux données
- Premier test automatisé en intégration continue

**Jalon :** Vision et architecture de base validées

### Itération 2 (Construction)
- Implémenter les cas d'utilisation restants en couches (métier et accès aux données)
- Créer les diagrammes de classes et de séquence
- Définir les tests unitaires et un test d'intégration (scénario nominal)

**Jalon :** Version bêta du produit

### Itération 3 (Transition)
- Tests finaux et corrections de bugs
- Revue croisée par une autre équipe
- Livraison du produit

**Jalon :** Produit livré au client
