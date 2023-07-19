import os
from launch import LaunchDescription 
from launch_ros.actions import Node 
from ament_index_python import get_package_share_directory


def generate_launch_description():
     
    config = os.path.join(
        get_package_share_directory('udp_driver'),
        'params',
        'udp_params.yaml'
        )

    return LaunchDescription([
        Node(
            package='udp_driver',
            executable='udp_bridge_node_exe',
            name='udp_bridge_node',
            parameters=[
                config,
            ]
        )
    ])