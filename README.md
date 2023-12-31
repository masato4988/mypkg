# ROS 2 パッケージ
* 千葉工業大学ロボットシステム学_2023の講義内で作成したリポジトリです．
* このリポジトリは ROS 2 のパッケージです．
* talker，listener，talker_random，avrtagr，listener_averageというノードがあります．
* talk_listen.launch.py, random_average.launch.pyというlaunchファイルがあります．
* talkerとlisteerを使うと，０からカウントアップしていき，それを表示することができます.
* talker_randomとaverageとlistener_averageを使うと， 0から100の整数の乱数を生成し，そのデータ１０個の平均を求め，表示することができます．


[![test](https://github.com/masato4988/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/masato4988/mypkg/actions/workflows/test.yml)

## 各ノードの説明
### talker
* 0.5秒ごとに0からカウントアップしていき，その値をトピック /countup に出力していく．
### listener
* トピック /countup からデータを取得し出力する．
### talker_random
* 0.5秒ごとに0から100の範囲で整数の乱数を生成し，トピック /random に出力していく．
### average
* トピック /random からデータを取得・記録し，過去10個のデータの平均値を，トピック /average に出力していく．
### listener_average
* トピック /average からデータを取得し出力する．

## トピックの説明
### /countup
* 符号あり16bit整数型(Int16)
### /random
* 符号あり16bit整数型(Int16)
### /average
* 符号あり16bit整数型(Int16)

## launchファイル
### talke_listen.lauch.py
* ノード（talker，listener）を同時に立ち上げることができる．
### random_average.launch.py
* ノード（talker_random，average，listener_average）を同時に立ち上げることができる．

## 使用方法
### talker
ターミナルで次のコマンドを実行する．
```
$ ros2 run mypkg talker
```
実行結果は表示されていない．
### listener
```
$ ros2 run mypkg listener
```
* 表示例:
もし，talker が実行されていた場合，次のように表示される．
```
[INFO] [1703740904.485308656] [listener]: Listen: 29
[INFO] [1703740904.965717856] [listener]: Listen: 30
[INFO] [1703740905.466480280] [listener]: Listen: 31
[INFO] [1703740905.967050387] [listener]: Listen: 32
[INFO] [1703740906.466313851] [listener]: Listen: 33
[INFO] [1703740906.966066638] [listener]: Listen: 34
[INFO] [1703740907.466762322] [listener]: Listen: 35
[INFO] [1703740907.965677160] [listener]: Listen: 36
[INFO] [1703740908.465864160] [listener]: Listen: 37
[INFO] [1703740908.965701982] [listener]: Listen: 38
[INFO] [1703740909.465783839] [listener]: Listen: 39
[INFO] [1703740909.965689054] [listener]: Listen: 40
[INFO] [1703740910.466347924] [listener]: Listen: 41
[INFO] [1703740910.965700621] [listener]: Listen: 42
　　　　　　　　　　　　　・
　　　　　　　　　　　　  ・
　　　　　　　　　　　　　・
```
### talker_random
ターミナルで次のコマンドを実行する．
```
$ ros2 run mypkg talker_random
```
実行結果は表示されない

### average
ターミナルで次のコマンドを実行する．
```
$ ros2 run mypkg average
```
実行結果は表示されない

### listener_average
ターミナルで次のコマンドを実行する．
```
$ ros2 run mypkg listener_average
```
* 表示例:
もし，talker_random，average が実行されている場合，次のように表示される．
```
[listener_average-3] [INFO] [1703741656.120329832] [listener_average]: Listen_average: 54
[listener_average-3] [INFO] [1703741656.613221926] [listener_average]: Listen_average: 41
[listener_average-3] [INFO] [1703741657.114272294] [listener_average]: Listen_average: 40
[listener_average-3] [INFO] [1703741657.612907856] [listener_average]: Listen_average: 48
[listener_average-3] [INFO] [1703741658.113268408] [listener_average]: Listen_average: 45
[listener_average-3] [INFO] [1703741658.612636497] [listener_average]: Listen_average: 52
[listener_average-3] [INFO] [1703741659.112976968] [listener_average]: Listen_average: 46
[listener_average-3] [INFO] [1703741659.612795787] [listener_average]: Listen_average: 52
[listener_average-3] [INFO] [1703741660.112616791] [listener_average]: Listen_average: 52
[listener_average-3] [INFO] [1703741660.613740325] [listener_average]: Listen_average: 47
[listener_average-3] [INFO] [1703741661.113692071] [listener_average]: Listen_average: 47
[listener_average-3] [INFO] [1703741661.614213462] [listener_average]: Listen_average: 53
[listener_average-3] [INFO] [1703741662.114027407] [listener_average]: Listen_average: 55
                          .
                          .
                          .
```

## launchを使って実行する場合
### talk_listen.launch.py
ターミナルで次のコマンドを実行する．
```
$ ros2 launch mypkg talk_listen.launch.py
```
* 表示例:
次のような表示がされる．
```
[listener-2] [INFO] [1703742583.420727471] [listener]: Listen: 0
[listener-2] [INFO] [1703742583.913882258] [listener]: Listen: 1
[listener-2] [INFO] [1703742584.414334535] [listener]: Listen: 2
[listener-2] [INFO] [1703742584.914358592] [listener]: Listen: 3
[listener-2] [INFO] [1703742585.413914346] [listener]: Listen: 4
[listener-2] [INFO] [1703742585.914636470] [listener]: Listen: 5
[listener-2] [INFO] [1703742586.414317193] [listener]: Listen: 6
[listener-2] [INFO] [1703742586.915439958] [listener]: Listen: 7
[listener-2] [INFO] [1703742587.414270776] [listener]: Listen: 8
[listener-2] [INFO] [1703742587.915263867] [listener]: Listen: 9
[listener-2] [INFO] [1703742588.415341537] [listener]: Listen: 10
[listener-2] [INFO] [1703742588.915387408] [listener]: Listen: 11
                          .
                          .
                          .
```
### random_average.launch.py
ターミナルで次のコマンドを実行する．
```
$ ros2 launch mypkg talk_listen.launch.py
```
* 表示例:
次のような表示がされる．
```
[listener_average-3] [INFO] [1703742801.150613060] [listener_average]: Listen_average: 42
[listener_average-3] [INFO] [1703742801.640017629] [listener_average]: Listen_average: 57
[listener_average-3] [INFO] [1703742802.141153465] [listener_average]: Listen_average: 51
[listener_average-3] [INFO] [1703742802.640023652] [listener_average]: Listen_average: 45
[listener_average-3] [INFO] [1703742803.140174406] [listener_average]: Listen_average: 36
[listener_average-3] [INFO] [1703742803.640198703] [listener_average]: Listen_average: 46
[listener_average-3] [INFO] [1703742804.141056168] [listener_average]: Listen_average: 46
[listener_average-3] [INFO] [1703742804.639158912] [listener_average]: Listen_average: 50
[listener_average-3] [INFO] [1703742805.139810696] [listener_average]: Listen_average: 45
[listener_average-3] [INFO] [1703742805.640461889] [listener_average]: Listen_average: 45
[listener_average-3] [INFO] [1703742806.140539148] [listener_average]: Listen_average: 46
[listener_average-3] [INFO] [1703742806.640725931] [listener_average]: Listen_average: 43
[listener_average-3] [INFO] [1703742807.140786713] [listener_average]: Listen_average: 42
[listener_average-3] [INFO] [1703742807.639774204] [listener_average]: Listen_average: 46
[listener_average-3] [INFO] [1703742808.140784930] [listener_average]: Listen_average: 54
                          .
                          .
                          .
```

## 必要なソフトウェア
* Python3
 * テスト済み: Python3.8.10
* ROS 2

## テスト環境
* Ubuntu 20.04
* Ubuntu 22.04
* ROS 2 Foxy
* ROS 2 Humble

## LICENSE
* このソフトウェアパッケージは．３条項BSDライセンスの下，再配布および使用が許可されます．
* このパッケージの一部コードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Masato Aita
