from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Base Link to LiDAR Transform
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.1', '0', '0.15', '0', '0', '0', 'base_link', 'lidar']
        ),
        
        # 2. Base Link to IMU Transform
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.0', '0', '0.05', '0', '0', '0', 'base_link', 'imu_link']
        ),

        # 3. Base Footprint to Base Link (Satisfies SLAM Toolbox)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link']
        ),

        # 4. Laser Odometry
        Node(
            package='rf2o_laser_odometry',
            executable='rf2o_laser_odometry_node',
            name='rf2o_laser_odometry',
            output='screen',
            parameters=[{
                'laser_scan_topic' : '/scan',
                'odom_topic' : '/odom',
                'publish_tf' : True,
                'base_frame_id' : 'base_footprint',  # <--- THIS IS THE FIX
                'odom_frame_id' : 'odom',
                'init_pose_from_topic' : '',
                'freq' : 10.0 
            }]
        )
    ])
