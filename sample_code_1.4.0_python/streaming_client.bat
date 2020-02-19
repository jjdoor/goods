@echo off
set arg4=%4
if "%arg4%" == "" (
    echo "USAGE: "
    echo "    $0 -u <box ip> -d <output dir> "
    exit 1
)
pushd %~dp0

if not exist "./venv" (
    python setup_windows.py
)
call ./venv/bin/activate
python ./sample_code/streaming_client.py %* -f -F -s"
call deactivate
popd
