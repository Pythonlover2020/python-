import os,webbrowser
from termcolor import colored

def install(name):
    with open('url.txt','r') as f2:
        url = f2.read()
    with open('path.txt', 'r') as f:
        path = r'%s' % f.read()
    os.system(f'cd {path}')
    if url == 'https://pypi.org/':
        b = os.system(f'pip install {name}')
        return b
    else:
        b = os.system(f'pip install {name} -i {url}')
        return b

def uninstall(name):
    a = os.system(f'pip uninstall {name}')
    return a

while True:
    print('---------------------------------\n1.下载\n2.删除\n3.退出\n4.设置Scripts路径\n5.换源\n6.手动安装\n---------------------------------')
    a = eval(input('请选择：'))
    if a == 1:
        name = str(input('请输入库名：'))
        if name == '__back_':
            continue
        else:
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
        if name == '__back_':
            continue
        else:
            test = uninstall(name)
            if test:
                print(f'\n---------------------------------\n您好像未安装{name}库。。。\n---------------------------------')
            else:
                print('\n---------------------------------\n删除成功！\n---------------------------------')
    elif a == 4:
        with open('path.txt','w') as f:
            f.write(str(input('请输入Scripts路径：')))
    elif a == 5:
        with open('url.txt','r') as f:
            print(f'您当前使用的是{f.read()}')
            print('为您推荐以下镜像：\n---------------------------------\nhttps://pypi.tuna.tsinghua.edu.cn/simple\t清华镜像\nhttps://pypi.org/\tPython官方\n---------------------------------')
            url = input('请输入(输入back返回)：')
            if url == 'back':
                continue
            else:
                with open('url.txt','w') as x:
                    x.write(url)
            print('设置完成！')
    elif a == 3:
        break
    elif a == 6:
        with open('path.txt','r') as f:
            path = f.read()
        os.system(input(f'{path}>'))
    else:
        print('......')