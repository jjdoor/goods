@echo off
set arg6=%6
if "%arg6%" == "" (
    echo "USAGE: $0 -u <box ip> -i <input dir> -r <repo id> [--apend]"
    echo "e.g.: -(insert images to existing repo)"
    echo "        $0 -u 10.10.10.10 -i ~/Pictures -r 99 --append "
    echo "      -(create or recreate repo and insert images) "
    echo "        $0 -u 10.10.10.10 -i ~/Pictures -r 99 "
    exit 1
)
pushd %~dp0

if not exist "./venv" (
    python setup_windows.py
)
call ./venv/bin/activate
python ./sample_code/batch_insert_tool.py %*
call deactivate
popd
