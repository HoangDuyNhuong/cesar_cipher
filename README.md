# 🔐 Application de Chiffrement de César (Streamlit)

Une application web simple développée avec **Streamlit** permettant de chiffrer et déchiffrer des messages à l'aide de l'algorithme de **César**.

---

## 🚀 Fonctionnalités

* 🔒 Chiffrement de message
* 🔓 Déchiffrement de message
* 🎛️ Interface utilisateur simple et interactive
* ⚡ Exécution rapide en local ou en ligne

---

## 🗂️ Structure du projet

```
project/
│
├── frontend.py        # Interface utilisateur (Streamlit)
├── backend.py         # Logique de chiffrement
├── requirements.txt   # Dépendances du projet
└── README.md          # Documentation
```

---

## 🧠 Principe du chiffrement de César

Le chiffrement de César consiste à décaler chaque caractère d’un message selon une clé numérique.

Exemple :

* Message : `Bonjour`
* Clé : `3`
* Résultat : `Erqmrxu`

⚠️ Dans cette version, le chiffrement est appliqué à **tout l’Unicode**, pas seulement aux lettres A-Z.

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-username/ton-repo.git
cd ton-repo
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l'application

```bash
streamlit run frontend.py
```

Puis ouvre ton navigateur à l’adresse indiquée (généralement http://localhost:8501).

---

## 🌍 Déploiement en ligne (Streamlit Cloud)

1. Pousser le projet sur GitHub
2. Aller sur https://streamlit.io/cloud
3. Cliquer sur **New app**
4. Sélectionner :

   * le dépôt
   * le fichier `frontend.py`
5. Cliquer sur **Deploy**

---

## 📦 Dépendances

* streamlit

---

## 📌 Améliorations possibles

* 🔤 Version classique (A-Z uniquement)
* 📋 Bouton copier le résultat
* 🎨 Interface utilisateur améliorée
* 🔑 Génération automatique de clé
* 🧪 Ajout de tests unitaires

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre d’un apprentissage de Python et Streamlit.

---

## 📄 Licence

Ce projet est libre d'utilisation à des fins éducatives.
