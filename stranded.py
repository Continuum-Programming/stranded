import time
import turtle
from os import system
import sys
import printfunctions

system("title " + "Stranded")


def map():
    turtle.reset()
    turtle.penup()
    turtle.forward(440)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(380)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(770)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(390)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(240)
    turtle.penup()
    turtle.goto(x=100, y=100)
    turtle.pendown()
    turtle.dot(size=10)
    turtle.penup()
    turtle.goto(x=0, y=0)


def map_2():
    turtle.reset()
    turtle.penup()
    turtle.forward(440)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(380)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(770)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(390)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(240)
    turtle.penup()
    turtle.goto(x=100, y=100)
    turtle.pendown()
    turtle.dot(size=10)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(135)
    turtle.forward(50)
    time.sleep(5)


def map_3():
    turtle.reset()
    turtle.penup()
    turtle.forward(440)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(380)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(770)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(390)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(240)
    turtle.penup()
    turtle.goto(x=100, y=100)
    turtle.pendown()
    turtle.dot(size=10)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(135)
    turtle.forward(100)
    turtle.right(90)
    time.sleep(5)


def map_4():
    turtle.reset()
    turtle.penup()
    turtle.forward(440)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(380)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(770)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(390)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(240)
    turtle.penup()
    turtle.goto(x=100, y=100)
    turtle.pendown()
    turtle.dot(size=10)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    time.sleep(5)


