#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���ľ����ξ�ɽ
���ڣ�2020/11/22
"""
import random  #����randomģ��
computer_choice=random.randint(0,4)
def name_to_number(name):
    if name=="ʯͷ":
        name=0
    elif name=="ʷ����":
        name=1
    elif name=="ֽ":
        name=2
    elif name=="����":
        name=3
    elif name=="����":
        name=4
    return name
def number_to_name(number):
    if number==0:
        number='ʯͷ'
    elif number==1:
        number='ʷ����'
    elif number==2:
        number='ֽ'
    elif number==3:
        number='����'
    elif number==4:
        number='����'
    return number
def rpsls(player_choice):
    i=name_to_number(player_choice)
    if i==0:
        if computer_choice==1 or 2:
            print('�����Ӯ��')
        elif computer_choice==3 or 4:
            print('��Ӯ��')
        elif computer_choice==0:
            print('���ͼ��������һ����')
    elif i==1:
        if computer_choice==3 or 2:
            print('�����Ӯ��')
        elif computer_choice==0 or 4:
            print('��Ӯ��')
        elif computer_choice==1:
            print('���ͼ��������һ����')
    elif i==2:
        if computer_choice==3 or 4:
            print('�����Ӯ��')
        elif computer_choice==1 or 0:
            print('��Ӯ��')
        elif computer_choice==2:
            print('���ͼ��������һ����')
    elif i==3:
        if computer_choice==0 or 4:
            print('�����Ӯ��')
        elif computer_choice==1 or 2:
            print('��Ӯ��')
        elif computer_choice==3:
            print('���ͼ��������һ����')
    elif i==4:
        if computer_choice==1 or 0:
            print('�����Ӯ��')
        elif computer_choice==2 or 3:
            print('��Ӯ��')
        elif computer_choice==4:
            print('���ͼ��������һ����')
    return
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name in ['����','ʯͷ','ʷ����','ֽ','����']:
    print('����ѡ��Ϊ��',choice_name)
    print('�������ѡ��Ϊ��',number_to_name(computer_choice))
    rpsls(choice_name)
else :
    print('Error: No Correct Name')