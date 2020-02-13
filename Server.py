from socket import *
import win32api
from random import randrange
from ctypes import Structure, c_short, windll, POINTER
from os import system
from msvcrt import getch
import time
import sys
import ctypes

std_out_handle = windll.kernel32.GetStdHandle(-11)

def textcolor(foreground, background, handle=std_out_handle):
    color = foreground+background*16
    windll.kernel32.SetConsoleTextAttribute(handle, color)

def Pgetch():
    return getch()

def gotoxy(x,y):
    class COORD(Structure):
            _fields_=[("X",c_short),("Y",c_short)]
    windll.kernel32.SetConsoleCursorPosition(win32api.GetStdHandle(win32api.STD_OUTPUT_HANDLE), (COORD(x,y)))

def clear():
    system("cls")

def send(sock, sendData):
    sock.send(sendData.encode('utf-8'))

def send2(sock, sendData):
    sock.send(str(sendData).encode('utf-8'))

def receive(sock):
    recvData = sock.recv(1024)
    return recvData.decode('utf-8')

def receive2(sock):
    recvData = sock.recv(1024)
    recvData.decode('utf-8')
    return int(recvData)

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)
print("오목 대전 게임")
print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

print("흑,백 정하는중 ...")
bw = randrange(1,3)
if bw == 1:
    print("흑돌입니다")
    send(connectionSock, "백돌")
elif bw == 2:
    print("백돌입니다")
    send(connectionSock, "흑돌")
