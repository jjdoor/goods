#!/bin/bash
if [ $# -lt 6 ]
then
    echo "USAGE: $0 -u <box ip> -i <input dir> -r <repo id> [--apend]"
    echo "e.g.: -(insert images to existing repo)"
    echo "        $0 -u 10.10.10.10 -i ~/Pictures -r 99 --append "
    echo "      -(create or recreate repo and insert images) "
    echo "        $0 -u 10.10.10.10 -i ~/Pictures -r 99 "
    exit 1
fi
set -e
pushd "$(dirname "$0")"
if [ ! -d "./venv" ]
then
    python3 setup.py
fi
source ./venv/bin/activate
python ./sample_code/batch_insert_tool.py $*
deactivate
popd
