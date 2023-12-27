import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

    talker_random = launch_ros.actions.Node(
        package='mypkg',
        executable='talker_random'
        )
    average = launch_ros.actions.Node(
        package='mypkg',
        executable='average'
        )
    listener_average = launch_ros.actions.Node(
        package='mypkg',
        executable='listener_average',
        output='screen',
        )

    return launch.LaunchDescription([talker_random, lverage, istener_average])
