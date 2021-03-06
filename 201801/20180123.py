# モジュール入門

## ライブラリ
"""
ある程度まとまった汎用性の高い処理(関数・クラス・その他)を
他のプログラムから読み込むことで利用できるようにしたもの
"""

## モジュール
"""
モジュールはある手続き(関数やメソッド)とデータ構造をひとまとめにした部品
"""

## モジュールのインポート
import sys

## 複数のモジュールをインポート
import sys, os

## mathモジュールのcos関数を利用したい場合
## モジュール名.関数名(メンバ名)
import math
print(math.cos(1)) # 0.5403023058681398s


## fromとimport
## 名前を指定せずにモジュール内のすべてのメンバをインポート
from random import *

def get_fortune():
	results = ['大吉', '吉', '小吉', '凶', '大凶', '末吉']
	return choice(results)

print(get_fortune())

