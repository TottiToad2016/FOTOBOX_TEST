#!/bin/sh

eog -f -w /home/pi/Fotokiste/blackscreen.png & #Balckscreen wird über Terminal gelegt ! Evtl. xli besser ?

mkdir -p -m 777 /home/pi/Fotokiste/Bilder/"`date --iso-8601`" && cd $_ #erstellt ein Verzeichniss des heutigen Tages im Ordner Unterordner Bilder und wechselt in diesen Ornder

gphoto2 --wait-event --hook-script=/home/pi/Fotokiste/Fotobox_hook.sh --filename="Fotobox-%Y-%m-%d--%H-%M-%S.%C" --force-overwrite #Foto wird gemacht angezeigt und runtergeladen
