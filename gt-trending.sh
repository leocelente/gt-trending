#!/bin/zsh

curl -sL "https://github.com/trending?spoken_language_code=en" >> trending.html
python3 `dirname "$0"`/main.py
rm trending.html