print("3초 뒤 계속 됨")
time.sleep(3)
map = [ #크기 15x15
    [3,7,7,7,7,7,7,7,7,7,7,7,7,7,4],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [10,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
    [5,9,9,9,9,9,9,9,9,9,9,9,9,9,6]
]
turn = 1
trash = "차례"
x, y = 7, 7
win = 0
clear()
while True:
    if bw == 1:
        while True:
            for i in range(0,15,1):
                for j in range(0,15,1):
                    if j < 11:
                        if map[i][j] == 1 and map[i][j+1] == 1 and map[i][j+2] == 1 and map[i][j+3] == 1 and map[i][j+4] == 1: win = 1
                        if map[i][j] == 2 and map[i][j+1] == 2 and map[i][j+2] == 2 and map[i][j+3] == 2 and map[i][j+4] == 2: win = 2
                    if i < 11:
                        if map[i][j] == 1 and map[i+1][j] == 1 and map[i+2][j] == 1 and map[i+3][j] == 1 and map[i+4][j] == 1: win = 1
                        if map[i][j] == 2 and map[i+1][j] == 2 and map[i+2][j] == 2 and map[i+3][j] == 2 and map[i+4][j] == 2: win = 2
                    if i < 11 and j < 11:
                        if map[i][j] == 1 and map[i+1][j+1] == 1 and map[i+2][j+2] == 1 and map[i+3][j+3] == 1 and map[i+4][j+4] == 1: win = 1
                        if map[i][j] == 2 and map[i+1][j+1] == 2 and map[i+2][j+2] == 2 and map[i+3][j+3] == 2 and map[i+4][j+4] == 2: win = 2
                    if i < 11 and j > 3:
                        if map[i][j] == 1 and map[i+1][j-1] == 1 and map[i+2][j-2] == 1 and map[i+3][j-3] == 1 and map[i+4][j-4] == 1: win = 1
                        if map[i][j] == 2 and map[i+1][j-1] == 2 and map[i+2][j-2] == 2 and map[i+3][j-3] == 2 and map[i+4][j-4] == 2: win = 2
            if win == 1:
                system("cls")
                for i in range(0,15,1):
                    for j in range(0,15,1):
                        textcolor(0,6)
                        if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                        elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                        elif map[i][j] == 1: print("●",end='')
                        elif map[i][j] == 2: print("○",end='')
                        elif map[i][j] == 3: print("┌─",end='')
                        elif map[i][j] == 4: print("┐",end='')
                        elif map[i][j] == 5: print("└─",end='')
                        elif map[i][j] == 6: print("┘",end='')
                        elif map[i][j] == 7: print("┬─",end='')
                        elif map[i][j] == 8: print("│",end='')
                        elif map[i][j] == 9: print("┴─",end='')
                        elif map[i][j] == 10: print("├─",end='')
                    print(" ")
                gotoxy(40,10)
                textcolor(0,3)
                print("흑돌 승리 !")
                textcolor(15,0)
                gotoxy(0,16)
                system("pause > nul")
                sys.exit()
            if win == 2:
                clear()
                for i in range(0,15,1):
                    for j in range(0,15,1):
                        textcolor(0,6)
                        if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                        elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                        elif map[i][j] == 1: print("●",end='')
                        elif map[i][j] == 2: print("○",end='')
                        elif map[i][j] == 3: print("┌─",end='')
                        elif map[i][j] == 4: print("┐",end='')
                        elif map[i][j] == 5: print("└─",end='')
                        elif map[i][j] == 6: print("┘",end='')
                        elif map[i][j] == 7: print("┬─",end='')
                        elif map[i][j] == 8: print("│",end='')
                        elif map[i][j] == 9: print("┴─",end='')
                        elif map[i][j] == 10: print("├─",end='')
                    print(" ")
                gotoxy(40,10)
                textcolor(0,3)
                print("백돌 승리 !")
                textcolor(15,0)
                gotoxy(0,16)
                system("pause > nul")
                sys.exit()
            if turn == 1:
                while True:
                    clear()
                    gotoxy(40,5)
                    textcolor(0,3)
                    print("You : ●      ◀")
                    gotoxy(40,6)
                    print("Opponent: ○    ")
                    textcolor(15,0)
                    gotoxy(0,0)
                    for i in range(0,15,1):
                        for j in range(0,15,1):
                            textcolor(0,6)
                            if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                            elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                            elif map[i][j] == 1: print("●",end='')
                            elif map[i][j] == 2: print("○",end='')
                            elif map[i][j] == 3: print("┌─",end='')
                            elif map[i][j] == 4: print("┐",end='')
                            elif map[i][j] == 5: print("└─",end='')
                            elif map[i][j] == 6: print("┘",end='')
                            elif map[i][j] == 7: print("┬─",end='')
                            elif map[i][j] == 8: print("│",end='')
                            elif map[i][j] == 9: print("┴─",end='')
                            elif map[i][j] == 10: print("├─",end='')
                        print(" ")
                    textcolor(15,0)
                    gotoxy(int(x)*2,int(y))
                    kkey = Pgetch()
                    kkey = list(kkey)
                    key = chr(kkey[0])
                    int(x)
                    int(y)
                    if key == 'w' and y > 0: y -= 1
                    elif key == 's' and y < 14: y += 1
                    elif key == 'a' and x > 0: x -= 1
                    elif key == 'd' and x < 14: x += 1
                    elif kkey[0] == 32 and map[y][x] != 1 and map[y][x] != 2: break
                map[y][x] = 1
                send2(connectionSock, x)
                trash = receive(connectionSock)
                send2(connectionSock, y)
                turn += 1
                continue
            if turn == 2:
                clear()
                gotoxy(40,5)
                textcolor(0,3)
                print("You : ●        ")
                gotoxy(40,6)
                print("Opponent: ○  ◀")
                textcolor(15,0)
                gotoxy(0,0)
                for i in range(0,15,1):
                    for j in range(0,15,1):
                        textcolor(0,6)
                        if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                        elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                        elif map[i][j] == 1: print("●",end='')
                        elif map[i][j] == 2: print("○",end='')
                        elif map[i][j] == 3: print("┌─",end='')
                        elif map[i][j] == 4: print("┐",end='')
                        elif map[i][j] == 5: print("└─",end='')
                        elif map[i][j] == 6: print("┘",end='')
                        elif map[i][j] == 7: print("┬─",end='')
                        elif map[i][j] == 8: print("│",end='')
                        elif map[i][j] == 9: print("┴─",end='')
                        elif map[i][j] == 10: print("├─",end='')
                    print(" ")
                textcolor(15,0)
                x = receive2(connectionSock)
                send(connectionSock, trash)
                y = receive2(connectionSock)
                map[y][x] = 2
                turn -= 1
    if bw == 2:
        while(True):
            for i in range(0,15,1):
                for j in range(0,15,1):
                    if j < 11:
                        if map[i][j] == 1 and map[i][j+1] == 1 and map[i][j+2] == 1 and map[i][j+3] == 1 and map[i][j+4] == 1: win = 1
                        if map[i][j] == 2 and map[i][j+1] == 2 and map[i][j+2] == 2 and map[i][j+3] == 2 and map[i][j+4] == 2: win = 2
                    if i < 11:
                        if map[i][j] == 1 and map[i+1][j] == 1 and map[i+2][j] == 1 and map[i+3][j] == 1 and map[i+4][j] == 1: win = 1
                        if map[i][j] == 2 and map[i+1][j] == 2 and map[i+2][j] == 2 and map[i+3][j] == 2 and map[i+4][j] == 2: win = 2
                    if i < 11 and j < 11:
                        if map[i][j] == 1 and map[i+1][j+1] == 1 and map[i+2][j+2] == 1 and map[i+3][j+3] == 1 and map[i+4][j+4] == 1: win = 1
                        if map[i][j] == 2 and map[i+1][j+1] == 2 and map[i+2][j+2] == 2 and map[i+3][j+3] == 2 and map[i+4][j+4] == 2: win = 2
                    if i < 11 and j > 3:
                        if map[i][j] == 1 and map[i+1][j-1] == 1 and map[i+2][j-2] == 1 and map[i+3][j-3] == 1 and map[i+4][j-4] == 1: win = 1
                        if map[i][j] == 2 and map[i+1][j-1] == 2 and map[i+2][j-2] == 2 and map[i+3][j-3] == 2 and map[i+4][j-4] == 2: win = 2
            if win == 1:
                system("cls")
                for i in range(0,15,1):
                    for j in range(0,15,1):
                        textcolor(0,6)
                        if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                        elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                        elif map[i][j] == 1: print("●",end='')
                        elif map[i][j] == 2: print("○",end='')
                        elif map[i][j] == 3: print("┌─",end='')
                        elif map[i][j] == 4: print("┐",end='')
                        elif map[i][j] == 5: print("└─",end='')
                        elif map[i][j] == 6: print("┘",end='')
                        elif map[i][j] == 7: print("┬─",end='')
                        elif map[i][j] == 8: print("│",end='')
                        elif map[i][j] == 9: print("┴─",end='')
                        elif map[i][j] == 10: print("├─",end='')
                    print(" ")
                gotoxy(40,10)
                textcolor(0,3)
                print("흑돌 승리 !")
                textcolor(15,0)
                gotoxy(0,16)
                system("pause > nul")
                sys.exit()
            if win == 2:
                system("cls")
                for i in range(0,15,1):
                    for j in range(0,15,1):
                        textcolor(0,6)
                        if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                        elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                        elif map[i][j] == 1: print("●",end='')
                        elif map[i][j] == 2: print("○",end='')
                        elif map[i][j] == 3: print("┌─",end='')
                        elif map[i][j] == 4: print("┐",end='')
                        elif map[i][j] == 5: print("└─",end='')
                        elif map[i][j] == 6: print("┘",end='')
                        elif map[i][j] == 7: print("┬─",end='')
                        elif map[i][j] == 8: print("│",end='')
                        elif map[i][j] == 9: print("┴─",end='')
                        elif map[i][j] == 10: print("├─",end='')
                    print(" ")
                gotoxy(40,10)
                textcolor(0,3)
                print("백돌 승리 !")
                textcolor(15,0)
                gotoxy(0,16)
                system("pause > nul")
                sys.exit()
            if turn == 1:
                clear()
                for i in range(0,15,1):
                    for j in range(0,15,1):
                        textcolor(0,6)
                        if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                        elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                        elif map[i][j] == 1: print("●",end='')
                        elif map[i][j] == 2: print("○",end='')
                        elif map[i][j] == 3: print("┌─",end='')
                        elif map[i][j] == 4: print("┐",end='')
                        elif map[i][j] == 5: print("└─",end='')
                        elif map[i][j] == 6: print("┘",end='')
                        elif map[i][j] == 7: print("┬─",end='')
                        elif map[i][j] == 8: print("│",end='')
                        elif map[i][j] == 9: print("┴─",end='')
                        elif map[i][j] == 10: print("├─",end='')
                    print(" ")
                textcolor(15,0)
                gotoxy(40,5)
                textcolor(0,3)
                print("You : ○        ")
                gotoxy(40,6)
                print("Opponent: ●  ◀")
                textcolor(15,0)
                gotoxy(0,0)
                x = receive2(connectionSock)
                send(connectionSock, trash)
                y = receive2(connectionSock)
                map[y][x] = 1
                turn += 1
                continue
            if turn == 2:
                while True:
                    clear()
                    gotoxy(40,5)
                    textcolor(0,3)
                    print("You : ○      ◀")
                    gotoxy(40,6)
                    print("Opponent: ●    ")
                    textcolor(15,0)
                    gotoxy(0,0)
                    for i in range(0,15,1):
                        for j in range(0,15,1):
                            textcolor(0,6)
                            if map[i][j] == 0 and map[i][j+1] != 2: print("┼─",end='')
                            elif map[i][j] == 0 and map[i][j+1] == 2: print("┼ ",end='')
                            elif map[i][j] == 1: print("●",end='')
                            elif map[i][j] == 2: print("○",end='')
                            elif map[i][j] == 3: print("┌─",end='')
                            elif map[i][j] == 4: print("┐",end='')
                            elif map[i][j] == 5: print("└─",end='')
                            elif map[i][j] == 6: print("┘",end='')
                            elif map[i][j] == 7: print("┬─",end='')
                            elif map[i][j] == 8: print("│",end='')
                            elif map[i][j] == 9: print("┴─",end='')
                            elif map[i][j] == 10: print("├─",end='')
                        print(" ")
                    textcolor(15,0)
                    gotoxy(int(x)*2,int(y))
                    kkey = Pgetch()
                    kkey = list(kkey)
                    key = chr(kkey[0])
                    int(x)
                    int(y)
                    if key == 'w' and y > 0: y -= 1
                    elif key == 's' and y < 14: y += 1
                    elif key == 'a' and x > 0: x -= 1
                    elif key == 'd' and x < 14: x += 1
                    elif kkey[0] == 32 and map[y][x] != 1 and map[y][x] != 2: break
                map[y][x] = 2
                send2(connectionSock, str(x))
                trash = receive(connectionSock)
                send2(connectionSock, str(y))
                turn -= 1
