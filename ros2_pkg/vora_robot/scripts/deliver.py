#!/usr/bin/python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseStamped
import sys

def main():
    rclpy.init()
    navigator = BasicNavigator()

    print("Activating Nav2 ...")
    navigator.waitUntilNav2Active()
    print("\nNav2 Activated!")

    # Coordinates
    locations = {
        'Class A': {
            'x': 3.435, 'y': -4.743, 'z': 0.0,
            'qx': 0.0, 'qy': 0.0, 'qz': -0.698, 'qw': 0.715
        },
        'Class B': {
            'x': -5.343, 'y': -4.193, 'z': 0.0,
            'qx': 0.0, 'qy': 0.0, 'qz': -0.666, 'qw': 0.745
        }
    }

    # Simple terminal menu
    print("\n--- Vora Robot Dispatcher ---")
    print("1: Send to Class A")
    print("2: Send to Class B")
    choice = input("Enter 1 or 2 (or q to quit): ")

    if choice == '1':
        target = 'Class A'
    elif choice == '2':
        target = 'Class B'
    elif choice == 'q':
        sys.exit(0)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(0)

    coords = locations[target]

    # Goal Pose message
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    
    # Set position
    goal_pose.pose.position.x = coords['x']
    goal_pose.pose.position.y = coords['y']
    goal_pose.pose.position.z = coords['z']
    
    # Set orientation
    goal_pose.pose.orientation.x = coords['qx']
    goal_pose.pose.orientation.y = coords['qy']
    goal_pose.pose.orientation.z = coords['qz']
    goal_pose.pose.orientation.w = coords['qw']

    print(f"\nSending robot to {target}...")
    navigator.goToPose(goal_pose)

    # printing real-time feedback while robot is moving
    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        if feedback:
            print(f"Estimated time remaining: {feedback.estimated_time_remaining.sec} seconds", end='\r')

    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print(f"\nGoal succeeded! The robot has arrived at {target}.")
    elif result == TaskResult.CANCELED:
        print("\nGoal was canceled.")
    elif result == TaskResult.FAILED:
        print("\n Goal failed! Obstacles might be blocking the path.")

    rclpy.shutdown()

if __name__ == '__main__':
    main()