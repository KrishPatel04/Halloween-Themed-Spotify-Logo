#Import ALL from python TURTLE extension
from turtle import *
#Math imports
from math import sin
from math import radians
Screen().setup(900, 650) #Screen settings
Screen().bgcolor("#000000") #Background color to black

def App_square(app_square_chose):
  begin_fill()
  color("#000000", app_square_chose)
  pu()
  goto(-200, -265)
  for i in range(2):
    fd(400)
    circle(24, 90)
    forward(400)
    circle(24,90)
  end_fill()
 #rounded off edges app square
def pumkin(teeth_choose1, choose2, choose3, choose4):
  fillcolor("#DC5F00") #Filled color for circle
  begin_fill()
  up()
  #Circle
  goto(0,-240)
  circle(180)
  end_fill()
  #Eye 1 (LEFT)
  up()
  setpos(-140, -45)
  fillcolor("#FFD700")
  begin_fill()
  fd(100) #Base
  lt(120)
  fd(100) #Second side
  lt(120)
  fd(100) #Third side
  end_fill()
  #Eye 2 (RIGHT)
  up()
  setpos(90, 40)
  fillcolor("#FFD700")
  begin_fill()
  fd(100) #Base
  lt(120)
  fd(100) #Second base
  lt(120)
  fd(100) #Third base
  end_fill()
  #Inverted triangle for NOSE
  up()
  setpos(0, -110)
  fillcolor("#FFD700")
  begin_fill()
  fd(40)
  rt(120)
  fd(40)
  rt(120)
  fd(40)
  end_fill()
  #Teeth!
  #Teeth tri 1
  up()
  setpos(-60, -120)
  fillcolor(teeth_choose)
  begin_fill()
  fd(50)
  rt(120)
  fd(50)
  rt(120)
  fd(50)
  end_fill()
  #Teeth tri 2
  up()
  setpos(-60, -120)
  fillcolor(teeth_choose)
  begin_fill()
  fd(50)
  rt(120)
  fd(50)
  rt(120)
  fd(50)
  end_fill()
  #Teeth tri 3
  up()
  setpos(14, -163)
  fillcolor(teeth_choose)
  begin_fill()
  fd(50)
  rt(120)
  fd(50)
  rt(120)
  fd(50)
  end_fill()
  #Teeth tri 4
  up()
  setpos(90, -120)
  fillcolor(teeth_choose)
  begin_fill()
  fd(50)
  rt(120)
  fd(50)
  rt(120)
  fd(50)
  end_fill()
  #Green stem
  fillcolor("#80FF00")
  begin_fill()
  goto(-20, 110)
  #First side
  fd(40)
  lt(90)
  #Second side
  fd(60)
  lt(90)
  #Third side
  fd(40)
  lt(90)
  #Fourth side
  fd(60)
  lt(90)
  end_fill()
  #Wavy line
  pu()
  goto(75, 150)
  pd()
  pensize(17)
  pencolor("orange")
  right(60)
  fd(0)
  circle(150, 60)
  #wavy 2
  pu()
  goto(115, 150)
  pd()
  pensize(17)
  pencolor("orange")
  right(60)
  fd(0)
  circle(100, 60)
  #wavy 3
  pu()
  goto(-210, 90)
  pd()
  pensize(17)
  pencolor("orange")
  left(10)
  fd(0)
  circle(100, 60)
  #wavy 4
  pu()
  goto(-215, 60)
  pd()
  pensize(17)
  pencolor("orange")
  right(60)
  fd(0)
  circle(150, 60)
  
  
  

def HappyHalloween_text():
  pu()
  goto(-85, -210)
  pd()
  pencolor("#1e41a1")
  write("Halloween X Spotify", font=("Narrow", 13, "italic"))


def Spotify_text():
  pu()
  goto(-200, 200)
  pencolor("#9CDBFF")
  pd()
  write("Listen to Stopify's new songs on Halloween!", font=("Narrow", 12, "bold"))
  
def headphones():
  width(10)
  pu()
  goto(-140, -240)
  pencolor("#FFFFFF")
  pd()
  circle(12, 360)
  seth(90)
  fd(20)
  circle(30, 180)
  fd(18)
  circle(12, 360)


speed(25)
app_square_chose = input("What color would you like the background of the back to be? Enter a hex code (e.g. '#F3DAAA'): ")
App_square(app_square_chose)
teeth_choose = input("What color would you like the teeth to be? Etner a hex code ('#00FFBB'): ")
pumkin(teeth_choose, teeth_choose, teeth_choose, teeth_choose)
HappyHalloween_text()
Spotify_text()
headphones()
hideturtle()


done()