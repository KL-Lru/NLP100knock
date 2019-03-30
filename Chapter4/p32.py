# 動詞の原形を全て抽出せよ

from p30 import getMecabData

if __name__ == "__main__":
    analysis = getMecabData()
    answer = []
    for sentence in analysis:
        for word in sentence:
            if word["pos"] == "動詞":
                answer.append(word["base"])
    print(answer)
