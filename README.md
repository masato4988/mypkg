# ROS 2
* 千葉工業大学ロボットシステム学_2023の講義内で作成したリポジトリです．
* このリポジトリは ROS 2 のパッケージで，talkerとlistenerというノードがあります．

[![test](https://github.com/masato4988/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/masato4988/mypkg/actions/workflows/test.yml)

## 各ノードの説明

### talker.py
* 符号あり整数を /countup というトピックでデータを出力する．
### listener.py
* /countup というトピックから受け取ったデータを出力する．

## LICENSE
* このソフトウェアパッケージは．３条項BSDライセンスの下，再配布および使用が許可されます．
* © 2023 Masato Aita
