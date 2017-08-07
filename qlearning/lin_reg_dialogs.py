import pandas as pd
import numpy as np

# Daten laden
df = pd.DataFrame.from_csv('dialogs_wo_header_2.csv', sep=";", header=None)

# Spaltennummern
num_turns = 4
rating = 32

# Nutzerbewertung (rating) und Dialoglänge (num_turns) extrahieren
x = df[num_turns]
y = df[rating]

# Lineares Modell für alle Dialoge  rechnen
regression = np.polyfit(x, y, 1)


# Ab hier: Koprus über Bestätigunsstrategie splitten und Modelle rechnen
none = df[df[2] == 0]
explicit = df[df[2] == 1]


x_none = none[num_turns]
y_none = none[rating]
regression_none = np.polyfit(x_none, y_none, 1)

x_explicit = explicit[num_turns]
y_explicit = explicit[rating]
regression_explicit = np.polyfit(x_explicit, y_explicit, 1)


print('Alle: Anstieg: {0}, Intercept: {1}'.format(regression[0], regression[1]))
print('Keine Bestätigung: Anstieg: {0}, Intercept: {1}'.format(regression_none[0], regression_none[1]))
print('Explizite Bestätigung: Anstieg: {0}, Intercept: {1}'.format(regression_explicit[0], regression_explicit[1]))

# Modell ohne Bestätigungsstrategie auf Daten mit expliziter Bestätigung anwenden und fehler berechnen
fit_explicit = x_explicit * regression_none[0] + regression_none[1]
degree_freedom = 1
error_explicit = (fit_explicit - y_explicit) * (fit_explicit - y_explicit)
me_explicit = np.sqrt(sum(error_explicit) / (len(error_explicit) - degree_freedom))
print('Mittlerer quadratischer Fehler bei Strategie: {0}'.format(me_explicit))

# Aufgabe
# =======
# Ab hier den Korpus zufällig teilen, für einen Teil eine lineares Modell erzeugen
# und dieses auf den anderen Teil anwenden.


