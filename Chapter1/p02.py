# "パトカー"と"タクシー"の文字を先頭から交互に連結して文字列"パタトクカシーー"を得よ

if __name__ == "__main__":
    text1 = "パトカー"
    text2 = "タクシー"
    answer = ""
    for (ti, tj) in zip(text1, text2):
        answer = answer + ti + tj
    print(answer)
