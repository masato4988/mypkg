import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class Talker_random():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "random", 10)
        node.create_timer(0.1, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = random.randint(0, 100)
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Node("talker_random")
    talker_random = Talker_random(node)
    rclpy.spin(node)
