from plyer import notification
from bs4 import BeautifulSoup
from tkinter import IntVar
import schedule
import time
import requests
import random
from datetime import datetime as date



count = 0
dic = []

# reading data from the save-file
def readDataFromFile():
    file = open('save-file.txt','r')
    global count,dic
    count = int(file.readline())
    dic = eval(file.readline())
    
def get_dic():
    global dic
    return dic

def get_word_number():
    global count
    return count

def todays_work():
    day = date.today().strftime("%A")
    if(dic[day] == 1):
        print(f'today is {day} at it is valid')
    
# write/rewrite data into the savefile 
def writeDataInFile(word,days):
     # getting number of words 
    file = open('save-file.txt','w')
    file.truncate(0)
    file.write(str(word)+"\n")
    file.write("{")
    size = len(days)
    for day,value in days.items():
        file.write(f"'{day}':{str(value.get())}")
        size -= 1
        if size != 0:
            file.write(',')
    file.write("}")
    file.close()

def schedule_next_run():
   time_str = '{:02d}:{:02d}'.format(random.randint(12, 11), random.randint(0, 59))
   schedule.clear()
   print("Scheduled for {}".format(time_str))
   schedule.every().day.at(time_str).do(job)


def generate_random_words():
    url = f"https://randomword.com/"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,"html.parser")
    random_word = soup.find("div",{"id":"random_word"}).get_text()
    random_word_meaning = soup.find("div",{"id":"random_word_definition"}).get_text()
    # print(f"{random_word} = {random_word_meaning}")
    return [random_word,random_word_meaning]
    

def notification_message():
    ls = generate_random_words()
    notification.notify(
        title=ls[0],
        message =ls[1],
        timeout = 15
    )

if __name__ == "__main__":
    readDataFromFile()
    todays_work()
    # schedule.every(20).seconds.do(notification_message)


    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)