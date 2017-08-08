f = open('Iambest.py', 'r',encoding="utf-8")
f2 = open('BestAssistant.py', 'w',encoding="utf-8")
line = f.readlines()
f.seek(0)
for l in line:
    for i in range(len(l)):
        if l[i]=='#':
            l=l[:i]+' '*(len(l)-i-1)+'\n'
            break
    f2.write(l)
f.close()
f2.close()


#正则表达式替换所有变量
import re


target_list=["Position",'price','strategy','count','confirm','refresh','moni','guopai','chujia','tijiao','second','lowest'
    ,'real_time','one_time'
             ]
result_list=['asd0o0o0o0','zxco0o0o0o0','qwe252148','ghjo0o0o0o0','sdfsf24324297','uioo0o000oo','o0sdofsfo0sodf0so0',
             'ooweo0o0werwr','oo0o0O0O0O0','oOO0O0O0O0O0O0','ooo0O0o0oO0O','O0O0O0O0O0O0O','oO0O0O0O0O0O0O0O0','0O00000o0']


def hunxiao(subject):
    result=subject
    for i in range(len(target_list)):
        reobj= re.compile(target_list[i])
        result, number = reobj.subn(result_list[i], result)

    reobj=re.compile("http://o0sdofsfo0sodf0so0.51hupai.org/")
    result,number=reobj.subn('http://moni.51hupai.org/',result)
    return result

#替换变量名
f3=open('BestAssistant.py','r',encoding='utf-8')
lines=f3.readlines()
f3.seek(0)  #文件指针
lines=''.join(lines)
results=hunxiao(lines)

f4 = open('BestAssistant.py', 'w',encoding="utf-8")
f4.write(results)
f3.close()
f4.close()