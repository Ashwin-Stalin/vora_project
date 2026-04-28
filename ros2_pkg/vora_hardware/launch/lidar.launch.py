import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # 1. Path to the official Slamtec launch file
    sllidar_launch_path = os.path.join(
        get_package_share_directory('rplidar_ros'),
        'launch',
        'rplidar_a1_launch.py'
    )

    return LaunchDescription([
        # 2. Launch the LiDAR node with custom parameters
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(sllidar_launch_path),
            launch_arguments={
                'serial_port': '/dev/ttyUSB0',  # Change if your port is different
                'frame_id': 'lidar',            # Matches your Vora URDF
                'inverted': 'false',
                'angle_compensate': 'true'
            }.items()
        )
    ])

