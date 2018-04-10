---
layout: default
---

2018年4月12日実施の「ロボットミドルウェア」の授業資料および宿題、参考リンクを掲載しています。

## 授業スライド

<iframe src="//www.slideshare.net/slideshow/embed_code/key/MYvxvO47qelwxm" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/openrtm/170420-75274184" title="170420 東工大授業「ロボット技術」資料" target="_blank">170420 東工大授業「ロボット技術」資料</a> </strong> from <strong><a href="//www.slideshare.net/openrtm" target="_blank">openrtm</a></strong> </div>

## レポート課題

### 1. ロボット制御に必要な以下のプログラムを示せ
2自由度のアームの逆運動学を計算する以下の仕様の関数のPythonプログラムを作成し、次のプログラムを完成させ、実行結果を示せ　（40点）
いかにプログラム例を示します。このプログラムを完成させてください。

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

- 問い合わせ： n-ando@aist.go.jp

