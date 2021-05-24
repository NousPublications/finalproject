# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:28:56 2020
 
@author: futur
"""
 
import os
import time
import random
import requests
import os.path
import pyperclip
import pyautogui
 
def generation_selector():
    generation_index = random.randint(0, 4)
 
    site_generations = [["loansandlaw.site", "mortgagehub.site"], 
                        ["insurancelab.site", "premiumlifeinsurance.xyz"], 
                        ["cryptocoinzforyou.xyz", "cryptoinformation.xyz"], 
                        ["findattorneyonretainer.xyz", "feministstudies.xyz"], 
                        ["howtoearnyourdegree.xyz", "artdealnearyou.xyz"]]
 
    social_entrance_one = ["https://lawandsociety.livejournal.com/342.html", 
                           "https://medium.com/law-and-society", 
                           "https://twitter.com/lawandsociety3", 
                           "https://lawandsociety1.blogspot.com/2021/03/blog-post.html", 
                           "https://www.quora.com/q/technologyandculture"]
 
    social_entrance_two = ["https://insurancelab.livejournal.com/258.html", 
                           "https://medium.com/insurance-lab", 
                           "https://twitter.com/InsuranceLab1", 
                           "https://lawandsociety1.blogspot.com/2021/05/blog-post.html", 
                           "https://insurancelab.quora.com/"]
 
    social_entrance_three = ["https://cryptocoinz.livejournal.com/368.html", 
                           "https://medium.com/crypto-coins-for-you", 
                           "https://twitter.com/CoinzYou", 
                           "https://lawandsociety1.blogspot.com/2021/05/blog-post_6.html", 
                           "https://cryptocoinzforyou.quora.com/"]
 
    social_entrance_four = ["https://find-attorney.livejournal.com/372.html", 
                           "https://medium.com/find-attorney-on-retainer", 
                           "https://twitter.com/AttorneyOn", 
                           "https://lawandsociety1.blogspot.com/2021/05/blog-post_78.html", 
                           "https://findattorneyonretainer.quora.com/"]
 
    social_entrance_five = ["https://earndegree.livejournal.com/498.html", 
                           "https://medium.com/how-to-earn-your-degree", 
                           "https://twitter.com/DegreeEarn", 
                           "https://lawandsociety1.blogspot.com/2021/05/blog-post_12.html", 
                           "https://howtoearnyourdegree.quora.com/"]
 
    social_build = [social_entrance_one, 
                    social_entrance_two, 
                    social_entrance_three, 
                    social_entrance_four, 
                    social_entrance_five]
 
    target_generation = site_generations[generation_index]
 
    site_one = target_generation[0]
    site_two = target_generation[1]
 
    return [social_build[generation_index], site_one, site_two, generation_index]
 
def browsercleanup():
    time.sleep(5)
    pyautogui.click(100, 15)
    x = 0
    while x < 6:
        site_address = "null"
        pyautogui.tripleClick(250, 50)
        pyperclip.copy('null')
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        site_address = pyperclip.paste()
        if len(site_address) > 150:
            pyautogui.keyDown('ctrl')
            pyautogui.press('f4')
            pyautogui.keyUp('ctrl')
            #time.sleep(1)
        elif generation_list[1] in site_address:
            x = x
        elif generation_list[2] in site_address:
            x = x
        elif 'null' in site_address:
            pyautogui.keyDown('ctrl')
            pyautogui.press('f4')
            pyautogui.keyUp('ctrl')
            #time.sleep(1)
        else:
            pyautogui.keyDown('ctrl')
            pyautogui.press('f4')
            pyautogui.keyUp('ctrl')
            #time.sleep(1)
        x = x + 1
        pyautogui.keyDown('ctrl')
        pyautogui.press('pgdn')
        pyautogui.keyUp('ctrl')
 
def correctproperty(property):
    pyautogui.click(100, 15)
    boolone = False
    x = 1
    site_address = "null"
    while boolone == False and x < 6:
        pyautogui.tripleClick(250, 50)
        pyperclip.copy('null')
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        site_address = pyperclip.paste()
        if len(site_address) > 150:
            pyautogui.keyDown('ctrl')
            pyautogui.press('f4')
            pyautogui.keyUp('ctrl')
            #time.sleep(1)
            pyautogui.keyDown('ctrl')
            pyautogui.press('pgdn')
            pyautogui.keyUp('ctrl')
        elif property in site_address:
            boolone = True
        else:
            pyautogui.keyDown('ctrl')
            pyautogui.press('pgdn')
            pyautogui.keyUp('ctrl')
        x = x + 1
 
def delete_old():
    if os.path.exists('C:\\Users\\futur\\ip_subset.txt'):
        os.remove('C:\\Users\\futur\\ip_subset.txt')
    if os.path.exists('C:\\Users\\futur\\master_ip_download.txt'):
        os.remove('C:\\Users\\futur\\master_ip_download.txt')
 
def get_proxy():
    #Retrieve and sort IP lists
    url = 'https://www.pastebin.com/raw/QewReu5C'
    request = requests.get(url, allow_redirects=True)
    open('master_ip_download.txt', 'wb').write(request.content)
    file = open('master_ip_download.txt')
    ip_list = file.readlines()
    subset = open("ip_subset.txt", 'a+')
    x = 0
    while x < 300:
        rand = random.randint(1, 1100)
        subset.write(ip_list[rand])
        x = x + 1
    subset.close()
    request.close()
    file.close()
 
def proxy_check_routine():
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
 
    try: 
        url = 'https://lawandsociety.site/wp-content/uploads/2021/03/Law-and-Society.jpg'
        request = requests.get(url, allow_redirects=True, timeout=3)
        open('test_image.jpg', 'wb').write(request.content)
        request.close()
        print('Attempt successful.')
        return True
    except:
        print('Attempt failed.')
        return False
    if os.path.exists('C:\\Users\\futur\\test_image.jpg'):
        os.remove('C:\\Users\\futur\\test_image.jpg')
 
def proxy_engage():
    pyautogui.click(370, 1060)
    time.sleep(3)
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(1)
    pyautogui.press('alt')
    time.sleep(1)
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('s')
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.press('alt')
    time.sleep(1)
    pyautogui.press('f')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(1)
    pyautogui.write('C:\\Users\\futur\\ip_subset.txt')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.click(20, 130)
    time.sleep(1)
    pyautogui.click(475, 130)
    time.sleep(1)
    pyautogui.press('alt')
    time.sleep(1)
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('s')
    time.sleep(1)
    pyautogui.rightClick(100, 160)
    time.sleep(1)
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(100, 160)
    index = 0
    while index < 40:
        pyautogui.press('down')
        index = index + 1
    time.sleep(1)
    pyautogui.click(315, 70)
    time.sleep(1)
    proxy_check_routine()
    bule = proxy_check_routine()
    while bule == False:
        pyautogui.press('up')
        time.sleep(1)
        pyautogui.click(315, 70)
        time.sleep(1)
        proxy_check_routine()
        bule = proxy_check_routine()
 
def proxy_manager():
    delete_old()    
    get_proxy()
    proxy_engage()
 
def tuxlerconfig():
    #Reset Tuxler Config
    pyautogui.click(170, 1060)
    time.sleep(1)
    pyautogui.click(170, 1060)
    time.sleep(1)
    pyautogui.click(170, 1060)
    time.sleep(5)
    pyautogui.click(45, 365)
    time.sleep(1)
    pyautogui.click(100, 555)
    time.sleep(1)
    pyautogui.click(45, 365)
    time.sleep(1)
    pyautogui.click(100, 535)
 
    #Open Tuxler
    pyautogui.click(170, 1060)
    time.sleep(1)
    pyautogui.click(170, 1060)
    time.sleep(1)
    pyautogui.click(170, 1060)
    time.sleep(5)
    pyautogui.click(345, 535)
    time.sleep(1)
 
    #Define Control variables
    controlvariableone = random.randint(1, 10)
    controlvariabletwo = random.randint(1, 180)
    if controlvariableone == 100:
        xcoordinate = 160
    if 1 <= controlvariableone <= 10:
        xcoordinate = 300
 
    #If Datacenter IP Address
    if controlvariableone == 100:
        #USA
        if 1 <= controlvariabletwo <= 65:
            scrollvariable = -100000
        #Australia
        if 66 <= controlvariabletwo <= 70:
            scrollvariable = 100000
        #Canada
        if 71 <= controlvariabletwo <= 75:
            scrollvariable = 100000
        #France
        if 76 <= controlvariabletwo <= 80:
            scrollvariable = 100000
        #Germany
        if 81 <= controlvariabletwo <= 85:
            scrollvariable = 100000
        #Japan
        if 86 <= controlvariabletwo <= 90:
            scrollvariable = -100000
        #Netherlands
        if 91 <= controlvariabletwo <= 95:
            scrollvariable = -100000
        #United Kingdon
        if 96 <= controlvariabletwo <= 100:
            scrollvariable = -100000            
 
    #If Residential IP Address
    if 1 <= controlvariableone <= 10:
        #USA
        if 1 <= controlvariabletwo <= 120:
            scrollvariable = -18500
        #New Zealand
        if 121 <= controlvariabletwo <= 122:
            scrollvariable = -12500
        #Australia
        if 123 <= controlvariabletwo <= 124:
            scrollvariable = -500
        #Canada
        if 125 <= controlvariabletwo <= 126:
            scrollvariable = -3000
        #France
        if 127 <= controlvariabletwo <= 128:
            scrollvariable = -6000
        #Germany
        if 129 <= controlvariabletwo <= 130:
            scrollvariable = -6500
        #Japan
        if 131 <= controlvariabletwo <= 132:
            scrollvariable = -9000
        #Netherlands
        if 133 <= controlvariabletwo <= 134:
            scrollvariable = -12500
        #United Kingdon
        if 135 <= controlvariabletwo <= 136:
            scrollvariable = -18500
 
        #Austria
        if 137 <= controlvariabletwo <= 138:
            scrollvariable = -500
        #Belgium
        if 139 <= controlvariabletwo <= 140:
            scrollvariable = -1500
        #Denmark
        if 141 <= controlvariabletwo <= 142:
            scrollvariable = -4500
        #Finland
        if 143 <= controlvariabletwo <= 144:
            scrollvariable = -6000
        #Ireland
        if 145 <= controlvariabletwo <= 146:
            scrollvariable = -8500
        #Italy
        if 147 <= controlvariabletwo <= 148:
            scrollvariable = -8500
        #Luxembourg
        if 149 <= controlvariabletwo <= 150:
            scrollvariable = -10500
        #Norway
        if 151 <= controlvariabletwo <= 152:
            scrollvariable = -13500
        #Singapore
        if 153 <= controlvariabletwo <= 154:
            scrollvariable = -15500
        #Spain
        if 155 <= controlvariabletwo <= 156:
            scrollvariable = -16500
        #Sweden
        if 157 <= controlvariabletwo <= 158:
            scrollvariable = -16500
        #Switzerland
        if 159 <= controlvariabletwo <= 160:
            scrollvariable = -16500
 
        #Argentina
        if controlvariabletwo == 161:
            scrollvariable = 0
        #Brazil
        if controlvariabletwo == 162:
            scrollvariable = -2000
        #China
        if controlvariabletwo == 163:
            scrollvariable = -3000
        #Costa Rica
        if controlvariabletwo == 164:
            scrollvariable = -3500
        #Greece
        if controlvariabletwo == 165:
            scrollvariable = -7000
        #India
        if controlvariabletwo == 166:
            scrollvariable = -8000
        #Indonesia
        if controlvariabletwo == 167:
            scrollvariable = -8000
        #Israel
        if controlvariabletwo == 168:
            scrollvariable = -8000
        #Latvia
        if controlvariabletwo == 169:
            scrollvariable = -10000
        #Lithuania
        if controlvariabletwo == 170:
            scrollvariable = -10000
        #Macedonia
        if controlvariabletwo == 171:
            scrollvariable = -11000
        #Malaysia
        if controlvariabletwo == 172:
            scrollvariable = -11000
        #Mexico
        if controlvariabletwo == 173:
            scrollvariable = -12000
        #Portugal
        if controlvariabletwo == 174:
            scrollvariable = -15000
        #Romania
        if controlvariabletwo == 175:
            scrollvariable = -15000
        #Russia
        if controlvariabletwo == 176:
            scrollvariable = -15000
        #Thailand
        if controlvariabletwo == 177:
            scrollvariable = -17000
        #Turkey
        if controlvariabletwo == 178:
            scrollvariable = -18000
        #Ukraine
        if controlvariabletwo == 179:
            scrollvariable = -18000
        #Vietnam
        if controlvariabletwo == 180:
            scrollvariable = -19000
 
    #Select Datacenter or Residential
    pyautogui.click(xcoordinate, 590)
    time.sleep(1)
 
    #Select Geolocation (Country)
    pyautogui.click(250, 720)
    time.sleep(1)
    pyautogui.moveTo(250, 850)
    time.sleep(1)
    pyautogui.scroll(100000)
    time.sleep(1)
    pyautogui.scroll(100000)
    time.sleep(1)
    pyautogui.scroll(scrollvariable)
    time.sleep(1)
    #If Residential IP Address
    if 1 <= controlvariableone <= 10:
        #USA
        if 1 <= controlvariabletwo <= 120:
            ycoordinate = 875
        #New Zealand
        if 121 <= controlvariabletwo <= 122:
            ycoordinate = 885
        #Australia
        if 123 <= controlvariabletwo <= 124:
            ycoordinate = 855
        #Canada
        if 125 <= controlvariabletwo <= 126:
            ycoordinate = 830
        #France
        if 127 <= controlvariabletwo <= 128:
            ycoordinate = 840
        #Germany
        if 129 <= controlvariabletwo <= 130:
            ycoordinate = 820
        #Japan
        if 131 <= controlvariabletwo <= 132:
            ycoordinate = 820
        #Netherlands
        if 133 <= controlvariabletwo <= 134:
            ycoordinate = 850
        #United Kingdon
        if 135 <= controlvariabletwo <= 136:
            ycoordinate = 840
 
        #Austria
        if 137 <= controlvariabletwo <= 138:
            ycoordinate = 885
        #Belgium
        if 139 <= controlvariabletwo <= 140:
            ycoordinate = 840
        #Denmark
        if 141 <= controlvariabletwo <= 142:
            ycoordinate = 850
        #Finland
        if 143 <= controlvariabletwo <= 144:
            ycoordinate = 810
        #Ireland
        if 145 <= controlvariabletwo <= 146:
            ycoordinate = 780
        #Italy
        if 147 <= controlvariabletwo <= 148:
            ycoordinate = 840
        #Luxembourg
        if 149 <= controlvariabletwo <= 150:
            ycoordinate = 850
        #Norway
        if 151 <= controlvariabletwo <= 152:
            ycoordinate = 800
        #Singapore
        if 153 <= controlvariabletwo <= 154:
            ycoordinate = 860
        #Spain
        if 155 <= controlvariabletwo <= 156:
            ycoordinate = 840
        #Sweden
        if 157 <= controlvariabletwo <= 158:
            ycoordinate = 870
        #Switzerland
        if 159 <= controlvariabletwo <= 160:
            ycoordinate = 900
 
        #Argentina
        if controlvariabletwo == 161:
            ycoordinate = 880
        #Brazil
        if controlvariabletwo == 162:
            ycoordinate = 850
        #China
        if controlvariabletwo == 163:
            ycoordinate = 890
        #Costa Rica
        if controlvariabletwo == 164:
            ycoordinate = 910
        #Greece
        if controlvariabletwo == 165:
            ycoordinate = 790
        #India
        if controlvariabletwo == 166:
            ycoordinate = 780
        #Indonesia
        if controlvariabletwo == 167:
            ycoordinate = 810
        #Israel
        if controlvariabletwo == 168:
            ycoordinate = 900
        #Latvia
        if controlvariabletwo == 169:
            ycoordinate = 770
        #Lithuania
        if controlvariabletwo == 170:
            ycoordinate = 910
        #Macedonia
        if controlvariabletwo == 171:
            ycoordinate = 800
        #Malaysia
        if controlvariabletwo == 172:
            ycoordinate = 890
        #Mexico
        if controlvariabletwo == 173:
            ycoordinate = 780
        #Portugal
        if controlvariabletwo == 174:
            ycoordinate = 760
        #Romania
        if controlvariabletwo == 175:
            ycoordinate = 820
        #Russia
        if controlvariabletwo == 176:
            ycoordinate = 860
        #Thailand
        if controlvariabletwo == 177:
            ycoordinate = 880
        #Turkey
        if controlvariabletwo == 178:
            ycoordinate = 800
        #Ukraine
        if controlvariabletwo == 179:
            ycoordinate = 860
        #Vietnam
        if controlvariabletwo == 180:
            ycoordinate = 910
 
        pyautogui.click(240, ycoordinate)
        time.sleep(1)
    #If Datacenter IP Address
    if controlvariableone == 100:
        #USA
        if 1 <= controlvariabletwo <= 65:
            ycoordinate = 900
        #Australia
        if 66 <= controlvariabletwo <= 70:
            ycoordinate = 850
        #Canada
        if 71 <= controlvariabletwo <= 75:
            ycoordinate = 830
        #France
        if 76 <= controlvariabletwo <= 80:
            ycoordinate = 840
        #Germany
        if 81 <= controlvariabletwo <= 85:
            ycoordinate = 820
        #Japan
        if 86 <= controlvariabletwo <= 90:
            ycoordinate = 820
        #Netherlands
        if 91 <= controlvariabletwo <= 95:
            ycoordinate = 810
        #United Kingdon
        if 96 <= controlvariabletwo <= 100:
            ycoordinate = 880
        pyautogui.click(240, ycoordinate)
        time.sleep(1)
    #Minimize Tuxler
    pyautogui.click(45, 365)
    time.sleep(1)
    pyautogui.click(100, 555)
    time.sleep(1)
    pyautogui.click(45, 365)
    time.sleep(1)
    pyautogui.click(100, 535)
 
def tuxleraccounts():
    #UserID and Password Comprehension
    Userid = ["danmckee03@gmail.com", "danmckee03@gmail.com", 
              "danmckee03@gmail.com", "danmckee03@gmail.com", 
              "futureslimitedco@gmail.com", "futureslimitedco@gmail.com", 
              "futureslimitedco@gmail.com", "futureslimitedco@gmail.com", 
              "danmckeex@outlook.com", "danmckeex@outlook.com", 
              "danmckeex@outlook.com", "danmckeex@outlook.com", 
              "aaronvesey@gmail.com", "aaronvesey@gmail.com", 
              "aaronvesey@gmail.com", "aaronvesey@gmail.com", 
              "futurescapecontact@gmail.com", "futurescapecontact@gmail.com", 
              "futurescapecontact@gmail.com", "futurescapecontact@gmail.com", 
              "futurescapecontact@gmail.com", "futurescapecontact@gmail.com", 
              "futurescapecontact@gmail.com", "futurescapecontact@gmail.com"]
 
    Password = ["3iubt37vq4", "3iubt37vq4", 
                "3iubt37vq4", "3iubt37vq4", 
                "duj3z4qe8p", "duj3z4qe8p", 
                "duj3z4qe8p", "duj3z4qe8p", 
                "icxpy3dn5m", "icxpy3dn5m", 
                "icxpy3dn5m", "icxpy3dn5m", 
                "FutureStudiesx09!", "FutureStudiesx09!", 
                "FutureStudiesx09!", "FutureStudiesx09!", 
                "FutureStudiesx09!", "FutureStudiesx09!", 
                "FutureStudiesx09!", "FutureStudiesx09!", 
                "FutureStudiesx09!", "FutureStudiesx09!", 
                "FutureStudiesx09!", "FutureStudiesx09!"]
 
    #Get Hour (Int)
    hour = time.strftime("%H")
    hour_int = int(hour)
 
    pyautogui.click(170, 1060)
    time.sleep(1)
    pyautogui.click(170, 1060)
    time.sleep(1)
    pyautogui.click(170, 1060)
    time.sleep(5)  
    pyautogui.click(50, 365)
    time.sleep(1)
    pyautogui.click(125, 400)
    time.sleep(1)
    pyautogui.click(230, 935)
    time.sleep(1)
    pyautogui.click(230, 720)
    time.sleep(1)
    pyperclip.copy(Userid[hour_int])
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.click(230, 760)
    time.sleep(1)
    pyperclip.copy(Password[hour_int])
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    pyautogui.click(230, 865)
    time.sleep(2)
    pyautogui.click(230, 1005)
    time.sleep(1)
    pyautogui.click(430, 365)
 
def tuxlerengage():
    #Open Tuxler
    pyautogui.click(170, 1060)
    time.sleep(2)
    pyautogui.click(170, 1060)
    time.sleep(2)
    pyautogui.click(170, 1060)
    time.sleep(2)
    pyautogui.click(345, 530)
    time.sleep(1)
 
    #Open Chrome
    pyautogui.click(220, 1060)
    time.sleep(8)
    pyautogui.click(500, 50)
    pyautogui.write('https://www.expressvpn.com/what-is-my-ip/')
    pyautogui.press('backspace')
    pyautogui.press('enter')
    time.sleep(10)
 
    #Get IP Address
    pyautogui.doubleClick(470, 510)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    ipaddress = pyperclip.paste()
    ip_list = open("IP List.txt", 'a+')
    write_expression = ipaddress + "\n"
    ip_list.write(write_expression)
    ip_list.close()
 
    #Validate IP Address
    while (ipaddress == "198.143.31.178") or (ipaddress == "73.62.240.227") or (ipaddress == "74.208.206.76") or (ipaddress == "198.251.68.55"):
        pyautogui.click(170, 1060)
        time.sleep(3)
        pyautogui.click(50, 365)
        time.sleep(1)
        pyautogui.click(100, 535)
        time.sleep(1)
        pyautogui.click(170, 1060)
        time.sleep(3)
        pyautogui.click(170, 1060)
        time.sleep(3)
        pyautogui.click(170, 1060)
        time.sleep(3)
        pyautogui.click(345, 530)
        time.sleep(1)
        pyautogui.click(220, 1060)
        pyautogui.press('f5')
        time.sleep(10)
        pyautogui.doubleClick(470, 510)
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        ipaddress = pyperclip.paste()
 
    #Close Chrome and Minimize Tuxler
    pyautogui.click(1805, 15)
    time.sleep(1)
    pyautogui.click(1805, 15)
    time.sleep(1)
    pyautogui.click(1805, 15)
    time.sleep(1)
    pyautogui.click(430, 365)
    time.sleep(1)
    pyautogui.click(430, 365)
 
def metadata():
    #Open Browsers, Incognito
    pyautogui.click(220, 1060)
    time.sleep(1)
    pyautogui.click(270, 1060)
    time.sleep(1)
    pyautogui.click(320, 1060)
    time.sleep(10)
    pyautogui.click(220, 1060)
    time.sleep(3)
    pyautogui.click(1890, 50)
    time.sleep(1)
    pyautogui.click(1890, 130)
    time.sleep(1)
    pyautogui.click(220, 1060)
    time.sleep(1)
    pyautogui.click(205, 910)
    time.sleep(1)
    pyautogui.click(270, 1060)
    time.sleep(3)
    pyautogui.click(1895, 50)
    time.sleep(1)
    pyautogui.click(1895, 130)
    time.sleep(1)
    pyautogui.click(270, 1060)
    time.sleep(1)
    pyautogui.click(250, 910)
    time.sleep(1)
    pyautogui.click(320, 1060)
    time.sleep(3)
    pyautogui.click(1890, 50)
    time.sleep(1)
    pyautogui.click(1890, 150)
    time.sleep(1)
    pyautogui.click(320, 1060)
    time.sleep(1)
    pyautogui.click(305, 910)
 
    #Create Metadata List
    Metadata = ['philpapers.org', 'quantamagazine.org', 'technologyreview.com', 
                'phys.org', 'newscientist.com', 'cnn.com', 'blogs.nature.com', 
                'blogs.scientificamerican.com', 'plato.standford.edu', 'wired.com', 
                'forbes.com', 'inverse.com', 'neurosciencenews.com', 'npr.org', 
                'theatlantic.com', 'washingtonpost.com', 'arstechnica.com', 
                'medicalexpress.com', 'newyorktimes.com', 'thehill.com', 
                'researchgate.net', 'techxplore.com', 'singularityhub.com', 
                'futurism.com', 'politico.com', 'bbc.com', 'theguardian.com', 
                'realclearpolitics.com', 'cleantechnica.com', 'aeon.co', 
                'salon.com', 'slate.com', 'thenation.com', 'consumerreports.org', 
                'jfsdigital.org', 'linkedin.com', 'sciencealert.com', 
                'sciencemag.org', 'theverge.com', 'cnet.com', 'reuters.com', 
                'apnews.com', 'futuretimeline.net', 'theconversation.com', 
                'philosophynow.org', 'newyorker.com', 'marketwatch.com', 
                'cnbc.com', 'seekingalpha.com', 'wikipedia.org']
 
    #Open Tabs and Goto Nonaligned Sites
    pyautogui.click(220, 1060)
    time.sleep(1)
    pyautogui.click(270, 15)
    time.sleep(1)
    pyautogui.click(510, 15)
    time.sleep(1)
    pyautogui.click(150, 15)
    time.sleep(1)
    pyautogui.click(500, 50)
    meta_one = random.randint(0,49)
    pyautogui.write(Metadata[meta_one])
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(350, 15)
    time.sleep(1)
    pyautogui.click(500, 50)
    meta_one = random.randint(0,49)
    pyautogui.write(Metadata[meta_one]) 
    pyautogui.press('enter')
    pyautogui.click(270, 1060)
    time.sleep(1)
    pyautogui.click(270, 15)
    time.sleep(1)
    pyautogui.click(510, 15)
    time.sleep(1)
    pyautogui.click(150, 15)
    time.sleep(1)
    pyautogui.click(500, 50)
    meta_one = random.randint(0,49)
    pyautogui.write(Metadata[meta_one])
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(350, 15)
    time.sleep(1)
    pyautogui.click(500, 50)
    meta_one = random.randint(0,49)
    pyautogui.write(Metadata[meta_one])
    pyautogui.press('enter')
    pyautogui.click(320, 1060)
    time.sleep(1)
    pyautogui.click(260, 15)
    time.sleep(1)
    pyautogui.click(500, 15)
    time.sleep(1)
    pyautogui.click(150, 15)
    time.sleep(1)
    pyautogui.click(500, 50)
    meta_one = random.randint(0,49)
    pyautogui.write(Metadata[meta_one]) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(350, 15)
    time.sleep(1)
    pyautogui.click(500, 50)
    meta_one = random.randint(0,49)
    pyautogui.write(Metadata[meta_one])
    pyautogui.press('enter')
 
def socialentrance():
    #Social Pass-through for Chrome
    social_random = random.randint(0, 4)
    pyautogui.click(220, 1060)
    time.sleep(1)
    pyautogui.click(550, 15)
    time.sleep(1)
    pyautogui.click(1000, 50)
    pyautogui.write(social_list[social_random])
    pyautogui.press('enter')
    time.sleep(20)
 
    #LiveJournal
    if social_random == 0:
        pyautogui.keyDown('ctrl')
        pyautogui.click(700, 725)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(1000, 725)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Medium
    if social_random == 1:
        pyautogui.click(1910, 1000)
        pyautogui.click(1910, 1000)
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(950, 530)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(950, 810)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Twitter
    if social_random == 2:
        pyautogui.keyDown('ctrl')
        pyautogui.click(650, 460)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(650, 480)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Blogger
    if social_random == 3:
        pyautogui.keyDown('ctrl')
        pyautogui.click(730, 270)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(730, 310)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Quora
    if social_random == 4:
        pyautogui.keyDown('ctrl')
        pyautogui.click(1200, 640)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(1200, 670)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Social Pass-through for Chromium
    social_random = random.randint(0, 4)
    pyautogui.click(270, 1060)
    time.sleep(1)
    pyautogui.click(550, 15)
    time.sleep(1)
    pyautogui.click(1000, 50)
    pyautogui.write(social_list[social_random])
    pyautogui.press('enter')
    time.sleep(20)
 
    #LiveJournal
    if social_random == 0:
        pyautogui.keyDown('ctrl')
        pyautogui.click(700, 725)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(1000, 725)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Medium
    if social_random == 1:
        pyautogui.click(1910, 1000)
        pyautogui.click(1910, 1000)
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(950, 530)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(950, 810)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Twitter
    if social_random == 2:
        pyautogui.keyDown('ctrl')
        pyautogui.click(650, 460)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(650, 480)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Blogger
    if social_random == 3:
        pyautogui.keyDown('ctrl')
        pyautogui.click(730, 270)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(730, 310)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Quora
    if social_random == 4:
        pyautogui.keyDown('ctrl')
        pyautogui.click(1200, 640)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(1200, 670)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Social Pass-through for Edge
    social_random = random.randint(0, 4)
    pyautogui.click(320, 1060)
    time.sleep(1)
    pyautogui.click(550, 15)
    time.sleep(1)
    pyautogui.click(1000, 50)
    pyautogui.write(social_list[social_random])
    pyautogui.press('enter')
    time.sleep(20)
 
    #LiveJournal
    if social_random == 0:
        pyautogui.keyDown('ctrl')
        pyautogui.click(700, 725)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(1000, 725)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Medium
    if social_random == 1:
        pyautogui.click(1910, 1000)
        pyautogui.click(1910, 1000)
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(950, 530)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(950, 810)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Twitter
    if social_random == 2:
        pyautogui.keyDown('ctrl')
        pyautogui.click(650, 460)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(650, 480)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Blogger
    if social_random == 3:
        pyautogui.keyDown('ctrl')
        pyautogui.click(730, 270)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(730, 310)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
    #Quora
    if social_random == 4:
        pyautogui.keyDown('ctrl')
        pyautogui.click(1200, 640)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.click(1200, 670)
        pyautogui.keyUp('ctrl')
        time.sleep(1)
 
def propertyentry():
    #Validate Property One on Chrome
    pyautogui.click(220, 1060)
    time.sleep(1)
    pyautogui.click(750, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'loansandlaw' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[1])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property Two on Chrome
    pyautogui.click(990, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'mortgagehub' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[2])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property One on Chromium
    pyautogui.click(270, 1060)
    time.sleep(1)
    pyautogui.click(750, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'loansandlaw' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[1])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property Two on Chromium
    pyautogui.click(990, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'mortgagehub' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[2])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property One on Edge
    pyautogui.click(320, 1060)
    time.sleep(1)
    pyautogui.click(750, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'loansandlaw' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[1])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property Two on Edge
    pyautogui.click(990, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'mortgagehub' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[2])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Delete Site_Check File
    os.remove("Site_Check.txt")
 
    #Validate Property One on Chrome
    pyautogui.click(220, 1060)
    time.sleep(1)
    pyautogui.click(750, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'loansandlaw' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[1])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property Two on Chrome
    pyautogui.click(990, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'mortgagehub' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[2])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property One on Chromium
    pyautogui.click(270, 1060)
    time.sleep(1)
    pyautogui.click(750, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'loansandlaw' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[1])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property Two on Chromium
    pyautogui.click(990, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'mortgagehub' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[2])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property One on Edge
    pyautogui.click(320, 1060)
    time.sleep(1)
    pyautogui.click(750, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'loansandlaw' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[1])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Validate Property Two on Edge
    pyautogui.click(990, 15)
    pyautogui.tripleClick(300, 50)
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    site_address = pyperclip.paste()
    site_checkfile = open("Site_Check.txt", "w")
    site_checkfile.write(site_address)
    site_checkfile.close()
    with open("Site_Check.txt", "r") as rd:
        if not 'mortgagehub' in rd.read():
            pyautogui.tripleClick(300, 50)
            #time.sleep(1)
            pyautogui.press('backspace')
            #time.sleep(1)
            pyautogui.write(generation_list[2])
            pyautogui.press('Enter')
            #time.sleep(1)
 
    #Delete Site_Check File
    os.remove("Site_Check.txt")
 
    #Scroll Property One Main Page on Chrome
    pyautogui.click(220, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
 
    #Scroll Property Two Main Page on Chrome
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
 
    #Scroll Property One Main Page on Chromium
    pyautogui.click(270, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
 
    #Scroll Property Two Main Page on Chromium
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
 
    #Scroll Property One Main Page on Edge
    pyautogui.click(320, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1100, 115)
 
    #Scroll Property Two Main Page on Edge
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1100, 115)
 
def articleread():
    #Scroll Property One Main Page on Chrome
    pyautogui.click(220, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 9):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 9):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
 
    #Scroll Property Two Main Page on Chrome
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 9):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 9):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
 
    #Scroll Property One Main Page on Chromium
    pyautogui.click(270, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 9):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 9):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
 
    #Scroll Property Two Main Page on Chromium
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 9):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 9):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
 
    #Scroll Property One Main Page on Edge
    pyautogui.click(320, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 9):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 9):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(800, 115)
 
    #Scroll Property Two Main Page on Edge
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 9):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 9):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(800, 115)
 
def exitbehavior():
    #Scroll Recent Articles and Navigate to Resources        
    #Scroll Property One Main Page on Chrome
    pyautogui.click(220, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
 
    #Scroll Property Two Main Page on Chrome
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
 
    #Scroll Property One Main Page on Chromium
    pyautogui.click(270, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
 
    #Scroll Property Two Main Page on Chromium
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
 
    #Scroll Property One Main Page on Edge
    pyautogui.click(320, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[1])
    pyautogui.click(1280, 115)
 
    #Scroll Property Two Main Page on Edge
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
    time.sleep(2)
    for x in range(0, 7):
        pyautogui.click(1910, 100)
    #time.sleep(1)
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
    time.sleep(2)
    correctproperty(generation_list[2])
    pyautogui.click(1280, 115)
 
    #Scroll Down on Resources
    #Scroll Property One Main Page on Chrome
    pyautogui.click(220, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
 
    #Scroll Property Two Main Page on Chrome
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
 
    #Scroll Property One Main Page on Chromium
    pyautogui.click(270, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
 
    #Scroll Property Two Main Page on Chromium
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
 
    #Scroll Property One Main Page on Edge
    pyautogui.click(320, 1060)
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    browsercleanup()            
    correctproperty(generation_list[1])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[1])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
 
    #Scroll Property Two Main Page on Edge
    x_1 = random.randint(50, 1850)
    y_1 = random.randint(50, 1000)
    x_2 = random.randint(250, 1500)
    y_2 = random.randint(250, 750)
    pyautogui.moveTo(x_1, y_1)
    pyautogui.moveTo(x_2, y_2, duration=0.1)
    pyautogui.click(x_2, y_2)
    time.sleep(3)
    #browsercleanup()            
    correctproperty(generation_list[2])
    pyautogui.click(1910, 1000)
    correctproperty(generation_list[2])
    for x in range(0, 7):
        pyautogui.click(1910, 1000)
 
def adclicking():
    #Click Ads on First Property
    #Column One
    link_list = ["test object"]
    pyperclip.copy("test/")
    pyautogui.click(220, 1060)
    browsercleanup()
    #time.sleep(1)
    correctproperty(generation_list[1])
    pyautogui.keyDown('ctrl')
    pyautogui.click(1720, 920)
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('ctrl')
    pyautogui.click(1850, 120)
    pyautogui.keyUp('ctrl')
    y = 1000
    while y > 300:
        pyautogui.moveTo(400, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
    #Column Two
    y = 1000
    while y > 300:
        pyautogui.moveTo(800, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
    #Column Three
    y = 1000
    while y > 300:
        pyautogui.moveTo(1200, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
    #Column Four
    y = 1000
    while y > 300:
        pyautogui.moveTo(1500, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
 
    #Click Ads on Second Property
    #Column One
    link_list = ["test object"]
    pyperclip.copy("test/")
    pyautogui.click(270, 1060)
    browsercleanup()
    #time.sleep(1)
    correctproperty(generation_list[2])
    pyautogui.keyDown('ctrl')
    pyautogui.click(1720, 920)
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('ctrl')
    pyautogui.click(1850, 120)
    pyautogui.keyUp('ctrl')
    y = 1000
    while y > 300:
        pyautogui.moveTo(400, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
    #Column Two
    y = 1000
    while y > 300:
        pyautogui.moveTo(800, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
    #Column Three
    y = 1000
    while y > 300:
        pyautogui.moveTo(1200, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
    #Column Four
    y = 1000
    while y > 300:
        pyautogui.moveTo(1500, y)
        pyautogui.click(button='right')
        pyautogui.press('e')
        link_test = pyperclip.paste()
        pyautogui.press('esc')
        if not link_test in link_list:
            pyautogui.keyDown('ctrl')
            pyautogui.click()
            pyautogui.keyUp('ctrl')
            link_list.append(link_test)
            if "test object" in link_list:
                link_list.remove("test object")
        y -= 50
 
def browserclose():
    #Exit Browseers
    time.sleep(1)
    pyautogui.click(1895, 15)
    time.sleep(1)
    pyautogui.click(1895, 15)
    time.sleep(1)
    pyautogui.click(1895, 15)
    time.sleep(1)
    pyautogui.click(1895, 15)
    time.sleep(1)
    pyautogui.click(1895, 15)
 
def proxy_close():
    os.system("TASKKILL /F /IM EPS.exe")
    os.system("powershell set-itemproperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -name ProxyEnable -value 0")
 
#Run Program
generation_selector()
generation_list = generation_selector()
social_list = generation_list[0]
generation_index = generation_list[3]
if generation_index == 1:
    proxy_manager()
else:
    tuxlerconfig()
    tuxleraccounts()
    tuxlerengage()
metadata()
socialentrance()
propertyentry()
articleread()
exitbehavior()
adclicking()
browserclose()
proxy_close()
#WindowsRestart
os.system("shutdown /r /t 1")