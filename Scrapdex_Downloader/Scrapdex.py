from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import base64
import sys
import os
import re
# import urllib.request
# from multiprocessing import Process
# from selenium.webdriver.common.action_chains import ActionChains
# import requests
# import json
# from requests import Session

path=''
gpcnt=1
driver_list = []

def get_script_folder():
    if getattr(sys, 'frozen', False):
        script_path = os.path.dirname(sys.executable)
    else:
        script_path = os.path.dirname(
            os.path.abspath(sys.modules['__main__'].__file__)
        )
    return script_path

def get_data_folder():
    if getattr(sys, 'frozen', False):
        data_folder_path = sys._MEIPASS
    else:
        data_folder_path = os.path.dirname(
            os.path.abspath(sys.modules['__main__'].__file__)
        )
    return data_folder_path

def get_html(url):
    curr_file = os.path.abspath(__file__)
    dir_nm = os.path.dirname(curr_file)
    gecko_path = dir_nm+'\\geckodriver.exe'
    service = Service(executable_path=gecko_path)
    os.environ['MOZ_HEADLESS'] = '1'
    with webdriver.Firefox(service=service) as driver:
        # WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')
        # # time.sleep(4)
        try:
            driver.get(url)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(7) > div.grid.gap-2.two-col > div:nth-child(1) > div.stats > div:nth-child(1)')))
            # time.sleep(4)
            html_text = driver.page_source
        except Exception as e:
            print(e)
        finally:
            driver_list.append(driver)
            return html_text
            # session = requests.Session()
            # for cookie in driver.get_cookies():
            #     session.cookies.set(cookie['name'], cookie['value'])

def get_downloader_html(url):
    curr_file = os.path.abspath(__file__)
    dir_nm = os.path.dirname(curr_file)
    gecko_path = dir_nm+'\\geckodriver.exe'
    service = Service(executable_path=gecko_path)
    os.environ['MOZ_HEADLESS'] = '1'
    with webdriver.Firefox(service=service) as driver:
        try:
            driver.get(url)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.flex-col > div.rounded.flex.flex-col.gap-2')))
            time.sleep(3)
            html_text = driver.page_source
        except Exception as e:
            print(e)
        finally:
            driver_list.append(driver)
            return html_text
