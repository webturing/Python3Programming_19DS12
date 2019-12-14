#encoding = 'utf8'
import requests
from bs4 import BeautifulSoup
from tkinter import *
import datetime

def refresh():
    pass

requests.session()
r = requests.get('http://wthrcdn.etouch.cn/WeatherApi?citykey=101020100')
#print(r.status_code)
soup = BeautifulSoup(r.text,'lxml')
#print(soup.prettify())
a = soup.find_all('city')
city = a[0].get_text()
print(a[0].get_text())
a = soup.find_all('wendu')
wendu = a[0].get_text()
print('温度为：',a[0].get_text())
a = soup.find_all('shidu')
shidu = a[0].get_text()
print('湿度为：',a[0].get_text())
a = soup.find_all('fengli')
fengli = a[0].get_text()
print('风力：',a[0].get_text())
a = soup.find_all('fengxiang')
fengxiang = a[0].get_text()
print('风向：',a[0].get_text())
a = soup.find_all('quality')
quality = a[0].get_text()
print('空气质量：',a[0].get_text())
a = soup.find_all('pm25')
pm25 = a[0].get_text()
print('PM2.5：',a[0].get_text())

date_time = datetime.datetime.now().strftime('%Y_%m_%d')
filename = date_time +'.txt'

with open(filename,'w',encoding='utf8') as f:
    f.write('城市：'+city +'\n')
    f.write('温度：'+wendu +'\n')
    f.write('湿度：'+str(shidu) +'\n')
    f.write('风力：'+ fengli +'\n')
    f.write('风向：'+ fengxiang +'\n')
    f.write('空气质量：'+quality +'\n')
    f.write('PM2.5：'+pm25 +'\n')
####下面是界面程序
gui =Tk()
gui.title("天气查询 by 刘云飞")
gui.geometry('400x320')

l_da = Label(gui,text="日期:"+date_time,font = 'Helvetica -18')
l_da.pack(side = TOP)
l_chengshi = Label(gui,text = '城市:'+city,font = 'Arial -18',width = 20,height =1)
l_chengshi.pack(side = TOP)
l_wendu = Label(gui,text = '温度:'+wendu,font = 'Helvetica -18',width = 20,height =1)
l_wendu.pack(side = TOP)
l_shidu = Label(gui,text = '湿度:'+shidu,font = 'Helvetica -18',width = 20,height =1)
l_shidu.pack(side = TOP)
l_fengx = Label(gui,text = '风向:'+fengxiang,font = 'Helvetica -18',width = 20,height =1)
l_fengx.pack(side = TOP)
l_fengli= Label(gui,text = '风力:'+fengli,font = 'Helvetica -18',width = 20,height =1)
l_fengli.pack(side = TOP)
l_qu = Label(gui,text = '空气质量:'+quality,font = 'Helvetica -18',width = 20,height =1)
l_qu.pack(side = TOP)
l_pm = Label(gui,text = 'PM2.5:'+pm25,font = 'Helvetica -18',width = 20,height =1)
l_pm.pack(side = TOP)

ref = Button(gui,text = "更新",font = 'Helvetica -18',command = refresh,activeforeground = 'white',\
             activebackground = 'green')
ref.pack(side = TOP)
gui.mainloop()
