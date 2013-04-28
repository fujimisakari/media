#! /bin/bash

LOG (){
    pid=$$
    tag="rsync_mediadata[${pid}]"

    exec 3> >(while read line; do /usr/bin/logger -t $tag -p user.notice     -- "stdout| $line"; done)
    exec 4> >(while read line; do /usr/bin/logger -t $tag -p user.err        -- "stderr| $line"; done)

    ("$@") 1>&3 2>&4

    exec 3>&-
    exec 4>&-
}

MAIN() {
    echo "------------ rsync start. --------------"

    /usr/bin/rsync -avz -e ssh --bwlimit=1000 /home/fujimo/media moon:/home/fujimo

    echo "------------ rsync done. --------------"
}

LOG MAIN
