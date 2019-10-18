import sys
import time
import random
import telepot
import telepot.helper
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import (
    per_chat_id, per_callback_query_origin, create_open, pave_event_space)
import bs4 as bs
import urllib.request

#opening up connection, grabbing page
source_1 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/index.aspx").read()

source_2 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/Supermarkets.aspx").read()

source_3 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/ConvenienceStores.aspx").read()

source_4 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/Lifestyle.aspx").read()

source_5 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/ComputerStore.aspx").read()

source_6 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/BookStore.aspx").read()

source_7 = urllib.request.urlopen("http://www.ntu.edu.sg/has/RnS/Pages/Travel.aspx").read()

source_8_1 = urllib.request.urlopen("http://www.ntu.edu.sg/has/FnB/Pages/NorthSpine.aspx").read()

source_8_2 = urllib.request.urlopen("http://www.ntu.edu.sg/has/FnB/Pages/SouthSpine.aspx").read()

source_8_3 = urllib.request.urlopen("http://www.ntu.edu.sg/has/FnB/Pages/HallCanteens.aspx").read()

source_8_4 = urllib.request.urlopen("http://www.ntu.edu.sg/has/FnB/Pages/AroundCampus.aspx").read()

source_9 = urllib.request.urlopen("http://www.ntu.edu.sg/has/Serv/Pages/MedicalClinic.aspx").read()

#html parsing
soup_1= bs.BeautifulSoup(source_1,"html.parser")

soup_2= bs.BeautifulSoup(source_2,"html.parser")

soup_3= bs.BeautifulSoup(source_3,"html.parser")

soup_4= bs.BeautifulSoup(source_4,"html.parser")

soup_5= bs.BeautifulSoup(source_5,"html.parser")

soup_6= bs.BeautifulSoup(source_6,"html.parser")

soup_7= bs.BeautifulSoup(source_7,"html.parser")

soup_8_1= bs.BeautifulSoup(source_8_1,"html.parser")

soup_8_2 = bs.BeautifulSoup(source_8_2,"html.parser")

soup_8_3 = bs.BeautifulSoup(source_8_3,"html.parser")

soup_8_4 = bs.BeautifulSoup(source_8_4,"html.parser")

soup_9 = bs.BeautifulSoup(source_9,"html.parser")

#1)Supermarketlinks

#Giant Express
Giant = soup_2.findAll("tbody")[0].a["href"]

#Prime Supermarket
Prime = soup_2.findAll("tbody")[1].a["href"]

#2)Convenience Stores

#Hall 2 7 eleven
Hall_2_7 = "http://maps.ntu.edu.sg/maps#q:7-Eleven - Hall 2"

#Hall 14 7 eleven
Hall_2_14 = "http://maps.ntu.edu.sg/maps#q:7-Eleven - Hall 14"

#Tanjong Hall Smart 99 Mart
Smart_99 = soup_3.findAll("tbody")[2].a["href"]


#3) Lifestyle

#Flower Cottage by Noel
Flower = soup_4.findAll("tbody")[0].a["href"]

#HerVelvetVase
Her = soup_4.findAll("tbody")[1].a["href"]

#LadyFirst
Lady = soup_4.findAll("tbody")[2].a["href"]

#Mini-Toons
Mini = soup_4.findAll("tbody")[3].a["href"]

#U-shop
U_shop = soup_4.findAll("tbody")[4].a["href"]


#4)Computer Store

#Eight Flags
Eight = soup_5.findAll("tbody")[0].a["href"]

#5)Bookstore

#Booklink Pte Ltd
Book = "http://maps.ntu.edu.sg/maps#q:Booklink Pte Ltd"

#Travel

#STA Travel
Travel = soup_7.findAll("tbody")[0].a["href"]

#4)Food and Beverage


#North Spine Plaza
north_spine = "http://maps.ntu.edu.sg/maps#q:NorthSpine"
#this represents all shops in north spine 

#South Spine
Koufu = soup_8_2.findAll("div",{"class":"estb_profile"})[0].a["href"]
Llao_llao = soup_8_2.findAll("div",{"class":"estb_profile"})[1].a["href"]

#Hall F&B
Court_1 = soup_8_3.findAll("div",{"class":"estb_profile"})[0].a["href"]

Court_2 = soup_8_3.findAll("div",{"class":"estb_profile"})[1].a["href"]

Court_4 = soup_8_3.findAll("div",{"class":"estb_profile"})[2].a["href"]