def downloader_pg_chg(url,cng):
    curr_file = os.path.abspath(__file__)
    dir_nm = os.path.dirname(curr_file)
    gecko_path = dir_nm+'\\geckodriver.exe'
    service = Service(executable_path=gecko_path)
    global gpcnt
    os.environ['MOZ_HEADLESS'] = '1'
    if cng=='p':
        if gpcnt==1:
            print('\nYou are on the first page\n')
            return get_downloader_html(url)
        else:
             with webdriver.Firefox(service=service) as driver:
                try:
                    # driver.maximize_window()
                    driver.get(url)
                    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                    button = driver.find_element(By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.justify-center.flex-wrap.gap-2.mt-6 > button:nth-child(5)')
                    button.click()
                    textbox = driver.find_element(By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.justify-center.flex-wrap.gap-2.mt-6 > input')
                    gpcnt-=1
                    textbox.send_keys(str(gpcnt))
                    textbox.send_keys(Keys.RETURN)
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.flex-col > div.rounded.flex.flex-col.gap-2')))
                except Exception as e:
                    print(e)
                finally:
                    driver_list.append(driver)
                    html_text = driver.page_source
                    return html_text
    elif cng=='n':
        with webdriver.Firefox(service=service) as driver:
                try:
                    # driver.maximize_window()
                    driver.get(url)
                    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                    button = driver.find_element(By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.justify-center.flex-wrap.gap-2.mt-6 > button:nth-child(5)')
                    button.click()
                    textbox = driver.find_element(By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.justify-center.flex-wrap.gap-2.mt-6 > input')
                    gpcnt+=1
                    textbox.send_keys(str(gpcnt))
                    textbox.send_keys(Keys.RETURN)
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div:nth-child(9) > div.flex.gap-6.items-start > div.flex-grow > div:nth-child(2) > div.flex.flex-col > div.rounded.flex.flex-col.gap-2')))
                except Exception as e:
                    print(e)
                finally:
                    driver_list.append(driver)
                    html_text = driver.page_source
                    return html_text
    else:
        print("Invalid input")
        return

def dnmgpg(url):
    curr_file = os.path.abspath(__file__)
    dir_nm = os.path.dirname(curr_file)
    gecko_path = dir_nm+'\\geckodriver.exe'
    service = Service(executable_path=gecko_path)
    os.environ['MOZ_HEADLESS'] = '1'
    with webdriver.Firefox(service=service) as driver:
        try:
            driver.get(url)
            # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'stats')))
            element = driver.find_element(By.CSS_SELECTOR, 'div[data-v-15b67c8b]')
            text = element.text.split('\n')
            # print((text[2])
            j=-1
            # print(text[1])
            for i in range(int(text[1])):
                j+=1
                print(f'Downloading page {i+1} of {text[1]}')
                # if (i)%2==0 and i!=0:
                #     driver.get(url+'/{}'.format(i+1))
                #     if j>=4:
                #         j=2
                #     time.sleep(2.5)
                if(i==2):
                    driver.get(url+'/{}'.format(i+1))
                    # time.sleep(1)
                if((i)%5==0 and i!=0): #sliding window approach
                    driver.get(url+'/{}'.format(i+2))
                    j=0
                    # time.sleep(1)
                css_sel='#__nuxt > div.flex.flex-grow.text-color > div.flex.flex-col.flex-grow > div.md-content.flex-grow > div > div.md--reader-chapter > div.min-w-0.relative.pages-wrap.md--reader-pages > div.overflow-x-auto.flex.items-center.h-full > div > img:nth-child('+str(j+1)+')'
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_sel)))
                # print(css_sel)
                img=driver.find_element(By.CSS_SELECTOR, css_sel)
                # src=img.get_attribute('src')
                # imgnm=str(i+1)+'.png'
                # urllib.request.urlretrieve(src, os.path.join('test', imgnm))
                blob_url = img.get_attribute('src')
                script = f'''
                var xhr = new XMLHttpRequest();
                xhr.open('GET', '{blob_url}', true);
                xhr.responseType = 'blob';
                xhr.onload = function(e) {{
                    if (this.status == 200) {{
                        var blob = this.response;
                        var reader = new FileReader();
                        reader.readAsDataURL(blob);
                        reader.onloadend = function() {{
                            var base64data = reader.result;
                            document.body.setAttribute('data-base64', base64data);
                        }}
                    }}
                }};
                xhr.send();
                '''
                driver.execute_script(script)
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body[data-base64]')))
                data_url = driver.find_element(By.CSS_SELECTOR, 'body').get_attribute('data-base64')

                # Download the image from the data URL
                base64_data = data_url.split(',')[1]
                image_data = base64.b64decode(base64_data)
                imgnm=str(i+1)+'.png'
                global path
                with open(os.path.join(path, imgnm), 'wb') as f:
                    f.write(image_data)
            # html_text = driver.page_source
            # hmt=BeautifulSoup(html_text, 'lxml')

        except Exception as e:
            print(e)
        finally:
            print('\n')
            driver_list.append(driver)
       
def fetch(html_text):
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)
    mag = soup.find_all('div')
    for maga in mag:
        magan=maga.find('div',class_='md-content flex-grow')
        break
    # print(magan)
    magana=magan.find_all('div',class_='page-container wide')
    # print(magana)
    dik=dict()
    i=0
    ola=[]
    score=[]
    status=[]
    for maga in magana:
        mog=maga.find_all('div',attrs={'data-v-65134efb': ''})
        for mdr in mog:
            mom=mdr.find('div',class_='grid gap-2 two-col')
            if mom is not None:
                mama=mom.find_all('div',class_='manga-card')
                if mama is not None:
                    for mag in mama:
                        magma=mag.find('a',class_='font-bold title')
                        if magma is not None:
                            ole=magma.find('span').text
                            ola.append(ole)
                            dik[i]=magma['href']
                            # print(i,':',ole,':',magma['href'])
                            i+=1
                mana=mom.find_all('div',class_='stats')
                papa=mom.find_all('div',class_='flex flex-wrap status mb-auto')
                # print(len(papa))
                for i in range(len(papa)):
                    status.append(papa[i].text)
                # print(mana[1].text)
                # print(len(mana))

                for i in range(len(mana)):
                    score.append(mana[i].text[0:4])
    return dik,ola,score,status

def downloader(html_text):
    data=[]
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)
    mag = soup.find_all('div')
    for maga in mag:
        magan=maga.find('div',class_='md-content flex-grow')
        break

    if magan is not None:
        maa=magan.find('div',class_='flex flex-col')
        maana=magan.find_all('div',class_='flex flex-col mb-6')
        # print(maana)
        for anaa in maana:
            if anaa is not None:
                manana=anaa.find_all('div',class_='bg-accent rounded-sm')
                # print(manana)
                for blade in manana:
                    ryn=blade.find('div',class_='flex').text
                    gosling=blade.find_all('div',class_='flex chapter relative read')
                    bhola=[]
                    bhola.append(ryn)
                    for gos in gosling:
                        lolo=gos.find('a',class_='flex flex-grow items-center')
                        if lolo is not None:
                            lolo2=lolo.find('img',class_='inline-block select-none flex-shrink-0 !h-5 !w-5 -mx-0.5')
                            if lolo2 is not None:
                                bhola.append([lolo2['title'],lolo['href']])
                
                    data.append(bhola)
                # print(data)

        # print(maa)
    if maa is not None:
        moon=maa.find_all('div',class_='bg-accent rounded-sm')
        # print(moon)
    for mon in moon:
        ole=mon.find('div',class_='flex').text
        ola=mon.find_all('div',class_='flex chapter relative read')
        # olaole=ola.find_all('div')
        # print(ola)
        link=[]
        link.append(ole)
        for ol in ola:
            olo=ol.find('a',class_='flex flex-grow items-center')
            lolo=olo.find('img',class_='inline-block select-none flex-shrink-0 !h-5 !w-5 -mx-0.5')
            link.append([lolo['title'],olo['href']])
        data.append(link)
    print("\nChapter:-")
    for i in range(len(data)):
        print(i+1,':',data[i][0])
    fol=input("Enter p to go to previous page\nEnter n to go to next page\nEnter the number corresponding to the chapter you want to download:")
    if fol=='p':
        downloader(downloader_pg_chg(url,'p'))
    elif fol=='n':
        downloader(downloader_pg_chg(url,'n'))
    else:
        fo=int(fol)-1
        fname = data[fo][0]
        safe_fname = re.sub(r'[<>:"/\\|?*]', '_', fname)
        global path
        path=path+'\\'+safe_fname
        print("\nAvailable languages:-")
        for i in range(1,len(data[fo])):
            print(i,':',data[fo][i][0])
        lo=int(input("Enter the number corresponding to the language you want to download:"))
        flang=data[fo][lo][0]
        safe_flang=re.sub(r'[<>:"/\\|?*]', '_', flang)
        path=path+'\\'+safe_flang
        if not os.path.exists(path):
            os.makedirs(path)
        # print("Link",data[fo][lo][1])
        url2='https://mangadex.org'+data[fo][lo][1]
        dnmgpg(url2)
    # print(data)
        # print(ola,'\n')


