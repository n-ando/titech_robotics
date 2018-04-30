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

点P2 <img src="https://latex.codecogs.com/gif.latex?(x,&space;y)"> の の値を <img src="https://latex.codecogs.com/gif.latex?l_1,&space;l_2,&space;\theta_1,&space;\theta_2"> で表す。

まず、点P1 <img src="https://latex.codecogs.com/gif.latex?(x_1,&space;y_1)">  の座標は、

<!--
$$
\begin{eqnarray}
x_1 & = & l_1 \cos\theta_1 \\
y_1 & = & l_1 \sin\theta_1
\end{eqnarray}
$$
-->
<img src="https://latex.codecogs.com/gif.latex?x_1&space;=&space;l_1\cos\theta_1"><br>
<img src="https://latex.codecogs.com/gif.latex?x_2&space;=&space;l_1\sin\theta_2">

点P1からみた点P2の座標 <img src="https://latex.codecogs.com/gif.latex?(x_2,&space;y_2)"> は、

<!--$$
\begin{eqnarray}
x_2 & = & l_2 \times \cos(\theta_1 + \theta_2) \\
y_2 & = & l_2 \times \sin(\theta_1 + \theta_2)
\end{eqnarray}
$$-->
<img src="https://latex.codecogs.com/gif.latex?x_2&space;&&space;=&space;&&space;l_2&space;\cos(\theta_1&space;&plus;&space;\theta_2)"><br>
<img src="https://latex.codecogs.com/gif.latex?x_2&space;&&space;=&space;&&space;l_2&space;\sin(\theta_1&space;&plus;&space;\theta_2)">

であり、最終的に (x, y) は以下の式で表される。

<!--
$$
//\begin{eqnarray}
x = l_1\cos\theta_1 + l_2\cos(\theta_1 + \theta_2) \\
y = l_1\sin\theta_1 + l_2\sin(\theta_1 + \theta_2)
\end{eqnarray}
$$
-->
<img src="https://latex.codecogs.com/gif.latex?x&space;=&space;l_1\cos\theta_1&space;&plus;&space;l_2\cos(\theta_1&space;&plus;&space;\theta_2)"><br>
<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;l_1\sin\theta_1&space;&plus;&space;l_2\sin(\theta_1&space;&plus;&space;\theta_2)">



### 課題2 (逆運動学 (2自由度))
<img src="https://github.com/n-ando/titech_robotics2018/raw/master/figs/q0_fig2.png" align="right">

右のアームの逆運動学 (<img src="https://latex.codecogs.com/gif.latex?(x,&space;y)"> が与えられたとき、<img src="https://latex.codecogs.com/gif.latex?l_1,&space;l_2"> を用いて
<img src="https://latex.codecogs.com/gif.latex?(\theta_1,&space;\theta_2)"> を求める。) を求めよ。


### 解答2

図中 <img src="https://latex.codecogs.com/gif.latex?\theta_1,&space;\theta_2"> は <img src="https://latex.codecogs.com/gif.latex?\alpha,&space;\beta,&space;\phi"> を用いて以下の式で表される。

<!--
$$
\begin{eqnarray}
\theta_1 & = & \frac{\pi}{2} - \alpha - \phi \\
\theta_2 & = & \pi - \beta
\end{eqnarray}
$$
-->
<img src="https://latex.codecogs.com/gif.latex?\theta_1&space;=&space;\frac{\pi}{2}&space;-&space;\alpha&space;-&space;\phi"><br>
<img src="https://latex.codecogs.com/gif.latex?\theta_2&space;=&space;\pi&space;-&space;\beta">

余弦定理と逆関数を使って、<img src="https://latex.codecogs.com/gif.latex?\cos\alpha,&space;\cos\beta,&space;\tan\phi"> の値を求めると、

