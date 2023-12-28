# SPDX-FileCopyrightText: 2023 Masato Aita
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


def cb(msg):
    global node
    node.get_logger().info("Listen_average: %d" % msg.data)

rclpy.init()
node = Node("listener_average")
pub = node.create_subscription(Int16, "numbers_average", cb, 10)
rclpy.spin(node)
