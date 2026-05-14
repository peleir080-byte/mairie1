import os

template_file = 'demarche-naissance.html'

with open(template_file, 'r', encoding='utf-8') as f:
    template = f.read()

nav_from = """<a href="services.html" class="text-secondary font-bold border-b-2 border-secondary pb-1 font-label-sm">Citoyenneté</a>
                <a href="urbanisme.html" class="text-on-surface-variant hover:text-secondary font-label-sm font-semibold transition-colors">Urbanisme</a>"""
nav_to = """<a href="services.html" class="text-on-surface-variant hover:text-secondary font-label-sm font-semibold transition-colors">Citoyenneté</a>
                <a href="urbanisme.html" class="text-secondary font-bold border-b-2 border-secondary pb-1 font-label-sm">Urbanisme</a>"""

base_template = template.replace(nav_from, nav_to)

# 1. Permis de construire
pc_content = base_template.replace('<title>Demande d\'Acte de Naissance - Commune de Lomé</title>', '<title>Demande de Permis de Construire - Commune de Lomé</title>')
pc_content = pc_content.replace('https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=2070&auto=format&fit=crop', 'https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=2000&auto=format&fit=crop')
pc_content = pc_content.replace('Bébé noir souriant', 'Chantier de construction')
pc_content = pc_content.replace('<a href="services.html" class="hover:text-white transition-colors">Citoyenneté</a>', '<a href="urbanisme.html" class="hover:text-white transition-colors">Urbanisme</a>')
pc_content = pc_content.replace('Acte de Naissance', 'Permis de Construire')
pc_content = pc_content.replace('Demande d\'<span class="text-gold-accent">Acte de Naissance</span>', 'Demande de <span class="text-gold-accent">Permis de Construire</span>')
pc_content = pc_content.replace('Obtenez rapidement une copie intégrale ou un extrait de votre acte de naissance.', 'Déposez votre demande de permis de construire en ligne de manière simple et sécurisée.')
pc_content = pc_content.replace('Recevez un numéro de suivi par SMS et email pour consulter l\'avancement.', 'Un ingénieur traitera votre dossier et vous tiendra informé.')
pc_content = pc_content.replace('Retrait de l\'acte', 'Délivrance du permis')
pc_content = pc_content.replace('Récupérez votre document officiel à la mairie centrale ou par email certifié.', 'Téléchargez votre permis de construire signé électroniquement.')
pc_content = pc_content.replace('Copie de l\'ancien acte', 'Plan architectural')
pc_content = pc_content.replace('Obligatoire pour les extraits (format PDF, JPG).', 'Signé par un architecte agréé de l\'ONAT.')
pc_content = pc_content.replace('Pièce d\'identité', 'Titre foncier')
pc_content = pc_content.replace('CNI ou Passeport valide de l\'un des parents ou du demandeur.', 'Copie du titre de propriété ou de la convention de vente.')
pc_content = pc_content.replace('Timbre fiscal de 500 FCFA (paiement au retrait).', 'Frais d\'étude selon le barème en vigueur (Devis envoyé après analyse).')
pc_content = pc_content.replace('Copie Intégrale', 'Construction Nouvelle')
pc_content = pc_content.replace('Reproduction totale de l\'acte.', 'Bâtiment neuf sur terrain nu.')
pc_content = pc_content.replace('Extrait d\'acte', 'Modification / Extension')
pc_content = pc_content.replace('Synthèse des informations.', 'Ajout à une structure existante.')
pc_content = pc_content.replace('Nom de famille (sur l\'acte)', 'Nom du propriétaire')
pc_content = pc_content.replace('Date de naissance', 'Superficie du terrain (m²)')
pc_content = pc_content.replace('type="date"', 'type="number"')
pc_content = pc_content.replace('Numéro de l\'acte (optionnel)', 'Numéro de Titre Foncier')

with open('demarche-permis-construire.html', 'w', encoding='utf-8') as f:
    f.write(pc_content)

