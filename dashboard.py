# streamlit run dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Kundendashboard", layout="wide")         # für streamlit layout

from data_load import datei_konfiguration, lade_daten, lade_verbrauch           # noch kein verbrauch weil erstmal nur csv
from streamlit_config import setze_styles, baue_panel, zeige_panel
from plot_functions import zeige_verbrauch_plot

#------------------konfiguration---------------------

setze_styles()

KATEGORIEN = {
    "Allgemein": [
        "Firmenname", "Betreiber", "Standort", "Branche",
        "Ansprechpartner", "E-Mail", "Telefon",
    ],
    "Energieversorgung": [
        "Hauptenergieträger", "Strombereitstellung", "Erneuerbare Energie",
        "Energieversorger", "Tarif", "Vertragsende", "Lastgangmanagement",
        "Spannungsebene", "Maßnahmen",
    ],
    "Strom": [
        "Stromverbrauch MWh/a", "Spitzenlast Strom kW", "Grundlast kW",
    ],
    "Wärme": [
        "Wärmebedarf MWh/a", "Spitzenlast Wärme kW", "Grundlast Wärme kW",
        "Prozesstemperatur °C",
    ],
    "Speicher & Flexibilität": [
        "Batteriespeicher", "Thermischer Speicher", "Abwärme vorhanden",
    ],
}

# Pfade aus session_state
STAMMDATEN_FILE = st.session_state.get("stammdaten_pfad", None)
STROM_FILE = st.session_state.get("strom_pfad", None)
GAS_FILE = st.session_state.get("gas_pfad", None)
STROM_DATUM_SPALTE = st.session_state.get("strom_datum_spalte", "")
STROM_VERBRAUCH_SPALTE = st.session_state.get("strom_verbrauch_spalte", "")
GAS_DATUM_SPALTE = st.session_state.get("gas_datum_spalte", "")
GAS_VERBRAUCH_SPALTE = st.session_state.get("gas_verbrauch_spalte", "")
# session state nötig, da interaktives Programm und dadurch rerun, variablen werden über reruns gespeichert

#--------------------------start Dashboard-------------------------------

# Dateien laden
st.title("Kunden-Dashboard")
if st.button("⚙️ Dateien laden", key="load_button"):
    datei_konfiguration()
st.markdown("---")

if not STAMMDATEN_FILE:
    st.info("Bitte zuerst Dateien konfigurieren.")
    st.stop()

df = lade_daten(STAMMDATEN_FILE)

# Kundenauswahl
kunden_liste = df["Firmenname"].tolist()  # ← Spaltenname anpassen
ausgewaehlter_kunde = st.selectbox("Kunde auswählen", kunden_liste, key = "kunde_auswahl")

# Nur die Zeile des ausgewählten Kunden
kunde = df[df["Firmenname"] == ausgewaehlter_kunde].iloc[0]


kunde = df.iloc[0]

# panels einrichten
alle_panels = [
    baue_panel(kunde, "Allgemein",              KATEGORIEN["Allgemein"],              stil="steckbrief"),
    baue_panel(kunde, "Energieversorgung",       KATEGORIEN["Energieversorgung"],       stil="steckbrief"),
    baue_panel(kunde, "Strom",                  KATEGORIEN["Strom"],                  stil="steckbrief"),
    baue_panel(kunde, "Wärme",                  KATEGORIEN["Wärme"],                  stil="steckbrief"),
    baue_panel(kunde, "Speicher & Flexibilität", KATEGORIEN["Speicher & Flexibilität"], stil="steckbrief"),
]

gefuellte_panels = [p for p in alle_panels if p is not None]

# panels zeigen wenn nicht leer
if gefuellte_panels:
    cols = st.columns(len(gefuellte_panels))
    for col, (titel, vorhandene, stil) in zip(cols, gefuellte_panels):
        with col:
            zeige_panel(titel, vorhandene, stil)

# ------------- Stromverbrauch -----------------

if STROM_FILE:
    try:
        vdf_strom = lade_verbrauch(STROM_FILE, STROM_DATUM_SPALTE, STROM_VERBRAUCH_SPALTE)
        st.markdown("---")
        st.subheader("⚡ Stromverbrauch")

        zeige_verbrauch_plot(vdf_strom, STROM_DATUM_SPALTE, STROM_VERBRAUCH_SPALTE, titel="strom", farbe="#F59E0B")

        k1, k2, k3 = st.columns(3)
        k1.metric("Gesamtverbrauch", f"{vdf_strom[STROM_VERBRAUCH_SPALTE].sum():,.0f} kWh")
        k2.metric("Ø pro Zeitpunkt",  f"{vdf_strom[STROM_VERBRAUCH_SPALTE].mean():,.1f} kWh")
        k3.metric("Spitzenwert",       f"{vdf_strom[STROM_VERBRAUCH_SPALTE].max():,.0f} kWh")

    except Exception as e:
        st.error(f"Fehler beim Laden der Stromdaten: {e}")
        st.stop()

else:
    st.info("Keine Stromdaten konfiguriert.")


# ---------------- Gasverbrauch ---------------------------------

if GAS_FILE:
    try:
        vdf_gas= lade_verbrauch(GAS_FILE, GAS_DATUM_SPALTE, GAS_VERBRAUCH_SPALTE)
        st.markdown("---")
        st.subheader("Gasverbrauch")

        zeige_verbrauch_plot(vdf_gas, GAS_DATUM_SPALTE, GAS_VERBRAUCH_SPALTE, titel="gas", farbe="#220BF5")

        k1, k2, k3 = st.columns(3)
        k1.metric("Gesamtverbrauch", f"{vdf_gas[GAS_VERBRAUCH_SPALTE].sum():,.0f} kWh")
        k2.metric("Ø pro Zeitpunkt",  f"{vdf_gas[GAS_VERBRAUCH_SPALTE].mean():,.1f} kWh")
        k3.metric("Spitzenwert",       f"{vdf_gas[GAS_VERBRAUCH_SPALTE].max():,.0f} kWh")

    except Exception as e:
        st.error(f"Fehler beim Laden der Gasdaten: {e}")
        st.stop()
else:
    st.info("Keine Gasdaten konfiguriert.")
    
