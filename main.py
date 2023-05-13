import kivy.properties
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import aiohttp
import asyncio
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS
import requests
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

HEADERS = {"User-Agent": UserAgent().random}



# Введите номер группы, к примеру 22-АО-АУТ1
KV = """

MyBL: 
        orientation: "vertical"
        size_hint: (0.95,0.95)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        
        btn2: r2
        ScrollView:
                do_scroll_x: False
                do_scroll_y: True
                Label: 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 0
                        halign: 'center'
                        valign: 'middle'
                        text: root.data_label

        Button:
                id: r2
                text: "Выбор института/факультета"
                bold: True
                background_color:'#00FFCE'
                size_hint:(1,0.5)
                on_press: root.callback2()


              
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Kubstu")
    https = "https://elkaf.kubstu.ru/timetable/default/time-table-student-ofo?iskiosk=0&fak_id="
    buttonsToRemove = []
# ------------------------------------------------------- #
    def del_button(self, fromList):
        if fromList:
            for i in self.buttonsToRemove:
                self.remove_widget(i)

        else:
            btn2 = ObjectProperty(None)
            self.remove_widget(self.btn2)
    def gen_href_inst(self, id):
        self.https += str(id)
        self.del_button(True)

        if len(self.https) < 88:
            self.list_kurs()
        elif len(self.https) < 95:
            self.set_data_label("Введите группу")
            self.group_names()


    def gen_button(self,text, id):
        return  Button(
            text= text,
            bold=True,
            background_color = '#00FFCE',
            size_hint = (1, 0.3),
            on_press= lambda x: self.gen_href_inst(id)
        )
    def set_data_label(self, data):
        self.data_label = str(data)

# ------------------------------------------------------- #
    def callback(self): # Расписание
        self.get_data()

    def callback2(self): # Выбор
        self.set_data_label(self.https)
        self.listFak()
# ------------------------------------------------------- #


    def listFak(self):
        self.set_data_label("Выберите институт/факультет")
        self.del_button(True)
        try:
            self.del_button(False)
        except:
            pass





        btn495 = self.gen_button("Институт нефти, газа и энергетики", 495)
        self.add_widget(btn495)
        self.buttonsToRemove.append(btn495)
        
        btn516 = self.gen_button("Институт компьютерных систем и информационной безопасности", 516)
        self.add_widget(btn516)
        self.buttonsToRemove.append(btn516)

        btn490 = self.gen_button("Институт пищевой и перерабатывающей промышленности", 490)
        self.add_widget(btn490)
        self.buttonsToRemove.append(btn490)

        btn29 = self.gen_button("Институт экономики, управления и бизнеса", 29)
        self.add_widget(btn29)
        self.buttonsToRemove.append(btn29)

        btn538 = self.gen_button("Институт строительства и транспортной инфраструктуры", 538)
        self.add_widget(btn538)
        self.buttonsToRemove.append(btn538)

        btn539 = self.gen_button("Институт механики, робототехники, инженерии траспортных и технических систем", 539)
        self.add_widget(btn539)
        self.buttonsToRemove.append(btn539)

        btn540 = self.gen_button("Институт фундаментальных наук", 540)
        self.add_widget(btn540)
        self.buttonsToRemove.append(btn540)

        btn541 = self.gen_button("Инженерно-технологический колледж", 541)
        self.add_widget(btn541)
        self.buttonsToRemove.append(btn541)

        btn34 = self.gen_button("Подготовительное отделения для иностранных граждан", 34)
        self.add_widget(btn34)
        self.buttonsToRemove.append(btn34)

        btn50 = self.gen_button("Новороссийский политехнический институт", 50)
        self.add_widget(btn50)
        self.buttonsToRemove.append(btn50)

        btn52 = self.gen_button("Армавирский механико-технологический институт", 52)
        self.add_widget(btn52)
        self.buttonsToRemove.append(btn52)



        btn = Button(
            text= "X",
            bold=True,
            background_color = '#00FFCE',
            size_hint = (0.05, 0.2),
            on_press=lambda x: self.returnToMain()

        )
        self.buttonsToRemove.append(btn)
        self.add_widget(btn)

    def list_kurs(self):
        self.set_data_label("Выберите курс")
        btn1 = self.gen_button("1", "&kurs=1")
        self.add_widget(btn1)
        self.buttonsToRemove.append(btn1)

        btn2 = self.gen_button("2", "&kurs=2")
        self.add_widget(btn2)
        self.buttonsToRemove.append(btn2)

        btn3 = self.gen_button("3", "&kurs=3")
        self.add_widget(btn3)
        self.buttonsToRemove.append(btn3)

        btn4 = self.gen_button("4", "&kurs=4")
        self.add_widget(btn4)
        self.buttonsToRemove.append(btn4)

        btn5 = self.gen_button("5", "&kurs=5")
        self.add_widget(btn5)
        self.buttonsToRemove.append(btn5)

        btn6 = self.gen_button("6", "&kurs=6")
        self.add_widget(btn6)
        self.buttonsToRemove.append(btn6)

        btn = Button(
            text= "X",
            bold=True,
            background_color = '#00FFCE',
            size_hint = (0.05, 0.2),
            on_press=lambda x: self.returnToMain()

        )
        self.buttonsToRemove.append(btn)
        self.add_widget(btn)

    def set_group(self, input):
        text = str(input.text)
        print(text)
        self.gen_href_inst("&gr=" + text.upper() + "&ugod=2022&semestr=2")
        self.get_data()
    def group_names(self):
        input = TextInput(
            multiline = False,
            size_hint = (1, 0.2),
            hint_text = "К примеру: 20-КБ-ПР1"
        )
        self.buttonsToRemove.append(input)
        self.add_widget(input)

        btn = Button(
            text="Вывод расписания",
            bold=True,
            background_color='#00FFCE',
            size_hint=(1, 0.5),
            on_press=lambda x: self.set_group(input)
        )
        self.buttonsToRemove.append(btn)
        self.add_widget(btn)

        btn = Button(
            text= "X",
            bold=True,
            background_color = '#00FFCE',
            size_hint = (0.05, 0.2),
            on_press=lambda x: self.returnToMain()

        )
        self.buttonsToRemove.append(btn)
        self.add_widget(btn)





    def returnToMain(self):
        self.https = "https://elkaf.kubstu.ru/timetable/default/time-table-student-ofo?iskiosk=0&fak_id="
        print(self.https)
        self.set_data_label("Kubstu")
        self.del_button(True)
        self.buttonsToRemove = []
        btnC = Button(
            text="Выбор института/факультета",
            bold=True,
            background_color='#00FFCE',
            size_hint=(1, 0.5),
            on_press=lambda x: self.callback2()
        )
        self.buttonsToRemove.append(btnC)
        self.add_widget(btnC)



# ------------------------------------------------------- #
    def get_data(self):
        print(self.https)
        try:
            response = requests.get(self.https, headers=HEADERS, verify=False)
            soup = BS(response.content, "html.parser")

            items = soup.find_all("div", {"class": "panel-collapse collapse in"})
            for item in items:
                title = item.find("h4", {"class": "panel-title"}).text
                title1 = item.find("div", {"class": "panel-body"}).text
                text1 = title.strip()
                text2 = title1.strip()
                print(text1)
                print(text2)
            kkk = text1 + text2
            self.set_data_label(kkk)
            btn = Button(
                text="X",
                bold=True,
                background_color='#00FFCE',
                size_hint=(0.05, 0.05),
                on_press = lambda x: self.returnToMain()

            )
            self.buttonsToRemove.append(btn)
            self.add_widget(btn)


        except:
            self.set_data_label("Вы неправильно ввели группу")
            self.https = self.https[:self.https.find("&gr")]
            print(self.https)
            self.del_button(True)
            self.group_names()

# ------------------------------------------------------- #


class MyApp(App):
    running = True
    title = 'Kubstu'



    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self.running = False


MyApp().run()

# id факультетов fak_id
# 495 - Институт нефти, газа и энергетики
# 516 - Институт компьютерных систем и информационной безопасности
# 490 - Институт пищевой и перерабатывающей промышленности
# 29 - Институт экономики, управления и бизнеса
# 538 - Институт строительства и транспортной инфраструктуры
# 539 - Институт механики, робототехники, инженерии траспортных и технических систем
# 540 - Институт фундаментальных наук
# 541 - Инженерно-технологический колледж
# 34 - Подготовительное отделения для иностранных граждан
# 50 - Новороссийский политехнический институт
# 52 - Армавирский механико-технологический институт
# Везде по 6 курсов