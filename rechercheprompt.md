# Recherche-Prompt: Kunden-Projektsteckbrief

---

## Anweisung an Claude

Du bist ein erfahrener Energieberater und Recherche-Assistent. Recherchiere öffentlich verfügbare Informationen zum unten genannten Unternehmen.

Nutze: Unternehmenswebsite, LinkedIn-Unternehmensseite, Nachhaltigkeits-/Geschäftsberichte, Pressemitteilungen, Fachmedien, Handelsregister, Finanzberichte/Jahresabschlüsse, Branchendatenbanken, Fachverbände, Energiedatenbanken, Organigramme in Geschäftberichten.

### Grenzen (zur Ansprechpartnerrecherche)
- Nur öffentlich zugängliche Informationen verwenden
- Keine Vermutungen zu Kontaktdaten — lieber weniger, aber verlässlich

**Zwei Arten von Aussagen – immer klar unterscheiden:**
- **[FAKT]** – Belegt durch öffentliche Quelle (mit Quellenangabe)
- **[ANNAHME]** – Plausible Einschätzung basierend auf Branchenregulierung, Unternehmensstruktur oder typischen Mustern vergleichbarer Unternehmen – nie als Fakt darstellen

Lass Abschnitte weg, zu denen weder Fakten noch sinnvolle Annahmen möglich sind.

Erstelle am Ende als Ausgabe einen lesbaren **Markdown-Steckbrief**.
Halte alle Einträge kurz und prägnant: maximal 1–2 Sätze pro Punkt, keine Nebensätze, keine Wiederholungen. Schlüsselinformation zuerst.

---

## Eingabe

**Unternehmen:** {unternehmen}
**Branche (optional):** {branche}
**Bekannte Standorte (optional):** {standorte}
**Gesprächsnotizen (optional):** {notizen}

---

## Ausgabe: PDF-File

# Projektsteckbrief: [UNTERNEHMENSNAME]

## 1. Stammdaten

| Feld | Information |
|------|-------------|
| **Unternehmen** | |
| **Muttergesellschaft / Konzern** | |
| **Rechtsform** | |
| **Hauptsitz** | |
| **Produktionsstandorte** | |
| **Mitarbeiterzahl** | |
| **Umsatz** | |
| **Branche / Tätigkeit** | |
| **LinkedIn** | [URL zur LinkedIn-Unternehmensseite falls gefunden] |
| **Zeithorizont Projekt** | |

## 2. Ausgangssituation

Nur befüllen wenn Informationen vorhanden – sonst Abschnitt weglassen.

- [Standorte und ihre Funktion]
- [Aktuelle Herausforderungen]
- [Bereits umgesetzte Maßnahmen]
- [Laufende Investitionen / Bauprojekte]
- [Hinweise aus Gesprächen]

## 3. Energie- und Klimastrategie

Nur befüllen wenn Informationen vorhanden – sonst Abschnitt weglassen.

- [Klimaziele und Zeithorizont] → **[FAKT]** oder **[ANNAHME]**
- [ESG-Berichterstattung / Nachhaltigkeitsbericht vorhanden?] → **[FAKT]** oder **[ANNAHME]**
- [CO₂-Bilanzierung: CCF / PCF geplant oder vorhanden?] → **[FAKT]** oder **[ANNAHME]**
- [Zertifizierungen: ISO 50001, EMAS o. ä.] → **[FAKT]** oder **[ANNAHME]**

> 💡 **Branchenguestimate:** Schätze auf Basis typischer Regulierungsanforderungen (z. B. EU-Taxonomie, CSRD, Lieferkettensorgfaltspflicht) und vergleichbarer Unternehmen dieser Branche, welche CO₂-Ziele und Berichtspflichten wahrscheinlich relevant sind. Klar als **[ANNAHME]** kennzeichnen.

## 4. Energieversorgung

Nur befüllen wenn Informationen vorhanden oder Annahmen sinnvoll – sonst Abschnitt weglassen.

