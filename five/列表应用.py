menu=["咖喱鸡","辣子鸡","红烧肉","西红柿蛋汤","红烧牛肉","扬州炒饭","酸辣粉","松鼠鳜鱼","狮子头","宫保鸡丁"]
submenu=["lc1","lc2","lc3","lc4","lc5"]
for i in range(5):
    menu.insert(5,submenu[i])
#menu.insert(5,submenu)
menu.extend(submenu)
menu.sort()
menu.pop(3)
print(menu)
if "红烧肉" in menu:
    print("有红烧肉")
if menu.count("红烧肉")>=1 :
    print("有红烧肉")
    menu.remove("红烧肉")
print(menu)
del menu[2:10]
for i in range(0,len(menu)):
    print("{} ".format(menu[i]),end="")
print()
del menu[0:len(menu)]
print(menu)