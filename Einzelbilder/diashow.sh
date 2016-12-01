FILENAME=$1                     # Übernahme des Dateinamens als Parameter
echo "Filename: $FILENAME"      # Ausgabe des Dateinamens (nur für debug-Zwecke)
killall feh                     # schließen der aktuell laufenden Slideshow

# Anzeige des aktuell geknipsten Bildes für 3 Sekunden, danach Start der Slideshow
feh -F --cycle-once -D6 ./$FILENAME && feh -z -F -R 2 -D 1 -Z ./*.jpg 
# Option -F steht für "Vollbild", --cycle-once sorgt dafür, dass das Programm nach der eingestellten Anzeigedauer von -D 3 (3 Sekunden) nicht neu gestartet wird. Ist die Ausführung des ersten feh-Aufrufs beendet, folgt der zweite Aufruf mit allen jpg-Bilder im Unterordner slideshow. -R 2 bedeutet, dass alle 2 Sekunden die Dateiliste neu geladen wird, so dass auch neu hinzugefügte Bilder angezeigt werden.-z für Radom wiedergabe

FILE2TRANSFER=$FILENAME

REMOTEDIR=/

FTP_SERVER=192.168.178.173  #Bsp.: 192.168.0.100
FTP_PORT=26000
FTP_USER=snitch
FTP_PASS=fotobox

#Die Datei welche uebertragen werden soll
FILE2TRANSFER=$FILENAME

#Das Verzeichnis wohin die Datei uebertragen werden soll
REMOTEDIR=/

### ENDE DER EINSTELLUNGEN

# Dateien per FTP auf den Server schieben
ftp -ni << END_UPLOAD
  open $FTP_SERVER
  user $FTP_USER $FTP_PASS
#  cd $REMOTEDIR
  bin
  mput $FILE2TRANSFER $(basename $FILE2TRANSFER)
  quit
END_UPLOAD

exit 0
