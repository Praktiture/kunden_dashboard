import streamlit as st
import pandas as pd
import os
from spalten_finden import erkenne_spalten

@st.dialog("Dateien konfigurieren")
def datei_konfiguration():
    # pop up fenster mit 3 eingaben
    st.markdown("**Bitte Dateipfade eingeben:**")
    stammdaten = st.file_uploader("Kundendaten Excel", type=["xlsx", "xls"])
    strom = st.file_uploader("Strom Excel", type = ["xlsx", "xls"])
    gas = st.file_uploader("Gas Excel", type = ["xlsx", "xls"])

    # Stromspalte prüfen
    if strom:
        vdf_raw = pd.read_excel(strom)              # vdf = values data frame
        vdf_raw.columns = vdf_raw.columns.str.strip()
        datum_erkannt, verbrauch_erkannt = erkenne_spalten(vdf_raw, typ="strom")

        alle_spalten = vdf_raw.columns.tolist()
        st.markdown("**Stromspalte prüfen:**")
        datum_strom = st.selectbox("Datumspalte Strom", alle_spalten, 
            index = alle_spalten.index(datum_erkannt[0]) if datum_erkannt else 0, key = "datum_strom")
        verbrauch_strom = st.selectbox("Verbrauchsspalte Strom", alle_spalten, 
            index = alle_spalten.index(verbrauch_erkannt[0]) if verbrauch_erkannt else 0, key = "verbrauch_strom")

    # Gasspalte
    if gas:
        vdf_raw = pd.read_excel(gas)              # vdf = values data frame
        vdf_raw.columns = vdf_raw.columns.str.strip()
        datum_erkannt, verbrauch_erkannt = erkenne_spalten(vdf_raw, typ="gas")

        alle_spalten = vdf_raw.columns.tolist()
        st.markdown("**Gasspalte prüfen:**")
        datum_gas = st.selectbox("Datumspalte Gas", alle_spalten, index = alle_spalten.index(datum_erkannt[0]) if datum_erkannt else 0, key = "datum_gas")
        verbrauch_gas = st.selectbox("Verbrauchsspalte Gas", alle_spalten, index = alle_spalten.index(verbrauch_erkannt[0]) if verbrauch_erkannt else 0, key = "verbrauch_gas")


    # Speichern
    if st.button("Speichern", key="save_config_button"):
        st.session_state["stammdaten_pfad"] = stammdaten
        st.session_state["strom_pfad"] = strom
        st.session_state["gas_pfad"] = gas
        st.session_state["strom_datum_spalte"] = datum_strom if strom else ""
        st.session_state["strom_verbrauch_spalte"] = verbrauch_strom if strom else ""
        st.session_state["gas_datum_spalte"] = datum_gas if gas else ""
        st.session_state["gas_verbrauch_spalte"] = verbrauch_gas if gas else ""
        st.rerun()

@st.cache_data
def lade_daten(file):
    file.seek(0)
    df = pd.read_excel(file, header = 2)
    df.columns = df.columns.str.strip()

    umbenennung = {
        "Name": "Firmenname",
        "Unterelemente": "Betreiber",
        "Anschrift des Unternehmens": "Standort",
        "In welcher Branche ist Ihr Unternehmen tätig": "Branche",
        "Ansprechpartner (Name)": "Ansprechpartner",
        "Ihre E-Mail Adresse": "E-Mail",
        "Telefon (bevorzugt Handy)": "Telefon",
        "Mit welchen Hauptenergieträger stellen Sie Ihre Energieversorgung sicher?": "Hauptenergieträger",
        "Wie erfolgt die Bereitstellung von Strom?": "Strombereitstellung",
        "Nutzung von erneuerbaren Energie bereits vorhanden": "Erneuerbare Energie",
        "Welche Maßnahmen sind umgesetzt oder geplant?": "Maßnahmen",
        "Lastgangmanagement vorhanden?": "Lastgangmanagement",
        "Netzanschluss Spannungsebene (in kV) wenn bekannt": "Spannungsebene",
        "Ihr aktueller Energieversorger": "Energieversorger",
        "Tarifname (Optional)": "Tarif",
        "Wann endet der aktuelle Vertrag?": "Vertragsende",
        "Durchschnittlicher Stromverbrauch pro Jahr in MWh:": "Stromverbrauch MWh/a",
        "Ergänzend dazu, Spitzenlast Strom in kW:": "Spitzenlast Strom kW",
        "Mindestlast / Grundlast in kW:": "Grundlast kW",
        "Durchschnittlicher Jahreswärmebedarf in MWh:": "Wärmebedarf MWh/a",
        "Spitzenlast Wärme in kW:": "Spitzenlast Wärme kW",
        "Grundlast Wärme in kW:": "Grundlast Wärme kW",
        "Temperaturanforderungen Ihres Hauptwärmeprozesses (°C):": "Prozesstemperatur °C",
        "Batteriespeicher vorhanden?": "Batteriespeicher",
        "Thermische Speicher vorhanden?": "Thermischer Speicher",
        "Sind große Mengen an freier Abwärme vorhanden?": "Abwärme vorhanden",
    }
    df = df.rename(columns = umbenennung)
    return df

@st.cache_data
def lade_verbrauch(file, datum_spalte, verbrauch_spalte):
    file.seek(0)
    df = pd.read_excel(file, usecols=[datum_spalte, verbrauch_spalte])
    df.columns = df.columns.str.strip()

    df[datum_spalte] = parse_datum(df[datum_spalte])        # umwandlung in standard Format

    df[verbrauch_spalte]= (
        df[verbrauch_spalte]
        .astype(str)
        .str.replace(",",".", regex=False)
        .pipe(pd.to_numeric, errors="coerce")    
    )
    df = df.sort_values(datum_spalte)
    return df

def parse_datum(series):
    formate = [
        "%d.%m.%Y",
        "%d.%m.%Y %H:%M",
        "%d.%m.%Y %H:%M:%S",
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S",
        "%d.%m.%Y.%H",  
        "%d/%m/%Y", 
        "%d/%m/%Y %H:%M",
    ]
    # automatisch versuchen:
    try: 
        return pd.to_datetime(series, dayfirst = True)
    except:
        pass

    for fmt in formate:
        try: 
            return pd.to_daytime(series, format=fmt)
        except:
            continue
    
    raise ValueError(f"Datumsformat nicht erkannt. Beispielwert: {series.iloc[0]}")