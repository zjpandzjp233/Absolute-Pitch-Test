# Absolute Pitch Test: Sound Playback and Note Name Response Trainer
# This module plays a sound, and the user responds with the name of the note heard.

# 安装所需的库（在命令行中运行）
# pip install pygame

# 导入所需的库
import pygame
import time
import random
import os
from time import sleep
import platform

operating_system = platform.system() 
def clear_console():
    # 获取操作系统类型
    # 根据操作系统类型选择清屏命令
    if operating_system == "Windows":
        os.system("cls") 
    elif operating_system in ["Linux", "Darwin"]:  # Darwin 是 macOS 的内核名称
        os.system("clear") 
    else:
        print("不支持的操作系统")

def load_audio(file_path):
    """ 加载音频文件 """
    return pygame.mixer.Sound(file_path)

# 按键名字，和音频对应
Piano_keys_list=['A0', 'A0s', 'B0', 'C1', 'C1s', 'D1', 'D1s', 'E1', 'F1', 'F1s', 'G1',
'G1s', 'A1', 'A1s', 'B1', 'C2', 'C2s', 'D2', 'D2s', 'E2', 'F2', 'F2s', 'G2', 'G2s', 
'A2', 'A2s', 'B2', 'C3', 'C3s', 'D3', 'D3s', 'E3', 'F3', 'F3s', 'G3', 'G3s', 'A3', 'A3s', 
'B3', 'C4', 'C4s', 'D4', 'D4s', 'E4', 'F4', 'F4s', 'G4', 'G4s', 'A4', 'A4s', 'B4', 'C5', 'C5s', 
'D5', 'D5s', 'E5', 'F5', 'F5s', 'G5', 'G5s', 'A5', 'A5s', 'B5', 'C6', 'C6s', 'D6', 'D6s', 'E6', 'F6', 
'F6s', 'G6', 'G6s', 'A6', 'A6s', 'B6', 'C7', 'C7s', 'D7', 'D7s', 'E7', 'F7', 'F7s', 'G7', 'G7s', 'A7', 'A7s', 'B7', 'C8']
# 生成所有琴键名称列表
# list1=['C','Cs','D','Ds','E','F','Fs','G','Gs','A','As','B']
# list2=[1,2,3,4,5,6,7]
# list_total=["A0","A0s","B0"]
# i=1
# while i<=7:
#     for one in list1:
#         if len(one)==2:
#             one=one.replace("s",str(i))
#             one+='s'
#             list_total.append(one)
#         else :
#             list_total.append(one+str(i))
#     i+=1
# list_total.append("C8")
# print(list_total)
# print(len(list_total))

#准备好所有音频文件放入不同轨道，然后所有轨道一起播放
def combine_and_play(play_list,slow_play=False,answer=None):
    is_True=False
    channel_list=[]
    int_i=0
    for one in play_list:
        channel_list.append(pygame.mixer.Channel(int_i))
        int_i+=1 # 也表示了通道channel的数目
    if int_i>=3:
        is_True=True
    volume_infact=int_i
    int_2=int_i
    play_buffer=[] # 缓解卡顿 ，先准备齐所有文件，后播放，不然卡
    int_playBuffer=-1
    while not int_i==0:
        back_name=str(play_list[int_i-1])
        file_name_final="钢琴音色WAV/"+back_name+".wav"
        play_buffer.append(load_audio(file_name_final))
        int_playBuffer+=1
        if is_True:
            channel_list[int_i-1].set_volume(2/volume_infact) # 一起播放文件太多，减少些所有文件的音量
        int_i-=1
    while not int_2==0:
        channel_list[int_2-1].play(play_buffer[int_playBuffer])
        int_playBuffer-=1
        if slow_play:
            print("答案是：",end='')
            play_list=sorted(list(play_list),reverse=True)
            print(f"{list_to_keyNameList(play_list)[int_2-1]}")
            time.sleep(0.35)
        int_2-=1
    if is_True:
        is_True=False
        for channel_one in channel_list:
            if not pygame.mixer.get_busy():
                channel_one.set_volume(1) # 如果音量之前被减少，播放完让音量回到最大音量，虽然好像这个代码没有发挥作用


# 在88个键里随机产生一个指定长度的按键列表，且生成的音阶一定程度符合实际情况
def random_list(num):
    num=int(num)
    list1=[]
    counter=1
    if num==1:
        random_80_in_100=random.randint(1,10)
        if random_80_in_100<=8:
            key=random.randint(16,75)
        else:
            key=random.randint(1,88)
        return [key]
    else:
        random_80_in_100=random.randint(1,10)
        if random_80_in_100<=8:
            key=random.randint(16+12,75-12)
        else:
            key=random.randint(1,88)
        top=key+14
        if top>=88:
            top=88
        bottom=key-14
        if bottom<=0:
            bottom=1
        list1.append(key)
        range0=list(range(bottom,top+1))
        while_i=num
        len_range0=len(range0)
        while counter<=while_i:
            key0=random.randint(0,len_range0-1)
            len_range0-=1
            list1.append(range0[key0])
            range0.pop(key0)
            counter+=1
        list1.pop(0)
        list1.sort()
        return list1

