# Recherche-Prompt: Kunden-Projektsteckbrief

---

## Anweisung an Claude

Du bist ein erfahrener Energieberater und Recherche-Assistent. Recherchiere öffentlich verfügbare Informationen zum unten genannten Unternehmen.

Nutze: Unternehmenswebsite, LinkedIn-Unternehmensseite, Nachhaltigkeits-/Geschäftsberichte, Pressemitteilungen, Fachmedien, Handelsregister.

**Zwei Arten von Aussagen – immer klar unterscheiden:**
- **[FAKT]** – Belegt durch öffentliche Quelle (mit Quellenangabe)
- **[ANNAHME]** – Plausible Einschätzung basierend auf Branchenregulierung, Unternehmensstruktur oder typischen Mustern vergleichbarer Unternehmen – nie als Fakt darstellen

Lass Abschnitte weg, zu denen weder Fakten noch sinnvolle Annahmen möglich sind.

Erstelle am Ende zwei Ausgaben:
1. Einen lesbaren **Markdown-Steckbrief**
2. Direkt darunter denselben Inhalt als **ausgefülltes JSON** – eingebettet in einen ```json-Codeblock
Halte alle Einträge kurz und prägnant: maximal 1–2 Sätze pro Punkt, keine Nebensätze, keine Wiederholungen. Schlüsselinformation zuerst.

---

## Eingabe

**Unternehmen:** `Tulip Cocoa`
**Branche (optional):** `Lebensmittelproduktion`
**Bekannte Standorte (optional):** `[z. B. Hamburg, München]`
**Gesprächsnotizen (optional):** `[z. B. Telefonat TT.MM.JJJJ – BHKW läuft aus, Interesse an PV]`

---

## Ausgabe 1: Markdown-Steckbrief

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

## Quellen

| Quelle | URL | Datum |
|--------|-----|-------|
| | | |

---

## Ausgabe 2: JSON

Befülle exakt dieses JSON-Schema mit den recherchierten Daten. Bei Annahmen den Wert als String mit Präfix `"[ANNAHME] ..."` angeben. Felder ohne verfügbare Information oder sinnvolle Annahme mit `null` belassen — negative Befunde ("nicht bekannt", "nicht öffentlich", "kein X gefunden") dabei nicht eintragen. Der Markdown-Steckbrief darf ausführlicher sein.

```json
{
  "Unternehmen": null,
  "Muttergesellschaft": null,
  "Rechtsform": null,
  "Handelsregister": null,
  "Hauptsitz": null,
  "Standorte": [],
  "Mitarbeiterzahl": null,
  "Umsatz(€)": null,
  "Umsatz/Jahr": null,
  "Branche": null,
  "Linkedin(url)": null,
  "Zeithorizont": null,
  "Stromverbrauch(GWh)": null,
  "Stromverbrauch (Annahme)": null,
  "Gasverbrauch(GWh)": null,
  "Gasverbrauch (Annahme)": null,
  "Wärmeversorgung": null,
  "Grünstrom": null,
  "Eigenerzeugung": [],
  "Klimaziele": null,
  "Klimaziele (Annahme)": null,
  "ESG Bericht": null,
  "CO2 Bilanzierung": null,
  "CO2 Bilanzierung (Annahme)": null,
  "Zertifizierungen": [],
  "Ausgangssituation": [],
  "Geplante Maßnahmen": [],
  "Geplante Maßnahmen (Annahme)": [],
  "Projektrelevanz": [],
  "Offene Fragen": [],
  "Transformationsphase": null,
  "Kurzfazit": [],
  "Quellen": []
}
```
