from gtts import gTTS
import playsound as suara
import os
import datetime
Date = datetime.datetime.now()
import random
from tkinter import  *

#input data dari sensor atau data dummy / random
ANGIN = random.randint(240,245)
DATA_VISIBILITY  = random.randint(0,9)
weather_prez = 'HAZY'
DATA_CLOUDFEW = random.randint(1500,2500)
DATA_SUHU = random.randint(15,30)
DATA_KELEMBAPAN = random.randint(30,80)
DATA_ALTIMETER = random.randint(1001,1200)
DATA_PRESSURE = random.randint(1101,1130)
RUNWAY_LEFT = random.randint(20,30)
RUNWAY_RIGHT = random.randint(21,28)
FREQUENCY = random.uniform(110,130)

#tkinter
tk = Tk()
frame = Frame(
    tk,
    bg= 'white',
    height = '100'
)
frame.pack(fill = X)
frame1 = Frame(
    tk,
    bg= 'white',
    height='850'
)
frame1.pack(fill = X)
label = Label(frame, text = "Contoh Text to Speech",
              font = "bold, 30",
              bg="white"
              )
label.place(x = 100, y = 40)
entry = Entry(frame1,
        font=14)
entry.grid(row=3, column=0, pady=10)
entry.place(x=100, y=152,width=500,
        height=100)
entry.insert(0, "")

my_listbox = Listbox(frame1,
        font=14)
my_listbox.grid(row=3, column=0, pady=10)
my_listbox.place(x=250, y=50,width=200,
        height=100)
my_listbox.insert(END, "1. English")
my_listbox.insert(END, "2. Indonesia")
my_list = ['3.China', '4. France']
for item in my_list:
    my_listbox.insert(END, item)
def inputTextToSpeech(text):
    gts = gTTS(text=text, lang='en', slow=False)
    namaFileInput = 'OUTPUT_HASIL-' + str(Date.day) + '-' + str(Date.month) + '-'\
               + '-' + str(Date.year) + '-' \
               + str(Date.second) + ':' + str(Date.minute) + '.mp3'
    gts.save(namaFileInput)
    suara.playsound(namaFileInput)
    os.remove(namaFileInput)
def gui():
    btn = Button(frame1, text="SUBMIT",
                 width="15", pady=10, command=gui,
                 font="bold, 15",
                 bg='yellow')
    btn.place(x=230,
              y=270)
    tk.title("Contoh Text To Speech")
    tk.geometry("650x550+150+200")
    print(entry.get())
    if entry.get() != '':
        inputTextToSpeech(entry.get())
    tk.mainloop()
#airport indentity
AIRPORT_IDENTITY = "THIS IS AERODROME TERMINAL INFORMATION SERVICE FOR HUSEIN AIRPORT INFORMATION CHARLIE,"
#report Weather
Detik_Menit_Parsing = str(Date.second) + str(Date.minute)
data = []
for tgl in Detik_Menit_Parsing:
    data.append(tgl)

dt = data[3] if len(data) > 3 else str(random.randint(0,9))
REPORT_WEATHER = ',WEATHER REPORT AT,' + str(data[0]) + ',' + str(data[1]) + ',' \
                 + str(data[2]) + ',' + str(dt) + ', ' + ",UTC,"
#surface wind
data1 = []
for wind in str(ANGIN):
    data1.append(wind)
SURFACE_WIND = ',SURFACE WIND,' + str(data1[0]) + ',' + str(data1[1]) + ',' \
                + str(data1[2]) + ',' + 'DEGREES' + ',' + str(0) + ',' + str(random.randint(5,9)) + ',' + 'KNOTS,'
#visibility
data2 = []
for visible in str(DATA_VISIBILITY):
    data2.append(visible)
VISIBILITY = 'VISIBILITY,' + str(0) + ',' + str(data2[0])
#present weather
PRESENT_WEATHER = ',PRESENT WEATHER ' + str(weather_prez) + ', '
#cloud_few
data3 = []
for feet in str(DATA_CLOUDFEW):
    data3.append(feet)
CLOUD_FEW = ',CLOUD FEW, ' + str(data3[0]) + ',' + str(data3[1]) + ',' \
                 + str(data3[2]) + ',' + str(data3[3]) + ',' + 'FEET'
#temperature dan dew poin
data4 = [];data5 = []
for temp in str(DATA_SUHU):
    data4.append(temp)
for hum in str(DATA_KELEMBAPAN):
    data5.append(hum)
TEMPERATURE = ',TEMPERATURE, ' + str(data4[0]) + ',' + str(data4[1])  + ',' + 'DEGREES CENTIGRADE,'
DEW_POINT   = 'DEW POINT,' + str(data5[0]) + ',' + str(data5[1])  + ',' + 'DEGREES CENTIGRADE,'
#@altimeter dan pressure
data6 = [];data7 = []
for almimet in str(DATA_ALTIMETER):
    data6.append(almimet)
for pressur in str(DATA_PRESSURE):
    data7.append(pressur)
ALTIMETERS = ',ALTIMETER, ' + str(data6[0]) + ',' + str(data6[1]) + ',' \
                 + str(data6[2]) + ',' + str(data6[3]) + ',' + 'MILLIBARS,'
PRESSURE = ',PRESSURE, ' + str(data7[0]) + ',' + str(data7[1]) + ',' \
                 + str(data7[2]) + ',' + str(data7[3]) + ',' + 'MILLIBARS,'
#runaway
data8 = [];data9 = []
for left in str(RUNWAY_LEFT):
    data8.append(left)
for right in str(RUNWAY_RIGHT):
    data9.append(right)
RUNWAY = ',RUNWAY IN USE, ' + str(data8[0]) + ',' + str(data8[1]) + ',' + 'LEFT, AND,' \
                 + str(data9[0])  + str(data9[1]) + ',' + 'RIGHT,'
REMARK = "REMARK ALL DEPARTING AIRCRAFT ARE REQUESTED TO CONTACT HUSEIN DELIVERY CONTROL ON FREQ" + ',' \
    + str(FREQUENCY) + ',' + str(random.randint(10,15)) + 'MINUTES BEFORE START TO OBTAIN ATC CLEARANCE,' #remark aircraft
CLEAR = ",INFORM ATC ON INITIAL CONTACT THAT YOU HAVE RECEIVED INFORMATION CHARLIE,"
TOTAL_DATA = str(AIRPORT_IDENTITY) + str(REPORT_WEATHER) + str(SURFACE_WIND) + str(VISIBILITY) \
    + str(PRESENT_WEATHER) + str(CLOUD_FEW) \
    + str(TEMPERATURE) + str(DEW_POINT) + str(ALTIMETERS) \
    + str(PRESSURE) + str(RUNWAY) + \
             str(REMARK) + str(CLEAR)

def textToSpeechAirnav(text):
    tts = gTTS(text=text, lang='en', slow=False)
    namaFile = 'OUTPUT_AIRNAV_ATIS-' + str(Date.day) + '-' + str(Date.month) + '-'\
               + '-' + str(Date.year) + '-' \
               + str(Date.second) + ':' + str(Date.minute)
    tts.save(namaFile)
    suara.playsound(namaFile)
    os.remove(namaFile)
print("1. Text to speech ATIS Husein Airport")
print("2. Text to speech Input Terminal")
inputan_switch = str(input("pilih nomor :"))
def numbers_to_strings(argument):
    if argument == '1':
        textToSpeechAirnav(TOTAL_DATA)
    elif argument == '2':
        gui()
    else:
        print("tidak ada")
if __name__ == "__main__":
    argument = 0
    print(numbers_to_strings(inputan_switch))
