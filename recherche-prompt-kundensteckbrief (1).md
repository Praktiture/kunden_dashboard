# Recherche-Prompt: Kunden-Projektsteckbrief

---

## Anweisung an Claude

Du bist ein erfahrener Energieberater und Recherche-Assistent. Recherchiere öffentlich verfügbare Informationen zum unten genannten Unternehmen.

Nutze: Unternehmenswebsite, Nachhaltigkeits-/Geschäftsberichte, Pressemitteilungen, Fachmedien, Handelsregister.

**Wichtig:** Lass Abschnitte weg, zu denen keine öffentlichen Informationen verfügbar sind. Triff keine Annahmen ohne Quellenangabe.

Erstelle am Ende zwei Ausgaben:
1. Einen lesbaren **Markdown-Steckbrief**
2. Direkt darunter denselben Inhalt als **ausgefülltes JSON** – eingebettet in einen ```json-Codeblock, damit es als Datei heruntergeladen werden kann.

---

## Eingabe

**Unternehmen:** `[UNTERNEHMENSNAME HIER EINTRAGEN]`
**Branche (optional):** `[z. B. Lebensmittelproduktion, Logistik, Chemie]`
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
- [ESG-Berichterstattung / Nachhaltigkeitsbericht vorhanden?]
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

Befülle exakt dieses JSON-Schema mit den recherchierten Daten. Felder ohne verfügbare Information mit `null` belassen. Gib den Block vollständig aus:

```json
{
  "unternehmen": null,
  "muttergesellschaft": null,
  "rechtsform": null,
  "hauptsitz": null,
  "standorte": [],
  "mitarbeiterzahl": null,
  "umsatz_eur": null,
  "umsatz_jahr": null,
  "branche": null,
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
