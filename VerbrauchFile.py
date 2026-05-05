import streamlit as st
from spalten_finden import erkenne_spalten
import pandas as pd
from data_load import lade_verbrauch
from plot_functions import zeige_verbrauch_plot

class VerbrauchFile:
    file = None
    datum = None
    verbrauch = None
    vdf = None
    
    def __init__(self, vTyp):   
        self.vTyp = vTyp
        self.subHeader = "Verbrauch"
        self.farbe = "#000000"
        if vTyp == "Strom":
            self.subHeader = "⚡ Stromverbrauch"
            self.farbe ="#F59E0B"
        elif vTyp == "Gas":
            self.subHeader = "🔥 Gasverbrauch"
            self.farbe ="#3B82F6"
            
    # optional make_name_avaiable für 
    def set_file(self): 
        self.file = st.session_state.get(f"{self.vTyp}_file")       
    
    def checkAndCleanData(self):
        try:
            self.file.seek(0)
            vdf_raw = pd.read_excel(self.file)
            vdf_raw.columns = vdf_raw.columns.str.strip()
            datum_erkannt, verbrauch_erkannt = erkenne_spalten(vdf_raw, typ=self.vTyp)
            alle_spalten = vdf_raw.columns.tolist()
            st.markdown(f"**{self.vTyp}spalten prüfen:**")
            self.datum = st.selectbox((f"Datumsspalte {self.vTyp}"), alle_spalten,
                index=alle_spalten.index(datum_erkannt[0]) if datum_erkannt else 0,
                key=(f"datum_{self.vTyp}"))
            self.verbrauch = st.selectbox((f"Verbrauchsspalte {self.vTyp}"), alle_spalten,
                index=alle_spalten.index(verbrauch_erkannt[0]) if verbrauch_erkannt else 0,
                key=(f"verbrauch_{self.vTyp}"))
        except Exception as e:
            st.error(f"Fehler bei {self.vTyp}daten: {e}")

    def make_col(self, col):
        with col: 
            st.subheader(self.subHeader)
            try:
                self.vdf = lade_verbrauch(self.file, self.datum, self.verbrauch)
                zeige_verbrauch_plot(self.vdf, self.datum, self.verbrauch, titel=self.vTyp, farbe=self.farbe)
                k1, k2, k3 = st.columns(3)
                k1.badge(f"Gesamtverbrauch: {self.vdf[self.verbrauch].sum():,.0f} kWh", color = "blue")
                k2.badge(f"Ø pro Zeitpunkt: {self.vdf[self.verbrauch].mean():,.1f} kWh", color = "green")
                k3.badge(f"Spitzenwert: {self.vdf[self.verbrauch].max():,.0f} kWh", color = "red")
            except Exception as e:
                st.error(f"Fehler beim Laden der {self.vTyp}daten: {e}")
