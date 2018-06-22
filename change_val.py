import os

def get_filename(path):
    files = os.listdir(path)
    files = map(lambda x : path + '\\' + x, files)
    files = list(files)
    return files


def deal_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        contents = []
        for line in lines:
            con = deal_line(line)

            print(con)
            contents.append(con)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("".join(contents))


def deal_line(line):
    temp = deal_zhushi(line)
    if temp:
        vars, var_zhushi = temp
    else:
        vars = line
        var_zhushi = '\n'

    a = change_setval(vars, var_zhushi)
    if not a:
        b = change_getval(vars, var_zhushi)
        if b:
            return b ## getval内容
        else:
            return line  ## 原样返回
    else:
        return a ##发现是set_val

#替换 set_val
def change_setval(vars, var_zhushi):
    num = get_space(vars)
    varslist = vars.split()
    if len(varslist) == 2:
        var1 = varslist[0]
        var2 = varslist[1]
        print(var1)
        if var1[:8] == 'set_val(':
            name1 = var1[9:-2]  #获得变量名
            name2 = var2[:-1]
            res = " " * num + "V_global.{0} = {1}".format(name1, name2) + var_zhushi
            print(res)
            return res
    return None

def get_space(vars):
    num = 0
    for v in vars:
        if v ==' ':
          num += 1
        else:
            break
    return num


#替换  get_val
#url_nodianxin = get_val('url_nodianxin')
def change_getval(vars, var_zhushi):
    num = get_space(vars)
    varslist = vars.split()
    if len(varslist) >= 3:
        var1 = varslist[0]
        var2 = varslist[1]
        var3 = varslist[2]
        if var3[:8] == 'get_val(':
            name1 = var1
            name2 = var3[9:-2]
            print(name1, name2)
            res = " " * num + "{0} = V_global.{1}".format(name1, name2) + var_zhushi
            print(res)
            return res
    return None

def deal_zhushi(vars):
    vars = vars.split('#')
    if len(vars) > 1:
        var1 = vars[0]
        var2 = ' ##' + vars[-1]
        print(var1, var2)
        return (var1, var2)
    return None


if __name__ == '__main__':
    # a = "            set_val('guopai_dianxin', False)"
    # change_setval(a, '智能出价')
    #
    # b = "                smartprice_chujia = get_val('smartprice_chujia')  ##智能出价"
    # change_getval(b, '智能出价')
    # files = get_filename('.\\need_change')
    files = get_filename('.\\nedd')
    print(files)
    for filename in files:
        deal_file(filename)
    # print(get_space("   434  55"))