#!/bin/sh

mkdir -p /Bilder/"`date --iso-8601`" && cd $_ #erstellt ein Verzeichniss des heutigen Tages im Ordner Unterordner Bilder und wechselt in diesen Ornder

gphoto2 --capture-image-and-download --hook-script=home/pi/Fotokiste/Fotobox_hook.sh --filename="Fotobox-%Y-%m-%d--%H-%M.%C" --force-overwrite #Foto wird gemacht angezeigt und runtergeladen
