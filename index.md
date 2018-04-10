---
layout: default
---

2018年4月12日実施の「ロボットミドルウェア」の授業資料および宿題、参考リンクを掲載しています。

## 授業スライド

<iframe src="//www.slideshare.net/slideshow/embed_code/key/MYvxvO47qelwxm" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/openrtm/170420-75274184" title="170420 東工大授業「ロボット技術」資料" target="_blank">170420 東工大授業「ロボット技術」資料</a> </strong> from <strong><a href="//www.slideshare.net/openrtm" target="_blank">openrtm</a></strong> </div>

## 授業中課題

ここに、授業中に出題した課題の回答を掲載します。


## レポート課題

### 1. ロボット制御に必要な以下のプログラムを示せ（40点）
2自由度のアームの逆運動学を計算する以下の仕様の関数のPythonプログラムを作成し、次のプログラムを完成させ、実行結果を示せ　

（注）以下にプログラム例を示します。このプログラムを完成させてください。

```python
import math
def invkinem(link, pos):
  l1 = link[0]
  l2 = link[1]
  x = pos[0]
  y = pos[1]
  ld = 
  b = 
  a = 
  phi = 
  th = 
  th[0] = 
  th[1] = 
  return th

link = (1.0, 1.0)
path = ((-1.0, 1.0), (-0.5, 1.0), (0.0, 1.0), (0.5, 1.0), (1.0,1.0))
for pos in path:
  print invkinem(link, pos)
```

プログラミングには [paiza.io](https://paiza.io/ja/) を利用してもよい。
paiza.ioはブラウザ上で様々なプログラミング言語を利用してプログラムの記述・実行ができるサイト。
アカウント登録をすると、作成したプログラムを保存することもできます。
レポートに保存したプログラムのURLを張り付けて提出することを推奨します。

* [paiza.io](https://paiza.io/ja/) 


### 2.ミドルウエアを利用したサンプルプログラムを示せ
#### a) ロボットミドルウエアを一つ選び、データの送信を行う手順・方法を調べ説明せよ（20点）
結果として、コメントを付したソースコード（完全である必要はないが、データ送信に必要な最低限の部分を示すこと。例えばRTMであればonExecute関数部分。）を添付せよ。

#### b) 同様に、データの受信を行う手順・方法を調べ説明せよ（20点）
結果として、コメントを付したソースコード（完全である必要はないが、データ受信に必要な最低限の部分を示すこと。例えばRTMであればonExecute関数部分。 ）を添付せよ。

（注）この課題では、Web上から適切なプログラムを取得し、その内容を理解しているかどうかを見ます。1行ごとに何をしているか理解し、適切なコメントを付記しているかどうかで理解度を採点します。

### 3. 授業の感想（20点）
授業の感想、プログラミング、ロボットミドルウェアに対しての感想を記載してください。


- 問い合わせ： n-ando@aist.go.jp

