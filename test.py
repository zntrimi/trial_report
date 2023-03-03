filename = 'line_followup.txt'  # 読み込むファイル名を指定する
with open(filename) as file:
    lines = file.readlines()  # ファイルの全ての行をリストで読み込む
    for line in lines:
        line.format(name)  # 文章の途中に変数を入れて出力する