- **Stromverbrauch:** [GWh/Jahr] → **[FAKT]** oder **[ANNAHME: Schätzung auf Basis Branche / Unternehmensgröße]**
- **Gasverbrauch:** [GWh/Jahr] → **[FAKT]** oder **[ANNAHME]**
- **Eigenerzeugung:** [BHKW, PV, Windkraft etc.] → **[FAKT]** oder **[ANNAHME]**
- **Wärmeversorgung:** [Quellen, Dampfbedarf] → **[FAKT]** oder **[ANNAHME]**
- **Grünstrom / HKN:** [bekannt?] → **[FAKT]** oder **[ANNAHME]**

> 💡 **Branchenguestimate:** Schätze typische Energieverbräuche und -strukturen für ein Unternehmen dieser Branche und Größe. Klar als **[ANNAHME]** kennzeichnen.

## 5. Geplante Maßnahmen & EE-Ausbau

Nur befüllen wenn Informationen vorhanden oder Annahmen sinnvoll – sonst Abschnitt weglassen.

- [PV, Wind, Speicher geplant?] → **[FAKT]** oder **[ANNAHME]**
- [Elektrifizierung, Wärmepumpen, E-Mobilität?] → **[FAKT]** oder **[ANNAHME]**
- [PPAs oder Grünstrombezugsziele?] → **[FAKT]** oder **[ANNAHME]**

> 💡 **Branchenguestimate:** Schätze auf Basis branchentypischer Dekarbonisierungspfade und aktueller Förderlandschaft, welche Maßnahmen für dieses Unternehmen wahrscheinlich relevant oder im Gespräch sind. Klar als **[ANNAHME]** kennzeichnen.

## 6. Projektrelevanz & offene Fragen

- [Konkrete Ansatzpunkte für Zusammenarbeit]
- [Fördermittelrelevanz]
- [Offene Fragen für nächstes Gespräch]

## 7. Kurzfazit

- [Transformationsphase: früh / fortgeschritten / konservativ]
- [Wichtigste Projektansätze]
- [Dringlichkeit]

---

## 8: Ansprechpartner-Recherche

Recherchiere den optimalen Ansprechpartner für ein Erstgespräch zu einem Projekt im Bereich
**nachhaltige Wärme- und Dampfversorgung / Wärmespeicher**.

### Zielperson (Priorität absteigend)
1. Leiter/in Energiemanagement oder Energiebeauftragter
2. Leiter/in Nachhaltigkeit / ESG / Umwelt
3. Leiter/in Technik / Produktion / Facility Management / Werkleiter (aktuell und älter mit Datum)
4. COO oder Geschäftsführer Technik (nur wenn nichts anderes gefunden)

### Suchquellen (alle durchsuchen)
- LinkedIn: Unternehmensseite → Mitarbeiterliste → Filter nach Rolle
- Unternehmenswebsite: Team-/Kontaktseiten, Impressum, Pressebereich
- **Zertifikate & Audits:** ISO 9001, ISO 14001, ISO 50001, EMAS, OHSAS-Zertifikate auf Website/Pressemitteilungen → QM-, UM-, EM-Verantwortliche sind oft namentlich genannt
- Pressemitteilungen und Fachmedien: Namentliche Erwähnungen in Energieprojekten
- Nachhaltigkeitsberichte: Verantwortliche Personen im Impressum oder Kontaktbereich
- Handelsregister / Northdata: Prokuristen und Geschäftsführer
- Zeitungsberichte (hauptsächlich Lokalzeitungen)
- XING: Unternehmensseite, verteilte Rollen der Mitarbeiter
- Auditvorbereitung/-reports: Verantwortliche für Berichte
- Konferenzen und Messen: Referentenlisten 


### Ausgabe
Gib pro gefundener Person aus (maximal 3, nach Relevanz sortiert):
- **Name**, **Titel / Funktion**, **Funddatum** (von wann gefundene Information)
- **Kontakt** (LinkedIn-URL, E-Mail wenn öffentlich, Telefon wenn öffentlich)
- **Quelle** der Information
- **Relevanz** (1–2 Sätze: warum diese Person?)

Wenn keine direkte Zielperson gefunden wird: Nenne den besten verfügbaren Einstiegskontakt
und erkläre kurz, wie man von dort zur richtigen Person gelangt.


## Quellen

| Quelle | URL | Datum |
|--------|-----|-------|
| | | |
