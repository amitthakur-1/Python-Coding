# with open("practice.txt","w+") as f:
#     (f.write("hi everyone \nwe learned file i/o \nusing java \ni like programming in java"))
    
#     f.seek(0)

#     data=f.read()
#     new_data1=data.replace("java","python")
#     print(new_data1)

# 2write the program to read the text from a given file poem.txt and find the text "twinkle"
# with open("file.txt","w+") as f:
#     f.write("twinkle twinkle little star")
#     f.seek(0)
#     data=f.read()
#     print(data)
#     if("twinkle"in data):
#         print("found")
#     else:
#         print("not found")

# 3 game() in a program let a user to play a game and return the integer
# import  random
# def game():
#     print("you are enterd in the game...")
# score= random.randint(1,100)
# with open("highscore.txt") as f:
#    highscore=f.read()
#    if(highscore!=""):
#        highscore=int(highscore)
#    else:
#        highscore=0
# print(f"your score:{score}")
# if(score>highscore): 
#     with open("highscore.txt","w")as f:
#         f.write(str(score))
# game()...xxxxxxxxxxxxxxxxxx...wrong answer....xxxxxx

# printing the table and add it to the file
# n = int(input("enter a number: "))
# with open("new.txt", "w+") as f:
#     for i in range(1,11):
#         x = f"{n} x {i} = {n*i}"
#         print(x)
#         f.write(x + "\n")
#     f.seek(0)   
#     data = f.read()
#     print("\nData from file:")
#     print(data)



def genrateTable(n):
    table=""
    for i in range(1,11):
        table+=f"{n}X{i}={n*i}\n"
    with open("table/")
