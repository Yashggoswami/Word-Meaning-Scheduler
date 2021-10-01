from plyer import notification
from bs4 import BeautifulSoup
import schedule
import time
import requests


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

schedule.every(20).seconds.do(notification_message)


while True:
    schedule.run_pending()
    time.sleep(1)