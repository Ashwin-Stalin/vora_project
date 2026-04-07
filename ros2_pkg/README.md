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

## To create a map for new world

1. Change the world file.
2. Run the below commands in the seperate terminal.
    `Terminal 1`

    ```bash
    ros2 launch vora_robot gz_sim.launch.py 
    ```
    
    `Terminal 2` - Make sure run it before rviz

    ```bash
    ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/vora_robot/config/slam_params.yaml use_sim_time:=true 
    ```
    
    `Terminal 3`
    ```bash
    ros2 launch vora_robot rviz.launch.py 
    ```
    
    `Terminal 4` -To navigate the robot around the world.
    ```bash
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
    ```

3. Add `map` by clicking on add by topic on `rviz`.
4. Navigate the world and after gone through all the unmapped area in the world.
5. Save it using the following command.

    ```bash
    ros2 run nav2_map_server map_saver_cli -f my_map --ros-args -p use_sim_time:=true
    ```

## To move robot to Class A or B by terminal

1. Change permission to `deliver.py` which is in folder `scripts`
    ```bash
    chmod +x deliver.py
    ```

2. Now run the file
    ```bash
    python deliver.py
    ```