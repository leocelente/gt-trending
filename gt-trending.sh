#!/bin/zsh

curl -sL "https://github.com/trending?spoken_language_code=en" >> trending.html
python3 main.py
rm trending.html