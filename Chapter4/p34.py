# 「AのB」となる名詞句を全て抽出せよ

from p30 import getMecabData

if __name__ == "__main__":
    analysis = getMecabData()
    answer = []
    for sentence in analysis:
        for idx in range(len(sentence)-2):
            if sentence[idx]["pos"] == "名詞" \
                    and sentence[idx+1]["surface"] == "の" \
                    and sentence[idx+2]["pos"] == "名詞":
                answer.append(sentence[idx]["surface"]
                              + sentence[idx+1]["surface"]
                              + sentence[idx+2]["surface"])
    print(answer)