Court_9 = soup_8_3.findAll("div",{"class":"estb_profile"})[3].a["href"]

Court_11 = soup_8_3.findAll("div",{"class":"estb_profile"})[4].a["href"]

Court_13 = soup_8_3.findAll("div",{"class":"estb_profile"})[5].a["href"]

Court_14 = soup_8_3.findAll("div",{"class":"estb_profile"})[6].a["href"]

Court_16 = soup_8_3.findAll("div",{"class":"estb_profile"})[7].a["href"]

Crespion = soup_8_3.findAll("div",{"class":"estb_profile"})[8].a["href"]

North_hill = soup_8_3.findAll("div",{"class":"estb_profile"})[9].a["href"]

Top_pot = soup_8_3.findAll("div",{"class":"estb_profile"})[10].a["href"]

Spruce_North = soup_8_3.findAll("div",{"class":"estb_profile"})[11].a["href"]

#Around campus
Spruce_bistro_bar = soup_8_4.findAll("tbody")[0].a["href"]

Coffee_bean = soup_8_4.findAll("tbody")[1].a["href"]

Liho = soup_8_4.findAll("tbody")[2].a["href"]

Subway_ssc = soup_8_4.findAll("tbody")[3].a["href"]

O_brien = soup_8_4.findAll("tbody")[4].a["href"]

Co_op_cafe = soup_8_4.findAll("tbody")[5].a["href"]

Cafe_for_u = soup_8_4.findAll("tbody")[6].a["href"]

Sukho_thai = soup_8_4.findAll("tbody")[7].a["href"]


#4)Services
#Health
Medical_centre = Dental_centre = soup_9.findAll("tbody")[0].a["href"]




keyboard0 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Start', callback_data='start')],
                   ])

keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Supermarket', callback_data='supermarket')],
                   [InlineKeyboardButton(text='Convenience Stores', callback_data='Convenience')],
                   [InlineKeyboardButton(text='Lifestyle', callback_data='lifestyle')],
                   [InlineKeyboardButton(text='Computer Store', callback_data='computer')],
                   [InlineKeyboardButton(text='Bookstores', callback_data='bookstore')],
                   [InlineKeyboardButton(text='Travel', callback_data='travel')],
                   [InlineKeyboardButton(text='F&B', callback_data='fnb')],
                   [InlineKeyboardButton(text='Services', callback_data='service')],
                    ])
keyboard2 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Giant Express', callback_data='giant')],
                   [InlineKeyboardButton(text='Prime Supermarket', callback_data='prime')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
                   
keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='7-Eleven (Hall 2)', callback_data='7-11')],
                   [InlineKeyboardButton(text='7_Eleven (Hall 14)', callback_data='7-14')],
                   [InlineKeyboardButton(text='Smart99', callback_data='99')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
keyboard4 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Flower Cottage by Noel', callback_data='flower')],
                   [InlineKeyboardButton(text='HerVelvetVase', callback_data='velvet')],
                   [InlineKeyboardButton(text='LadyFirst', callback_data='lady')],
                   [InlineKeyboardButton(text='Mini Toons & More', callback_data='mini')],
                   [InlineKeyboardButton(text='U-Shop', callback_data='u-shop')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                    ])
keyboard5 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Eight Flags Computer System & Supplies', callback_data='cpu')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
keyboard6 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Booklink Pte Ltd', callback_data='booklink')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
keyboard7 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='STA Travel', callback_data='sta')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
keyboard8 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='North Spine', callback_data='ns')],
                   [InlineKeyboardButton(text='South Spine', callback_data='ss')],
                   [InlineKeyboardButton(text='Hall F&B', callback_data='hallfnb')],
                   [InlineKeyboardButton(text='Around Campus', callback_data='campus')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
keyboard9 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Medical Centre', callback_data='mc')],
                   [InlineKeyboardButton(text='Dental Centre', callback_data='dc')],
                   [InlineKeyboardButton(text='Go back', callback_data='return')],
                   ])
keyboard10 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Dunkin Donuts', callback_data='donuts')],
                   [InlineKeyboardButton(text='Each-A-Cup', callback_data='eachacup')],
                   [InlineKeyboardButton(text='KFC', callback_data='kfc')],
                   [InlineKeyboardButton(text='KFC Coffee', callback_data='kfcc')],
                   [InlineKeyboardButton(text="Long John Silver's", callback_data='ljs')],
                   [InlineKeyboardButton(text="Mcdonald's", callback_data='mac')],
                   [InlineKeyboardButton(text='Mia Pizza & Paste Express', callback_data='pizza')],
                   [InlineKeyboardButton(text='North Spine Food Court', callback_data='nsfoodcourt')],
                   [InlineKeyboardButton(text='Next', callback_data='next')],
                    ])
