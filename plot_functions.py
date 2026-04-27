import streamlit as st
import plotly.express as px

def zeige_verbrauch_plot(vdf, datum_spalte, verbrauch_spalte, titel, farbe):
    
    # intervall der Messdaten ermitteln
    try:
        intervall = erkenne_intervall(vdf, datum_spalte)
    except ValueError as e:
        st.warning(f"⚠️ {e}")
        intervall = "unbekannt"

    if intervall in ["minütlich", "15-Minuten", "30-Minuten", "stündlich"]:     # ist Tagesverlauf möglich?
        optionen = ["Gesamtverlauf", "Tagesverlauf", "Jahresverlauf (Tagesspitzen)"]
    elif intervall == "täglich":
        optionen = ["Gesamtverlauf"]
    else:
        optionen = ["Gesamtverlauf"]

    ansicht = st.radio("Ansicht", optionen, horizontal = True, key = f"ansicht_{titel}")

    if ansicht == "Tagesverlauf":
        verfuegbare_tage = vdf[datum_spalte].dt.date.unique()
        tag = st.date_input("Tag auswählen",
            value = verfuegbare_tage[0],
            min_value = verfuegbare_tage[0],
            max_value = verfuegbare_tage[-1],
            key = f"tag_{titel}"
        )
        plot_df = vdf[vdf[datum_spalte].dt.date == tag]
        x_label = "Uhrzeit"

    elif ansicht == "Jahresverlauf (Tagesspitzen)":
        plot_df = (
            vdf.set_index(datum_spalte)
            .resample("D")[verbrauch_spalte]
            .max()
            .reset_index()
        )
        x_label = "Datum"
    
    else:               # Gesamtverlauf
        plot_df = vdf
        x_label = "Datum"

    fig = px.line(
        plot_df,
        x = datum_spalte,
        y = verbrauch_spalte,
        labels = {datum_spalte: x_label, verbrauch_spalte: "Verbrauch kWh"},
        template = "plotly_white"
    )
    fig.update_traces(line_color = farbe, line_width = 2)
    fig.update_layout(hovermode = "x unified", margin = dict(t=20))
    st.plotly_chart(fig, width = 'stretch')

def erkenne_intervall(df, datum_spalte):
    if len(df) < 2:
        return "unbekannt"
    
    diff_minuten = df[datum_spalte].diff().dropna().median().total_seconds() / 60

    if 0 <= diff_minuten <= 2:
        return "minütlich"
    elif 13 <= diff_minuten <= 17:
        return "15-Minuten"
    elif 25 <= diff_minuten <= 35:
        return "30-Minuten"
    elif 55 <= diff_minuten <= 65:
        return "stündlich"
    elif 1380 <= diff_minuten <= 1500:
        return "täglich"
    else: 
        raise ValueError(
            f"Zeitintevall nicht erkannt."
            f"Medianer Abstand zwischen Messpunkten:{diff_minuten:.1f}  Minuten."
        )
    