print("Scrapdex\n(a mangadex downloader)\nVersion:1.0\n")
op=input("\nSelect the type of operation:\n1)Search for a manga\n2)Download a manga\n3)exit\n")
if op=='1':
    str1 = input("Enter the manga name: ")
    # str1='takagi san'
    str1=str1.replace(' ','+')
    pgcnt=1
    url = f'https://mangadex.org/titles?q={str1}&page={pgcnt}&onlyAvailableChapters=false'
    print(url)
    dikk=dict()
    ole=[]
    scores=[]
    stats=[]
    dikk,ole,scores,stats=fetch(get_html(url))
    for i in range(len(ole)):
        print(i+1,':',ole[i],'\nRating:',scores[i],'\nStatus:',stats[i],'\nhttps://mangadex.org/'+dikk[i],'\n\n')
    while True:
        inp=input('Enter p to go to previous page\nEnter n to go to next page\nEnter e to exit\nEnter the manga number to download: ')
        if inp=='p':
            if pgcnt==1:
                print('\nYou are on the first page\n')
                continue
            pgcnt-=1
            url = f'https://mangadex.org/titles?q={str1}&page={pgcnt}&onlyAvailableChapters=false'
            print(url)
            dikk=dict()
            ole=[]
            scores=[]
            stats=[]
            dikk,ole,scores,stats=fetch(get_html(url))
            for i in range(len(ole)):
                print(i+1,':',ole[i],'\nRating:',scores[i],'\nStatus:',stats[i],'\nhttps://mangadex.org/'+dikk[i],'\n\n')
        elif inp=='n':
            pgcnt+=1
            url = f'https://mangadex.org/titles?q={str1}&page={pgcnt}&onlyAvailableChapters=false'
            print(url)
            dikk=dict()
            ole=[]
            scores=[]
            stats=[]
            dikk,ole,scores,stats=fetch(get_html(url))
            for i in range(len(ole)):
                print(i+1,':',ole[i],'\nRating:',scores[i],'\nStatus:',stats[i],'\nhttps://mangadex.org/'+dikk[i],'\n\n')
        elif inp=='e':
            ii=0
            for driver in driver_list:
                ii+=1
                print('Closing driver',ii)
                driver.quit()
            break
        else:
            url='https://mangadex.org'+dikk[int(inp)-1]
            fname = dikk[int(inp)-1]
            safe_fname = re.sub(r'[<>:"/\\|?*]', '_', fname)
            # curr_file = os.path.abspath(__file__)
            # dir_nm = os.path.dirname(curr_file)
            dir_nm = get_script_folder()
            pth=dir_nm+'\\Mangadex\\'+ole[int(inp)-1]
            path=pth
            downloader(get_downloader_html(url))
            ii=0
            for driver in driver_list:
                ii+=1
                print('Closing driver',ii)
                driver.quit()
            aole=input("\nDownload Finished!\nPress enter to exit...")
            break
elif op=='2':
    url=input("Enter the url of the manga: ")
    fname = url
    safe_fname = re.sub(r'[<>:"/\\|?*]', '_', fname)
    # curr_file = os.path.abspath(__file__)
    # dir_nm = os.path.dirname(curr_file)
    dir_nm = get_script_folder()
    pth=dir_nm+'\\Mangadex\\'+safe_fname
    path=pth
    downloader(get_downloader_html(url))
    ii=0
    for driver in driver_list:
        ii+=1
        print('Closing driver',ii)
        driver.quit()
    aole=input("\nDownload Finished!\nPress enter to exit...")
elif op=='3':
    exit()
else:
    print("Invalid input")
    exit()
