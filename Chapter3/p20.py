#
# jsonを読み込め
#
import json
import gzip

def get_json():
  with gzip.open("jawiki-country.json.gz","rt") as file:
    for line in file:
      js=json.loads(line)
      if "イギリス" == js["title"]:
        return js["text"]

if __name__ == "__main__":
    answer=get_json()
    print(answer)