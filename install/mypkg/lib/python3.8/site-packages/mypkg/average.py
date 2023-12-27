import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("average")
pub = node.create_publisher(Int16, "numbers_average", 10)
numbers = []

def cb(msg):
    global numbers 
    numbers.append(msg.data)
    if len(numbers) > 10:
        del numbers[0]
    msg.data = int(sum(numbers) / len(numbers))
    pub.publish(msg)

sub = node.create_subscription(Int16, "random", cb, 10)
rclpy.spin(node)
