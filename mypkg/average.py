import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("average")            #ノード作成（nodeという「オブジェクト」を作成）
sub = node.create_subscription(Int16, "random", cb, 10)
pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャのオブジェクト作成
numbers = [] #記録用リスト

def cb():          #17行目で定期実行されるコールバック関数
    global numbers #関数を抜けてもnがリセットされないようにしている
    msg = Int16()  #メッセージの「オブジェクト」
    numbers.append(msg.data)
    if len(numbers) > 10:
        del a[0]
    msg.data = sum(numbers) / len(numbers)   #msgオブジェクトの持つdataにnumbersの平均値を結び付け
    pub.publish(msg)        #pubの持つpublishでメッセージ送信

rclpy.spin(node)            #実行（無限ループ）
