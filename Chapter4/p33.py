# 「AのB」の名詞を全て抽出せよ

from p30 import getMecabData

if __name__ == "__main__":
    analysis = getMecabData()
    answer = []
    for sentence in analysis:
        for idx in range(len(sentence)-3):
            if sentence[idx]["pos"] == "名詞" \
               and sentence[idx+1]["base"] == "の" \
               and sentence[idx+2]["pos"] == "名詞":
                answer.append("".join([w["surface"] for w in sentence[idx:idx+3]]))
    print(answer)
