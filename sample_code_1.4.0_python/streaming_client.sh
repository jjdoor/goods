#!/bin/bash

if [ $# -lt 5 ]
then
    echo "USAGE: "
    echo "    $0 -u <box ip> -d <output dir> -f -F -s"
    exit 1
fi

trap 'onCtrlC' INT
function onCtrlC() {
    deactivate
}

set -e
pushd "$(dirname "$0")"
if [ ! -d "./venv" ]
then
    python3 setup.py
fi
source ./venv/bin/activate
python ./sample_code/streaming_client.py $*
deactivate
popd

