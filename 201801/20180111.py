# 変数
# データを保存する箱
lang = 'Python' # langという変数に文字列'Python'を代入
x = 5 # xという変数に5という数値を代入

# 大文字と小文字は区別される
var = 'var'
Var = 'Var'

print(var)
print(Var)

# 二単語繋げる場合は「_」で繋げる
hello_world = 'Hello World'
print(hello_world)


# 定数
"""
定数は値が変えられない変数
Pythonに定数はないため、定数のような意図を持って定義する場合には、すべて大文字で変数名を定義する
"""


# 予約後
"""
関数名や変数名に使用できない単語
予約語を用いるとSyntax Errorになる
"""
print(__import__('keyword').kwlist) # 予約語一覧を出力
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# 変数と型
"""
Pythonの変数には型宣言がないため、変数にどのような型でも入れることができる
"""
x = 5
print(x) # 5
x = 'Python'
print(x) # Python


# データ型
"""
'Hello' 文字列型(str)
10 数値型(int)
データ型が異なるとプログラムは異なる動作をする
"""
print(10 + 5) # 15
print('10' + '5') #105

# type()でデータ型を出力する
suu = 5
print(type(suu)) # <class 'int'>

string = 'Hello'
print(type(string)) # <class 'str'>


# 型変換(キャスト)
"""
データ型の異なる文字列と数値を連結しようとするとエラーになる
エラーを回避するにはデータ型を変える。これを型変換(キャスト)という
"""
name = 'Tom'
age = 24
# int型をstr型に変換
print('My name is ' + name + 'My age is ' + str(age)) # My name is TomMy age is 24

strig_price = '1000'
price = 500
# str型をint型に変換
total_price = int(strig_price) + price
print(total_price) # 1500