#!/usr/bin/env python3
#
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
#

def case_string(x, y, z):
  return "%s時の%sは%s" % (x, y, z)
#end def

if __name__ == "__main__":
  answer = case_string(12, "気温", 22.4)
  print(answer)