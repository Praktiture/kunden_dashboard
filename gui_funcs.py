import re

def fill_prompt(template, daten):
    result = template
    result = result.replace("{unternehmen}", daten["Unternehmen"])
    result = result.replace("{branche}", daten["Branche(optional)"])
    result = result.replace("{standorte}", daten["Standorte(optional)"])
    result = result.replace("{notizen}", daten["Notizen(optional)"])

    return result