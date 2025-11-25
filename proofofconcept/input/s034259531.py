int_list = sorted(list(map(int,input().split()))) #標準入力してリスト化して小さい順に並べる
int_list.reverse() #リストの順番を逆にする
l = [str(a) for a in int_list] #リストのタイプをstr化する
s = ' '.join(l) #リストを連結する
print(s) #出力
