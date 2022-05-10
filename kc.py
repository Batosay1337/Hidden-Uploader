import os,requests,random,threading,time,sys,ctypes,re,urllib3
from multiprocessing.dummy import Pool,Lock
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore,Style,init
from concurrent.futures import ThreadPoolExecutor
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def Folder(directory):
  if not os.path.exists(directory):
      os.makedirs(directory)
Folder("result")

urllib3.disable_warnings()
Good = 0
x = requests.session()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path =  str(sys.argv[0]).split('\\')
    exit('\n  [!] python3 '+path[len(path)-1]+' list.txt')

def kcf(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/admin/kcfinder/upload.php','/js/kcfinder/upload.php','/assets/admin/kcfinder/upload.php','/kcfinder/upload.php','/assets/js/kcfinder/upload.php','/admin/assets/js/ckeditor/kcfinder/upload.php','/ckeditor/plugins/kcfinder/upload.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req_first = x.get(url, headers=head)
            if 'alert("Unknown error");' in req_first.text :
                print(fg+"Found KCF >> "+url)
                open("result/kcfinder.txt","a").write(url+"\n")
                break
            elif "alert('Unknown error');" in req_first.text :
                print(fg+"Found KCF >> "+url)
                open("result/kcfinder.txt","a").write(url+"\n")
                break
            else :
                print(fc+""+fw+"["+fr+"X"+fw+"] "+fr+"Not Found KCF >>> "+i)
                pass
        except :
            pass

def rfm(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/filemanager/dialog.php','/assets/administrator/filemanager/dialog.php','/assets/admin/js/filemanager/dialog.php','/assets/plugins/filemanager/dialog.php','/assets/filemanager/dialog.php','/admin/tinymce/plugins/filemanager/dialog.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req_first = x.get(url, headers=head)
            if "Responsive FileManager" in req_first.text :
                print(fg+"Found RFM >> "+url)
                open("result/RFM.txt","a").write(url+"\n")
                break
            else :
                print(fc+""+fw+"["+fr+"X"+fw+"] "+fr+"Not Found RFM >>> "+i)
                pass
        except :
            pass


def exploit(i):
    try:
        kcf(i)
        rfm(i)
    except:
       pass

def rangeip(ips):
    ur = ips.rstrip()
    ch = ips.split('\n')[0].split('.')
    ip1 = ch[0]
    ip2 = ch[1]
    ip3 = ch[2]
    taz = str(ip1) + '.' + str(ip2) + '.'
    i = 0
    while i <= 255:
        i += 1
        c = 0
        while c <= 255:
            c += 1
            print ("Ranging ==>" + str(taz) + str(c) + '.' + str(i))
            open('rangeip.txt', 'a').write(str(taz) + str(c) + '.' + str(i) + '\n')

def revip(ip):
	try:
		onx = requests.get("https://diskominfo.sampangkab.go.id/twibbon/assets/upload/rev.php/?ip=" + ip)
		if "" in onx.text:
			print('\r\033[91m  Got Nothing\033[0m »»————> ' + ip)
		else:
			print('\r\033[92m  Got {0} Domain\033[0m »»————> {1}'.format(str(len(onx.text)), ip))
			open('domain.txt','a').write(str(onx.text.replace("cpanel.", "").replace("webmail.", "").replace("autodiscover.", "").replace("webdisk.", "").replace("www.", "").replace("mail.", "").replace("ns.", "").replace("ns1.", "").replace("webmaster.", "").replace("cpcontacts.", "").replace("hostmaster.", "").replace("cpcalendars.", "").replace("ns2.", "").replace("ftp.", "").replace("max.", "").replace("whm.", "").replace("smtp.", "").replace("ns1.", "").replace("ns2.", "").replace("ns3.", "").replace("ns4.", "").replace("cdn.", "").replace("mta-sts.", ""))+'\n')
	except:
		pass

if __name__ == "__main__":
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """\n
          \\\|||||//         
          (  O O  )          
|--ooO-------(_)------------|
|                           |
| AutoXploiter Bot By RzkyO |
|                           |
|----------------------Ooo--|
          |__||__|           
           ||  ||            
          ooO  Ooo           
"""
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )
    p = Pool(30)
    p.map(exploit, target)
    p.close()
    p.join()
    print("""\n
          \\\|||||//         
          (  O O  )          
|--ooO-------(_)------------|
|                           |
|        DONE MASZEH        |
|                           |
|----------------------Ooo--|
          |__||__|           
           ||  ||            
          ooO  Ooo           
""")
    x = requests.session()
