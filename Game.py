from tkinter import *
import random
# game parameter
width=600
hieght=600
size=20
score=0
speed=100
food_color="red"
snake_color="blue"
w=Tk()

label=Label(w,text="SCORE :{}".format(score),font=("consolas",40))
label.pack(side="top")
canvas=Canvas(w,background="black",width=width,height=hieght)
canvas.pack()
w.update()
print(int((w.winfo_width()/2)))
w.geometry("{}x{}+{}+{}".format(w.winfo_width(),w.winfo_height(),int((w.winfo_screenwidth()-width)/2),int((w.winfo_screenheight()-hieght)/2)-75))

class Food:
    def __init__(self):
        x,y=random.randrange(30),random.randrange(30)
        self.coordination=[x,y]
        canvas.create_oval(x*size,y*size,x*size+size,y*size+size,fill=food_color,tag="food")

class Snake:
    def __init__(self):
        self.coordination=[]
        self.squares=[]
        self.food=Food()
        self.direction="down"
        for i in range(3):
            self.coordination.append([0,0])
            square=canvas.create_rectangle(0,0,size,size,fill=snake_color)
            self.squares.append(square)

    def change_direction(self,str):
        dir=self.direction
        if( dir=="left" and str!="right"):
            self.direction=str
        elif(dir=="right" and str!="left"):
            self.direction=str
        elif(dir=="up" and str!="down"):
            self.direction=str
        elif(dir=="down" and str!="up"):
            self.direction=str

    def check_game(self):
        x,y=self.coordination[0]
        if( x<0 or x >29 or y<0 or y>29):
            return False
        for i in range(1,len(self.coordination)):
            if( x== self.coordination[i][0] and y==self.coordination[i][1]):
                return False
        return True

    def game_over(self):
        canvas.delete(ALL)
        canvas.create_text(width/2,hieght/2-40,text="GAME OVER BABY ;)",fill="red",font=("consolas",45))

    def move(self):
        x,y=self.coordination[0]
        dir=self.direction
        if(dir=="down"):
            y+=1
        elif(dir=="up"):
            y-=1
        elif(dir=="right"):
            x+=1
        elif(dir=="left"):
            x-=1

        self.coordination.insert(0,[x,y])
        square=canvas.create_rectangle(x*size,y*size,x*size+size,y*size+size,fill=snake_color)
        self.squares.insert(0,square)
        if(x== self.food.coordination[0] and y== self.food.coordination[1]):
            global score
            score+=1
            label.config(text="SCORE :{}".format(score))
            canvas.delete("food")
            self.food=Food()
        else:
            self.coordination.pop()
            canvas.delete(self.squares[-1])
            del self.squares[-1]
        if(not self.check_game()):
            self.game_over()
        else:
         w.after(speed,self.move)

if __name__=="__main__":
 snake=Snake()
 snake.move()
 canvas.focus_set()
 w.bind("<Up>",lambda event: snake.change_direction("up"))
 w.bind("<Down>",lambda event: snake.change_direction("down"))
 w.bind("<Right>",lambda event: snake.change_direction("right"))
 w.bind("<Left>",lambda event: snake.change_direction("left"))

 w.mainloop()