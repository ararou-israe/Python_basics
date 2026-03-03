donnees = [
 ("Sara", "Math", 12, "G1"),
 ("Sara", "Info", 14, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Adam", "Chimie", 18, "G1"),
 ("Sara", "Math", 11, "G1"), 
 ("Bouchra", "Info", "abc", "G2"), 
 ("", "Math", 10, "G1"), 
 ("Yassine", "Info", 22, "G2"), 
 ("Ahmed", "Info", 13, "G2"),
 ("Adam", "Math", None, "G1"), 
 ("Sara", "Chimie", 16, "G1"),
 ("Adam", "Info", 7, "G1"),
 ("Ahmed", "Math", 9, "G2"), 
 ("Hana", "Physique", 15, "G3"), 
 ("Hana", "Math", 8, "G3"),
]
# PARTIE1
def valider(enregistrement):

    nom, matiere, note, groupe = enregistrement

    if not nom or not matiere or not groupe:
        return False, "champ vide"

    try:
        note = float(note)
    except (ValueError, TypeError):
        return False, "note non numerique"

    if note < 0 or note > 20:
        return False, "note hors intervalle"

    return True, ""


def filtrer_donnees(donnees):

    donnees_valides = []
    erreurs = []
    doublons_exacts = set()
    double = set()

    for enregistrement in donnees:

        if enregistrement in double:
            doublons_exacts.add(enregistrement)
        else:
            double.add(enregistrement)

        valide, raison = valider(enregistrement)

        if valide:
            nom, matiere, note, groupe = enregistrement
            donnees_valides.append((nom, matiere, float(note), groupe))
        else:
            erreurs.append({
                "ligne": enregistrement,
                "raison": raison
            })

    return donnees_valides, erreurs, doublons_exacts

# partie2:structuration
def struct_matiere(enregistrement):
    matieres = set()

    for nom, matiere, note, groupe in enregistrement:
        matieres.add(matiere)

    return list(matieres)

def struct_donnees(valides):
    etudiants = {}
    for nom, matiere, note, groupe in valides:
        if nom not in etudiants:
            etudiants[nom] = {}
        if matiere not in etudiants[nom]:
            etudiants[nom][matiere] = []
        etudiants[nom][matiere].append(note)
    return etudiants
def struct_groupe(valides):
    groupes = {}
    for nom, matiere, note, groupe in valides:
        if groupe not in groupes:
            groupes[groupe] = set()
        groupes[groupe].add(nom)
    return groupes
# parie3.calculs et statistiques
def somme_notes(notes):
    if not notes:
        return 0
    return sum(notes)

def moyenne_notes(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)
def moyennes(donnees_organisees):
    moyennes_par_etudiant = {}
    for nom, matieres in donnees_organisees.items():
        moyennes_par_etudiant[nom] = {}
        for matiere, notes in matieres.items():
            moyennes_par_etudiant[nom][matiere] = moyenne_notes(notes)
    return moyennes_par_etudiant
# partie4: detection des anomalies
def detecter_anomalies(donnees_organisees, matieres_totales, seuil_moyenne=10):
    alertes = {
        "doublons": [],
        "profils_incomplets": [],
        "groupes_faibles": []
    }

    for nom, matieres in donnees_organisees.items():
        toutes_les_notes = []

        for matiere, notes in matieres.items():
            toutes_les_notes.extend(notes)
            # doublons si plus d'une note pour la même matière
            if len(notes) > 1:
                alertes["doublons"].append((nom, matiere, notes))

        # profil incomplet
        if set(matieres.keys()) != set(matieres_totales):
            alertes["profils_incomplets"].append(nom)
        
        # moyenne générale
        if toutes_les_notes:
            moyenne_etudiant = sum(toutes_les_notes) / len(toutes_les_notes)
            if moyenne_etudiant < seuil_moyenne:
                alertes["groupes_faibles"].append(nom)

    return alertes

# tester les fonvtions


valides, erreurs, doublons = filtrer_donnees(donnees)
matieres = struct_matiere(valides)
donnees_organisees = struct_donnees(valides)
groupes = struct_groupe(valides)
moyennes_par_etudiant = moyennes(donnees_organisees)
alertes = detecter_anomalies(donnees_organisees, matieres)
# afficher les resultats



print("Données valides :", valides)
print("\n Erreurs :", erreurs)
print("\n Doublons :", doublons)
print("\nMatières :", matieres)
print("\nDonnées organisées par étudiant et matière :")
for nom, matieres_etudiant in donnees_organisees.items():
    print(f" {nom}:")
    for matiere, notes in matieres_etudiant.items():
        print(f" {matiere} : {notes}")
    print()

print("\nDonnées organisées par groupe :")
for groupe, etudiants in groupes.items():
    print(f"{groupe}:")
    for nom in etudiants:
        print(f"  {nom} ")
print("\nMoyennes par matiere et moyenne generale :")
for nom, matieres_etudiant in moyennes_par_etudiant.items():
    print(f"{nom}:")
    for matiere, moyenne in matieres_etudiant.items():
        print(f"  {matiere} : {moyenne:.2f}")
    moyenne_generale = moyenne_notes([moyenne for moyenne in matieres_etudiant.values()])
    print(f"  Moyenne générale : {moyenne_generale:.2f}\n")

print("\nAlertes détectées :")
print("Doublons :")
for ligne, matiere, notes in alertes["doublons"]:
    print(f"  {ligne} - {matiere} : {notes}")
print("\nprofils incomplets :")
for nom in alertes["profils_incomplets"]:
    print(f"  {nom}")
print("\nGroupes faibles :")
for nom in alertes["groupes_faibles"]:
    print(f"  {nom}")