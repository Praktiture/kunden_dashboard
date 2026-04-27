import streamlit as st
import pandas as pd
import json
from data_load import lade_verbrauch, parse_datum
from plot_functions import zeige_verbrauch_plot
from streamlit_config import setze_styles, baue_panel2, zeige_panel
from spalten_finden import erkenne_spalten

st.set_page_config(page_title="Kundendashboard", layout="wide")

setze_styles()

# ─────────────────────────────────────────────
# KONFIGURATION
# ─────────────────────────────────────────────
KATEGORIEN = {
    "Allgemein": ["Unternehmen", "Muttergesellschaft", "Rechtsform", "Hauptsitz", "Standorte", "Mitarbeiterzahl", "Umsatz(€)", "Umsatz/Jahr", "Branche"],
    "Energie": ["Stromverbrauch(GWh)", "Gasverbrauch(GWh)", "Wärmeversorgung", "Grünstrom", "Eigenerzeugung"],
    "Nachhaltigkeit": ["Klimaziele", "ESG Bericht", "CO2 Bilanzierung", "Zertifizierungen"],
    "Strategie": ["Ausgangssituation", "Geplante Maßnahmen", "Projektrelevanz", "Kurzfazit"],
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

    if strom_file is not None:
        st.session_state["strom_file"] = strom_file

    if gas_file is not None:
        st.session_state["gas_file"] = gas_file

    json_file = st.session_state.get("json_file")
    strom_file = st.session_state.get("strom_file")
    gas_file = st.session_state.get("gas_file")

    # Stromspalten auswählen
    strom_datum = None
    strom_verbrauch = None
    if strom_file is not None:
        try:
            strom_file.seek(0)
            vdf_raw = pd.read_excel(strom_file)
            vdf_raw.columns = vdf_raw.columns.str.strip()
            datum_erkannt, verbrauch_erkannt = erkenne_spalten(vdf_raw, typ="strom")
            alle_spalten = vdf_raw.columns.tolist()
            st.markdown("**Stromspalten prüfen:**")
            strom_datum = st.selectbox("Datumsspalte Strom", alle_spalten,
                index=alle_spalten.index(datum_erkannt[0]) if datum_erkannt else 0,
                key="datum_strom")
            strom_verbrauch = st.selectbox("Verbrauchsspalte Strom", alle_spalten,
                index=alle_spalten.index(verbrauch_erkannt[0]) if verbrauch_erkannt else 0,
                key="verbrauch_strom")
        except Exception as e:
            st.error(f"Fehler bei Stromdaten: {e}")

    # Gasspalten auswählen
    gas_datum = None
    gas_verbrauch = None
    if gas_file is not None:
        try:
            gas_file.seek(0)
            vdf_raw = pd.read_excel(gas_file)
            vdf_raw.columns = vdf_raw.columns.str.strip()
            datum_erkannt, verbrauch_erkannt = erkenne_spalten(vdf_raw, typ="gas")
            alle_spalten = vdf_raw.columns.tolist()
            st.markdown("**Gasspalten prüfen:**")
            gas_datum = st.selectbox("Datumsspalte Gas", alle_spalten,
                index=alle_spalten.index(datum_erkannt[0]) if datum_erkannt else 0,
                key="datum_gas")
            gas_verbrauch = st.selectbox("Verbrauchsspalte Gas", alle_spalten,
                index=alle_spalten.index(verbrauch_erkannt[0]) if verbrauch_erkannt else 0,
                key="verbrauch_gas")
        except Exception as e:
            st.error(f"Fehler bei Gasdaten: {e}")

# ─────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────
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
        baue_panel2(kunde, "Energie",        KATEGORIEN["Energie"],        stil="steckbrief"),
        baue_panel2(kunde, "Nachhaltigkeit", KATEGORIEN["Nachhaltigkeit"], stil="steckbrief"),
        baue_panel2(kunde, "Strategie",      KATEGORIEN["Strategie"],      stil="steckbrief"),
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
if strom_file is not None and gas_file is not None:
    col1, col2 = st.columns(2)

    with col1: 
        st.subheader("⚡ Stromverbrauch")
        try:
            vdf_strom = lade_verbrauch(strom_file, strom_datum, strom_verbrauch)
            zeige_verbrauch_plot(vdf_strom, strom_datum, strom_verbrauch, titel="strom", farbe="#F59E0B")
            k1, k2, k3 = st.columns(3)
            k1.metric("Gesamtverbrauch", f"{vdf_strom[strom_verbrauch].sum():,.0f} kWh")
            k2.metric("Ø pro Zeitpunkt",  f"{vdf_strom[strom_verbrauch].mean():,.1f} kWh")
            k3.metric("Spitzenwert",       f"{vdf_strom[strom_verbrauch].max():,.0f} kWh")
        except Exception as e:
            st.error(f"Fehler beim Laden der Stromdaten: {e}")
    
    with col2:
        st.subheader("🔥 Gasverbrauch")
        try:
            vdf_gas = lade_verbrauch(gas_file, gas_datum, gas_verbrauch)
            zeige_verbrauch_plot(vdf_gas, gas_datum, gas_verbrauch, titel="gas", farbe="#3B82F6")
            k1, k2, k3 = st.columns(3)
            k1.metric("Gesamtverbrauch", f"{vdf_gas[gas_verbrauch].sum():,.0f} kWh")
            k2.metric("Ø pro Zeitpunkt",  f"{vdf_gas[gas_verbrauch].mean():,.1f} kWh")
            k3.metric("Spitzenwert",       f"{vdf_gas[gas_verbrauch].max():,.0f} kWh")
        except Exception as e:
            st.error(f"Fehler beim Laden der Gasdaten: {e}")
    
else:
    if strom_file and strom_datum and strom_verbrauch:
        st.markdown("---")
        st.subheader("⚡ Stromverbrauch")
        try:
            vdf_strom = lade_verbrauch(strom_file, strom_datum, strom_verbrauch)
            zeige_verbrauch_plot(vdf_strom, strom_datum, strom_verbrauch, titel="strom", farbe="#F59E0B")
            k1, k2, k3 = st.columns(3)
            k1.metric("Gesamtverbrauch", f"{vdf_strom[strom_verbrauch].sum():,.0f} kWh")
            k2.metric("Ø pro Zeitpunkt",  f"{vdf_strom[strom_verbrauch].mean():,.1f} kWh")
            k3.metric("Spitzenwert",       f"{vdf_strom[strom_verbrauch].max():,.0f} kWh")
        except Exception as e:
            st.error(f"Fehler beim Laden der Stromdaten: {e}")

    # ── Gasverbrauch ──────────────────────────────
    if strom_file and strom_datum and strom_verbrauch:
        st.markdown("---")
        st.subheader("🔥 Gasverbrauch")
        try:
            vdf_gas = lade_verbrauch(gas_file, gas_datum, gas_verbrauch)
            zeige_verbrauch_plot(vdf_gas, gas_datum, gas_verbrauch, titel="gas", farbe="#3B82F6")
            k1, k2, k3 = st.columns(3)
            k1.metric("Gesamtverbrauch", f"{vdf_gas[gas_verbrauch].sum():,.0f} kWh")
            k2.metric("Ø pro Zeitpunkt",  f"{vdf_gas[gas_verbrauch].mean():,.1f} kWh")
            k3.metric("Spitzenwert",       f"{vdf_gas[gas_verbrauch].max():,.0f} kWh")
        except Exception as e:
            st.error(f"Fehler beim Laden der Gasdaten: {e}")