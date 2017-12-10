#
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
#
def caseString(x,y,z):
  return "%s時の%sは%s"%(x,y,z)
#end def

if __name__=="__main__":
  ans=caseString(12,"気温",22.4)
  print(ans)