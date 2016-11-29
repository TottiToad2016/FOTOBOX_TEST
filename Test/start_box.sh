#!/bin/sh

/usr/local/bin/gphoto2 --wait-event-and-download --hook-script=test-hook.sh --filename="fotobox-%Y%m%d-%H%M%S.jpg" --force-overwrite
