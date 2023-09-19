import pandas as pd
import altair as alt
from urllib import request
import json

# Eingabe von Kennzahlen aus Meta
TOTAL_FOLLOWERS = 400000
NEW_NET_FOLLOWERS = 250
TOTAL_AUDIENCE = 10000000

# Deutsche Formatvorlagen für Altair laden

with request.urlopen('https://raw.githubusercontent.com/d3/d3-format/master/locale/de-DE.json') as f:
    de_format = json.load(f)
with request.urlopen('https://raw.githubusercontent.com/d3/d3-time-format/master/locale/de-DE.json') as f:
    de_time_format = json.load(f)

alt.renderers.set_embed_options(
    formatLocale=de_format, timeFormatLocale=de_time_format)

# Daten einlesen und vorbereiten

# Daten importieren
df = pd.read_csv(
    "https://raw.githubusercontent.com/kirenz/datasets/master/facebook-ad-data.csv", decimal=',')

# Auswahl der Kampagnen anhand der Id
KAMPAGNEN = [344, 375]
df = df[df['Id'].isin(KAMPAGNEN)]

# Daten anpassen
df['Plattform'] = df['Plattform'].astype('category')


# Berechnung einiger Kennzahlen

# AWARENESS KENNZAHLEN
PUBLIKUMS_WACHSTUMSRATE = (NEW_NET_FOLLOWERS / TOTAL_AUDIENCE) * 100
POST_REICHWEITE = (df['Reichweite'] / TOTAL_FOLLOWERS) * 100

# ENGAGEMENT KENNZAHLEN
DURCH_ENGAGEMENT = (df['Beitragsinteraktionen'] / TOTAL_FOLLOWERS) * 100
AMPLIFIKATION = (df['Geteilte Beiträge'] / TOTAL_FOLLOWERS) * 100
KONVERSATION = (df['Beitragskommentare'] / TOTAL_FOLLOWERS) * 100

# CONERSION KENNZAHLEN
CTR = df['CTR (Link-Klickrate)']
CPC = df['CPC (alle) (EUR)']
CONVERSION = df['Ergebnisrate']
TKP = df['Kosten pro 1.000 erreichten Personen (EUR)']
CPM = df['CPM (Kosten pro 1.000 Impressionen) (EUR)']

# Funktion für das Ausgabeformat der Pandas-Tabellen


def make_pretty(styler):
    styler.format(precision=0, thousands=".", decimal=",")
    return styler
