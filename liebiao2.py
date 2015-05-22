__author__ = 'liubo'

import sys
import os
import time,datetime

fav_movies = ["The Holy Grail","The life of Brian","The Holy grail","the life of brian","the meaning of life"]

print(fav_movies[0])
print(fav_movies[1])

print("-------------------")

for each_flick in fav_movies:
    print(each_flick)


print("-------------------")

count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count =  count+1

print("-------------------")
#time_format = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.now()
print(today)
print("-------------------")
now = time.strftime('%Y%m%d%H%M%S')
print(now)