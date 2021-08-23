#! /bin/bash

cd `dirname $0`

dummy001() {
    bochs
}

case "$1" in 
    *)
        $1
        ;;
esac
