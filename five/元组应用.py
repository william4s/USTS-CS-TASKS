menu=("咖喱鸡","辣子鸡","红烧肉","西红柿蛋汤","红烧牛肉","扬州炒饭","酸辣粉","松鼠鳜鱼","狮子头","宫保鸡丁")
print(menu[5],menu[len(menu)-1])
menu=menu[:2]+menu[8:]
print(menu)
menu=menu[0:0]
print(menu)