# 在指定八度内随机生成指定数目的按键列表
def one_8_range_list(num,which_8_range): #生成几个，第几个八度（1-7）
    num=int(num)
    list1=[]
    counter=1
    num0=int(which_8_range)
    start=(num0-1)*12+4
    top=start+11
    range0=list(range(start,top+1))
    while_i=num
    len_range0=len(range0)
    while counter<=while_i:
        key0=random.randint(0,len_range0-1)
        len_range0-=1
        list1.append(range0[key0])
        range0.pop(key0)
        counter+=1
    list1.sort()
    return list1

# 判断输入与播放列表符合数，按照符合数打分，用户输入顺序无所谓
def is_correct(list_input,list_right):
    right_len=len(list_right)
    bool_1=False
    score=0
    for L in list_input:
        for L2 in list_right:
            if L2==L:
                score+=1
    return score

# 数字（钢琴按键从左往右数的排位） 转 音名 如 1->A0
def list_to_keyNameList(list):
    keyNameList=[]
    for one in list:
        one=int(one)
        keyNameList.append(Piano_keys_list[one-1])
    # print(f"list_to_keyNameList：{keyNameList}")
    return keyNameList

# 对用户输入的格式化
def answer_format(str):
    str=str.replace('，',',')
    return str.split(',')


pygame.mixer.init() #初始化pygame的混音器

#菜单页面  可能做的不是很迅捷
while True:
    clear_console()
    print('模式1：全键88键模式    |    模式2：八度模式')
    print()
    mode=input("请先选择模式（可输入1或2）：")
    if mode=="":
        mode=2
    mode=int(mode)
    if mode==2:
        clear_console()
        print('你选了八度模式，请选择要听第几个C-B，例如：你输入2的话则是选择了C2-B2要听的音。')
        print()
        one_to_seven=input('请选择（可输入1-7）：')
        if one_to_seven=='':
            one_to_seven=4
        clear_console()
        print(f"打算一次从C{one_to_seven}到B{one_to_seven}听几个音？")
        how_much=input()
        if how_much=="":
            how_much=1
        while True:
            clear_console()
            input("开始咯，（按任意键开始）：")
            clear_console()
            play_list=one_8_range_list(how_much,one_to_seven)
            while True:
                combine_and_play(play_list)
                print("按回车可再听一遍，输入 1 结束听音过程，开始填写答案哦。")
                option=input()
                if option=="1":
                    clear_console()
                    break
                clear_console()
            print("答案的格式表示方法，音名加逗号分隔，如：C4,D4,G4,A4s   |   其中s表示#，是sharp的缩写，表示升调。")
            print()
            inputs=input("输入你的答案:")
            clear_console()
            inputs_list=answer_format(inputs)
            score=is_correct(inputs_list,list_to_keyNameList(play_list))
            print(f'你的答案是：    {inputs}    ,总共弹了{how_much}个音，答对{score}个')
            if not score==how_much:
                print()
                input("按任意键看答案：\n")
                combine_and_play(play_list,True,answer=play_list)
                
            else:
                print("厉害！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
            print()
            input("按任意键再玩一次:")
    else:
        clear_console()
        print("在88键里面，我要一次按几个？ (可输入1-8)")
        sound_num=input()
        while True:
            
            if sound_num=="":
                sound_num=1
            play_list2=random_list(sound_num)
            print(f"开始咯，我将播放{sound_num}个键，按任意键开始")
            clear_console()
            while True:
                combine_and_play(play_list2)
                print("按回车可再听一遍，输入 1 结束听音过程，开始填写答案哦。")
                option=input()
                if option=="1":
                    clear_console()
                    break
                clear_console()
            print("答案的格式表示方法，音名加逗号分隔，如：C4,D4,G4,A4s   |   其中s表示#，是sharp的缩写，表示升调。")
            print()
            inputs2=input("输入你的答案:")
            clear_console()
            inputs_list2=answer_format(inputs2)
            score=is_correct(inputs_list2,list_to_keyNameList(play_list2))
            print(f'你的答案是：   {inputs2}   ,总共弹了{sound_num}个音，答对{score}个')
            if not score==sound_num:
                print()
                input("按任意键看答案：\n")
                combine_and_play(play_list2,True,answer=play_list2)
            else:
                print("厉害！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
            print()
            input("按任意键再答一次:")





