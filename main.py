#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
import requests as req
import requests 
import urllib2
import urllib
import json
from telebot import types

bot = telebot.TeleBot("239845551:AAGrwDWVpDYtIs9QUTnp3eCkJq6K8cTfReo")



@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	itembtna = types.InlineKeyboardButton('Channel \xF0\x9F\x94\x97',url='http://telegram.me/specialteam_ch')
	b2 = types.InlineKeyboardButton("Developer", url="https://telegram.me/sudo1")
	b3 = types.InlineKeyboardButton("Git", url="https://gihub.com/")
	markup.row(itembtna,b2,b3)
	bot.reply_to(message, "سلام به مدیا بوت خوش امدی",reply_markup=markup,parse_mode='markdown',disable_web_page_preview=True)
@bot.message_handler(commands=['help'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	itembtna = types.InlineKeyboardButton('Channel \xF0\x9F\x94\x97',url='http://telegram.me/specialteam_ch')
	b2 = types.InlineKeyboardButton("Developer", url="https://telegram.me/sudo1")
	b3 = types.InlineKeyboardButton("Git", url="https://gihub.com/")
	markup.row(itembtna,b2,b3)
	bot.reply_to(message, "/gif [text] \n /qr [text] \n /stickerpro [text]",reply_markup=markup,parse_mode='markdown',disable_web_page_preview=True) 	
@bot.message_handler(commands=['gif'])
def aparat(m):
    text = m.text.replace('/gif ','')
    url = "http://www.flamingtext.com/net-fu/image_output.cgi?_comBuyRedirect=false&script=blue-fire&text={}&symbol_tagname=popular&fontsize=70&fontname=futura_poster&fontname_tagname=cool&textBorder=15&growSize=0&antialias=on&hinting=on&justify=2&letterSpacing=0&lineSpacing=0&textSlant=0&textVerticalSlant=0&textAngle=0&textOutline=off&textOutline=false&textOutlineSize=2&textColor=%230000CC&angle=0&blueFlame=on&blueFlame=false&framerate=75&frames=5&pframes=5&oframes=4&distance=2&transparent=off&transparent=false&extAnim=gif&animLoop=on&animLoop=false&defaultFrameRate=75&doScale=off&scaleWidth=240&scaleHeight=120&&_=1469943010141".format(text)
    res = urllib.urlopen(url)
    parsed_json = json.loads(res.read())
    gif = parsed_json['src']
    link = parsed_json['gimpHost']
    urllib.urlretrieve("{}".format(gif), "aaa.gif")
    bot.send_document(m.chat.id, open('aaa.gif'), caption="●︿●")          
    
    
@bot.message_handler(commands=['stickerpro'])
def aparat(m):
    text = m.text.replace('/imagepro ','')
    url = "https://assets.imgix.net/examples/clouds.jpg?blur=150&w=150&h=150&fit=crop&txt={}&txtsize=50&txtclr=blue&txtalign=middle,center&txtfont=Futura%20Condensed%20Medium&mono=ff6598cc".format(text)
    res = urllib.urlopen(url)
    urllib.urlretrieve("{}".format(url), "aaa.png")
    bot.send_sticker(m.chat.id, open('aaa.jpg'))
@bot.message_handler(commands=['qr'])
def code(message):
    text = message.text.split()[1]
    urllib.urlretrieve("https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl={}".format(text), 'qr.jpg')
    bot.send_photo(message.chat.id, open('qr.jpg'))
@bot.message_handler(commands=['imagepro'])
def aparat(m):
    text = m.text.replace('/imagepro ','')
    url = "https://assets.imgix.net/examples/clouds.jpg?blur=150&w=150&h=150&fit=crop&txt={}&txtsize=50&txtclr=blue&txtalign=middle,center&txtfont=Futura%20Condensed%20Medium&mono=ff6598cc".format(text)
    res = urllib.urlopen(url)
    urllib.urlretrieve("{}".format(url), "aaa.png")
    bot.send_photo(m.chat.id, open('aaa.jpg'), caption="در کانال ما عضو بشید @specialteam_ch \n good luck...")

bot.polling(True)
