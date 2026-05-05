import streamlit as st
import plotly.express as px

def zeige_verbrauch_plot(vdf, datum_spalte, verbrauch_spalte, titel, farbe):
    
    # intervall der Messdaten ermitteln
    try:
        intervall, faktor = erkenne_intervall(vdf, datum_spalte)
    except ValueError as e:
        st.warning(f"⚠️ {e}")
        intervall = "unbekannt"
        

    if intervall in ["minütlich", "15-Minuten", "30-Minuten", "stündlich"]:
        optionen = ["Gesamtverlauf", "Tagesverlauf", "Tagesverbrauch", "Jahresverlauf (Tagesspitzen)", "Lastdauerlinie"]
    elif intervall == "täglich":
        optionen = ["Gesamtverlauf", "Tagesverbrauch"]
    else:
        optionen = ["Gesamtverlauf"]

    with st.expander("Ansicht"):
        ansicht = st.radio("Auswahl:", optionen, horizontal = True, key = f"ansicht_{titel}")

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
    
    elif ansicht == "Lastdauerlinie":
        sorted_values = (
            vdf[verbrauch_spalte].dropna().sort_values(ascending=False).reset_index(drop=True)
        )
        plot_df = sorted_values.to_frame(name=verbrauch_spalte)
        plot_df["Lastdauer"] = (plot_df.index +1)*faktor
        x_label = f"Dauer[h] pro Jahr"

    elif ansicht == "Tagesverbrauch":
        plot_df = (
            vdf.set_index(datum_spalte)
            .resample("D")[verbrauch_spalte]
            .sum()
            .reset_index()
        )
        x_label = "Datum"
    
    else:               # Gesamtverlauf
        plot_df = vdf
        x_label = "Datum"

    x_achse = datum_spalte if ansicht != "Lastdauerlinie" else "Lastdauer"

    fig = px.line(
        plot_df,
        x = x_achse,
        y = verbrauch_spalte,
        labels = {x_achse: x_label, verbrauch_spalte: "Verbrauch kWh"},
        template = "plotly_white"
    )
    fig.update_traces(line_color = farbe, line_width = 2)
    fig.update_layout(hovermode = "x unified", margin = dict(t=20))
    st.plotly_chart(fig, width = 'stretch')

def erkenne_intervall(df, datum_spalte):
    if len(df) < 2:
        faktor = "unbekannt"
        return "unbekannt", faktor
    
    diff_minuten = df[datum_spalte].diff().dropna().median().total_seconds() / 60

    if 0 <= diff_minuten <= 2:
        faktor = 1/60
        return "minütlich", faktor
    elif 13 <= diff_minuten <= 17:
        faktor = 0.25
        return "15-Minuten", faktor
    elif 25 <= diff_minuten <= 35:
        faktor = 0.5
        return "30-Minuten", faktor
    elif 55 <= diff_minuten <= 65:
        faktor = 1
        return "stündlich", faktor
    elif 1380 <= diff_minuten <= 1500:
        faktor = 1
        return "täglich", faktor
    else: 
        raise ValueError(
            f"Zeitintevall nicht erkannt."
            f"Medianer Abstand zwischen Messpunkten:{diff_minuten:.1f}  Minuten."
        )

    