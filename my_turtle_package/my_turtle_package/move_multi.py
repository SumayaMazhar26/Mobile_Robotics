import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MultiPatternController(Node):
    def __init__(self):
        super().__init__('multi_pattern_controller')
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)
        
        # Timer runs 10 times per second (0.1s)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.timer_count = 0

    def timer_callback(self):
        self.timer_count += 1
        
        # --- TURTLE 1: PERFECT CIRCLE ---
        t1 = Twist()
        t1.linear.x = 1.5
        t1.angular.z = 1.0
        self.pub1.publish(t1)

        # --- TURTLE 2: SQUARE (90 degree turns) ---
        # Cycle of 40 (20 counts move, 20 counts turn)
        t2 = Twist()
        if (self.timer_count % 40) < 20:
            t2.linear.x = 1.0  # Move
            t2.angular.z = 0.0
        else:
            t2.linear.x = 0.0
            t2.angular.z = 0.785 # Turn (adjusting speed for 2 seconds)
        self.pub2.publish(t2)

        # --- TURTLE 3: TRIANGLE (120 degree turns) ---
        # Cycle of 50 (25 counts move, 25 counts turn)
        t3 = Twist()
        if (self.timer_count % 50) < 25:
            t3.linear.x = 1.0
            t3.angular.z = 0.0
        else:
            t3.linear.x = 0.0
            t3.angular.z = 0.838 # 120 degrees over 2.5 seconds
        self.pub3.publish(t3)

def main(args=None):
    rclpy.init(args=args)
    node = MultiPatternController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()