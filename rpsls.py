#coding:gbk
"""
程序目的：完成一个游戏
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：付子萌
日期：2020/11/20
"""
import random
def name_to_number(name):#将name与number对应起来，以便于后续比较
    if name=='石头':
        return 0
    elif name=='史波克':
        return 1
    elif name=='布':
        return 2
    elif name=='蜥蜴':
        return 3
    elif name=='剪刀':
        return 4
    else:
        return "Error: No Correct Name"
    return
def number_to_name(number):#再将number重新对应到name上，方便输出
    if number==0:
        return '石头'
    elif number==1:
        return '史波克'
    elif number==2:
        return '布'
    elif number==3:
        return '蜥蜴'
    elif number==4:
        return '剪刀'
    else:
        print("Error: No Correct Name")
    return
def rpsls(player_choice):#定义函数，规定游戏规则，我用的是数字比较，将number对应到name上，再通过罗列情况，将游戏规则表达
    s=name_to_number(player_choice)
    if s=='Error: No Correct Name':#这个if函数应用是我觉得自己比较好的一次应用，通过if，else的双层嵌套，中断了后续程序运行，原本我的程序是在50行运用elif输出错误值，我觉得不如在这里中断。
        print("Error: No Correct Name")
    else:
        print('------')
        print("您的选择为："+player_choice)
        x=random.randint(0,5)#让计算机随机取0~4任意一个数
        y=number_to_name(x)  #再把这个数对应到name上，方便输出
        print("计算机的选择为："+y)
        if (s==0 and (x==4 or x==3)) or (s==1 and (x==4 or x==0)) or (s==2 and (x==0 or x==1)) or (s==3 and (x==1 or x==2)) or (s==4 and (x==2 or x==3)):#规则
            print("您赢了！")
        elif s==x:
            print("您和计算机出的一样呢")
        else:
            print("计算机赢了")
    return s
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)



