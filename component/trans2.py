# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/1/25 13:34
'''


def trans_setval(filename, newname):
    newcontent = []
    with open(filename, 'r', encoding="utf-8") as file:
        contents = file.readlines()
        for content in contents:
            co = content.split("#")  # 去注释
            con = co[0].strip().split('=')
            co2 = "".join(co[1:]).strip()  # 注释部分
            if len(con) == 2:
                new1 = "set_val('{0}',{1})".format(con[0].strip(), con[1])
                new3 = "{0} = get_val('{0}')".format(con[0].strip()) + '\n'
                print(new1)
                if co2:
                    new2 = new1 + "  #" + co2 + "\n"
                else:
                    new2 = new1 + "\n"
                newcontent.append(new2)
                newcontent.append(new3)

    with open(newname, 'w', encoding="utf-8") as file:
        file.write("".join(newcontent))


trans_setval("newval.py", "val.py")
