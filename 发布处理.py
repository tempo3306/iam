# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/9 11:05
'''
import re,random,os
filename="Iambest5.0.py"  ##文件名
newname="Iambest5.0_1.py"  ##文件名

target_list=["Position_frame",'strategy','refresh','guopai','chujia','tijiao','lowestprice'
    ,'real_time','one_time','yanzhengma','imgpos','findpos','a_time'
             ]

#获取variable.py中的变量名
def get_vars(file):
    with open(file, 'r', encoding='utf-8') as fil:
        vars = []
        lines = fil.readlines()
        for line in lines:
            l1 = line.split()
            if l1:
                l3 = l1[0].split('(')
                if l3[0].strip() == 'set_val':
                    tem = l3[1][1:-2]
                    if len(tem)>6:
                        vars.append(tem)
    return vars


#获取所有文件名
def get_filename(path):
    names = os.listdir(path)
    new = ['.//component//'+name for name in names]
    new = filter(lambda x : os.path.isfile(x), new)
    a = list(new)
    return a


###去空行
def delete_n(filename,newname):
    f = open(filename, 'r',encoding="utf-8")
    f2 = open(newname, 'w',encoding="utf-8")
    line = f.readlines()
    f.seek(0)
    for l in line:
        temp= l.split()
        if temp:
            f2.write(l)
    f.close()
    f2.close()

###去注释
def delete_help(filename):
    newname = "tem.py"
    delete_n(filename, newname)
    f = open(filename, 'r',encoding="utf-8")
    f2 = open(newname, 'w',encoding="utf-8")
    line = f.readlines()
    f.seek(0)
    for l in line:
        temp = l.strip()
        if len(temp)!=0:
            for i in range(len(l)):
                if l[i]=='#':
                    l=l[:i]+' '*(len(l)-i-1) +'\n'
                    break
            f2.write(l)
    f.close()
    f2.close()
    with open(newname, 'r', encoding="utf-8") as fil:
        content = fil.readlines()
        result = "".join(content)
    with open(file, 'w', encoding="utf-8") as fil:
        fil.write(result)


def randval():
    vl = ['o','0']
    result = ["o"]
    for i in range(20):
        val = random.choice(vl)
        result.append(val)
    return "".join(result)  #返回结果集

def getnewval():
    valset = set()
    for i in range(1000):
        temp = randval()
        valset.add(temp)
    return list(valset)

def getdefval(newname):
    vals = set()
    with open(newname, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        for content in contents:
            con = content.split()
            if con:
                if con[0] == "def":
                    con2 = con[1:]
                    con3 = "".join(con2).split("(")  #  左括号隔开
                    if len(con3[0])>= 8 and con3[0] != "__init__":
                        vals.add(con3[0])  # 加入到变量集合中
    return list(vals)

def getglobalval(newname):
    vals = set()
    with open(newname, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        for content in contents:
            con = content.split()
            if con:
                if con[0] == "global":
                    con2 = con[1:]
                    con3 = "".join(con2).split(",")  # 去掉global
                    for element in con3:
                        if len(element) >= 7:
                            vals.add(element)  # 加入到变量集合中
    val1 = list(vals)
    val2 = getdefval(newname)
    val1.extend(val2)
    return val1




def hunxiao(newvals,vals,file):
    with open(file, 'r', encoding='utf-8') as fil:
        lines = fil.readlines()
        result = "".join(lines)
        print(result)
        for i in range(len(vals)):
            reobj= re.compile(vals[i])
            result, number = reobj.subn(newvals[i], result)
    with open(file, 'w', encoding='utf-8') as fil:
        fil.write(result)

#去注释

if __name__ == '__main__':
    #获取文件名
    filenames = get_filename('.//component')
    print(filenames)

    filenames.append('Newlife1.0.py')
    #获取变量名
    vars = get_vars('.//component//variable.py')
    defvars = []
    for file in filenames:
        var = getdefval(file)
        defvars.extend(var)

    #获取所有需要处理的变量名
    vars.extend(defvars)

    #得到一个SET，去重
    setvar = set(vars)
    #最终到的LIST
    finalvars = list(setvar)
    #获取乱码LIST
    newvars = getnewval()

    ###处理
    #去注释
    print(filenames)
    for file in filenames:
        delete_help(file)
        hunxiao(newvars, finalvars, file)




