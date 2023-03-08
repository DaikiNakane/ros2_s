#!/usr/bin/python3
# SPDX-FilecopyrightText: 2023 Daiki Nakane
# SPDX-License-Identifier: GPL-3.0
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
          
                      
def generate_launch_description():
                                              
    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )
                                                            
    return launch.LaunchDescription([talker, listener])
