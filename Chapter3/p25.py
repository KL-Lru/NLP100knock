#
# 基礎情報を辞書型に格納せよ
#
from p20 import getjson
from pprint import pprint
import re

# re.subが.*で改行を読んで勝手に改行するのでキレたがフラグを付けると挙動を変えられることを知った
# re.DOTALL: .に\nを含ませる
ans={re.sub("^(.*?) = .*","\\1",st,flags=re.DOTALL):re.sub(".* = (.*)","\\1",st,flags=re.DOTALL) for st in re.sub(".*(\{\{基礎情報.*?\n)}}.*","\\1",getjson(),flags=re.DOTALL).split("\n|")[1:]}
pprint(ans)