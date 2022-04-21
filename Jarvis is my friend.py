import datetime
import os
import webbrowser
import time
import pyautogui
import pyjokes
import speech_recognition as sr
import pyttsx3
import wikipedia
from pywikihow import search_wikihow
import requests
import pywhatkit as kit
import cv2


engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

# print(voices[1].id)

def talk(command):
    engine.say(command)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        talk("Good Morning sir!")
    elif hour >=12 and hour <17:
        talk("Good Afternoon sir!")
    else:
        talk("Good Evening sir!")
    talk("I am Jarvis sir. Please tell me how may I help you")

def takecommand():
    listener=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        listener.pause_threshold=1
        voice=listener.listen(source)

    try:
        print("Recognizing........")
        query= listener.recognize_google(voice,language='en-in')
        print(f"user said: { query}\n")

    except:
        print("say that again please.........")
        return "None"
    return query

wishme()

while True:
    query = takecommand().lower()

    #logic for executing task based on query

    if 'please tell me about' in query:
        print("Searching Wikipedia.......")
        query = query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        talk("According to Wikipedia")
        print(results)
        talk(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")

    elif "open google" in query:
        webbrowser.open("google.com")

    elif 'open facebook' in query:
        webbrowser.open("https://www.facebook.com/")

    elif 'open instagram' in query:
        webbrowser.open("https://www.instagram.com/")

    elif 'open stackoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com/")

    elif 'open college website' in query:
        webbrowser.open("http://www.iert.ac.in/")

    elif "play music" in query or "play song" in query:
        music_path="D:\\English musics\\mymusic"
        songs=os.listdir(music_path)
        print(songs)
        os.startfile(os.path.join(music_path,songs[0]))

    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow("webcam", img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    elif "send message" in query:
        talk("sir what should i say")
        mssg=takecommand()

        from twilio.rest import Client

        account_sid = 'your id'
        auth_token = 'your token'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body= mssg,
            from_='+19035188504',
            to='+918887865211'
        )

        print(message.sid)
        talk("message has been sent sir")


    elif "send whatsapp message" in query:
        kit.sendwhatmsg(phone_no="+918004723595", message="jai mata di adarsh", time_hour=23, time_min=47, wait_time=27,
                        tab_close=True, close_time=15)
        time.sleep(120.2)
        talk("message has been sent")


    elif "write a note" in query :
        talk("please sir tell me,what to write")
        note=takecommand()
        with open("writenote.txt","w") as f:
            f.write(note)

        f.close()
        talk("notes has been  successfully write sir ,please check your main folder")

    elif "write an assignment" in query:
        talk("please sir tell me,what to write")
        note = takecommand()

        kit.text_to_handwriting(note, save_to="assign.jpg", rgb=(0, 0, 138))
        # time.sleep(15)
        # kit.sendwhats_image(receiver="+918004723595", img_path="assign.jpg", caption="jai mata di", wait_time=40,
        #                     tab_close=True, close_time=15)
        talk("assignment has been  successfully write sir ,please check your main folder")

    elif "convert image to text" in query:

        talk("converting image to text please wait")

        # .............................thankyou for breaking my heart darling!....................
        image = cv2.imread("hemant.jpg")

        # ....this code convert image to gray image........
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # .....this code convert negative image to positive image.......
        inverted = 255 - gray_image

        # ......this code convert image to blurred from of image
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

        # .......this code converted blurred image to invertedblur(negative from)
        invertedblur = 255 - blurred

        # .......this code converted image to pencilsketch........
        pencilsketch = cv2.divide(gray_image, invertedblur, scale=256.0)

        # .......save the file
        cv2.imwrite("me-grayscale.jpg", gray_image)
        print("............successfuly converted into grayscale.........")
        cv2.imwrite("me-sketch.jpg", pencilsketch)
        print("............successfuly converted into pencilsketch.........")
        cv2.imwrite("me-inverted.jpg", inverted)
        print("............successfuly converted into invertedimage.........")

        # cv2.imshow("grayscale", gray_image)
        cv2.imshow("sketch", pencilsketch)
        # cv2.imshow("inverted", inverted)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("............proccess finished enjoy your day.........")
        talk("image to sketch  has been  successfully converted sir,please check your main folder")


    elif "volume up" in query:
        pyautogui.press("volumeup",3)

    elif "volume down" in query:
        pyautogui.press("volumedown",3)

    elif "volume mute" in query:
        pyautogui.press("volumemute")

    #...................this code for know time.....................

    elif "the time" in query:
        strTime=datetime.datetime.now().strftime("%M minutes past %I %p")
        talk(f"Sir, the time is {strTime}")

    elif "open sublime" in query:
        sublimepath="C:\\Program Files\\Sublime Text\\sublime_text.exe"
        os.startfile(sublimepath)

    elif "close sublime" in query:
        os.system("taskkill  /f /im sublime_text.exe")

    elif "take a screenshot" in query:
        talk("sir please tell me, what the name of screenshot")
        name=takecommand().lower()
        talk("sir please hold screen  i am taking screenshot between few second")
        time.sleep(3)
        kit.take_screenshot(name,delay=3, show=True)
        talk("screenshot successfully captured sir ,please check your main folder")

        #..........to know the weather........................


    elif "weather in" in query or "temperature in" in query:
        # importing requests and json
        import requests, json

        # base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY=query.replace("tell me weather in","")
        API_KEY = "your api key"
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature} kelvin")
            print(f"Humidity: {humidity} percent")
            print(f"Pressure: {pressure} m Bar")
            print(f"Weather Report: {report[0]['description']}")
        else:
            # showing the error message
            print("Error in the HTTP request")
        talk(f"Sir  the  weather  in  {CITY}  is  {temperature}  kelvin  Humidity is {humidity} percent {pressure} m Bar "
             f"Weather Report: {report[0]['description']}")

