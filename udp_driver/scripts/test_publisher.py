#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from udp_msgs.msg import UdpPacket


class UdpTestPublisher(Node):

    def __init__(self):
        super().__init__('udp_test_publisher')
        self.publisher_ = self.create_publisher(UdpPacket, '/udp_write', 10)
        timer_frequency = 10 # Hz
        timer_period = 1/timer_frequency  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        udp_packet = UdpPacket()
        udp_packet.data = []
        for i in range(24):
            udp_packet.data.append(int(0))

        udp_packet.data[0] = int(10)
        udp_packet.data[1] = int(10)

        self.publisher_.publish(udp_packet)
        self.get_logger().info('Publishing udp packet')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = UdpTestPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()