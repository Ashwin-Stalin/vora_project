# VORA
VORA - Voice Operated Robotic Assistant

## Setup
1. Copy the `vora_project` folder into the `src` folder of your workspace.
2. Run this command to install dependencies.
    ```bash
    rosdep install --from-paths src --ignore-src -r -y
    ```
3. Build the package using `colcon build`.

## Working

1. Run the below commands in the seperate terminal.

    `Terminal 1`

    ```bash
    ros2 launch vora_robot gz_sim.launch.py 
    ```

    `Terminal 2`

    ```bash
    ros2 launch vora_robot rviz.launch.py 
    ```

    `Terminal 3 `

    ```bash
    ros2 launch vora_robot navigation.launch.py
    ```
2. Now go to rviz 
    - change the fixed frame to `map`
    - Click on `2D Pose Estimate` and mark the estimated position and orientation of the robot.
3. Now click on `2D Goal Pose` and mark the goal position and orientation of the robot.