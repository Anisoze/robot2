#!/usr/bin/env python3
import rospy
import random
import moveit_commander
import geometry_msgs.msg
import sys
def generate_pose():
   # Функция для генерации случайной позы
   # Возвращает позицию (x, y, z) и ориентацию (x, y, z, w) в виде списков

	position = [0, 0, 0]
   
	orientation = [0, 0, 0, 0]

	position_hand = [0, 0, 0.0]
   
	orientation_hand = [0, 0, 0, 0]
   
	return position, orientation, position_hand, orientation_hand 
	
def main():
	rospy.init_node('moveit_random_pose', anonymous=True)

	moveit_commander.roscpp_initialize(sys.argv)

	robot = moveit_commander.RobotCommander()

	scene = moveit_commander.PlanningSceneInterface()

	group_arm = moveit_commander.MoveGroupCommander("panda_arm")

	group_hand = moveit_commander.MoveGroupCommander("panda_hand")

	num_random_poses = 5

	for _ in range(1):
		position, orientation, position_hand, orientation_hand  = generate_pose()

		pose_target = geometry_msgs.msg.Pose()
		pose_target.position.x = position[0]
		pose_target.position.y = position[1]
		pose_target.position.z = position[2]
		pose_target.orientation.x = orientation[0]
		pose_target.orientation.y = orientation[1]
		pose_target.orientation.z = orientation[2]
		pose_target.orientation.w = orientation[3]

		pose_target_hand = geometry_msgs.msg.Pose()
		pose_target_hand.position.x = position_hand[0]
		pose_target_hand.position.y = position_hand[1]
		pose_target_hand.position.z = position_hand[2]
		pose_target_hand.orientation.x = orientation_hand[0]
		pose_target_hand.orientation.y = orientation_hand[1]
		pose_target_hand.orientation.z = orientation_hand[2]
		pose_target_hand.orientation.w = orientation_hand[3]

		group_arm.set_pose_target(pose_target)
		group_hand.set_pose_target(pose_target_hand)

		plan = group_arm.plan()
		plan_hand = group_hand.plan()

		if isinstance(plan, tuple):
			success = plan[0]
			trajectory = plan[1]
		else:
			success = True
			trajectory = plan
		if isinstance(plan_hand, tuple):
			success_hand = plan_hand[0]
			trajectory_hand = plan_hand[1]
		else:
			success_hand = True
			trajectory_hand = plan_hand
		
		# if success and len(trajectory.joint_trajectory.points) > 0 and success_hand and len(trajectory_hand.joint_trajectory.points) > 0:
		# 	group_arm.execute(trajectory, wait=True)
		# 	group_hand.execute(trajectory_hand, wait=True)
		# else:
		# 	rospy.logwarn("Планирование не удалось для данной позы.")
		if success_hand and len(trajectory_hand.joint_trajectory.points) > 0:
			group_hand.execute(trajectory_hand, wait=True)
		else:
			rospy.logwarn("Планирование не удалось для данной позы.")
		rospy.sleep(1)

	moveit_commander.roscpp_shutdown()

if __name__ == "__main__":
	main()
