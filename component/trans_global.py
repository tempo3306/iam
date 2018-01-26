# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/22 16:53
'''

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

def trans_setval(filename, newname ,globalval):
    newcontent = []
    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        for content in contents:
            co = content.split("#")  #去注释
            con = co[0].split()
            co2= "".join(co[1:]).strip() #注释部分
            if con:
                if con[0] in globalval:
                    num = get_space(content)
                    temp = "".join(con[2:])
                    new1 = "set_val('{0}',{1})".format(con[0],temp)
                    if co2:
                        new2 = " "*num + new1 +"  #"+co2 +"\n"
                    else:
                        new2 = " "*num + new1 + "\n"
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

def total(filename):
    globalval = getglobalval(filename)
    newname = 'new'+filename
    finalname = 'final'+filename
    trans_setval(filename,newname,globalval)
    trans_getval(newname,finalname)

# total("OperationFrame.py")
# total("staticmethod.py")
# total("imgcut.py")
# total("app_thread.py")
total("TopFrame_backup.py")