keyboard10_2 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Paik Bibim', callback_data='paik')],
                   [InlineKeyboardButton(text='Peach Garden Chinese Restaurant', callback_data='peach')],
                   [InlineKeyboardButton(text='Pen & Inc', callback_data='pen')],
                   [InlineKeyboardButton(text='Pizza Hut Express', callback_data='pizzahut')],
                   [InlineKeyboardButton(text='Starbucks Coffee', callback_data='starbucks')],
                   [InlineKeyboardButton(text='Subway', callback_data='subway')],
                   [InlineKeyboardButton(text='The Sandwich Guys', callback_data='sandwich')],
                   [InlineKeyboardButton(text='The Soup Spoon Union', callback_data='soup')],
                   [InlineKeyboardButton(text='Udon Noodle Bar', callback_data='udon')],
                   [InlineKeyboardButton(text='Go back', callback_data='return2')],
                    ])

keyboard11 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Koufu @ the South Spine', callback_data='koufu')],
                   [InlineKeyboardButton(text='Llao Llao', callback_data='llao')],
                   [InlineKeyboardButton(text='Go back', callback_data='return2')],
                   ])
keyboard12 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Food Court 1', callback_data='fc1')],
                   [InlineKeyboardButton(text='Food Court 2', callback_data='fc2')],
                   [InlineKeyboardButton(text='Food Court 4', callback_data='fc4')],
                   [InlineKeyboardButton(text='Food Court 9', callback_data='fc9')],
                   [InlineKeyboardButton(text='Food Court 11', callback_data='fc11')],
                   [InlineKeyboardButton(text='Food Court 13', callback_data='fc13')],
                   [InlineKeyboardButton(text='Food Court 14', callback_data='fc14')],
                   [InlineKeyboardButton(text='Food Court 16', callback_data='fc16')],
                   [InlineKeyboardButton(text='Crespion Food Court', callback_data='crespion')],
                   [InlineKeyboardButton(text='North Hill Food Court', callback_data='northhill')],
                   [InlineKeyboardButton(text='Top Pot Steamboat & Mookata', callback_data='mookata')],
                   [InlineKeyboardButton(text='Spruce Bistro', callback_data='bistro')],
                   [InlineKeyboardButton(text='Go back', callback_data='return2')],
                   ])
keyboard13 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Spruce Bistro Bar', callback_data='spruce')],
                   [InlineKeyboardButton(text='The Coffee Bean & Tea Leaf', callback_data='coffeebean')],
                   [InlineKeyboardButton(text='LiHo', callback_data='liho')],
                   [InlineKeyboardButton(text='Subway @ SSC', callback_data='subwayssc')],
                   [InlineKeyboardButton(text="O'Briens Irish Sandwich Cafe @ LKC Medicine", callback_data='obrien')],
                   [InlineKeyboardButton(text='Co-op @ NTU Cafe', callback_data='Coop')],
                   [InlineKeyboardButton(text='Cafe-for-You @ SPMS', callback_data='spms')],
                   [InlineKeyboardButton(text='Sukho Thai @ WKWSCI', callback_data='sukho')],
                   [InlineKeyboardButton(text='Go back', callback_data='return2')],
                   ])

keyboard14 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d0')],
                   ])       
keyboardd1 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d1')],
                   ])       
keyboardd2 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d2')],
                   ])       
keyboardd3 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d3')],
                   ])       
keyboardd4 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d4')],
                   ])       
keyboardd5 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d5')],
                   ])       
keyboardd6 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d6')],
                   ])       
keyboardd7 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d7')],
                   ])       
keyboardd8 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d8')],
                   ])       
keyboardd9 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d9')],
                   ])       
keyboardd10 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d10')],
                   ])       
keyboardd11 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d11')],
                   ])       
keyboardd12 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d12')],
                   ])       
keyboardd13 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d13')],
                   ])
keyboardd14 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d14')],
                   ])    
keyboardd16 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d16')],
                   ])       
keyboardd17 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d17')],
                   ])
keyboardd18 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d18')],
                   ])
keyboardd19 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d19')],
                   ])
