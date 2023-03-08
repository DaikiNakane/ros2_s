1 import rclpy
2 from rclpy.node import Node
3 from std_msgs.msg import Int16
4
5 def cb(msg):
6     global node
7     node.get_logger().info("Listen: %d" % msg.data)
8
9 rclpy.init()
10 node = Node("listener")
11 pub = node.create_subscription(Int16, "countup", cb, 10)
12 rclpy.spin(node)  
