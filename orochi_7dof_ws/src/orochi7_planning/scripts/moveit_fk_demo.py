#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
# from control_msgs.msg import GripperCommand

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
        
        # 初始化需要使用move group控制的机械臂中的gripper group
        # gripper = moveit_commander.MoveGroupCommander('gripper')
        
        # 设置机械臂和夹爪的允许误差值
        arm.set_goal_joint_tolerance(0.001)
        # gripper.set_goal_joint_tolerance(0.001)
        
        # 设置每次运动规划的时间限制：1s
        arm.set_planning_time(1)

        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(0.5)
         
        # 设置夹爪的目标位置，并控制夹爪运动
        # gripper.set_joint_value_target([0.01])
        # gripper.go()
        # rospy.sleep(0.1)
        
        # ---------------------  第一段轨迹生成，关节空间插值  ---------------------#
        
        # 设置机械臂的目标位置，使用七轴的位置数据进行描述（单位：弧度）
        joint_positions = [-0.867, -0.674, 0.2832, -1.220, -1.273, -1.3, 0]
        arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(0.5)

        # ---------------------  第二段轨迹生成，关节空间插值  ---------------------#

        # 设置机械臂的目标位置，使用七轴的位置数据进行描述（单位：弧度）
        joint_positions = [0.867, 0.674, -0.2832, 1.220, 1.273, 1.2, 0]
        arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(0.5)       
        
        # ---------------------  第三段轨迹生成，关节空间插值  ---------------------#

        # 设置机械臂的目标位置，使用七轴的位置数据进行描述（单位：弧度）
        joint_positions = [0, 0, 0, 0, 0, 0, 0]
        arm.set_joint_value_target(joint_positions)
                 
        # 控制机械臂完成运动
        arm.go()
        rospy.sleep(1)

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
