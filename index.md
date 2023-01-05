---
layout: default
---
<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax:{inlineMath:[['\$','\$'],['\\(','\\)']],processEscapes:true},CommonHTML: {matchFontHeight:false}});</script>
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML"></script>


<!-- ソースを見ようと思った君は賢いね！！でも、宿題は自力でやりましょう。-->

# 「ロボットミドルウェア(2023年4月20日)」

2023年4月20日実施の「ロボットミドルウェア」の授業資料および宿題、参考リンクを掲載しています。

**目次**

<!-- TOC -->

- [1. 授業スライド](#1-%E6%8E%88%E6%A5%AD%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%89)
- [2. レポート課題](#2-%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E8%AA%B2%E9%A1%8C)
    - [2.1. 課題1 順運動学 2自由度 20点](#21-%E8%AA%B2%E9%A1%8C1-%E9%A0%86%E9%81%8B%E5%8B%95%E5%AD%A6-2%E8%87%AA%E7%94%B1%E5%BA%A6-20%E7%82%B9)
    - [2.2. 解答1](#22-%E8%A7%A3%E7%AD%941)
    - [2.3. 課題2 逆運動学 2自由度 20点](#23-%E8%AA%B2%E9%A1%8C2-%E9%80%86%E9%81%8B%E5%8B%95%E5%AD%A6-2%E8%87%AA%E7%94%B1%E5%BA%A6-20%E7%82%B9)
    - [2.4. 解答2](#24-%E8%A7%A3%E7%AD%942)
    - [2.5. 課題3. ロボット制御に必要な以下のプログラムを示せ（40点）](#25-%E8%AA%B2%E9%A1%8C3-%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E5%88%B6%E5%BE%A1%E3%81%AB%E5%BF%85%E8%A6%81%E3%81%AA%E4%BB%A5%E4%B8%8B%E3%81%AE%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0%E3%82%92%E7%A4%BA%E3%81%9B40%E7%82%B9)
    - [2.6. 解答3](#26-%E8%A7%A3%E7%AD%943)
    - [2.7. 授業の感想（20点）](#27-%E6%8E%88%E6%A5%AD%E3%81%AE%E6%84%9F%E6%83%B320%E7%82%B9)
- [3. 問い合わせ](#3-%E5%95%8F%E3%81%84%E5%90%88%E3%82%8F%E3%81%9B)

<!-- /TOC -->

## 1. 授業スライド

<iframe src="//www.slideshare.net/slideshow/embed_code/key/74ywXAP8EaUn8S" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/NoriakiAndo/230420pdf" title="230420_東工大授業「ロボット技術」資料.pdf" target="_blank">230420_東工大授業「ロボット技術」資料.pdf</a> </strong> from <strong><a href="//www.slideshare.net/NoriakiAndo" target="_blank">NoriakiAndo</a></strong> </div>


* [授業スライドPDF](230420_Titech_RobotTechnology_Middleware.pdf)

## 2. レポート課題

回答作成にWeb検索やChatGPTの使用も認めます。使用した際は、その旨レポートに記載してください。減点はしません。

ただし、プログラム作成課題は、実際に動作するかを確認して、実行結果を添付してください。
プログラムの実行には paiza.io の使用を推奨します。

- https://paiza.io

### 2.1. 課題1 (順運動学 (2自由度)) (20点)
<img src="https://github.com/n-ando/titech_robotics/raw/master/figs/q0_fig1.png" align="right" width="320">

右の2自由度アームの順運動学を求めよ。
(関節角 $(\theta_1, \theta_2)$ がわかっているときの、手先座標 $(x, y)$ を求める。ただし、$l_1, l_2$ は既知であるとする。)

<br />
<br />
<br />
<br />
<br />
<br />

### 2.2. 解答1

<!--
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
-->

点P2 $(x, y)$ の値を $l_1, l_2, \theta_1, \theta_2$ で表す。

まず、点P1 $(x_1, y_1)$  の座標は、

\begin{eqnarray}
x_1 & = & l_1 \cos\theta_1 \\\\  
y_1 & = & l_1 \sin\theta_1
\end{eqnarray}

点P1からみた点P2の座標 $(x_2, y_2)$ は、


\begin{eqnarray}
x_2 & = & l_2 \times \cos(\theta_1 + \theta_2) \\\\  
y_2 & = & l_2 \times \sin(\theta_1 + \theta_2)
\end{eqnarray}

であり、最終的に $(x, y)$ は以下の式で表される。


\begin{eqnarray}
x = l_1\cos\theta_1 + l_2\cos(\theta_1 + \theta_2) \\\\  
y = l_1\sin\theta_1 + l_2\sin(\theta_1 + \theta_2)
\end{eqnarray}




### 2.3. 課題2 (逆運動学 (2自由度)) (20点)

<img src="https://github.com/n-ando/titech_robotics/raw/master/figs/q0_fig2.png" align="right" width="320">

右のアームの逆運動学 ($(x, y) $ が与えられたとき、 $l_1, l_2 $ を用いて
 $(\theta_1, \theta_2) $ を求める。) を求めよ。

なお、解は2つあるので、基本的には右図実線の方の解を求めることとする。

<br />
<br />
<br />
<br />
<br />
<br />



### 2.4. 解答2

<!--
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
-->

図中  $\theta_1, \theta_2 $ は  $\alpha, \beta, \phi $ を用いて以下の式で表される。

\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} - \alpha - \phi \\\\  
\theta_2 & = & \pi - \beta
\end{eqnarray}

余弦定理と逆関数を使って、 $\cos\alpha, \cos\beta, \tan\phi $ の値を求めると、

\begin{eqnarray}
\cos\alpha & = & \left\(\frac{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\right\) \\\\  
\cos\beta  & = & \left\(\frac{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\right\) \\\\  
\tan\phi   & = & \frac{x}{y}
\end{eqnarray}

逆関数を用いて以下のように表すことができる。

\begin{eqnarray}
\alpha & = & \arccos\left\(\frac{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\right\) \\\\  
\beta  & = & \arccos\left\(\frac{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\right\) \\\\  
\phi   & = & \arctan\frac{x}{y}
\end{eqnarray}


以上より、求める角度は、

\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} - \arccos\left(\frac{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\right) - \arctan\frac{x}{y} \\\\  
\theta_2 & = & \pi - \arccos\left(\frac{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\right)
\end{eqnarray}

なお、この逆運動学には以下のもう一つの解があります。

\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} + \arccos\left(\frac{l_1^2 + l_d^2 - l_2^2}
{2l_1l_d}\right) - \arctan\frac{x}{y} \\\\  
\theta_2 & = & -\pi + \arccos\left(\frac{l_1^2 + l_2^2 + l_d^2}{2l_1l_2}\right) 
\end{eqnarray}


### 2.5. 課題3. ロボット制御に必要な以下のプログラムを示せ（40点）
2自由度のアームの逆運動学を計算する以下の仕様の関数のPythonプログラムを作成し、次のプログラムを完成させ、実行結果を示せ。　

（注）以下にプログラム例を示します。このプログラムを完成させてください。このプログラでは、path変数に代入されている手先目標座標列に対する関節角度を順に出力します。
順運動学も上で求められているので、検算結果を表示しても良いでしょう。

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
  print(invkinem(link, pos))
```

プログラミングには [paiza.io](https://paiza.io/ja/) の利用を推奨します。
paiza.ioはブラウザ上で様々なプログラミング言語を利用してプログラムの記述・実行ができるサイトです。
アカウント登録をすると、作成したプログラムを保存することもできます。
レポートに保存したプログラムのURLを張り付けて提出することを推奨します。

* [paiza.io](https://paiza.io/ja/) 

### 2.6. 解答3

<!--
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />

逆運動学は2つの解があり、以下の二通りのプログラムが正解となります。
-->

逆運動学は2つの解があり、以下の二通りのプログラムを正解とします。

```python
import math

def invkinem(link, pos):
    l1 = link[0]
    l2 = link[1]
    x = pos[0]
    y = pos[1]
    ld = math.sqrt(x ** 2 + y ** 2)
    b = math.acos((l1 ** 2 + l2 ** 2 - ld ** 2) / (2 * l1 * l2))
    a = math.acos((l1 ** 2 + ld ** 2 - l2 ** 2) / (2 * l1 * ld))
    phi = math.atan2(x, y)
    th = [0] * 2
    th[0] = (math.pi / 2) - a - phi
    th[1] = math.pi - b
    return th

link = (1.0, 1.0)
path = ((-1.0, 1.0), (-0.5, 1.0), (0.0, 1.0), (0.5, 1.0), (1.0,1.0))
for pos in path:
  print invkinem(link, pos)
```

```python
import math

def invkinem(link, pos):
    l1 = link[0]
    l2 = link[1]
    x = pos[0]
    y = pos[1]
    ld = math.sqrt(x * x + y * y)
    b = math.acos((l1 * l1 + l2 * l2 - ld * ld) / (2 * l1 * l2))
    a = math.acos((l1 * l1 + ld * ld - l2 * l2) / (2 * l1 * ld))
    phi = math.atan2(x, y)
    th = [0] * 2
    th[0] = math.pi / 2 + a - phi
    th[1] = - math.pi + b
    return th
  
link = (1.0, 1.0)
path = ((-1.0, 1.0), (-0.5, 1.0), (0.0, 1.0), (0.5, 1.0), (1.0,1.0))
for pos in path:
  print invkinem(link, pos)
```

以下の paiza.io 上のプログラムでは、以上の2通りのプログラムを実行し逆運動学を求めたうえで、順運動学で検算をしています。
以下のURLにアクセスして試しに実行してみましょう。

* [paiza.io上で実行](https://paiza.io/projects/vdH54uDmeMUJlUO1J1DD-Q)

<iframe src="https://paiza.io/projects/e/vdH54uDmeMUJlUO1J1DD-Q?theme=twilight" width="100%" height="500" scrolling="no" seamless="seamless"></iframe>

また、[python/invkinem.py](python/invkinem.py) ([paiza.io上で表示](https://paiza.io/projects/zDnVK5TveR6IpNVgpJOnkA)) では matplotlib を使用して、アームのリンクの状態を以下のように表示させることができます。(paiza.io上ではmatplotlibによるグラフ表示はできません。ローカルにダウンロードして、matplotlibでグラフ表示できる環境で実行してください。)

<a href="https://github.com/n-ando/titech_robotics/raw/master/python/results.png"><img src="https://github.com/n-ando/titech_robotics/raw/master/python/results.png" align="center" width="820"></a>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<!--
### 2.7. 課題4.ミドルウエアを利用したサンプルプログラムを示せ

#### 2.7.1. a) ロボットミドルウエアを一つ選び、データの送信を行う手順・方法を調べ説明せよ（15点）
結果として、コメントを付したソースコード（完全である必要はないが、データ送信に必要な最低限の部分を示すこと。例えばRTMであればonExecute関数部分、ROSであれば Publisherの宣言〜データ送信部分を、行ごとに何をしているのかコメントを付して）を添付せよ。

#### 2.7.2. b) 同様に、データの受信を行う手順・方法を調べ説明せよ（15点）
結果として、コメントを付したソースコード（完全である必要はないが、データ受信に必要な最低限の部分を示すこと。例えばRTMであればonExecute関数部分、ROSであれば Subscriberの部分（コールバック関数含む）を行ごとに何をしているのかコメントを付して）を添付せよ。

（注）この課題では、Web上から適切なプログラムを取得し、その内容を理解しているかどうかを見ます。1行ごとに何をしているか理解し、適切なコメントを付記しているかどうかで理解度を採点します。

### 2.8. 解答4

#### 2.8.1. a) データの送信を行う手順・方法

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
-->
<!--
OpenRTM-aistのConsoleInサンプルのConsoleIn.cppのonExecute部分。

* [参考ページ(OpenRTM)](http://hmatsudaiac.wixsite.com/venus-robotix/define-namingformats-c-windows)


```cpp
RTC::ReturnCode_t ConsoleIn::onExecute(RTC::UniqueId ec_id) // Active状態で周期実行される関数。
{
  std::cout << "input number: ";  // ユーザに入力を促す。
  std::cin >> m_data.data; // ユーザからの入力値を得る。
  setTimestamp(m_data); // データにタイムスタンプを押す。
  m_dataOut.write(); // OutPortからデータを送信。
  return RTC::RTC_OK;
}
```

ROSの送信コード（パブリッシャ）のコードを以下に示す。


* [参考ページ(ROS)](http://wiki.ros.org/ja/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)


```cpp
#include "ros/ros.h"  // ROSメインヘッダのインクルード
#include "std_msgs/String.h" // ROSメッセージ形式 std_msgs/String のインクルード
#include <sstream> // 標準string streamのインクルード

int main(int argc, char **argv) // メイン関数
{
  ros::init(argc, argv, "talker"); // ROS初期化
  ros::NodeHandle n; // ROSノード(ROSモジュールの基本単位)のハンドルの宣言
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000); // 送信を行うPublisherの作成
  ros::Rate loop_rate(10); 

  int count = 0;
  while (ros::ok()) // メインループ
  {
    std_msgs::String msg;
    std::stringstream ss;
    ss << "hello world " << count; // 送信文字列を作成
    msg.data = ss.str(); // 送信文字列を代入
    ROS_INFO("%s", msg.data.c_str()); 
    chatter_pub.publish(msg); // 文字列をサブスクライバに対して送信
    ros::spinOnce(); // するべきその他の仕事（コールバック処理等）をする。おまじない。
    ++count;
  }
  return 0;
}
```
-->
<!--
#### 2.8.2. b) データの受信を行う手順・方法

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
-->
<!--

OpenRTMのConsoleOutサンプルのConsoleOut.cppのonExecute部分。

* [参考ページ(OpenRTM)](http://hmatsudaiac.wixsite.com/venus-robotix/define-namingformats-c-windows)

```cpp
RTC::ReturnCode_t ConsoleOut::onExecute(RTC::UniqueId ec_id) // Active状態で周期実行される関数。
{
  if(m_dataIn.isNew()) // データ入力があれば以下を実行。
  {
    m_dataIn.read(); // InPortからデータを読み込み。
    std::cout << "received: " << m_data.data << std::endl; // 読み込まれたデータを表示。
    std::cout << "sec: " << m_data.tm.sec << " nsec: " << m_data.tm.nsec << std::endl; // 読み込まれたデータのタイムスタンプを表示。
  }
  return RTC::RTC_OK;
}
```

ROSの受信コード（サブスクライバ）のコードを以下に示す。

* [参考ページ(ROS)](http://wiki.ros.org/ja/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)


```cpp
#include "ros/ros.h"  // ROSメインヘッダのインクルード
#include "std_msgs/String.h" // ROSメッセージ形式 std_msgs/String のインクルード

void chatterCallback(const std_msgs::String::ConstPtr& msg) // データ受信のためのコールバック関数
{
  // データが受信されるとString型データが msg に代入されて受け取ることができる。
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener"); // ROS初期化
  ros::NodeHandle n; // このノードのハンドル
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback); // サブスクライバの作成
  ros::spin(); // サブスクライバ等の仕事が来るまで待つループ。終了の割り込み等が入るまで永遠にブロックされる。
  return 0;
}
```
-->

### 2.7. 授業の感想（20点）

授業の感想、プログラミング、ロボットミドルウェアに対しての感想を記載してください。

※感想も課題の一つですが、よく忘れる人がいます。忘れずに書いてください。サービス問題です。


## 3. 問い合わせ

n-ando@aist.go.jp までメールください。