def map_5():
    turtle.reset()
    turtle.penup()
    turtle.forward(440)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(380)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(770)
    turtle.right(90)
    turtle.forward(890)
    turtle.right(90)
    turtle.forward(390)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(200)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(240)
    turtle.penup()
    turtle.goto(x=100, y=100)
    turtle.pendown()
    turtle.dot(size=10)
    turtle.penup()
    turtle.goto(x=0, y=0)
    turtle.right(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    time.sleep(5)


def printcustom(text, optional=None, optional2=None):
    if optional2 is not None:
        printfunctions.print_with_wait_and_delay(
            text + " " + str(optional) + " " + str(optional2), 1
        )
    elif optional is not None:
        printfunctions.print_with_wait_and_delay(text + " " + str(optional), 1)
    else:
        printfunctions.print_with_wait_and_delay(text, 1)


def game_over():
    printcustom("You lost! Game will close in 5 seconds.")
    time.sleep(5)
    quit()


def main():
    if sys.platform == "darwin":
        printcustom("Please put the terminal window in fullscreen.")
    elif sys.platform == "win32":
        printcustom("Please hit f11 to put the terminal window in fullscreen.")
    time.sleep(1)
    name = input("What is your name? ")
    printcustom("Hello, " + name + "!")
    time.sleep(1)
    friend_name = input("What is your best friend's name? ")
    time.sleep(1)
    printcustom("You are in the carribean, on an undiscovered island.")
    time.sleep(1)
    printcustom(
        "You were in a plane crash with", friend_name, "and everyone else died."
    )
    time.sleep(1)
    printcustom(
        "  ______  __    __       ___      .______   .___________. _______ .______          __  "
    )
    printcustom(
        " /      ||  |  |  |     /   \     |   _  \  |           ||   ____||   _  \        /_ | "
    )
    printcustom(
        "   ,----'|  |__|  |    /  ^  \    |  |_)  | `---|  |----`|  |__   |  |_)  |        | | "
    )
    printcustom(
        "|  |     |   __   |   /  /_\  \   |   ___/      |  |     |   __|  |      /         | | "
    )
    printcustom(
        "|  `----.|  |  |  |  /  _____  \  |  |          |  |     |  |____ |  |\  \----.    | | "
    )
    printcustom(
        " \______||__|  |__| /__/     \__\ | _|          |__|     |_______|| _| `._____|    |_| "
    )
    time.sleep(5)
    printcustom("You: Hey,", friend_name)
    time.sleep(1)
    printcustom(friend_name + ": Yes?")
    time.sleep(1)
    printcustom("You: Are you okay?")
    time.sleep(1)
    printcustom(friend_name + ": Yes...")
    time.sleep(1)
    printcustom("You: What are we going to eat other than Doritos from the plane?")
    time.sleep(1)
    printcustom(friend_name + ": coconut. (not)")
    time.sleep(1)
    food = input("Do you want coconut or watermelon? ")
    printcustom(friend_name + ": Okay.")
    time.sleep(1)
    printcustom(friend_name + ": I will go try and find some", food)
    time.sleep(1)
    printcustom(friend_name + ": Go set up the tent, Okay?")
    time.sleep(1)
    printcustom("...")
    time.sleep(1.5)
    printcustom("Later that day...")
    time.sleep(1)
    printcustom("You: It's time to go to bed,", friend_name)
    time.sleep(1)
    printcustom(
        " ______  __    __       ___      .______   .___________. _______ .______          ___   "
    )
    printcustom(
        " /      ||  |  |  |     /   \     |   _  \  |           ||   ____||   _  \        |__ \  "
    )
    printcustom(
        "|  ,----'|  |__|  |    /  ^  \    |  |_)  | `---|  |----`|  |__   |  |_)  |          ) | "
    )
    printcustom(
        "|  |     |   __   |   /  /_\  \   |   ___/      |  |     |   __|  |      /          / /  "
    )
    printcustom(
        "|  `----.|  |  |  |  /  _____  \  |  |          |  |     |  |____ |  |\  \----.    / /_  "
    )
    printcustom(
        " \______||__|  |__| /__/     \__\ | _|          |__|     |_______|| _| `._____|   |____| "
    )
    time.sleep(5)
    printcustom("You : Yawn....")
    time.sleep(1)
    printcustom("You : Hey", friend_name)
    time.sleep(3)
    printcustom("You : Hmm,", friend_name, "isn't answering.")
    time.sleep(1)
    printcustom("Outside of the banana leaf tent...")
    time.sleep(1)
    printcustom(
        "You: There are footprints. Maybe", friend_name, "is finding breakfast?"
    )
    time.sleep(1)
    printcustom("You: Why are there other footprints that", friend_name, "didn't make?")
    time.sleep(1)
    map1 = input("Do you want to open the map? Type 'yes' to open map. ")
    if map1 == "yes":
        map()
    else:
        printcustom("Why wouldn't you say yes???")
        time.sleep(2)
        game_over()
    printcustom("The dot is", friend_name, " and the arrow is you")
    dir1 = input("Do you go right or left? Type 'l' for left and 'r' for right. ")
    if dir1 == "l":
        printcustom(
            "You went left and encountered a group of man eating baboons. Good job. You died."
        )
        time.sleep(2)
        game_over()
    map2 = input("Do you want to open the map? Type 'yes' to open map. ")
    if map2 == "yes":
        map_2()
        time.sleep(1)
    else:
        printcustom("Why wouldn't you say yes???")
        time.sleep(2)
        game_over()
    dir2 = input("Do you go right or left? Type 'l' for left and 'r' for right. ")
    if dir2 == "l":
        printcustom(
            "You went left, and ended back up at your tent, where you found a group of wolves eating your Doritos. You died."
        )
        time.sleep(2)
        game_over()
    map3 = input("Do you want to open the map? Type 'yes' to open map. ")
    if map3 == "yes":
        map_3()
        time.sleep(1)
    else:
        printcustom("Why wouldn't you say yes???")
        time.sleep(2)
        game_over()
    dir3 = input("Do you go right or left? Type 'l' for left and 'r' for right. ")
    if dir3 == "d":
        printcustom("You went south, and found a shack.")
        time.sleep(1)
        printcustom(
            "You entered the shack, and found a man inside saying 'AHAHAHAHAH! It's ALIVE!'."
        )
        time.sleep(1)
        printcustom(
            "By now you realize that Frankenstein has ripped your head off. You Died."
        )
        time.sleep(1)
        game_over()
    map4 = input("Do you want to open the map? Type 'yes' to open map. ")
    if map4 == "yes":
        map_4()
        time.sleep(1)
    else:
        printcustom("Why wouldn't you say yes???")
        time.sleep(2)
        game_over()
    dir4 = input("Do you go up or down? Type 'u' for up, and 'd' for down. ")
    if dir4.lower() == "d" or dir4.lower() == "down":
        printcustom(
            "You went back to where you were before. You hear some shouting, and then you see frankenstein."
        )
        time.sleep(1)
        printcustom("After that, You Ded. You have failed. Great job.")
        time.sleep(1)
        game_over()
    map5 = input("Do you want to open the map? Type 'yes' to open map. ")
    if map5.lower() == "yes":
        map_5()
        time.sleep(1)
    else:
        printcustom("Why wouldn't you say yes???")
        time.sleep(2)
        game_over()
    printcustom(
        "Robert the Kidnapper: Da boss will be mad dat our secret base was found...."
    )
    time.sleep(1)
    printcustom("Bobert the Kidnapper: Yeh...")
    time.sleep(1)
    printcustom(friend_name + ": MPMFHFPM!!")
    at1 = input(
        "Do you want to go in now, or wait till night? Type 'now' to go in now, or type 'later' to go at night. "
    )
    if at1 == ("now"):
        printcustom("Robert: *Y A W N*, I am gonna go to bed.")
    else:
        printcustom("You went in, and you died. Lol")
        game_over()
    printcustom("Bobert: Me too.")
    time.sleep(1)
    printcustom(
        "You sneak in and as you finish untying", friend_name + ",Robert wakes up."
    )
    time.sleep(1)
    printcustom("Robert: Bobert! What are you doing?")
    time.sleep(1)
    printcustom("Robert: Wait, YOU'RE NOT BOBERT!!!")
    time.sleep(1)
    printcustom("You spot a cave in the secret base.")
    time.sleep(1)
    printcustom("You decide to run into the cave. You run deeper and deeper...")
    time.sleep(1)
    printcustom("You hear water on the left.")
    time.sleep(1)
    printcustom("You see a waterfall with light on the other side.")
    time.sleep(1)
    printcustom("You go left...")
    time.sleep(1)
    printcustom("You go through the waterfall...")
    time.sleep(3)
    printcustom("...")
    time.sleep(3)
    printcustom("You jump")
    time.sleep(3)
    printcustom("And you land")
    time.sleep(3)
    printcustom("And you get squished by", friend_name)
    printcustom(friend_name + ": We escaped Robert and Bobert!!!!!!!!!!!!!!!!!")
    printcustom(
        ".___________. __    __   _______     _______ .__   __.  _______   __   __   __  "
    )
    printcustom(
        "|           ||  |  |  | |   ____|   |   ____||  \ |  | |       \ |  | |  | |  | "
    )
    printcustom(
        "`---|  |----`|  |__|  | |  |__      |  |__   |   \|  | |  .--.  ||  | |  | |  | "
    )
    printcustom(
        "    |  |     |   __   | |   __|     |   __|  |  . `  | |  |  |  ||  | |  | |  | "
    )
    printcustom(
        "    |  |     |  |  |  | |  |____    |  |____ |  |\   | |  '--'  ||__| |__| |__| "
    )
    printcustom(
        "    |__|     |__|  |__| |_______|   |_______||__| \__| |_______/ (__) (__) (__) (or is it...)"
    )
    time.sleep(1)
    printcustom("Created by eanderso2")
    time.sleep(1)
    printcustom("Bug-fixed by ThePTNT")
    time.sleep(1)
    printcustom("Easter eggs added/Tested by xorb999999999")
    time.sleep(1)
    printcustom("Made in 1 year")
    time.sleep(1)
    printcustom("Coding finished on August 24th, 2021")
    time.sleep(1)
    printcustom(
        "     _______.___________..______          ___      .__   __.  _______   _______  _______  "
    )
    printcustom(
        "    /       |           ||   _  \        /   \     |  \ |  | |       \ |   ____||       \ "
    )
    printcustom(
        "   |   (----`---|  |----`|  |_)  |      /  ^  \    |   \|  | |  .--.  ||  |__   |  .--.  |"
    )
    printcustom(
        "    \   \       |  |     |      /      /  /_\  \   |  . `  | |  |  |  ||   __|  |  |  |  |"
    )
    printcustom(
        ".----)   |      |  |     |  |\  \----./  _____  \  |  |\   | |  '--'  ||  |____ |  '--'  |"
    )
    printcustom(
        "|_______/       |__|     | _| `._____/__/     \__\ |__| \__| |_______/ |_______||_______/ "
    )
    time.sleep(1)
    printcustom("Closing in 5 seconds")
    time.sleep(5)
    sys.exit(0)


if __name__ == "__main__":
    main()
