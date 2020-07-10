import pyttsx3
import requests
import json
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)
def speak(str):
    engine.say(str)
    engine.runAndWait()

if __name__ == "__main__":
    speak('Todays top News Headlines are')
    news = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9686640170ae49859199a55161819389').text
    news = json.loads(news)
    # print(news['articles'])
    art = news['articles']
    for articles in art:
        print(f"{articles['title']}")
        speak(articles['title'])
        speak('Moving to the next')
    speak('Thank You for your time')


