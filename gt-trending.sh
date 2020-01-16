#!/bin/zsh
#set to English language
curl -sL "https://github.com/trending?spoken_language_code=en" >> trending.html
# in between quotes becomes the path to the location of the current script
python3 `dirname "$0"`/main.py
rm trending.html