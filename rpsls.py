#coding:gbk
"""
����Ŀ�ģ����һ����Ϸ
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/11/20
"""
import random
def name_to_number(name):#��name��number��Ӧ�������Ա��ں����Ƚ�
    if name=='ʯͷ':
        return 0
    elif name=='ʷ����':
        return 1
    elif name=='��':
        return 2
    elif name=='����':
        return 3
    elif name=='����':
        return 4
    else:
        return "Error: No Correct Name"
    return
def number_to_name(number):#�ٽ�number���¶�Ӧ��name�ϣ��������
    if number==0:
        return 'ʯͷ'
    elif number==1:
        return 'ʷ����'
    elif number==2:
        return '��'
    elif number==3:
        return '����'
    elif number==4:
        return '����'
    else:
        print("Error: No Correct Name")
    return
def rpsls(player_choice):#���庯�����涨��Ϸ�������õ������ֱȽϣ���number��Ӧ��name�ϣ���ͨ���������������Ϸ������
    s=name_to_number(player_choice)
    if s=='Error: No Correct Name':#���if����Ӧ�����Ҿ����Լ��ȽϺõ�һ��Ӧ�ã�ͨ��if��else��˫��Ƕ�ף��ж��˺����������У�ԭ���ҵĳ�������50������elif�������ֵ���Ҿ��ò����������жϡ�
        print("Error: No Correct Name")
    else:
        print('------')
        print("����ѡ��Ϊ��"+player_choice)
        x=random.randint(0,5)#�ü�������ȡ0~4����һ����
        y=number_to_name(x)  #�ٰ��������Ӧ��name�ϣ��������
        print("�������ѡ��Ϊ��"+y)
        if (s==0 and (x==4 or x==3)) or (s==1 and (x==4 or x==0)) or (s==2 and (x==0 or x==1)) or (s==3 and (x==1 or x==2)) or (s==4 and (x==2 or x==3)):#����
            print("��Ӯ�ˣ�")
        elif s==x:
            print("���ͼ��������һ����")
        else:
            print("�����Ӯ��")
    return s
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)



