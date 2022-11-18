# simple python game
# import module
from tkinter import *


# Create a display window
root = Tk()
root.geometry('500x500')
root.title('Mad Libs Generator')
Label(root, text= 'Mad Libs Generator\n Have Fun!', font= 'arial 20 bold').pack()
Label(root, text = 'Click Any one :', font='arial 20 bold').place(x=40, y=80)

 # define Function
def madlib1():
    animals= input("enter the name of animal :")
    profession= input("enter a profession name :")
    cloth = input("enter a cloth name :")
    things = input('enter a thing name :')
    name = input('enter a name :')
    place = input("enter a place name :")
    food = input("enter a food name: ")
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to '\
     + place + ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as '\
     + animals + ' pretending to be a ' + profession + '. When we saw the second photo, it was exactly what I wanted. We both looked like '\
     + things + ' wearing' + cloth + ' I was exactly what I had in mind')

def madlib2():
    adjactive = input('enter an adjective :')
    color = input( 'enter a colour :')
    thing = input ("enter a thing :")
    place = input ( 'enter a place :')
    person = input( "enter a person name :")
    adjactive1= input("enter a adjactive :")
    insect = input("enter a insect :")
    food = input("enter a food name :")
    verb = input("enter a verb :")
    print('Last night I dreamed I was a ' + adjactive + ' butterfly with ' + color + ' splocthes that looked like ' + thing + '. I flew to ' + place +\
    ' with my bestfriend and ' + person + ' who was a ' + adjactive1 + '. We ate some ' + food + ' when we go there we decided to ' + verb + \
    ' and the dream ended when I said -- Lets ' + verb + '.')

def madlib3():
    person = input("enter the name of the person :")
    color = input( 'enter the colour :')
    foods = input("enter food :")
    adjactive = input('enter an adjective :')
    thing = input( 'enter a thing :')
    place = input("enter a place :")
    verb = input('enter a verb :')
    adverb = input("enter an adverb :")
    food = input('enter a food :')
    things = input("enter a thing :")
    print("Today we picked apple from " + place + "'s Orchard. I had no idea there were so many different varieties of apples. I ate "\
     + color + " apples straight off the tree that tested like "+ foods + ". Then there was a " + adjactive + " apple that looked like a " + things + \
      ". When our bag were full, we went on a free hay ride to " + place + " and back. It ended at a hay pile where we got to " + verb + "" + adverb + \
      ".I can hardly wait to get home and cook with the apples. We are going to make apple " + food + " and " + things + " pies!" )


# define buttons
Button(root, text= 'The photographer', font= 'arial 15', command= madlib1, bg= 'ghost white'). place(x= 60, y=120)
Button(root, text= 'apple and apple', font= 'arial 15', command= madlib2, bg= 'ghost white'). place(x= 70, y=180)
Button(root, text= 'The butterfly', font= 'arial 15', command= madlib3, bg= 'ghost white'). place(x= 80, y=240)

root.mainloop()



