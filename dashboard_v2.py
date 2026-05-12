import streamlit as st
import pandas as pd
import json
from streamlit_config import setze_styles, baue_panel2, zeige_panel
from VerbrauchFile import VerbrauchFile

st.set_page_config(page_title="Kundendashboard", layout="wide")

setze_styles()

# ─────────────────────────────────────────────
# KONFIGURATION
# ─────────────────────────────────────────────
KATEGORIEN = {
    "Allgemein": [
        "Unternehmen", "Muttergesellschaft", "Rechtsform", "Hauptsitz",
        "Standorte", "Mitarbeiterzahl", "Umsatz(€)", "Umsatz/Jahr",
        "Branche", "Linkedin(url)", "Zeithorizont"
    ],
    "Ansprechpartner": [
        "Ansprechpartner"
    ],
    "Energie": [
        "Stromverbrauch(GWh)", "Stromverbrauch (Annahme)",
        "Gasverbrauch(GWh)", "Gasverbrauch (Annahme)",
        "Wärmeversorgung", "Grünstrom", "Eigenerzeugung"
    ],
    "Nachhaltigkeit": [
        "Klimaziele", "Klimaziele (Annahme)",
        "ESG Bericht",
        "CO2 Bilanzierung", "CO2 Bilanzierung (Annahme)",
        "Zertifizierungen"
    ],
    "Strategie": [
        "Ausgangssituation",
        "Geplante Maßnahmen", "Geplante Maßnahmen (Annahme)",
        "Projektrelevanz", "Transformationsphase"
    ],
    "Abschließend": [
        "Offene Fragen", "Kurzfazit"],
}

# ─────────────────────────────────────────────
# SIDEBAR – Datei Upload
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("📂 Daten laden")
    
    json_file = st.file_uploader("Kundendaten JSON", type=["json"])
    strom_file = st.file_uploader("Strom Excel", type=["xlsx", "xls"])
    gas_file = st.file_uploader("Gas Excel", type=["xlsx", "xls"])

    if json_file is not None:
        st.session_state["json_file"] = json_file
    json_file = st.session_state.get("json_file")

    if strom_file is not None:
        st.session_state["Strom_file"] = strom_file

    if gas_file is not None:
        st.session_state["Gas_file"] = gas_file

    stromObject = VerbrauchFile("Strom")
    gasObject = VerbrauchFile("Gas")
    stromObject.set_file()
    gasObject.set_file()

    if stromObject.file is not None:
        stromObject.checkAndCleanData()

    if gasObject.file is not None:
        gasObject.checkAndCleanData()

    verbrauch_objects = []
    if stromObject.file is not None:
        verbrauch_objects.append(stromObject)
    if gasObject.file is not None:
        verbrauch_objects.append(gasObject)


# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
st.image("Logo.png", width = 300, output_format = "png")
st.title("Kunden-Dashboard")
st.markdown("---")

# ── JSON Kundendaten ──────────────────────────
if not json_file:
    st.info("Bitte Kundendaten JSON in der Sidebar hochladen.")

else:
    try:
        json_file.seek(0)
        kunde = json.load(json_file)
    except Exception as e:
        st.error(f"Fehler beim Laden der Kundendaten: {e}")

    # Panels aufbauen
    alle_panels = [
        baue_panel2(kunde, "Allgemein",      KATEGORIEN["Allgemein"],      stil="steckbrief"),
        baue_panel2(kunde, "Ansprechpartner", KATEGORIEN["Ansprechpartner"], stil="text"),
        baue_panel2(kunde, "Energie",        KATEGORIEN["Energie"],        stil="steckbrief"),
        baue_panel2(kunde, "Nachhaltigkeit", KATEGORIEN["Nachhaltigkeit"], stil="steckbrief"),
        baue_panel2(kunde, "Strategie",      KATEGORIEN["Strategie"],      stil="steckbrief"),
        baue_panel2(kunde, "Abschließend",   KATEGORIEN["Abschließend"],   stil="text"),
    ]

    gefuellte_panels = [p for p in alle_panels if p is not None]
    panels_pro_zeile = 3

    if gefuellte_panels:
        for i in range(0, len(gefuellte_panels), panels_pro_zeile):
            gruppe = gefuellte_panels[i:i + panels_pro_zeile]
            cols = st.columns(len(gruppe))
            for col, (titel, vorhandene, stil) in zip(cols, gruppe):
                with col:
                    zeige_panel(titel, vorhandene, stil)

# ── Stromverbrauch ────────────────────────────

if verbrauch_objects:
    cols = st.columns(len(verbrauch_objects))
    for col, obj in zip(cols, verbrauch_objects):
        obj.make_col(col)
