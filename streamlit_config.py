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
            if isinstance(wert[0], dict):
                wert = "<br><br>".join(
                    "<br>".join(f"<b>{k}:</b> {v}" for k, v in obj.items() if v)
                    for obj in wert)
            else:
                wert = "<br>".join(str(x) for x in wert)
    
    if not vorhandene:
        return None
    return (titel, vorhandene, stil)

def zeige_panel(titel, vorhandene, stil):
    if stil == "steckbrief":
        zeilen = "".join(
            f"<div style='"
            f"display: grid;"
            f"grid-template-columns: minmax(0, 1fr) minmax(0, 2fr);"
            f"gap: 4px 12px;"
            f"margin-bottom: 6px;"
            f"align-items: start;"
            f"'>"
            f"<span style='"
            f"font-size: 13px;"
            f"font-weight: 600;"
            f"color: #555;"
            f"word-break: break-word;"
            f"'>{feld}</span>"
            f"<span style='"
            f"font-size: 13px;"
            f"word-break: break-word;"
            f"'>{wert}</span>"
            f"</div>"
            for feld, wert in vorhandene.items()
        )
        st.markdown(f"""
            <div class="panel">
                <div style="font-weight:700; font-size:16px;">{titel}</div>
                <hr style="margin:8px 0; border:none; border-top: 1px solid #eee;">
                {zeilen}
            </div>
        """, unsafe_allow_html=True)
    
    elif stil == "text":
        abschnitte = "".join(
            f"<div style='margin-bottom: 12px;'>"
            f"<div style='font-size:13px; font-weight:600; color:#555; margin-bottom:4px;'>{feld}</div>"
            f"<div style='font-size:14px; line-height:1.6; color:#333;'>{wert}</div>"
            f"</div>"
            for feld, wert in vorhandene.items()
        )
        st.markdown(f"""
            <div class="panel">
                <div style="font-weight:700; font-size:16px;">{titel}</div>
                <hr style="margin:8px 0; border:none; border-top: 1px solid #eee;">
                {abschnitte}
            </div>
        """, unsafe_allow_html=True)
