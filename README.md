# Mairie de Lomé - Portail Municipal Officiel

Un site web municipal moderne et fonctionnel pour la commune de Lomé, Togo.

## 🎯 Objectif

Créer un portail municipal qui incarne l'excellence administrative tout en étant parfaitement adapté au contexte togolais, avec un design minimaliste inspiré des standards internationaux.

## 🚀 Fonctionnalités Clés

### 📋 Services Municipaux
- **État Civil**: Actes de naissance, mariage, décès et légalisation
- **Foncier**: Consultation cadastrale et permis de construire  
- **Fiscalité**: Taxes municipales et paiements en ligne
- **Mobilité**: Transport urbain et planification des déplacements

### 🧮 Simulateur de Taxes
- Calcul automatique des taxes municipales
- Support des différents types de biens (résidentiel, commercial, industriel)
- Intégration des quartiers réels de Lomé (Bé, Tokoin, Dékondji, Adidogomé, Baguida)
- Estimation en Francs CFA (XOF)

### 📄 Formulaires Administratifs
- Téléchargement de formulaires PDF officiels
- Demande d'acte de naissance
- Permis de construire
- Déclaration de taxes
- Autorisation commerciale
- Certificat de mariage
- Carte de résident

### 📅 Agenda Municipal
- Conseils municipaux et dates importantes
- Événements culturels (Festival Lomé en Lumière)
- Journées portes ouvertes
- Opérations de propreté

## 🎨 Design & Architecture

### Design System
- **Palette**: Bleu nuit (#1B1B1F), Or municipal (#D4AF37), Émeraude (#006A4E)
- **Typography**: Montserrat (titres), Inter (corps de texte)
- **Style**: Glassmorphism minimaliste inspiré de Dubaï
- **Approche**: Mobile First avec responsive design

### Structure Technique
- **HTML5** sémantique et accessible
- **CSS3** moderne avec animations fluides
- **JavaScript** vanilla pour les interactions
- **Performance**: Optimisé pour les connexions mobiles

## 📱 Mobile First

Le site est optimisé pour :
- Smartphones (écrans jusqu'à 767px)
- Tablettes (768px - 1439px)  
- Desktop (1440px et plus)

## 🌍 Contenu Localisé

### Références Togolaises
- **Quartiers**: Bé (Centre), Tokoin, Dékondji, Adidogomé, Baguida
- **Institutions**: Références aux procédures administratives togolaises
- **Monnaie**: Francs CFA (XOF) pour tous les montants
- **Contact**: +228 22 21 00 00 (format téléphonique togolais)

### Contenu Authentique
- Procédures administratives spécifiques au Togo
- Légalisation de documents selon les normes locales
- Taxes de voirie et impôts municipaux réels
- Événements culturels pertinents

## 🚀 Déploiement

### Maquettes Stitch (9) et pages du site

Chaque page à la racine du projet reprend le HTML exporté de la maquette correspondante (dossiers `stitch_togo_excellence_civic_portal*`).

| Maquette (dossier) | Page publique |
|--------------------|----------------|
| `stitch_togo_excellence_civic_portal` | `index.html` (accueil) |
| `stitch_togo_excellence_civic_portal (1)` | `services.html` (citoyenneté / état civil, grille services) |
| `stitch_togo_excellence_civic_portal (2)` | `etat-civil.html` (variante bento état civil) |
| `stitch_togo_excellence_civic_portal (3)` | `espace-citoyen.html` |
| `stitch_togo_excellence_civic_portal (4)` | `urbanisme.html` |
| `stitch_togo_excellence_civic_portal (5)` | `fiscalite.html` |
| `stitch_togo_excellence_civic_portal (6)` | `actualites.html` |
| `stitch_togo_excellence_civic_portal(7)` | `evenements.html` |
| `stitch_togo_excellence_civic_portal(8)` | `mairie.html` |

**Page utilitaire (liens pied de page, contact, légal) :** `plan-du-site.html`

Les pages utilisent **Tailwind via CDN** (comme les maquettes). Le fichier `styles.css` à la racine n’est plus relié aux pages actuelles ; vous pouvez le supprimer ou le réutiliser pour des ajustements globaux si besoin.

### Fichiers Principaux
- `index.html` - Accueil (maquette portail)
- `services.html`, `urbanisme.html`, `fiscalite.html`, `actualites.html`, `espace-citoyen.html`, `evenements.html`, `mairie.html`, `etat-civil.html` - Autres vues
- `README.md` - Documentation du projet

### Technologies Utilisées
- Tailwind CSS (via CDN)
- Google Fonts (Montserrat & Inter)
- Material Symbols Icons
- JavaScript vanilla

## 🎯 Cibles Utilisateurs

### Citoyens
- Accès rapide aux services administratifs
- Téléchargement de formulaires
- Simulation de taxes
- Information sur les événements municipaux

### Entreprises
- Demande d'autorisations commerciales
- Permis de construire
- Déclarations fiscales
- Information réglementaire

### Touristes
- Informations sur la ville
- Événements culturels
- Services municipaux

## 🔧 Maintenance

### Mises à jour Régulières
- Actualités municipales
- Agenda des événements
- Formulaires administratifs
- Taux de taxation

### Évolutivité
- Structure modulaire pour ajouter de nouveaux services
- API prête pour l'intégration backend
- Support multilangue (français/anglais) prévu

## 📞 Contact

**Mairie de Lomé**
- Adresse: Avenue de la Mairie, Lomé, Togo
- Téléphone: +228 22 21 00 00
- Email: contact@lome.tg

---

*Développé avec excellence pour servir les citoyens de Lomé*
