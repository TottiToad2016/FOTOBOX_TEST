FILENAME=$1 # Übernahme des Dateinamens als Parameter
echo "Filename: $FILENAME" # Ausgabe des Dateinamens (nur für debug-Zwecke)
killall feh # schließen der aktuell laufenden Slideshow

# Anzeige des aktuell geknipsten Bildes für 3 Sekunden
feh -F --cycle-once -D 3 ./$FILENAME
# Option -F steht für "Vollbild", --cycle-once sorgt dafür, dass das Programm nach der eingestellten Anzeigedauer von -D 3 (3 Sekunden) nicht neu gestartet wird.
