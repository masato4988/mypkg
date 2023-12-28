#!/bin/bash
# SPDX-FileCopyrightText: 2023 Masato Aita
# SPDX-Licence-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep 'Listen: 10'

found=0
timeout 10 ros2 launch mypkg random_average.launch.py > /tmp/mypkg.log
if awk '{
		if ($(NF-1) == "Listen_average:") {
			if ($NF >= 0 && $NF <= 100) {
				found = 1
			}
		}
	}
	END { exit !found }' "/tmp/mypkg.log"; then
	echo "random_average.launch.py: OK"
else
	echo "random_average.launch.py: not OK"
fi
