import pandas as pd

def erkenne_spalten(df, typ):
    
    datum_kandidaten = ["stunde", "datum", "date", "zeit", "zeitpunkt", "minute"]

    if typ == "Strom":
        verbrauch_kandidaten = ["kwh", "strom", "verbrauch", "werte", "e endgültig", "e vorläufig"]
    elif typ == "Gas":
        verbrauch_kandidaten = ["verbrauch", "kwh", "gas", "werte", "g endgültig", "g vorläufig"]

    datum_spalten = []
    verbrauch_spalten = []

    for col in df.columns:
        col_lower = col.lower().strip()
        if any(k in col_lower for k in datum_kandidaten):
            datum_spalten.append(col)
        if any(k in col_lower for k in verbrauch_kandidaten):
            verbrauch_spalten.append(col)

    # Fallback – nichts gefunden, nach Inhalt suchen
    if not datum_spalten:
        datum_spalten = erkenne_datum_per_inhalt(df)
        if not datum_spalten:
            #pass        # "mache nichts", eig keine gute praxis für fehler
            raise ValueError(f"Es konnte keine Datumszeile gefunden werden.")
    
    
    if not verbrauch_spalten and datum_spalten:
        verbrauch_spalten = erkenne_verbrauch_per_inhalt(df, datum_spalten)
        if not verbrauch_spalten:
            raise ValueError(f"Es konnte keine Verbrauchszeile gefunden werden.")
        
    return datum_spalten, verbrauch_spalten


def erkenne_datum_per_inhalt(df):
    """Fallback – sucht Spalten mit Datumswerten."""
    gefunden = []
    for col in df.columns:
        probe = df[col].dropna().iloc[0] if not df[col].dropna().empty else None    # probe ist wert aus df wenn nicht leer
        if probe is None:
            continue
        try:
            parsed = pd.to_datetime(probe, dayfirst=True)
            if 2000 <= parsed.year <= 2100:
                gefunden.append(col)
        except:
            pass
    return gefunden


def erkenne_verbrauch_per_inhalt(df, datum_spalten):
    """Fallback – sucht numerische Spalten mit gleicher Länge wie Datumsspalte."""
    gefunden = []
    
    if not datum_spalten:
        return gefunden
    
    datum_len = df[datum_spalten[0]].dropna().shape[0]
    
    for col in df.columns:
        if col in datum_spalten:
            continue
        col_data = df[col].dropna()
        if len(col_data) != datum_len:
            continue
        try:
            pd.to_numeric(col_data.astype(str).str.replace(",", "."), errors="raise")
            gefunden.append(col)
        except:
            pass
    
    return gefunden