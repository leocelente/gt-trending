#!/bin/python3
from bs4 import BeautifulSoup

html_content = ""

with open("trending.html", "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
titles = soup.find_all("h1", class_="h3")
descriptions = soup.find_all("p", class_="pr-4")


def extract_name(text):
    start = text.find("/")
    end = text.find(">") - 1
    return text[start:end]


repos_names = []
repos_descs = []
d_ln = []

# test extraction
# testcase = '<a href="/golang/protobuf"> <svg aria-label="repo" '
# print(extract_name(testcase))


for title in titles:
    children = list(title.contents)
    name = extract_name(str(children[1]))
    repos_names.append((name[1:], children[1].sourceline))


for desc in descriptions:
    repos_descs.append((str(desc.contents[-1]), desc.sourceline))


for i in range(len(repos_names)):
    # in case there is no description (checked here by testing the distance between title and desc sourcelines), 
    # we add a empty description to the list
    if repos_descs[i][1] - repos_names[i][1] > 20:
        repos_descs.insert(i, ("\n", repos_names[i][1]))

for i in range(len(repos_names)):
    print("Name: ", repos_names[i][0])
    print("Description: ", repos_descs[i][0])
    print("")
    print(" --------------------------------------------------------------------------- ")
