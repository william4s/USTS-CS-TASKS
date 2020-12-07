dic = {"王小明":87,"william":99}
fo = open("ans.csv", "w")
for key, value in dic.items():
    fo.write('{},{}\n'.format(key, value))
fo.close()
