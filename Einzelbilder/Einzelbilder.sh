#!/bin/sh

mkdir -p /Bilder/"`date --iso-8601`" && cd $_ #erstellt ein Verzeichniss des heutigen Tages und wechselt in diesen Ornder

gphoto2 --capture-and-download --hook-script=Fotobox_hook.sh --filename="Fotobox-%Y-%m-%d--%H-%M.%C" --force-overwrite #Foto wird gemacht angezeigt und runtergeladen
