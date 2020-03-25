# -*- coding: UTF-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import os
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"g:/covid notification/download.ico",
        timeout=10
    )

def getHtmlData(url):
    r=requests.get(url)
    return r.text

def getdata():
    url="https://www.mohfw.gov.in/"
    myHtmlData=getHtmlData(url)

    soup=BeautifulSoup(myHtmlData,'html.parser')
    myData=""
    for tr in soup.find_all('tbody')[7].find_all('tr'):
        myData+=tr.get_text()
    myData=myData[1:]
    item=myData.split('\n\n')
    return item


#notifyMe("abs","knwdfnnbdef")
mm=0
st=[]
ti=0

# url="https://www.mohfw.gov.in/"
# myHtmlData=getHtmlData(url)

# soup=BeautifulSoup(myHtmlData,'html.parser')



#print(soup.prettify())
# cnt=0

# for table in soup.find_all('tbody')[7]:
#     print(table)
# print(cnt)


# myData=""
# for tr in soup.find_all('tbody')[7].find_all('tr'):
#     myData+=tr.get_text()
# myData=myData[1:]
# item=myData.split('\n\n')
    
item=getdata()
    
    # for it in item[:-5]:
    #     print(it.split("\n"))

    
if mm==0:
    ti=int(input("Time (in hrs) till you want to be notified: "))*3600
    # ti=int(input("Time (in hrs) till you want to be notified: "))
    gap=float(input("Enter the time (in hrs) gap you want to be notified : "))
    N =int(input("Enter no of States you Want Their Stats : "))
    print("Andhra Pradesh,Arunachal Pradesh ,Assam,Bihar,Chhattisgarh,Goa,Gujarat,Haryana,Himachal Pradesh,Jammu and Kashmir,Jharkhand,Karnataka,Kerala,Madhya Pradesh,Maharashtra,Manipur,Meghalaya,Mizoram,Nagaland,Odisha,Punjab,Rajasthan,Sikkim,Tamil Nadu,Telangana,Tripura,Uttar Pradesh,Uttarakhand,West Bengal,Andaman and Nicobar Islands,Chandigarh,Dadra and Nagar Haveli,Daman and Diu,Lakshadweep,Delhi,Puducherry")
    for i in range(N):
        l=input("State ")
        st.append(l)
mm=1
start=time.time()
while time.time()-start<ti:
    # myHtmlData=getHtmlData(url)

    # soup=BeautifulSoup(myHtmlData,'html.parser')
    # myData=""1
    
    # for tr in soup.find_all('tbody')[7].find_all('tr'):
    #     myData+=tr.get_text()
    #     myData=myData[1:]
    #     item=myData.split('\n\n')2
    item=getdata()
    states=['Uttar Pradesh','Telengana','Maharashtra']
    for it in item[:-5]:
        it_=it.split('\n')
        #print(it_)
        if it_[1] in st:
            #print(it_)
            nTitle="Total Covid-19 Cases in"
            nMessage=f"State : {it_[1]}\nIndian : {it_[2]} & Foreign : {it_[3]}\nCured : {it_[4]}\nDeath : {it_[5]}"
            notifyMe(nTitle,nMessage)
            time.sleep(5)
    it_ =item[-5]
    # print(it)
    tot_ind=it_.split('\n')[1]
    # print(tot_ind)
    it_ =item[-4]
    tot_fore=it_.split('\n')[0][:-1]
    # print(tot_fore)
    it_ =item[-3]
    cured=it_.split('\n')[1]
    it_ =item[-2]
    death=it_.split('\n')[1]
    nTitle="Covid-19 Cases in India"
    nMessage=f"Total : {int(tot_ind)}\nIndian : {int(tot_ind)-int(tot_fore)} & Foreign : {tot_fore}\nCured : {cured}\nDeath : {death}"
    notifyMe(nTitle,nMessage)
    time.sleep(5)
    # time.sleep(10)
    time.sleep(gap*3600)


os.system("taskkill /f /im Covid-19_Notification.exe")

# -*- coding: UTF-8 -*-
