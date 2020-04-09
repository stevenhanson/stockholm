"""
学生管理系统
"""


def showMenu():
    """
    展示系统功能
    :return: 无
    """
    print('*'*10, '学生管理系统', '*'*10)
    print('1,添加学生信息')
    print('2,修改学生信息')
    print('3,删除学生信息')
    print('4,查询单个学生信息')
    print('5,查询所有学生信息')
    print('*'*34)


def addStu():
    pass


def modifyStu():
    pass


def delStu():
    pass


def showStu():
    pass


def showAllStu():
    pass


if __name__ == '__main__':

    while True:
        showMenu()
        num = int(input('请选择需要操作的功能'))
        if num == 1:
            addStu()
        elif num == 2:
            modifyStu()
        elif num == 3:
            delStu()
        elif num == 4:
            showStu()
        elif num == 5:
            showAllStu()
        elif num == 6:
            print('操作结束，退出系统。')
            break
        else:
            print('你选择的功能不存在，请重新选择。')
