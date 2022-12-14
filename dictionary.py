import argparse

def dictionary(path):
    
    ##データの読み込み
    with open(path,encoding="utf-8") as f:
        text = [s.strip() for s in f.readlines()]
    
    ##行数の取得
    length = len(text)
    
    ##行数をIDとして表示
    for i in range(length):
        print("{}:{}".format(i+1,text[i]))

## コマンドライン引数の設定
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='テキストファイルの単語をID付きで出力するプログラム')
    parser.add_argument("path", default="dictionary-data.txt", help="単語ファイル名")
    args = parser.parse_args( )
    dictionary(args.path)
