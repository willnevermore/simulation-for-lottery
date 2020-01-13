import random

from progressbar import *
redball = []
i = 0
# while True:
#     i = i + 1
#     strnum = input("input redball %d num:"%i)
#     if int(strnum) < 30 and int(strnum) > 0:
#         redball.append(int(strnum))
#     else:
#         print("input error!")
#         exit()
#     if(i >= 6):
#         break
# blueball = int(input("input blueball num:"))
# if blueball < 0  and blueball > 10:
#     print("input error!")
redball = [5, 29, 14, 26, 9, 18]
blueball = 8
print("redball:" )
print(redball)
print("blueball:")
print(blueball)

random_red = []
random_blue = 0
cnt = 0
match_red_balls = []
match_blue_ball = -1

match_nums4_times = 0
match_nums5_times = 0
match_nums6_times = 0
total_randoms = 0
match_nums_blue_time = 0
balls_list = []
for i in range(0,35):
    balls_list.append(i)


progress = ProgressBar()
for i in progress(range(1000000)):


    random_red = random.sample(balls_list,6)
    for redone in redball:
        for random_redone in random_red:
            if redone == random_redone:
                match_red_balls.append(redone)


    random_blue = random.randrange(0,16)

    if blueball == random_blue:
        match_blue_ball = blueball


    if len(match_red_balls) > 0:
        #print(match_red_balls)

        if len(match_red_balls)  > 5:
            #print("-------------------")
            #print(match_red_balls)
            if match_blue_ball >= 0:
                #print(match_blue_ball)
                match_nums_blue_time = match_nums_blue_time + 1
                total_randoms = i
                break
            match_nums4_times = match_nums4_times + 1



    #print(random_red)


    random_red = []

    match_blue_ball = -1
    match_red_balls = []

print("total match 6 ball:%d"%match_nums4_times)
print("big price total :%d"%match_nums_blue_time)
print("somlation total cnt : %d"%total_randoms)
