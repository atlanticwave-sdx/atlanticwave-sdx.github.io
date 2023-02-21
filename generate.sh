#!/bin/sh
export PYTHON_POST_PROCESS_FILE="/usr/local/bin/yapf -i"

# Prepare the server-end code
#rm -r server
openapi-generator generate -i openapi.yml -g python-flask -o server/
rm ./server/requirements.txt
rm ./server/test-requirements.txt
cp -r ./requirements ./server/requirements
cp tox.ini ./server/

# Prepare the client-end code
#rm -r client
openapi-generator generate -i openapi.yml -g python -o client/
rm ./client/requirements.txt
rm ./client/test-requirements.txt
cp -r ./requirements ./client/requirements
cp tox.ini ./client/
