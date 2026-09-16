#!/usr/bin/env python3
while True:
	operation=input()
	match operation:
		case "w"|"W":
			print("角色向上移动")
		case "s"|"S":
			print("角色向下移动")
		case "a"|"A":
			print("角色向左移动")
		case "d"|"D":
			print("角色向右移动")
		case " ":
			print("角色跳跃")
		case "j"|"J":
			print("角色发起攻击")
		case "esc"|"ESC":
			print("角色退出游戏")
		case _:
			print("无效操作")
