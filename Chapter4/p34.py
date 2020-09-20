# 名詞の連接を最長一致で全て抽出せよ

from p30 import getMecabData

if __name__ == "__main__":
    analysis = getMecabData()
    answer = []
    for sentence in analysis:
        noun = ""
        cnt = 0
        for idx in range(len(sentence)):
            if sentence[idx]["pos"] == "名詞":
                noun += sentence[idx]["surface"]
                cnt += 1
            else:
                if cnt >= 2:
                    answer.append(noun)
                cnt = 0
                noun = ""
    print(answer)
