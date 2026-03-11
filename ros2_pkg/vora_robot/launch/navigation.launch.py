import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    vora_robot_dir = get_package_share_directory('vora_robot')

    map_yaml_file = os.path.join(vora_robot_dir, 'config', 'my_map.yaml')
    nav2_params_file = os.path.join(vora_robot_dir, 'config', 'nav2_params.yaml')

    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
            'map': map_yaml_file,
            'params_file': nav2_params_file
        }.items()
    )

    ld = LaunchDescription()
    ld.add_action(nav2_bringup_launch)

    return ld