# 2. Consultation cadastrale
cad_content = base_template.replace('<title>Demande d\'Acte de Naissance - Commune de Lomé</title>', '<title>Consultation Cadastrale - Commune de Lomé</title>')
cad_content = cad_content.replace('https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=2070&auto=format&fit=crop', 'https://images.unsplash.com/photo-1524813686514-a57563d77965?q=80&w=2000&auto=format&fit=crop')
cad_content = cad_content.replace('Bébé noir souriant', 'Plans cadastraux')
cad_content = cad_content.replace('<a href="services.html" class="hover:text-white transition-colors">Citoyenneté</a>', '<a href="urbanisme.html" class="hover:text-white transition-colors">Urbanisme</a>')
cad_content = cad_content.replace('Acte de Naissance', 'Consultation Cadastrale')
cad_content = cad_content.replace('Demande d\'<span class="text-gold-accent">Acte de Naissance</span>', '<span class="text-gold-accent">Consultation Cadastrale</span>')
cad_content = cad_content.replace('Obtenez rapidement une copie intégrale ou un extrait de votre acte de naissance.', 'Demandez un extrait du plan cadastral ou des informations sur une parcelle.')
cad_content = cad_content.replace('Retrait de l\'acte', 'Réception des documents')
cad_content = cad_content.replace('Récupérez votre document officiel à la mairie centrale ou par email certifié.', 'Recevez vos extraits par email ou à la mairie.')
cad_content = cad_content.replace('Copie de l\'ancien acte', 'Plan de situation')
cad_content = cad_content.replace('Obligatoire pour les extraits (format PDF, JPG).', 'Croquis ou coordonnées GPS de la parcelle.')
cad_content = cad_content.replace('Pièce d\'identité', 'Pièce d\'identité du demandeur')
cad_content = cad_content.replace('CNI ou Passeport valide de l\'un des parents ou du demandeur.', 'CNI ou Passeport en cours de validité.')
cad_content = cad_content.replace('Timbre fiscal de 500 FCFA (paiement au retrait).', 'Frais de recherche (1500 FCFA).')
cad_content = cad_content.replace('Copie Intégrale', 'Extrait de plan')
cad_content = cad_content.replace('Reproduction totale de l\'acte.', 'Document visuel de la parcelle.')
cad_content = cad_content.replace('Extrait d\'acte', 'Relevé de propriété')
cad_content = cad_content.replace('Synthèse des informations.', 'Historique des propriétaires.')
cad_content = cad_content.replace('Nom de famille (sur l\'acte)', 'Nom du demandeur')
cad_content = cad_content.replace('Date de naissance', 'Quartier / Zone')
cad_content = cad_content.replace('type="date"', 'type="text"')
cad_content = cad_content.replace('Numéro de l\'acte (optionnel)', 'Numéro de parcelle / Lot')

with open('demarche-cadastre.html', 'w', encoding='utf-8') as f:
    f.write(cad_content)

