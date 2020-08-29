def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)





if __name__ == '__main__':
    import requests
    import json

    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=8011edcd77bb4f959a0c1cf421ba4554"

    r = requests.get(url)
    text = r.text
    json1 = json.loads(text)
    print(json1)
    for i in range(0,11):
        speak(json1['articles'][i]['title'])