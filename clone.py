#<-------Imports Part Starting------->
import requests
import os
import time
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from datetime import datetime
import threading
#<-------Imports Part Ending------->
start_time = datetime.now() 
def elapsed_time():
    time_elapsed = datetime.now() - start_time 
    os.system('title Time Elapsed: {} made by 0x72'.format(str(time_elapsed).split('.')[0]))
    threading.Thread(target=elapsed_time, args=[]).start()
elapsed_time()
#<-------Get Source Starting------->
print('Insert link to page: ', end='')
link = input()
save_link = link.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '_')
if "https://" in link or "http://" in link:
    try:
        if not os.path.exists(save_link):
            os.makedirs(save_link)
        if not os.path.exists(save_link+'/javascript_files'):
                os.makedirs(save_link+'/javascript_files')
        if not os.path.exists(save_link+'/css_files'):
            os.makedirs(save_link+'/css_files')
        with requests.Session() as sess:
            sess.headers['user-agent'] = "Mozilla/5.0"
            request = sess.get(link)
            with open('{}/{}'.format(save_link,save_link), "a", encoding='utf-8', errors='ignore') as save_output:
                save_output.write(request.content.decode('utf-8'))
        soup = bs(request.content, "html.parser")

        script_files = []

        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                script_url = urljoin(link, script.attrs.get("src"))
                script_files.append(script_url)

        css_files = []

        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                css_url = urljoin(link, css.attrs.get("href"))
                css_files.append(css_url)
        for js_file in script_files:
            for_save_js = js_file.split('/')[-1]
            with open("{}/{}".format((save_link+'/javascript_files'),for_save_js), "w", encoding='utf-8',errors='ignore') as f:
                req = sess.get(js_file).content.decode('utf-8')
                f.write(req)
        with open("{}/css_files.txt".format(save_link+'/css_files'), "w", encoding='utf-8',errors='ignore') as f:
            for css_file in css_files:
                f.write(css_file+'\n')
    except Exception as e:
        print('Something went wrong, error: {}'.format(e))
        time.sleep(5)
        os._exit(0)
else:
    print('\nInvalid link format')
    time.sleep(2)
    os._exit(0)
#<-------Get Source Ending------->
print('\nDone')
input()
os._exit(0)
