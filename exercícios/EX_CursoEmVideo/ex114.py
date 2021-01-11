import  urllib
import urllib.request
try:
    site = (urllib.request.urlopen("http://www.pudim.com.br").getcode())
except urllib.error.URLError:
 print('\033[0;31mo site pudim não está acessível no momento')
else:
    print('\033[0;33mconsigui acessar o site pudim com sucesso')