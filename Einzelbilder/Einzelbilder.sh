#!/bin/sh

mkdir /Bilder/"`date --iso-8601`" && cd $_ #erstellt ein Verzeichniss des heutigen Tages im Ordner Unterordner Bilder und wechselt in diesen Ornder

gphoto2 --wait-event-and-download --hook-script=Fotobox_hook.sh --filename="Fotobox-%Y-%m-%d--%H-%M.%C" --force-overwrite #Foto wird gemacht angezeigt und runtergeladen
cd ~
