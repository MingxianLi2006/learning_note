#!/usr/bin/env python3
#shopping_cart={"Meta80":{"price":6999,"num":2},"鼠标":{...}...}
'''
1.user upload the name,price and number of the goods according to the tips
save the information of the goods in the shopping cart
2.ask user to input the goods' name in the shopping cart that need to be
modified.
change the information of the goods when finished
3.ask user to delete the name of shopping carts, delete the goods of the
shopping cart according to the name
4.show the information of goods in the shopping cart,
in that form: "name_of_the_goods:xxx,price_of_the_goods:xxx,the number of the goods:xxx"
5.exit
'''
menu='''
\t\t  购物车系统 
#\t\t1. 添加购物车\t\t#
#\t\t2. 修改购物车\t\t#
#\t\t3. 删除购物车\t\t#
#\t\t4. 查询购物车\t\t#
#\t\t5. 推出购物车\t\t#
'''
shopping_cart={}
while True:
	print(menu)
	ope=input("请选择要执行的操作（1-5）：")
	match ope:
		case "1":
				key=input("请输入商品名称：")
			if key in shopping_cart:
				print("商品已存在，请重新输入")
			else:
				price=float(input("请输入商品的价格："))
				num=int(input("请输入商品的数量："))
				shopping_cart[key]={"price":price,"num":num}
				print("商品信息已添加成功")
		case "2":
			key=input("请输入要修改的商品的名称：")
			if key not in shopping_cart:
				print("商品不存在，请重新输入")
			else:
				price=int(input("请输入商品的价格："))
				num=int(input("请输入商品的数量："))
				shopping_cart[key]={"price":price,"num":num}
				print("商品信息已修改成功")
		case "3":
			key=input("请输入商品名称：")
			if key in shopping_cart:
				del shopping_cart[key]
			else:
				print("商品不存在，请重新输入")
		case "4":
			for i,j in shopping_cart.items():
				print(f"商品名称：{i}\t商品价格：{j}['price']\t商品数量：{j['num']}")
		case "5":
			print("已退出购物车，欢迎下次光临")
			break
		case _:
			print("您输入的数字不正确，请重新输入")

'''
case 4
another method
for goods_name in shopping_cart.keys():
	goods_info=shopping_cart[goods_name]
	print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info{'num'}}")
'''
