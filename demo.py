from tkinter import *
import tkinter.messagebox


chessColorBlack = True
stop = False

#一行16个点
length = 16
chessPoint = [[0 for i in range(0,length)] for j in range(0,length)]
surface = tkinter.Tk()
surface.geometry('680x695')
surface.title("超级五子棋")

def win():
    global stop
    if chessColorBlack:
        tkinter.messagebox.showinfo("游戏结束","黑棋赢")
    else:
        tkinter.messagebox.showinfo("游戏结束","白棋赢")
    stop = True

def checkIfEnd (x,y):
    counter = 0
    for down in range (y+1,length+1):
        if chessPoint[x][down] == chessPoint[x][y]:
            counter += 1
        else:
            break
    for up in range (y-1,0,-1):
        if chessPoint[x][up] == chessPoint[x][y]:
            counter += 1
        else:
            break
    if counter == 4:
        win()
    counter = 0

    for left in range (x-1,0,-1):
        if chessPoint[left][y] == chessPoint[x][y]:
            counter += 1
        else:
            break
    for right in range (x+1,length+1):
        if chessPoint[right][y] == chessPoint[x][y]:
            counter += 1
        else:
            break
    if counter == 4:
        win()
    counter = 0

    for up,right in zip(range(y-1,0,-1),range (x+1,length+1)):
        if chessPoint[right][up] == chessPoint[x][y]:
            counter += 1
        else:
            break
    for down,left in zip(range (y+1,length+1),range (x-1,0,-1)):
        if chessPoint[left][down] == chessPoint[x][y]:
            counter += 1
        else:
            break
    if counter == 4:
        win()
    counter = 0

    for up,left in zip(range(y-1,0,-1),range (x-1,0,-1)):
        if chessPoint[left][up] == chessPoint[x][y]:
            counter += 1
        else:
            break
    for down,right in zip(range (y+1,length+1),range (x+1,length+1)):
        if chessPoint[right][down] == chessPoint[x][y]:
            counter += 1
        else:
            break
    if counter == 4:
        win()

def draw (event):
    #每个格子40像素
    if (event.x % 40 > 20):
        event.x = event.x // 40 + 1
    else:
        event.x = event.x // 40
    if (event.y % 40 > 20):
        event.y = event.y // 40 + 1
    else:
        event.y = event.y // 40

    if (event.x > length):
        event.x = length
    elif (event.y > length):
        event.y = length
    elif (event.x < 1):
        event.x = 1
    elif (event.y < 1):
        event.y = 1

    left = event.x * 40 - 17
    right = event.x * 40 + 17
    up = event.y * 40 - 17
    down = event.y * 40 + 17
    global chessColorBlack
    global chessPoint
    if (stop == False) :
        if chessPoint[event.x][event.y] == 0:
            if chessColorBlack == True :
                grill.create_oval(left,up,right,down,fill = 'black',tag ='chess')
                chessPoint[event.x][event.y] = 1
                checkIfEnd(event.x,event.y)
                chessColorBlack = False
            elif chessColorBlack == False:
                grill.create_oval(left,up,right,down,fill = 'white',tag ='chess')
                chessPoint[event.x][event.y] = 2
                checkIfEnd(event.x,event.y)
                chessColorBlack = True

def clear():
    grill.delete('chess')

grill = Canvas(surface,height = 600,width = 600)
grill.pack(expand=YES, fill=BOTH)
grill.bind("<Button-1>",draw)
clean = Button(surface,text ="清空棋子",command=clear,bg = "red")
clean.pack(fill = X)

def main():
    for row in range(1,length+1):
         grill.create_line(40,row*40,640,row*40,width = 2,dash = (5,2))
    for colonm in range(1,length+1):
         grill.create_line(colonm*40,40,colonm*40,640,width = 2,dash = (5,2))
    surface.mainloop()

if __name__ == "__main__":
    main()
