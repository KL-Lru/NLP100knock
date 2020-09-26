# データを整形せよ

import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
  cols = ["ID","Title","URL","PUBLISHER","CATEGORY","STORY","HOSTNAME","TIMESTAMP"]
  targets = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
  
  df = pd.read_csv("newsCorpora.csv", delimiter = "\t", header = None, names = cols)
  df = df[df["PUBLISHER"].isin(targets)]

  obj_col = pd.Series(df["CATEGORY"])

  train, remain, obj_train, obj_remain = train_test_split(df, obj_col, train_size = 0.8, stratify = obj_col, shuffle = True)
  valid, test, _, _ = train_test_split(remain, obj_remain, train_size = 0.5, stratify = obj_remain, shuffle = True)

  train.to_csv("train.txt", index=False)
  valid.to_csv("valid.txt", index=False)
  test.to_csv("test.txt", index=False)

