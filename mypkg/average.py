import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("average")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Int16, "numbers_average", 10)   #パブリッシャのオブジェクト作成
numbers = [] #記録用リスト

def cb(msg):
    global numbers 
    numbers.append(msg.data)
    if len(numbers) > 10:
        del numbers[0]
    msg.data = int(sum(numbers) / len(numbers))   #msgオブジェクトの持つdataにnumbersの平均値を結び付け
    pub.publish(msg)        #pubの持つpublishでメッセージ送信

sub = node.create_subscription(Int16, "random", cb, 10)
rclpy.spin(node)            #実行（無限ループ）
