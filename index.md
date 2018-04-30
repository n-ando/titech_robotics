---
layout: default
---

2018年4月12日実施の「ロボットミドルウェア」の授業資料および宿題、参考リンクを掲載しています。

## 授業スライド

<iframe src="//www.slideshare.net/slideshow/embed_code/key/gGqN886eS5iRzg" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/openrtm/ss-93470488" title="東京工業大学「ロボット技術」 ロボットミドルウェア" target="_blank">東京工業大学「ロボット技術」 ロボットミドルウェア</a> </strong> from <strong><a href="https://www.slideshare.net/openrtm" target="_blank">openrtm</a></strong> </div>

## 授業中課題

### 課題1 (順運動学 (2自由度))
<img src="https://github.com/n-ando/titech_robotics2018/raw/master/figs/q0_fig1.png" align="right">

右の2自由度アームの順運動学を求めよ。


### 解答1

点P2 <img src="https://latex.codecogs.com/gif.latex?(x,&space;y)"> の の値をl1, l2, θ1, θ2で表す。

まず、点P1 <img src="https://latex.codecogs.com/gif.latex?(x_1,&space;y_1)">  の座標は、

<img src="https://latex.codecogs.com/gif.latex?x_1&space;=&space;l_1\cos\theta_1">
<br>
<img src="https://latex.codecogs.com/gif.latex?x_2&space;=&space;l_1\sin\theta_2">

点P1からみた点P2の座標 <img src="https://latex.codecogs.com/gif.latex?(x_2,&space;y_2)"> は、

<img src="https://latex.codecogs.com/gif.latex?x_2&space;&&space;=&space;&&space;l_2&space;\cos(\theta_1&space;&plus;&space;\theta_2)">
<br>
<img src="https://latex.codecogs.com/gif.latex?x_2&space;&&space;=&space;&&space;l_2&space;\sin(\theta_1&space;&plus;&space;\theta_2)">

であり、原点座標系から見た時のP2の座標は

<img src="https://latex.codecogs.com/gif.latex?x&space;=&space;l_1\cos\theta_1&space;&plus;&space;l_2\cos(\theta_1&space;&plus;&space;\theta_2)">
<br>
<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;l_1\sin\theta_1&space;&plus;&space;l_2\sin(\theta_1&space;&plus;&space;\theta_2">

<!--
$$
//\begin{eqnarray}
x = l_1\cos\theta_1 + l_2\cos(\theta_1 + \theta_2) \\
y = l_1\sin\theta_1 + l_2\sin(\theta_1 + \theta_2
\end{eqnarray}
$$
-->

### 課題2 (逆運動学 (2自由度))
<img src="https://github.com/n-ando/titech_robotics2018/raw/master/figs/q0_fig2.png" align="right">

右のアームの逆運動学を求めよ。

### 解答2

<img src="https://github.com/n-ando/titech_robotics2018/raw/master/figs/q0_fig3.png" align="right">

図中 θ1, θ2 は以下の式で表される。

$$
\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} - \alpha - \phi \\
\theta_2 & = & \pi - \beta
\end{eqnarray}
$$

図のように長さを設定する点P1の位置は、

$$
\begin{eqnarray}
x_1 & = & l_1 \times \cos\theta_1 \\
y_1 & = & l_1 \times \sin\theta_1
\end{eqnarray}
$$

点P1から点P2の位置は、

$$
\begin{eqnarray}
x_2 & = & l_2 \times \cos(\theta_1 + \theta_2) \\
y_2 & = & l_2 \times \sin(\theta_1 + \theta_2)
\end{eqnarray}
$$
であり、最終的に (x, y) は、
$$
\begin{eqnarray}
x & = & l_1 \times \cos\theta_1 + l_2 \times \cos(\theta_1 + \theta_2) \\
y & = & l_1 \times \sin\theta_1 + l_2 \times \sin(\theta_1 + \theta_2)
\end{eqnarray}
$$
である。
余弦定理と逆関数を使って値を求めます。

$$
\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} - \alpha - \phi \\
\theta_2 & = & \pi - \beta
\end{eqnarray}
$$

$$
\begin{eqnarray}
\cos\alpha & = & \(\fram{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\) \\
\cos\beta  & = & \(\fram{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\) \\
\tan\phi   & = & \frac{y}{x}
\end{eqnarray}
$$

$$
\begin{eqnarray}
\alpha & = & \acos\(\fram{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\) \\
\beta  & = & \asin\(\fram{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\) \\
\phi   & = & \atan\frac{y}{x}
\end{eqnarray}
$$

求める角度は、
$$
\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} - \acos\(\fram{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\) - \atan\frac{y}{x} \\
\theta_2 & = & \pi - \asin\(\fram{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\)
\end{eqnarray}
$$





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

