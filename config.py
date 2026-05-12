import os

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    raise ValueError("ANTHROPIC_API_KEY ist nicht gesetzt!")

MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 8000
PROMPT_FILE = "rechercheprompt.md"
FIELDS = ("Unternehmen", "Branche(optional)", "Standorte(optional)", "Notizen(optional)")