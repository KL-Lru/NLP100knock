#!/usr/bin/env python3
#
# jsonを読み込め
#
from json import loads as jsloads
from gzip import open as gzopen

def get_json():
  with gzopen("jawiki-country.json.gz","rt") as file:
    for line in file:
      js = jsloads(line)
      if "イギリス" == js["title"]:
        return js["text"]

if __name__ == "__main__":
    answer = get_json()
    print(answer)