from plyer import notification
from bs4 import BeautifulSoup
from tkinter import IntVar
import schedule
import time
import requests


# write/rewrite data into the savefile 
def writeDataInFile(word,days):
     # getting number of words 
    file = open('save-file.txt','w')
    file.truncate(0)
    file.write(str(word)+"\n")
    file.write("[")
    for day,value in days.items():
        file.write(f"({day},{str(value.get())})")
    file.write("]")
    file.close()




def generate_random_words():
    url = f"https://randomword.com/"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,"html.parser")
    random_word = soup.find("div",{"id":"random_word"}).get_text()
    random_word_meaning = soup.find("div",{"id":"random_word_definition"}).get_text()
    # print(f"{random_word} = {random_word_meaning}")
    return [random_word,random_word_meaning]
    
# generate_random_words()

def notification_message():
    ls = generate_random_words()
    notification.notify(
        title=ls[0],
        message =ls[1],
        timeout = 15
    )

if __name__ == "__main__":
    schedule.every(20).seconds.do(notification_message)


    while True:
        schedule.run_pending()
        time.sleep(1)