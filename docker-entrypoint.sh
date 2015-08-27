#!/bin/sh
set -e

if [ "$1" = 'dpkg-buildpackage' ]; then
    TMP=$(mktemp -d)
    cp -r /mnt/src/ $TMP
    cd $TMP/src
    "$@"
    mv $TMP/*.deb /mnt/dst/
    exit 0
fi

exec "$@"
