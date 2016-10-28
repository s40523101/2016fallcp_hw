data3 = open("w6_group.txt").read()
#data3 = open("w6_list.txt").read()
#print(data3)
group = data3.splitlines()
#print(len(group))

# 希望將分組資料轉為學員數列, 令為變數名稱 result_g
result_g = []
# 已經註冊者數列設為 registered
registered = open("w6_list.txt").read()
registered=registered.splitlines()
#print(registered)
for line in group:
    # 去除每一行最後的空白成員
    sline = line.split(",")[:-1]
    #print(sline)
    # 再將各組拆成個別組員後, 串成 result_g
    for m in sline:
        result_g.append(m)
#print(result_g)
#not_in_group = [c for c in registered if c not in result_g]
#print(not_in_group)
for m in registered:
    if m not in result_g:
        print(m)
