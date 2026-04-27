import streamlit as st
import pandas as pd
import plotly.express as px
import os
from spalten_erkennung import spalten_auswahl

# streamlit run test_csvtodashboard.py

# ─────────────────────────────────────────────
# KONFIGURATION
# ─────────────────────────────────────────────
KATEGORIEN = {
    "Allgemein": ["Firmenname", "Betreiber", "Ansprechpartner", "Standort", "Mitarbeiter", "Jahresumsatz", "Kunden"],
    "Produktion": ["Produktion", "Produktionslinien", "Technologie"],
    "Netz & Zähler": ["Netzbetreiber", "Zählpunkt", "Anschlüsse"],
}

# Pfade aus session_state
STAMMDATEN_CSV = st.session_state.get("stammdaten_pfad", "")             
STROM_EXCEL = st.session_state.get("strom_pfad", "")
GAS_EXCEL = st.session_state.get("gas_pfad", "")
# session state nötig, da interaktives Programm und dadurch rerun, variablen werden über reruns gespeichert


st.set_page_config(page_title="Kundendashboard", layout="wide")


def setze_styles():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        .panel {
            background-color: white;
            padding: 16px;
            border-radius: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            margin-bottom: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

setze_styles()


# ─────────────────────────────────────────────
# POPUP – Dateien konfigurieren
# ─────────────────────────────────────────────
@st.dialog("Dateien konfigurieren")
def datei_konfiguration():
    st.markdown("**Bitte Dateipfade eingeben:**")
    stammdaten = st.text_input("Stammdaten CSV", value=st.session_state.get("stammdaten_pfad", ""))
    strom = st.text_input("Strom Excel", value=st.session_state.get("strom_pfad", ""))
    gas = st.text_input("Gas Excel", value=st.session_state.get("gas_pfad", ""))

    if st.button("Speichern"):
        st.session_state["stammdaten_pfad"] = stammdaten
        st.session_state["strom_pfad"] = strom
        st.session_state["gas_pfad"] = gas
        st.rerun()


st.title("Kunden-Dashboard")
if st.button("⚙️ Dateien konfigurieren"):
    datei_konfiguration()
st.markdown("---")


# ─────────────────────────────────────────────
# DATEN LADEN
# ─────────────────────────────────────────────
@st.cache_data
def lade_daten(pfad):
    df = pd.read_csv(pfad, sep=";", dtype=str, encoding="latin1")
    df.columns = df.columns.str.strip()
    return df


@st.cache_data
def lade_verbrauch(pfad, datum_spalte, verbrauch_spalte):
    df = pd.read_excel(pfad)
    df.columns = df.columns.str.strip()
    df[datum_spalte] = pd.to_datetime(df[datum_spalte], dayfirst=True)
    df = df.sort_values(datum_spalte)
    return df


if not STAMMDATEN_CSV:
    st.info("Bitte zuerst Dateien konfigurieren.")
    st.stop()

try:
    df = lade_daten(STAMMDATEN_CSV)
except FileNotFoundError:
    st.error(f"Datei nicht gefunden: `{STAMMDATEN_CSV}`")
    st.stop()

kunde = df.iloc[0]


# ─────────────────────────────────────────────
# PANELS
# ─────────────────────────────────────────────
def baue_panel(titel, felder, stil="steckbrief"):
    vorhandene = {
        feld: kunde[feld]
        for feld in felder
        if feld in kunde.index and pd.notna(kunde[feld]) and str(kunde[feld]).strip() != ""
    }
    if not vorhandene:
        return None
    return (titel, vorhandene, stil)


def zeige_panel(titel, vorhandene, stil):
    zeilen = "".join(
        f"<div style='display:flex; margin-bottom:6px;'>"
        f"<span style='flex:1; font-weight:600;'>{feld}</span>"
        f"<span style='flex:2;'>{wert}</span>"
        f"</div>"
        for feld, wert in vorhandene.items()
    )
    st.markdown(f"""
        <div class="panel">
            <div style="font-weight:700; font-size:16px;">{titel}</div>
            <hr style="margin:8px 0;">
            {zeilen}
        </div>
    """, unsafe_allow_html=True)


alle_panels = [
    baue_panel("Allgemein",     KATEGORIEN["Allgemein"],     stil="steckbrief"),
    baue_panel("Produktion",    KATEGORIEN["Produktion"],    stil="steckbrief"),
    baue_panel("Netz & Zähler", KATEGORIEN["Netz & Zähler"], stil="steckbrief"),
]

gefuellte_panels = [p for p in alle_panels if p is not None]

if gefuellte_panels:
    cols = st.columns(len(gefuellte_panels))
    for col, (titel, vorhandene, stil) in zip(cols, gefuellte_panels):
        with col:
            zeige_panel(titel, vorhandene, stil)


# ─────────────────────────────────────────────
# STROMVERBRAUCH
# ─────────────────────────────────────────────
st.markdown("---")
st.subheader("⚡ Stromverbrauch")

if not STROM_EXCEL:
    st.info("Keine Stromdaten konfiguriert.")
elif not os.path.exists(STROM_EXCEL):
    st.error(f"Datei nicht gefunden: `{STROM_EXCEL}`")
else:
    try:
        vdf_raw = pd.read_excel(STROM_EXCEL)
        vdf_raw.columns = vdf_raw.columns.str.strip()
        datum_spalte, verbrauch_spalte = spalten_auswahl(vdf_raw, typ="strom")

        vdf = lade_verbrauch(STROM_EXCEL, datum_spalte, verbrauch_spalte)

        col_von, col_bis = st.columns(2)
        mit_datumsfilter = st.toggle("Zeitraum filtern", value=False)
        if mit_datumsfilter:
            min_d = vdf[datum_spalte].min().date()
            max_d = vdf[datum_spalte].max().date()
            with col_von:
                von = st.date_input("Von", value=min_d, min_value=min_d, max_value=max_d)
            with col_bis:
                bis = st.date_input("Bis", value=max_d, min_value=min_d, max_value=max_d)
            vdf = vdf[
                (vdf[datum_spalte].dt.date >= von) &
                (vdf[datum_spalte].dt.date <= bis)
            ]

        fig = px.line(
            vdf,
            x=datum_spalte,
            y=verbrauch_spalte,
            labels={datum_spalte: "Datum", verbrauch_spalte: "Verbrauch kWh"},
            template="plotly_white",
        )
        fig.update_traces(line_color="#F59E0B", line_width=2)
        fig.update_layout(hovermode="x unified", margin=dict(t=20))
        st.plotly_chart(fig, width='stretch')

        k1, k2, k3 = st.columns(3)
        k1.metric("Gesamtverbrauch", f"{vdf[verbrauch_spalte].sum():,.0f} kWh")
        k2.metric("Ø pro Zeitpunkt",  f"{vdf[verbrauch_spalte].mean():,.1f} kWh")
        k3.metric("Spitzenwert",       f"{vdf[verbrauch_spalte].max():,.0f} kWh")

    except Exception as e:
        st.error(f"Fehler beim Laden der Stromdaten: {e}")


# ─────────────────────────────────────────────
# GASVERBRAUCH
# ─────────────────────────────────────────────
st.markdown("---")
st.subheader("🔥 Gasverbrauch")

if not GAS_EXCEL:
    st.info("Keine Gasdaten konfiguriert.")
elif not os.path.exists(GAS_EXCEL):
    st.error(f"Datei nicht gefunden: `{GAS_EXCEL}`")
else:
    st.info("Gasverbrauch – coming soon.")