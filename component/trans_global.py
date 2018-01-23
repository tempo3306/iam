# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 16:53
'''
globalval = []

#获取global变量列表
def getglobalval(filename):
    vals = set()
    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        for content in contents:
            con = content.split()
            if con:
                if con[0] == "global":
                    con2 = con[1:]
                    con3 = "".join(con2).split(",")  # 去掉global
                    for element in con3:
                        element = element.split('#')[0]
                        vals.add(element)  # 加入到变量集合中
    val1 = list(vals)
    return val1
#获取空格数量
def get_space(val):
    num = 0
    for v in val:
        if v == ' ':
            num+=1
        else:
            break
    return num

def trans_setval(filename, newname):
    newcontent = []
    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        for content in contents:
            con = content.split()
            if con:
                if con[0] in globalval:
                    num = get_space(content)
                    new1 = "set_val('{0}',{1})".format(con[0],con[2])
                    con[0] = new1
                    con[1] = ' '
                    con[2] = ' '
                    new2 = " "*num + "".join(con)+"\n"
                    newcontent.append(new2)
                else:
                    newcontent.append(content)

    with open(newname, 'w', encoding="utf-8") as file:
        file.write("".join(newcontent))

def trans_getval(filename, newname):
    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        finalcontent = []
        for content in contents:
            co = content.split("#")[0]  #去注释
            print(co)
            con = co.split()
            if con:
                if con[0] == 'global':
                    newcontent = []
                    num = get_space(content)
                    con2 = con[1:]
                    con3 = "".join(con2).split(",")  # 去掉global
                    for val in con3:
                        new1 =" "*num + "{0} = get_val('{0}')".format(val) + '\n'
                        newcontent.append(new1)
                    new2 = "".join(newcontent)
                    finalcontent.append(new2)
                else:
                    finalcontent.append(content)
    with open(newname,'w',encoding='utf-8') as file:
        file.write("".join(finalcontent))


globalval = getglobalval('OperationFrame.py')
print(globalval)
trans_setval('OperationFrame.py',"new.py")
trans_getval('new.py','final.py')