<!--$$
\begin{eqnarray}
\cos\alpha = \left\(\frac{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\right\) \\
\cos\beta  = \left\(\frac{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\right\) \\
\tan\phi   = \frac{y}{x}
\end{eqnarray}
$$-->
<img src="https://latex.codecogs.com/gif.latex?\cos\alpha&space;=&space;\left\(\frac{l_1^2&space;&plus;&space;l_d^2&space;-&space;l_2^2}{2l_1l_d}\right\)"><br>
<img src="https://latex.codecogs.com/gif.latex?\cos\beta&space;=&space;\left\(\frac{l_1^2&space;&plus;&space;l_2^2&space;-&space;l_d^2}{2l_1l_2}\right\)"><br>
<img src="https://latex.codecogs.com/gif.latex?\tan\phi&space;=&space;\frac{y}{x}">

逆関数を用いて以下のように表すことができる。

<!--
$$
\begin{eqnarray}
\alpha = \arccos\left\(\frac{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\right\) \\
\beta  = \arcsin\left\(\frac{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\right\) \\
\phi   = \arctan\frac{y}{x}
\end{eqnarray}
$$
-->
<img src="https://latex.codecogs.com/gif.latex?\alpha&space;=&space;\arccos\left\(\frac{l_1^2&space;&plus;&space;l_d^2&space;-&space;l_2^2}{2l_1l_d}\right\)"><br>
<img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;\arcsin\left\(\frac{l_1^2&space;&plus;&space;l_2^2&space;-&space;l_d^2}{2l_1l_2}\right\)"><br>
<img src="https://latex.codecogs.com/gif.latex?\phi&space;=&space;\arctan\frac{y}{x}">

以上より、求める角度は、

<!--
$$
\begin{eqnarray}
\theta_1 = \frac{\pi}{2} - \arccos\left(\frac{l_1^2 + l_d^2 - l_2^2}{2l_1l_d}\right) - \arctan\frac{y}{x}
\theta_2 = \pi - \arcsin\left(\frac{l_1^2 + l_2^2 - l_d^2}{2l_1l_2}\right)
\end{eqnarray}
$$
-->
<img src="https://latex.codecogs.com/gif.latex?\theta_1&space;=&space;\frac{\pi}{2}&space;-&space;\arccos\left(\frac{l_1^2&space;&plus;&space;l_d^2&space;-&space;l_2^2}{2l_1l_d}\right)&space;-&space;\arctan\frac{y}{x}"><br>
<img src="https://latex.codecogs.com/gif.latex?\theta_2&space;=&space;\pi&space;-&space;\arcsin\left(\frac{l_1^2&space;&plus;&space;l_2^2&space;-&space;l_d^2}{2l_1l_2}\right)">


なお、この逆運動学にはもう一つの解があります。

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

### 解答

逆運動学は2つの解があり、以下の二通りのプログラムが正解となります。

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
	phi = math.atan2(y, x)
	th = [0] * 2
	th[0] = - ((math.pi / 2) - a - phi)
	th[1] = -(math.pi - b)

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
	phi = math.atan2(y, x)
	th = [0] * 2
	th[0] = - (math.pi / 2 + a - phi)
	th[1] = math.pi - b
	return th
  
link = (1.0, 1.0)
path = ((-1.0, 1.0), (-0.5, 1.0), (0.0, 1.0), (0.5, 1.0), (1.0,1.0))
for pos in path:
  print invkinem(link, pos)
```

以下の paiza.io 上のプログラムでは、以上の2通りのプログラムを実行し逆運動学を求めたうえで、純運動学で検算をしています。
以下のURLにアクセスして試しに実行してみましょう。

* [paiza.io上で実行](https://paiza.io/projects/mxUaGuuAqr2DLu-9vS7Rmg)



### 2.ミドルウエアを利用したサンプルプログラムを示せ
#### a) ロボットミドルウエアを一つ選び、データの送信を行う手順・方法を調べ説明せよ（20点）
結果として、コメントを付したソースコード（完全である必要はないが、データ送信に必要な最低限の部分を示すこと。例えばRTMであればonExecute関数部分。）を添付せよ。

#### b) 同様に、データの受信を行う手順・方法を調べ説明せよ（20点）
結果として、コメントを付したソースコード（完全である必要はないが、データ受信に必要な最低限の部分を示すこと。例えばRTMであればonExecute関数部分。 ）を添付せよ。

（注）この課題では、Web上から適切なプログラムを取得し、その内容を理解しているかどうかを見ます。1行ごとに何をしているか理解し、適切なコメントを付記しているかどうかで理解度を採点します。

### 解答

#### a) データの送信を行う手順・方法

* [参考ページ](http://hmatsudaiac.wixsite.com/venus-robotix/define-namingformats-c-windows)
OpenRTM-aistのConsoleOut.cppのonExecute部分。

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

ROSのパブリッシャの場合。

```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
  ros::Rate loop_rate(10);

int count = 0;
  while (ros::ok())
  {
    std_msgs::String msg;
    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg);
    ros::spinOnce();
    ++count;
  }
  return 0;
}
```


#### b)
* [参考ページ](http://hmatsudaiac.wixsite.com/venus-robotix/define-namingformats-c-windows)

ConsoleIn.cppのonExecute部分。

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

ROSのSubscriberの場合。

```cpp
#include "ros/ros.h"
#include "std_msgs/String.h"
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  ros::spin();
  return 0;
}
```

### 3. 授業の感想（20点）
授業の感想、プログラミング、ロボットミドルウェアに対しての感想を記載してください。


- 問い合わせ： n-ando@aist.go.jp

