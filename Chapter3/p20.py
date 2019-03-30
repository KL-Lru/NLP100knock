# jsonを読み込め
import json
import gzip


def getUKText():
    with gzip.open("jawiki-country.json.gz", "rt") as lines:
        for line in lines:
            js = json.loads(line)
            if "イギリス" == js["title"]:
                return js["text"]
# end def

if __name__ == "__main__":
    answer = getUKText()
    print(answer)
