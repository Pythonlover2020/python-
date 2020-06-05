import os,webbrowser,importlib,re

def install(name):
    with open('url.txt','r') as f2:
        url = f2.read()
    with open('path.txt', 'r') as f:
        path = r'%s' % f.read()
    os.system(f'cd {path}')
    choose = input('请选择pip/pip3/pip2安装：')
    if choose == 'pip':
        b = os.system(f'pip install {name}')
        return b
    elif choose == 'pip2':
        b = os.system(f'pip2 install {name}')
        return b
    else:
        b = os.system(f'pip3 install {name} -i {url}')
        return b

def uninstall(name):
    a = os.system(f'pip uninstall {name}')
    return a

def find(name):
    try:
        importlib.import_module(name)
    except ModuleNotFoundError:
        print(f'未找到{name}库，是否为您安装？')
        flag = input('y/n>')
        flag = (flag == 'y')
        if flag:
            install(name)
        else:
            pass
    else:
        print('该库已存在，是否删除？')
        flag = input('y/n>')
        flag = (flag == 'y')
        if flag:
            uninstall(name)
        else:
            pass

while True:
    print('---------------------------------\n1.下载\n2.删除\n3.退出\n4.换源（永久）\n5.查找库\n6.创建虚拟环境\n---------------------------------')
    a = eval(input('请选择：'))
    if a == 1:
        name = str(input('请输入库名：'))
        if name == '__back_':
            continue
        else:
            test = install(name)
            if test:
                print('\n---------------------------------\n安装失败，是否为您查找帮助？\n---------------------------------')
                flag = input('y/n>')
                flag = (flag == 'y')
                if flag:
                    webbrowser.open(
                        url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd={}&fenlei=256&rsv_pq=8fcbd12d0002f908&rsv_t=41143LU%2BHE1dlk%2FdNBE6Gwi4l1fTUyytc%2BpuzjvEM%2FeZQAfX0F%2FBmS0zuic&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=18&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=9860&rsv_sug4=14698'.format(
                            f'pip安装{name}失败解决方案'),
                        new=0,
                        autoraise=True)
            else:
                print('\n---------------------------------\n安装成功\n---------------------------------')
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
        f = os.popen('set')
        path = r'%s' % re.findall('USERPROFILE=(.*?)\n',f.read())
        os.chdir(path)
        os.mkdir('pip')
        os.chdir('pip')
        with open('pip.ini','w') as f:
            text = f'''[global]
index-url = {input('请输入要更换的网址：')}
[install]
trusted-host=pypi.douban.com
'''
            f.write(text)
        print('成功！')
    elif a == 3:
        break
    elif a == 5:
        name = input('请输入库名：')
        if name == '__back_':
            continue
        else:
            find(name)
    elif a == 6:
        version = input('请选择python版本（python3/python2）：')
        try:
            import virtualenv
            virtualenv_path = input('请输入项目路径：')
            os.chdir(virtualenv_path)
            os.system(f'virtualenv venv -p {version}')
            print('\n---------------------------------\n成功！\n---------------------------------')
        except ModuleNotFoundError:
            pip_version = input('请选择（pip/pip2/pip3）：')
            print('正在为您安装相关依赖。。。')
            x = os.system(f'{pip_version} install virtualenv')
            virtualenv_path = input('请输入项目路径：')
            os.chdir(virtualenv_path)
            os.system(f'virtualenv venv -p {version}')
            print('\n---------------------------------\n成功！\n---------------------------------')
    else:
        print('......')