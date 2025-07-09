# Contributing to CS-Manim

Merci de votre intérêt pour contribuer à CS-Manim ! Ce guide vous aidera à démarrer.

## Comment contribuer

### Signaler des bugs

Si vous trouvez un bug, veuillez ouvrir un issue sur GitHub avec :

- Une description claire du problème
- Les étapes pour reproduire le bug
- Votre environnement (OS, version de Python, version de Manim)
- Si possible, un exemple de code minimal qui reproduit le problème

### Proposer des améliorations

Pour proposer de nouvelles fonctionnalités :

1. Ouvrez d'abord un issue pour discuter de l'idée
2. Attendez les commentaires avant de commencer l'implémentation
3. Forkez le projet et créez une branche pour votre fonctionnalité

### Développement

#### Configuration de l'environnement

```bash
# Cloner le dépôt
git clone https://github.com/PierreOlivierBrillant/cs-manim.git
cd cs-manim

# Installer en mode développement
pip install -e .[dev]
```

#### Standards de code

- Utilisez Black pour le formatage : `black cs_manim tests`
- Vérifiez avec Flake8 : `flake8 cs_manim tests`
- Vérifiez les types avec MyPy : `mypy cs_manim`
- Lancez les tests : `pytest`

#### Tests

- Écrivez des tests pour toute nouvelle fonctionnalité
- Assurez-vous que tous les tests passent
- Maintenez une couverture de code élevée

#### Pull Requests

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Conventions

- Utilisez des noms de variables et fonctions descriptifs
- Écrivez des docstrings pour les fonctions publiques
- Commentez le code complexe
- Respectez le style de code existant

### Questions

Si vous avez des questions, n'hésitez pas à ouvrir un issue avec le label "question".
