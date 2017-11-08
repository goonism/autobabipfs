#! /bin/sh

git clone "$1" "$2"
python fix.py "$2"
pushd "$2"
npm install
npm install --save-dev babel-cli babel-preset-env
npm run build
npm run babel
npm link

