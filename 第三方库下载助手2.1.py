'''请先在path.txt里设置你的Python的Scripts路径'''
import os,webbrowser
from termcolor import colored

with open('path.txt','r') as f:
    path = r'%s' % f.read()

def install(name):
    a = f'pip install {name} -i https://pypi.tuna.tsinghua.edu.cn/simple'
    os.system(f'cd {path}')
    b = os.system(a)
    return b

def uninstall(name):
    a = os.system(f'pip uninstall {name}')
    return a

while True:
    print('1.下载; 2.删除; 3.退出；4.设置Scripts路径')
    a = eval(input('请选择：'))
    if a == 1:
        name = str(input('请输入库名：'))
        test = install(name)
        if test:
            print('\n---------------------------------\n' + colored('安装失败，正在为您查找帮助。。。','red') + '\n---------------------------------')
            webbrowser.open(url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={}&fenlei=256&rsv_pq=8fcbd12d0002f908&rsv_t=41143LU%2BHE1dlk%2FdNBE6Gwi4l1fTUyytc%2BpuzjvEM%2FeZQAfX0F%2FBmS0zuic&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=18&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=9860&rsv_sug4=14698'.format(f'pip安装{name}失败解决方案'),
                            new=0,
                            autoraise=True)
        else:
            print('\n---------------------------------\n' + colored('安装成功','green') + '\n---------------------------------')
    elif a == 2:
        name = str(input('请输入库名：'))
        test = uninstall(name)
        if test:
            print(f'\n---------------------------------\n您好像未安装{name}库。。。\n---------------------------------')
        else:
            print('\n---------------------------------\n删除成功！\n---------------------------------')
    elif a == 4:
        with open('path.txt','w') as f:
            f.write(str(input('请输入Scripts路径：')))
    else:
        break
