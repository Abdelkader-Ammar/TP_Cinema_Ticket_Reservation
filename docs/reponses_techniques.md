# Réponses aux questions techniques

## 1. Quelle contrainte technique a influencé le choix de votre UC à risque ?

La contrainte technique principale qui a influencé le choix du cas d'utilisation "Effectuer le paiement" comme UC à risque est la **sécurité combinée à l'intégration avec un service externe de paiement**.

En effet, le paiement implique :
- La manipulation de données sensibles (numéro de carte, montants financiers)
- L'appel à un service externe (Service de paiement) dont la disponibilité et les temps de réponse ne sont pas maîtrisés localement
- La gestion des transactions (éviter les double-débits ou les paiements perdus)

Ces facteurs en font le cas d'utilisation le plus risqué sur le plan technique, d'où sa priorisation en premier dans la phase d'élaboration.

## 2. Qu'auriez-vous changé si une contrainte technique différente s'était imposée (par exemple une application mobile hors-ligne) ?

Si l'application devait être une application mobile fonctionnant hors-ligne, plusieurs changements auraient été nécessaires :

**Sur le choix de l'UC à risque :**
L'UC à risque ne serait plus forcément le paiement, mais plutôt la **gestion des réservations hors-ligne** (synchronisation des données lorsque la connexion est rétablie, gestion des conflits de places entre utilisateurs hors-ligne).

**Sur l'architecture :**
- Ajout d'une couche de stockage local (base de données SQLite sur le mobile)
- Mécanisme de synchronisation avec le serveur lors de la reconnexion
- Gestion des conflits (deux clients réservent la même place alors qu'ils sont hors-ligne)

**Sur les exigences techniques :**
- La contrainte "plateforme" passerait de "navigateur web" à "application mobile native (iOS/Android)"
- Une nouvelle exigence technique apparaîtrait : "hors-ligne : fonctionnement sans connexion internet avec synchronisation différée"
- L'exigence de performance inclurait la réactivité de l'interface même sans réseau

**Sur le V-modèle :**
Les tests d'intégration devraient inclure des scénarios de déconnexion/reconnexion et de résolution de conflits de données.
