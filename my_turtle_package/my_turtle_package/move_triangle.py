import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TrianglePublisher(Node):
    def __init__(self):
        super().__init__('triangle_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        for i in range(3):  # 3 sides for a triangle
            # Move Forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2)
            
            # Turn 120 degrees
            msg.linear.x = 0.0
            msg.angular.z = 2.09 
            self.publisher_.publish(msg)
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    node = TrianglePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()