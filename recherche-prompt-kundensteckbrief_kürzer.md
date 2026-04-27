# Recherche-Prompt: Kunden-Projektsteckbrief

---

## Anweisung an Claude

Du bist ein erfahrener Energieberater und Recherche-Assistent. Recherchiere öffentlich verfügbare Informationen zum unten genannten Unternehmen und befülle den Steckbrief.

Nutze: Unternehmenswebsite, Nachhaltigkeits-/Geschäftsberichte, Pressemitteilungen, Fachmedien, Handelsregister.

**Wichtig:** Lass Felder weg, zu denen keine öffentlichen Informationen verfügbar sind. Nur wenn Informationen vorhanden sind, werden sie ausgegeben. Triff keine Annahmen ohne Quellenangabe.

Erstelle **zwei Ausgaben**:
1. Den lesbaren **Markdown-Steckbrief**
2. Direkt darunter ein **JSON-Block** mit denselben Daten (maschinenlesbar)

---

## Eingabe

**Unternehmen:** `Tulip Cocoa FB GmbH`
**Branche (optional):** `[z. B. Lebensmittelproduktion]`
**Bekannte Standorte (optional):** 
**Gesprächsnotizen (optional):**

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

- [Klimaziele und Zeithorizont]
- [ESG-Berichterstattung / Nachhaltigkeitsbericht]
- [CO₂-Bilanzierung: CCF / PCF geplant oder vorhanden?]
- [Zertifizierungen: ISO 50001, EMAS o. ä.]

## 4. Energieversorgung

Nur befüllen wenn Informationen vorhanden – sonst Abschnitt weglassen.

- **Stromverbrauch:** [GWh/Jahr]
- **Gasverbrauch:** [GWh/Jahr]
- **Eigenerzeugung:** [BHKW, PV, Windkraft etc.]
- **Wärmeversorgung:** [Quellen, Dampfbedarf]
- **Grünstrom / HKN:** [bekannt?]

## 5. Geplante Maßnahmen & EE-Ausbau

Nur befüllen wenn Informationen vorhanden – sonst Abschnitt weglassen.

- [PV, Wind, Speicher geplant?]
- [Elektrifizierung, Wärmepumpen, E-Mobilität?]
- [PPAs oder Grünstrombezugsziele?]

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

Gib direkt nach dem Markdown-Steckbrief folgenden JSON-Block aus. Felder ohne verfügbare Information mit `null` befüllen. Keine Felder weglassen.

```json
{
  "unternehmen": "",
  "muttergesellschaft": null,
  "rechtsform": null,
  "hauptsitz": null,
  "standorte": [],
  "mitarbeiterzahl": null,
  "umsatz_eur": null,
  "umsatz_jahr": null,
  "branche": "",
  "zeithorizont": null,
  "ausgangssituation": [],
  "klimaziele": null,
  "esg_bericht": null,
  "co2_bilanzierung": null,
  "zertifizierungen": [],
  "stromverbrauch_gwh": null,
  "gasverbrauch_gwh": null,
  "eigenerzeugung": [],
  "waermeversorgung": null,
  "gruenstrom": null,
  "geplante_massnahmen": [],
  "projektrelevanz": [],
  "offene_fragen": [],
  "transformationsphase": null,
  "kurzfazit": [],
  "quellen": []
}
```
