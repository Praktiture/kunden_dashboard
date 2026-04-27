# spalten_erkennung.py

import pandas as pd
import streamlit as st


def erkenne_spalten(df, typ):
    
    # typ: "strom" oder "gas"
    
    datum_kandidaten = ["stunde", "datum", "date", "zeit", "zeitpunkt", "minute"]

    strom_kandidaten = ["kwh", "strom", "verbrauch", "werte", "e"]
    
    gas_kandidaten = ["verbrauch", "kwh", "gas", "werte", "g"]

    if typ == "strom":
        verbrauch_kandidaten = strom_kandidaten
    elif typ == "gas":
        verbrauch_kandidaten = gas_kandidaten

    datum_spalten = []
    verbrauch_spalten = []

    for col in df.columns:
        col_lower = col.lower().strip()
        if any(k in col_lower for k in datum_kandidaten):
            datum_spalten.append(col)
        if any(k in col_lower for k in verbrauch_kandidaten):
            verbrauch_spalten.append(col)

    return datum_spalten, verbrauch_spalten


def spalten_auswahl(df, typ):
    datum_spalte, verbrauch_spalte = erkenne_spalten(df, typ)

    print("\nGefundene Spalten:")
    for i, col in enumerate(df.columns):
        print(f"  {i}: {col}")

    print(f"\nErkannte Datumsspalte:    '{datum_spalte}'")
    print(f"Erkannte Verbrauchsspalte '{verbrauch_spalte}'")

    korrektur = input("\nKorrekt? (Enter = ja, n = nein): ")

    if korrektur.lower() == "n":
        datum_index = int(input("Index der Datumsspalte: "))
        verbrauch_index = int(input("Index der Verbrauchsspalte: "))
        datum_spalte = df.columns[datum_index]
        verbrauch_spalte = df.columns[verbrauch_index]

    return datum_spalte, verbrauch_spalte

def finde_daten_startzeile(file, max_rows = 20):
    file.seek(0)            # damit file aktiv bleibt
    df_roh = pd.read_excel(file, header=None, nrows=max_rows)

    header_kandidaten = ["datum", "date", "zeit", "zeitpunkt", "tag", "stunde", "time", "timestamp"]

    # suche nach header stichwörtern                     
    for i, row in df_roh.iterrows():
        for wert in row:
            if pd.isna(wert):       # falls kein wert in zelle
                continue
            if isintance(wert,str) and any(k in wert.lower() for k in header_kandidaten):            # ist wert in kandidaten
                return i+1, i           # zelle und nächste zurückgeben
            else:
                try:     
                    parsed = pd.to_datetime(wert, dayfirst=True)
                    if 2000<= parsed.year <= 2100:       # check ob sinnvolles Datum
                        header_zeile = i-1 if i>0 else None
                    return i, header_zeile
                except:
                    pass
    raise ValueError(
        f"Keine Datenzeile gefunden in den ersten {max_rows} Zeilen."
        f"Bitte Dateistruktur prüfen."
    )                

