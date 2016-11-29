self=`basename $0`

case "$ACTION" in
    init)
	echo "$self: INIT"
	# exit 1 # non-null exit to make gphoto2 call fail
	;;
    start)
	echo "$self: START"
	;;
    download)
	echo "$self: DOWNLOAD to $ARGUMENT"
		# nach abgeschlossenem Download der Bilder

		TYPE=`file --mime-type -b "$ARGUMENT"` # Typ des Bildes herausfinden
	
        if [ "$TYPE" = 'image/tiff' ]; then # Falls es sich um ein War-Foto handelt ...
					./convertPicture.sh $ARGUMENT &
        else # fuer das jpg-Bild
					./startSlideshow.sh "$ARGUMENT" &

        fi


	;;
    stop)
	echo "$self: STOP"
	;;
    *)
	echo "$self: Unknown action: $ACTION"
	;;
esac

exit 0
