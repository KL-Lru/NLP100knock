#
# jsonを読み込め
#
import json
import gzip

def getjson():
    with gzip.open("jawiki-country.json.gz","rt") as f:
        for line in f:
            j=json.loads(line)
            if "イギリス" == j["title"]:
                return j["text"]

if __name__ == "__main__":
    ans=getjson()
    print(ans)