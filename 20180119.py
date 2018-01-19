# 関数
# 関数とは
"""
あるデータを受け取り、関数に定義されている処理を実行し、その結果を返すもの
独自関数、標準関数（組み込み関数）がある
"""

# 関数の定義
"""
def 関数名():
	処理
"""

# 関数の定義
def hello():
	print('hello')

# 関数の呼び出し
hello() # hello


# 関数名
"""
小文字で定義する
単語二文字以上で関数名を定義する時は「_」でつなぐ
予約語、組み込み関数と名前が被らないようにする
"""
def lowercase_underscore():
	print('lowercase_underscore')
