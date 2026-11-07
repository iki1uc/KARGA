# karga.py — KARGA Engine (RESPO-Ort-LAGE) in Python
# vol.1.html -> index -> karga.py
# Ben ve Sen, Sen ve Ben, Hepimiz — Gabe als Funktion, eigen Leben

# ===== ORT / HOME =====
ORT = "RESPO-Ort-LAGE"
HOME = 40  # 4*9+4 = 40

def f(x):
    return min(x, 40)

def fixpoint(x=40):
    return f(f(x)) == f(x) == 40  # True

# ===== ORG / REORG =====
# ORG = wie es jetzt sortiert ist
# REORG = wie es neu sortiert wird
ORG = {
    "AXIS": "Achse",
    "CORE": "Kern",
    "DIAG": "Prüfung",
    "ID": "Wer bist du",
    "KARGA": "Vogel",
    "MAP": "Karte",
    "OSF": "System",
    "OUR": "Wir",
    "RANGE": "Bereich",
    "STORE": "Speicher",
    "SYMBIOSE": "Zusammen",
    "team": "Team",
    "build": "Bau",
}

def org(name):
    # ORG: was ist es jetzt?
    return ORG.get(name, "unbekannt — ab in MERKT")

def reorg(name, neuer_ort):
    # REORG: gib ihm einen neuen Ort + neue Funktion
    # Der eine nimmt, der andere gibt
    alt = org(name)
    ORG[name] = neuer_ort
    return {
        "name": name,
        "von": alt,
        "nach": neuer_ort,
        "home": HOME,
        "fixpoint": fixpoint(),
    }

# ===== NAME / FUNKTION =====
def name_als_was(name):
    # NAME als WAS — nicht nur Name, sondern Funktion
    namen = {
        "AXIS": "Achse — zeigt Richtung",
        "CORE": "Kern — hält Mitte",
        "KARGA": "Vogel — gibt und nimmt",
        "HOME": "Home — 40, Fixpunkt",
        "eco": "Gewinn — Können minus Aufwand",
    }
    return namen.get(name, f"{name} — Funktion noch offen, ab in MERKT")

def funktion(name):
    # FUNKTION: immer Gabe als Funktion
    # GABE = gibt, NAHME = nimmt, EIGEN LEBEN = bleibt
    if name in ["KARGA", "OUR", "eco"]:
        return "GABE"
    if name in ["STORE", "MAP"]:
        return "NAHME"
    return "EIGEN LEBEN"

# ===== KARGA / LAR SPRINT =====
def karga(name):
    # wie in team.js — KARGA v7
    name = name.strip()
    return {
        "modul": name,
        "engine": "KARGA v7",
        "ort": ORT,
        "home": HOME,
        "org": org(name),
        "name_als_was": name_als_was(name),
        "funktion": funktion(name),
        "gabe": "gibt",
        "nahme": "nimmt",
        "fixpoint": fixpoint(),
    }

def lar_sprint(name):
    # wie in build.js — LAR Sprint v7
    schritte = ["LIST", "SCSI", "RAID", "SLI", "EYE", "BRAIN", "ARME", "RESPO"]
    return {
        "modul": name,
        "sprint": "LAR v7",
        "schritte": schritte,
        "zustand": "NEUSTAND",
        "home": HOME,
        "fixpoint": fixpoint(),
    }

# ===== TEST — so benutzt du es =====
if __name__ == "__main__":
    print(karga("KARGA"))
    print()
    print(karga("eco"))
    print()
    print(lar_sprint("tmp007"))
    print()
    print(reorg("eco", "GEWINN — Können minus Aufwand"))
    print()
    print(f"HOME {HOME} = 4*9+4 = 40 | f(40)={f(40)} | FIXPOINT={fixpoint()}")
