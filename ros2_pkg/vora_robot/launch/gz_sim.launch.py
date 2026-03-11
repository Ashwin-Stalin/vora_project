import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
import xacro

def generate_launch_description():
    robotXacroName='robot'
    namePackage='vora_robot'
    modelFilRelativePath='urdf/mobile_robot.xacro'
    pathModelFile = os.path.join(get_package_share_directory(namePackage), modelFilRelativePath)
    robotDescription = xacro.process_file(pathModelFile).toxml()
    gazebo_rosPackageLaunch = PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'))
    world_file = os.path.join(get_package_share_directory(namePackage), 'worlds', 'room.sdf')
    gazeboLaunch = IncludeLaunchDescription(
        gazebo_rosPackageLaunch,
        launch_arguments={
            "gz_args" : f'-r -v 4 {world_file}',
            "on_exit_shutdown": 'true'
        }.items()
    )

    spawnRobotNode = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            "-topic", "robot_description",
            "-name", "robot",
            "-allow_renaming", "false",
            "-z", "0.32",
            "-x", "0.0",
            "-y", "0.0",
            "-Y", "0.0"
        ],            
        output='screen',
    )

    robotStatePublisherNode = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[{'robot_description': robotDescription, 'use_sim_time': True}],
    )

    bridge_params = os.path.join(
        get_package_share_directory(namePackage),
        'config',
        'bridge_parameters.yaml'
    )

    # Bridge ROS topics and Gazebo messages for establishing communication
    start_gazebo_ros_bridge_cmd = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ],
        parameters=[{'use_sim_time': True}],
        output='screen'
      )
    
    launchDescriptionObject = LaunchDescription()
    launchDescriptionObject.add_action(gazeboLaunch)
    launchDescriptionObject.add_action(spawnRobotNode)
    launchDescriptionObject.add_action(robotStatePublisherNode)
    launchDescriptionObject.add_action(start_gazebo_ros_bridge_cmd)

    return launchDescriptionObject