#.....................to know the location....................
    elif "where i am" in query or "where we are" in query:
        talk("wait sir, let me check the location")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            # print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()

            # print(geo_data)
            city = geo_data["city"]
            state = geo_data["region"]
            country = geo_data["country"]

            print(f"sir i am not sure, but i think we are in {city} city of {state} state of  {country}")
            talk(f"sir i am not sure, but i think we are in {city} city of {state} state of  {country} country")

        except Exception as e:
            talk("sorry sir, Due to network issue i am not able to find where we are")
            pass




    elif "how much power left" in query or "how much power we have" in query or "battery" in query:
        import psutil
        battery=psutil.sensors_battery()
        percantage=battery.percent
        print(f"our system have {percantage}% battery")
        talk(f"sir our system have {percantage} percent battery")
        if percantage >=75:
            talk("we have enough power to continue our work")
        elif percantage <75 and percantage >=45:
            talk("we should connect our system to charging point to charge our battery")

        elif percantage <45 and percantage >=20:
            talk("we have less power to work , please connect to charging")

        elif percantage <20:
            talk("we have very low power, please connect to charging the system will shutdown very soon")



    elif "activate how to do mod" in query:
        talk("how to do mode is activated")
        while True:
            talk("please tell me what you want know")
            how = takecommand()
            try:
                if "exit" in how or "close" in how:
                    talk("okay sir, how to do mode is closed")
                    break
                else:

                    max_results = 1
                    how_to = search_wikihow(how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    talk(how_to[0].summary)

            except Exception as e:
                talk("sorry sir, i am not able to find this")

    elif "exit" in query:
        talk("okay sir, thank you for your time")
        exit()

    elif "sapnon ki rani" in query:
        talk("Sir, i don't know but when it comes, it will come at 10 o'clock in the day")

    elif "joking" in query:
        talk("sorry sir, i am sorry sir")

    elif "tell me a joke" in query:
        joke=pyjokes.get_joke(language="en",category="neutral")
        print(joke)
        talk(joke)

    elif "can i" in query:

        talk("please don't love in your college,  you   will   be   fucked")


takecommand()