keyboardd20 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d20')],
                   ])
keyboardd21 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d21')],
                   ])
keyboardd22 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d22')],
                   ])
keyboardd23 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d23')],
                   ])
keyboardd24 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d24')],
                   ])
keyboardd25 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d25')],
                   ])
keyboardd26 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d26')],
                   ])
keyboardd27 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d27')],
                   ])
keyboardd28 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d28')],
                   ])
keyboardd29 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d29')],
                   ])
keyboardd30 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d30')],
                   ])
keyboardd31 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d31')],
                   ])
keyboardd32 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d32')],
                   ])
keyboardd33 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d33')],
                   ])
keyboardd34 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d34')],
                   ])
keyboardd35 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d35')],
                   ])
keyboardd36 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d36')],
                   ])
keyboardd37 = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Direction', callback_data='d37')],
                   ])

class ConvoStarter(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(ConvoStarter, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        self.sender.sendMessage('Hi! Welcome to Shopbot. We bring you the latest info on retail shops in NTU!\
Please choose from the categories below and find the retail shop you want!', reply_markup=keyboard0)


class Convo(telepot.helper.CallbackQueryOriginHandler):
    def __init__(self, *args, **kwargs):
        super(Convo, self).__init__(*args, **kwargs)
        self._next = None
      

    def _show_next_option(self):
        self.editor.editMessageText('What type of store are you looking for?', reply_markup=keyboard)

    def _show_second_option(self):
        self.editor.editMessageText('What type of store are you looking for?', reply_markup=keyboard)

    def _show_third_option(self):
        self.editor.editMessageText('These are the different Supermarkets available.', reply_markup=keyboard2)

    def _show_fourth_option(self):
        self.editor.editMessageText('These are the different Convenience Stores available.', reply_markup=keyboard3)

    def _show_fifth_option(self):
        self.editor.editMessageText('These are the different Lifestyle Stores available.', reply_markup=keyboard4)

    def _show_sixth_option(self):
        self.editor.editMessageText('These are the Computer Stores available.', reply_markup=keyboard5)    
        
    def _show_seventh_option(self):
        self.editor.editMessageText('These are the Bookstores available', reply_markup=keyboard6)

    def _show_eightth_option(self):
        self.editor.editMessageText('These are the Travel stores available', reply_markup=keyboard7)

    def _show_ninth_option(self):
        self.editor.editMessageText('These are the F&B available', reply_markup=keyboard8)    

    def _show_tenth_option(self):
        self.editor.editMessageText('These are the Services available.', reply_markup=keyboard9)

    def _show_eleventh_option(self):
        self.editor.editMessageText('These are the F&B Stores available in North Spine.', reply_markup=keyboard10)

    def _show_eleventh2_option(self):
        self.editor.editMessageText('These are the F&B Stores available in North Spine.', reply_markup=keyboard10_2)      

    def _show_12th_option(self):
        self.editor.editMessageText('These are the F&B Stores available in South Spine.', reply_markup=keyboard11)

    def _show_13th_option(self):
        self.editor.editMessageText('These are the F&B Stores available at different halls.', reply_markup=keyboard12)

    def _show_14th_option(self):
        self.editor.editMessageText('These are the F&B Stores available around the campus.', reply_markup=keyboard13)    

    def _show_15th_option(self):
        self.editor.editMessageText('Giant Express,\n35 Students Walk,\nSingapore 639548,\nTel: 6791 495,\nDaily: 8am to 12 midnight', reply_markup=keyboard14)

    def _show_16th_option(self):
        self.editor.editMessageText('North Spine Pl​aza,\n50 Nanyang Avenue,\nNS3-01-26/27/28,\nSingapore 639798,\nTel: 6694 2021,\nDaily: 8​am to 9pm', reply_markup=keyboardd1)

    def _show_17th_option(self):
        self.editor.editMessageText('35 Students Walk,\nSingapore 639548,\nTel: 6791 9​​331​,\nDaily: 24 hrs', reply_markup=keyboardd2)      

    def _show_18th_option(self):
        self.editor.editMessageText('34 Nanyang Crescent\nSingapore 637634 \n Tel: 6790 1832​​ \n Mon to Fri: 10am - 8pm \n Sat, Sun & PH: Clos​ed', reply_markup=keyboardd3)

    def _show_19th_option(self):
        self.editor.editMessageText('60 Nanyang Crescent\nBlk 20B, 03-06 \nSingapore 636957 \nHp: 8508 0232​​ \nMon to Sat: 9am to 9pm \nSun: Closed \n PH: Open', reply_markup=keyboardd4)      

    def _show_20th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-11\nSingapore 639798\nTel: 6262 3346\n​​Mon to Fri: 10am - 9pm\nSat: 10am - 6pm\nSun & PH: Closed', reply_markup=keyboardd5)

    def _show_21th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-12\nSingapore 639798​​\nTel: 6262 2404/n​​Mon to Fri: 10am - 8pm\nSat: 10am - 3pm\nSun & PH: Closed', reply_markup=keyboardd6)           

    def _show_22th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-01\nSingapore 639798\nTel: 6809 3232\nMon to Fri: 10.30am - 5.30pm\nSat, Sun & PH: Closed', reply_markup=keyboardd7)      

    def _show_23th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-17/18\nSingapore 639798\nTel: 6803 8207\n​​Mon to Fri: 10am - 7pm\nSat: 10am - 2pm\nSun & PH: Closed', reply_markup=keyboardd8)

    def _show_24th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-09\nSingapore 639798\n​​Mon to Fri: 10am - 9pm\nSat: 10am -​ 6pm\nSun & PH: Closed', reply_markup=keyboardd9)

    def _show_25th_option(self):
        self.editor.editMessageText('50 Nanyang Avenue\nSS3-B3-04\nSingapore 639798\nTel: 6793 5911\nMon to Fri: 9am - 6pm\nSat: 9.30am - 1pm\nSun & PH: Closed', reply_markup=keyboardd10)      

    def _show_26th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-25\nSingapore 639798\n​Tel: ​6265 7675\nFax: 6265 7157', reply_markup=keyboardd11)

    def _show_27th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01-13\nSingapore 639798\n​Tel: 6837 0584\nMon to Fri: 10am - 7pm\nSat: 10am - 5pm\nSun &​​ PH: Closed', reply_markup=keyboardd12)

    def _show_28th_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nSingapore 639798', reply_markup=keyboardd13)

    def _show_28th2_option(self):
        self.editor.editMessageText('North Spine Plaza\n76 Nanyang Drive\nN2.1-01/1-02\nSingapore 637331', reply_markup=keyboardd13)
        
    def _show_28th3_option(self):
        self.editor.editMessageText('North Spine Plaza\n50 Nanyang Avenue\nNS3-01\nSingapore 639798', reply_markup=keyboardd13)
 
    def _show_29th_option(self):
        self.editor.editMessageText('50 Nanyang Avenue \nSS3-B4 \nSingapore 639798\nTel: 6790 0355\nMon to Fri: 7am to 9pm\nSat: 7am to 3pm\nPH: Open (except Sun)', reply_markup=keyboardd16)                                    

    def _show_29th2_option(self):
        self.editor.editMessageText('50 Nanyang Avenue \nSS3-B4 \nSingapore 639798\nTel: 6790 0355\nMon to Fri: 7am to 9pm\nSat: 7am to 3pm\nPH: Open (except Sun)', reply_markup=keyboardd14)                                    

    def _show_30th_option(self):
        self.editor.editMessageText('21  Nanyang Circle \nSingapore 639778​\nHall 1 \nTel: 6368 3353\n​Daily: 7am to 9pm\nStalls: 9 | Seating capacity: 310', reply_markup=keyboardd17)

    def _show_31th_option(self):
        self.editor.editMessageText('35 Students Walk \nSingapore 639548​\nHall 2 \nTel: 6368 3353\nDaily: 7am to 9pm\nStalls: 10 | Seating capacity: 446', reply_markup=keyboardd18)

    def _show_32th_option(self):
        self.editor.editMessageText('10  Nanyang Drive \nSingapore 637720​​\nHall 4\nHp: 8112 7239\nDaily: 7am to 9pm\nStalls: 3 | Seating capacity: 216', reply_markup=keyboardd19)

    def _show_33th_option(self):
        self.editor.editMessageText('50 Nanyang Avenue \nSingapore 639798\n​Hall 9 \nHp: 9692 3456\nDaily: 7am to 9pm\nStalls: 9 | Seating capacity: 293', reply_markup=keyboardd20)

    def _show_34th_option(self):
        self.editor.editMessageText('20 Nanyang Avenue \nSingapore 639809\nHall 11 \nHp: 9786 6726\nDaily: 7am to 9pm\nStalls: 6 | Seating capacity: 210', reply_markup=keyboardd21)

    def _show_35th_option(self):
        self.editor.editMessageText('​32 Nanyang Cresent \nSingapore 637658​\nHall 13 \nHp: 9851 0908\nDaily: 7am to 9pm\nStalls: 8 | Seating capacity: 210', reply_markup=keyboardd22)

    def _show_36th_option(self):
        self.editor.editMessageText('​34 Nanyang Crescent  \nSingapore 637634​\nHall 14 \nHp: 8112 7239\nDaily: 7am to 9pm\nStalls: 6 | Seating capacity: 270', reply_markup=keyboardd23)

    def _show_37th_option(self):
        self.editor.editMessageText('​50 Nanyang Walk  \nSingapore 639929\nHall 16 \nHp: 9450 5893\nDaily: 7am to 9pm\nStalls: 5 | Seating capacity: 304', reply_markup=keyboardd24)

    def _show_38th_option(self):
        self.editor.editMessageText('​162 Nanyang Cresent \nSingapore 637033​\nPioneer Hall \nDaily: 7am to 9pm\nStalls: 12 | Seating capacity: 408', reply_markup=keyboardd25)

    def _show_39th_option(self):
        self.editor.editMessageText('​60 Nanyang Crescent\nBlk 21A, 02-02\nSingapore 636957​\nNorth Hill Precinct \nHp​: 8508 0232\nDaily: 7am to 9pm\nStalls: 8 | Seating capacity: 440​​​', reply_markup=keyboardd26)

    def _show_40th_option(self):
        self.editor.editMessageText('60 Nanyang Crescent\nBlk 20A, 03-02\nSingapore 636957​\nNorth Hill Precinct \nHp: 8170 7730/ 8159 7135\nDaily: 11am to 9pm (including PH)\nSeating capacity: 120​​​', reply_markup=keyboardd27)

    def _show_41th_option(self):
        self.editor.editMessageText('660 Nanyang Crescent\nBlk 20A, 01-03\nSingapore 636957​\nNorth Hill Precinct [m​​​ap]\nTel: 6264 8139\nMon to Fri: 12noon to 10​pm\nSat, Sun & PH: Closed\nSeating capacity: 50​​​', reply_markup=keyboardd28)

    def _show_42th_option(self):
        self.editor.editMessageText('31 Nanyang L​ink\nSingapore 637718\nNanyang Auditorium, Level 1\nTel: 6268 5819\nMon to Fri: 11.30am to 10pm\nSun & PH: Closed\nSeating capacity: 51 (includes outdoor seating)​​​', reply_markup=keyboardd29)

    def _show_43th_option(self):
        self.editor.editMessageText('50 Nanyang Avenue\nSS1-01-05/SS1-01-05A\nSingapore 639798\nNear Nanyang Auditorium [map]\nTel: 6793 2921\nDaily: 8am to 8pm (including PH)​\nSeating capacity: 120​​​', reply_markup=keyboardd30)

    def _show_44th_option(self):
        self.editor.editMessageText('​School of Humanities and School of Social Scienc​es Atrium\n14 Nanyang Drive\nSingapore 637332\nTel: 6316 9982\nMon to Fri: 8am to 6pm\nSat, Sun & PH: Closed\nSeating capacity: 70', reply_markup=keyboardd31)

    def _show_45th_option(self):
        self.editor.editMessageText('​42 Nanyang Avenue, \nStudent Service Centre, 01-02 \nSingapore 639815\nTel: 6262 4320\nMon to Fri: 8am to 5.30pm\nSat, Sun & PH:​ Closed\nSeating capacity: 12', reply_markup=keyboardd32)

    def _show_46th_option(self):
        self.editor.editMessageText('​Lee Kong Chian School of Medicine \nExperimental Medicine Building \n59 Nanyang Drive​\nLevel 3, Singapore 636921\nTel: 6255 1950\nMon to Fri: 8am to 6pm\nSat, Sun & PH: Closed\nSeating capacity: 28', reply_markup=keyboardd33)

    def _show_47th_option(self):
        self.editor.editMessageText('​​52 Nanyang Avenue \nAtrium at The Hive, \nLevel 1, Singapore 639816\n​Mon to Fri: 9am to 2.30​pm, ​3.30pm - 7.30pm\nSat, Sun & PH: Closed\nSeating capacity (shared): 103', reply_markup=keyboardd34)

    def _show_48th_option(self):
        self.editor.editMessageText('​School of Physical & Mathematical Sciences\n21 Nanyang Link\nSingapore 637371\nTel: 6793 0065\nMon to Fri: 8am to 9pm\nSat: 8am - 3pm\nSun & PH: Closed\nSeating capacity: 40', reply_markup=keyboardd35)

    def _show_49th_option(self):
        self.editor.editMessageText('​31 Nanyang Link\nSingapore 637718\nHp: 9673 2078\nMon to Fri: 8am to 8pm\nSat: 9am - 2pm\nSun & PH: Closed\nSeating capacity: 62', reply_markup=keyboardd36)

    def _show_50th_option(self):
        self.editor.editMessageText('​University Health Services Building\n36 Nanyang Avenue\nSingapore 639801\nTel: 6793​ 6828', reply_markup=keyboardd37)


    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

        if query_data =='start':
            self._next = self._show_next_option()

        elif query_data == 'supermarket':
            self._next = self._show_third_option()

        elif query_data == 'Convenience':
            self._next = self._show_fourth_option()

        elif query_data =='lifestyle':
            self._next = self._show_fifth_option()

        elif query_data =='computer':
            self._next = self._show_sixth_option()

        elif query_data =='bookstore':
            self._next = self._show_seventh_option()
             
        elif query_data =='travel':
            self._next = self._show_eightth_option()

        elif query_data =='fnb':
            self._next = self._show_ninth_option()

        elif query_data =='service':
            self._next = self._show_tenth_option()

        elif query_data =='ns':
            self._next = self._show_eleventh_option()

        elif query_data =='ss':
            self._next = self._show_12th_option()

        elif query_data =='hallfnb':
            self._next = self._show_13th_option()

        elif query_data =='campus':
            self._next = self._show_14th_option()
    
        elif query_data =='return':
            self._next = self._show_second_option()

        elif query_data =='return2':
            self._next = self._show_ninth_option()

        elif query_data =='giant':
            self._next = self._show_15th_option()

        if query_data =='d0':
            self.editor.editMessageText(Giant)

        elif query_data =='prime':
            self._next = self._show_16th_option()

        if query_data =='d1':
            self.editor.editMessageText(Prime)

        elif query_data =='7-11':
            self._next = self._show_17th_option()

        if query_data =='d2':
            self.editor.editMessageText(Hall_2_7)

        elif query_data =='7-14':
            self._next = self._show_18th_option()

        if query_data =='d3':
            self.editor.editMessageText(Hall_2_14)

        elif query_data =='99':
            self._next = self._show_19th_option()

        if query_data =='d4':
            self.editor.editMessageText(Smart_99)

        elif query_data =='flower':
            self._next = self._show_20th_option()

        if query_data =='d5':
            self.editor.editMessageText(Flower)

        elif query_data =='velvet':
            self._next = self._show_21th_option()

        if query_data =='d6':
            self.editor.editMessageText(Her)

        elif query_data =='lady':
            self._next = self._show_22th_option()

        if query_data =='d7':
            self.editor.editMessageText(Lady)

        elif query_data =='mini':
            self._next = self._show_23th_option()

        if query_data =='d8':
            self.editor.editMessageText(Mini)

        elif query_data =='u-shop':
            self._next = self._show_24th_option()

        if query_data =='d9':
            self.editor.editMessageText(U_shop)

        elif query_data =='cpu':
            self._next = self._show_25th_option()

        if query_data =='d10':
            self.editor.editMessageText(Eight)

        elif query_data =='booklink':
            self._next = self._show_26th_option()

        if query_data =='d11':
            self.editor.editMessageText(Book)

        elif query_data =='sta':
            self._next = self._show_27th_option()

        if query_data =='d12':
            self.editor.editMessageText(Travel)

        elif query_data =='donuts':
            self._next = self._show_28th_option()

        elif query_data =='eachacup':
            self._next = self._show_28th_option()

        elif query_data =='kfc':
            self._next = self._show_28th_option()

        elif query_data =='kfcc':
            self._next = self._show_28th_option()

        elif query_data =='ljs':
            self._next = self._show_28th_option()

        elif query_data =='mac':
            self._next = self._show_28th_option()

        elif query_data =='pizza':
            self._next = self._show_28th_option()

        elif query_data =='nsfoodcourt':
            self._next = self._show_28th_option()

        elif query_data =='paik':
            self._next = self._show_28th_option()

        elif query_data =='peach':
            self._next = self._show_28th2_option()

        elif query_data =='pen':
            self._next = self._show_28th2_option()

        elif query_data =='pizzahut':
            self._next = self._show_28th2_option()

        elif query_data =='starbucks':
            self._next = self._show_28th2_option()

        elif query_data =='subway':
            self._next = self._show_28th2_option()

        elif query_data =='sandwich':
            self._next = self._show_28th3_option()

        elif query_data =='soup':
            self._next = self._show_28th3_option()

        elif query_data =='Udon':
            self._next = self._show_28th3_option()

        if query_data =='d13':
            self.editor.editMessageText(north_spine)

        elif query_data =='koufu':
            self._next = self._show_29th_option()

        elif query_data =='llao':
            self._next = self._show_29th2_option()

        if query_data =='d14':
            self.editor.editMessageText(Llao_llao)

        if query_data =='d16':
            self.editor.editMessageText(Koufu)

        elif query_data =='fc1':
            self._next = self._show_30th_option()

        if query_data =='d17':
            self.editor.editMessageText(Court_1)

        elif query_data =='fc2':
            self._next = self._show_31th_option()

        if query_data =='d18':
            self.editor.editMessageText(Court_2)

        elif query_data =='fc4':
            self._next = self._show_32th_option()

        if query_data =='d19':
            self.editor.editMessageText(Court_4)

        elif query_data =='fc9':
            self._next = self._show_33th_option()

        if query_data =='d20':
            self.editor.editMessageText(Court_9)

        elif query_data =='fc11':
            self._next = self._show_34th_option()

        if query_data =='d21':
            self.editor.editMessageText(Court_11)

        elif query_data =='fc13':
            self._next = self._show_35th_option()

        if query_data =='d22':
            self.editor.editMessageText(Court_13)

        elif query_data =='fc14':
            self._next = self._show_36th_option()

        if query_data =='d23':
            self.editor.editMessageText(Court_14)

        elif query_data =='fc16':
            self._next = self._show_37th_option()

        if query_data =='d24':
            self.editor.editMessageText(Court_16)

        elif query_data =='crespion':
            self._next = self._show_38th_option()

        if query_data =='d25':
            self.editor.editMessageText(Crespion)

        elif query_data =='northhill':
            self._next = self._show_39th_option()

        if query_data =='d26':
            self.editor.editMessageText(North_hill)

        elif query_data =='mookata':
            self._next = self._show_40th_option()

        if query_data =='d27':
            self.editor.editMessageText(Top_pot)

        elif query_data =='bistro':
            self._next = self._show_41th_option()

        if query_data =='d28':
            self.editor.editMessageText(Spruce_North)

        elif query_data =='spruce':
            self._next = self._show_42th_option()

        if query_data =='d29':
            self.editor.editMessageText(Spruce_bistro_bar)

        elif query_data =='coffeebean':
            self._next = self._show_43th_option()

        if query_data =='d30':
            self.editor.editMessageText(Coffee_bean)

        elif query_data =='liho':
            self._next = self._show_44th_option()

        if query_data =='d31':
            self.editor.editMessageText(Liho)

        elif query_data =='subwayssc':
            self._next = self._show_45th_option()

        if query_data =='d32':
            self.editor.editMessageText(Subway_ssc)

        elif query_data =='obrien':
            self._next = self._show_46th_option()

        if query_data =='d33':
            self.editor.editMessageText(O_brien)

        elif query_data =='Coop':
            self._next = self._show_47th_option()

        if query_data =='d34':
            self.editor.editMessageText(Co_op_cafe)

        elif query_data =='spms':
            self._next = self._show_48th_option()

        if query_data =='d35':
            self.editor.editMessageText(Cafe_for_u)

        elif query_data =='sukho':
            self._next = self._show_49th_option()

        if query_data =='d36':
            self.editor.editMessageText(Sukho_thai)

        elif query_data =='mc':
            self._next = self._show_50th_option()

        elif query_data =='dc':
            self._next = self._show_50th_option()

        if query_data =='d37':
            self.editor.editMessageText(Medical_centre)

        elif query_data =='next':
            self._next = self._show_eleventh2_option()



TOKEN = '885760516:AAEjQvzf89OlPlwv6bzQ_T8IUNYTMcRnlHk'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, ConvoStarter, timeout=30),
    pave_event_space()(
        per_callback_query_origin(), create_open, Convo, timeout=30),
])

MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(30)