# 3. Certificat d'urbanisme
cu_content = base_template.replace('<title>Demande d\'Acte de Naissance - Commune de Lomé</title>', '<title>Certificat d\'Urbanisme - Commune de Lomé</title>')
cu_content = cu_content.replace('https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=2070&auto=format&fit=crop', 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2000&auto=format&fit=crop')
cu_content = cu_content.replace('Bébé noir souriant', 'Bâtiment moderne')
cu_content = cu_content.replace('<a href="services.html" class="hover:text-white transition-colors">Citoyenneté</a>', '<a href="urbanisme.html" class="hover:text-white transition-colors">Urbanisme</a>')
cu_content = cu_content.replace('Acte de Naissance', 'Certificat d\'Urbanisme')
cu_content = cu_content.replace('Demande d\'<span class="text-gold-accent">Acte de Naissance</span>', 'Demande de <span class="text-gold-accent">Certificat d\'Urbanisme</span>')
cu_content = cu_content.replace('Obtenez rapidement une copie intégrale ou un extrait de votre acte de naissance.', 'Obtenez les règles d\'urbanisme applicables à un terrain précis.')
cu_content = cu_content.replace('Retrait de l\'acte', 'Délivrance du certificat')
cu_content = cu_content.replace('Récupérez votre document officiel à la mairie centrale ou par email certifié.', 'Le certificat d\'urbanisme vous est envoyé numériquement.')
cu_content = cu_content.replace('Copie de l\'ancien acte', 'Note de renseignement')
cu_content = cu_content.replace('Obligatoire pour les extraits (format PDF, JPG).', 'Description sommaire du projet.')
cu_content = cu_content.replace('CNI ou Passeport valide de l\'un des parents ou du demandeur.', 'CNI du propriétaire ou de son représentant.')
cu_content = cu_content.replace('Timbre fiscal de 500 FCFA (paiement au retrait).', 'Gratuit pour une information simple.')
cu_content = cu_content.replace('Copie Intégrale', 'Certificat d\'information')
cu_content = cu_content.replace('Reproduction totale de l\'acte.', 'Renseigne sur les règles applicables.')
cu_content = cu_content.replace('Extrait d\'acte', 'Certificat opérationnel')
cu_content = cu_content.replace('Synthèse des informations.', 'Indique si le projet est réalisable.')
cu_content = cu_content.replace('Nom de famille (sur l\'acte)', 'Nom du demandeur')
cu_content = cu_content.replace('Date de naissance', 'Surface du terrain')
cu_content = cu_content.replace('type="date"', 'type="text"')
cu_content = cu_content.replace('Numéro de l\'acte (optionnel)', 'Adresse ou coordonnées de la parcelle')

with open('demarche-certificat-urbanisme.html', 'w', encoding='utf-8') as f:
    f.write(cu_content)

# 4. Mutation foncière
mf_content = base_template.replace('<title>Demande d\'Acte de Naissance - Commune de Lomé</title>', '<title>Mutation Foncière - Commune de Lomé</title>')
mf_content = mf_content.replace('https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=2070&auto=format&fit=crop', 'https://images.unsplash.com/photo-1560520653-9e0e4c89eb11?q=80&w=2000&auto=format&fit=crop')
mf_content = mf_content.replace('Bébé noir souriant', 'Documents fonciers')
mf_content = mf_content.replace('<a href="services.html" class="hover:text-white transition-colors">Citoyenneté</a>', '<a href="urbanisme.html" class="hover:text-white transition-colors">Urbanisme</a>')
mf_content = mf_content.replace('Acte de Naissance', 'Mutation Foncière')
mf_content = mf_content.replace('Demande d\'<span class="text-gold-accent">Acte de Naissance</span>', 'Demande de <span class="text-gold-accent">Mutation Foncière</span>')
mf_content = mf_content.replace('Obtenez rapidement une copie intégrale ou un extrait de votre acte de naissance.', 'Déclarez un changement de propriétaire pour mettre à jour les registres domaniaux et fiscaux.')
mf_content = mf_content.replace('Retrait de l\'acte', 'Validation de la mutation')
mf_content = mf_content.replace('Récupérez votre document officiel à la mairie centrale ou par email certifié.', 'Une attestation de mutation vous sera délivrée.')
mf_content = mf_content.replace('Copie de l\'ancien acte', 'Acte de cession / Vente')
mf_content = mf_content.replace('Obligatoire pour les extraits (format PDF, JPG).', 'Acte notarié ou jugement du tribunal.')
mf_content = mf_content.replace('Pièce d\'identité', 'Titre Foncier d\'origine')
mf_content = mf_content.replace('CNI ou Passeport valide de l\'un des parents ou du demandeur.', 'Copie du TF ou du plan visé.')
mf_content = mf_content.replace('Timbre fiscal de 500 FCFA (paiement au retrait).', 'Taxe de mutation (Calculée selon la valeur du bien).')
mf_content = mf_content.replace('Copie Intégrale', 'Vente / Cession')
mf_content = mf_content.replace('Reproduction totale de l\'acte.', 'Changement suite à un achat.')
mf_content = mf_content.replace('Extrait d\'acte', 'Héritage / Succession')
mf_content = mf_content.replace('Synthèse des informations.', 'Mutation suite à un décès.')
mf_content = mf_content.replace('Nom de famille (sur l\'acte)', 'Nom du nouveau propriétaire')
mf_content = mf_content.replace('Date de naissance', 'Date d\'acquisition')
mf_content = mf_content.replace('Numéro de l\'acte (optionnel)', 'Numéro de Titre Foncier')

with open('demarche-mutation-fonciere.html', 'w', encoding='utf-8') as f:
    f.write(mf_content)

print("4 files created successfully.")
