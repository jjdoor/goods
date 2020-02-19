#! /bin/bash
#
# package_startup_package.sh
#

set -e

pushd "$(dirname "$0")"

rm -rf _tmp
mkdir _tmp

pushd _tmp


rsync -avSH /mnt/WXEC0029/xclin/box/app_tool .
mv app_tool sample_code

pushd sample_code

mkdir sample_code

cp ../../batch_insert_tool.py sample_code
cp ../../streaming_client.py sample_code
cp ../../util.py sample_code
cp -r ../../schema sample_code

cp ../../*.sh .
cp ../../*.bat .

popd

rm -rf ../sample_code.tar.gz
tar -czvf ../sample_code.tar.gz sample_code 

popd

rm -rf _tmp

popd
