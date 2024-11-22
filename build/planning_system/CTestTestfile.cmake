# CMake generated Testfile for 
# Source directory: /home/user_robohub3/catkin_ws/src/moveit_experiments/planning_system
# Build directory: /home/user_robohub3/catkin_ws/build/planning_system
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_planning_system_roslaunch-check_tests_moveit_planning_execution.xml "/home/user_robohub3/catkin_ws/build/planning_system/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/user_robohub3/catkin_ws/build/planning_system/test_results/planning_system/roslaunch-check_tests_moveit_planning_execution.xml.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/user_robohub3/catkin_ws/build/planning_system/test_results/planning_system" "/opt/ros/noetic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/user_robohub3/catkin_ws/build/planning_system/test_results/planning_system/roslaunch-check_tests_moveit_planning_execution.xml.xml\" \"/home/user_robohub3/catkin_ws/src/moveit_experiments/planning_system/tests/moveit_planning_execution.xml\" ")
set_tests_properties(_ctest_planning_system_roslaunch-check_tests_moveit_planning_execution.xml PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/roslaunch/cmake/roslaunch-extras.cmake;66;catkin_run_tests_target;/home/user_robohub3/catkin_ws/src/moveit_experiments/planning_system/CMakeLists.txt;10;roslaunch_add_file_check;/home/user_robohub3/catkin_ws/src/moveit_experiments/planning_system/CMakeLists.txt;0;")
subdirs("gtest")
