import streamlit as st
import pandas as pd

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

def baue_panel(kunde, titel, felder, stil="steckbrief"):
    vorhandene = {
        feld: kunde[feld]
        for feld in felder
        if feld in kunde.index and pd.notna(kunde[feld]) and str(kunde[feld]).strip() != ""
    }
    if not vorhandene:
        return None
    return (titel, vorhandene, stil)

def baue_panel2(kunde, titel, felder, stil="steckbrief"):
    vorhandene = {}
    for feld in felder:
        wert = kunde.get(feld)  # .get() statt [] da es ein dict ist
        if wert is None:
            continue
        # Listen als kommagetrennten String darstellen
        if isinstance(wert, list):
            if not wert:  # leere Liste überspringen
                continue
            wert = ", ".join(str(x) for x in wert)
        vorhandene[feld] = wert
    
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