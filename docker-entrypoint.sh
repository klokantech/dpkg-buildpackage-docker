#!/bin/sh
set -e

if [ "$1" = 'dpkg-buildpackage' ]; then
    TMP=$(mktemp -d)
    cp -r /mnt/src/ $TMP
    cd $TMP/src
    "$@"
    mv $TMP/*.deb /mnt/src/
    exit 0
fi

exec "$@"
