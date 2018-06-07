#coding:utf-8
import json

with open('squad.json', 'r') as f:
    data = json.load(f)


num=[153, 27, 347, 357, 337, 249, 180, 238, 63, 195, 128, 81, 111, 296, 48, 93, 76, 300, 92, 212]
sel=[37, 31, 14, 8, 20, 8, 19, 11, 10, 31, 11, 55, 11, 29, 54, 7, 24, 16, 42, 0]


paras=[]
for i in range(20):
    art = data['data'][num[i]]
    len_ = len(art['paragraphs'])
    paras.append(art['paragraphs'][sel[i]]['context'])


#google
from googletrans import Translator
translator = Translator()
google_paras = []
for p in paras:
    p_ = translator.translate(p,dest='zh-CN').text
    google_paras.append(p_)

for i in range(20):
    with open('google-%d-%d.txt'%(num[i],sel[i]),'w',encoding='utf-8') as f:
        f.write(google_paras[i])
        f.write('\n')

#360

from trans_360 import *
_360=[]
for p in paras:
    p_ = trans_360(p)
    _360.append(p_)
for i in range(20):
    with open('./360/360-%d-%d.txt'%(num[i],sel[i]),'w',encoding='utf-8') as f:
        f.write(_360[i])
        f.write('\n')
        

#baidu
from baidu import *
baidu=[]
for p in paras:
    p_ = baidu_trans(p)
    baidu.append(p_)

for i in range(20):
    with open('./baidu/baidu-%d-%d.txt'%(num[i],sel[i]),'w',encoding='utf-8') as f:
        f.write(baidu[i])
        f.write('\n')
#youdao

from youdao import *
youdao=[]
for p in paras:
    p_ = youdao_trans(p)
    youdao.append(p_)
for i in range(20):
    with open('./youdao/youdao-%d-%d.txt'%(num[i],sel[i]),'w',encoding='utf-8') as f:
        f.write(youdao[i])
        f.write('\n')

#sogou
from sogou_translate import SogouTranslate, SogouLanguages

trans = SogouTranslate('46e702c1c007fc126d71835585931624', 'aad32e4ec4c69b1fd1bbd119409f62cc')
sogou=[]
for p in paras:
    p_ = trans.translate(p, from_language=SogouLanguages.EN, to_language=SogouLanguages.ZH_CHS)
    time.sleep(10)
    sogou.append(p_)
for i in range(20):
    with open('./sogou/sogou-%d-%d.txt'%(num[i],sel[i]),'w',encoding='utf-8') as f:
        f.write(sogou[i])
        f.write('\n')
with open('total.txt','w',encoding='utf-8') as f:
    for i in range(20):
        f.write(paras[i])
        f.write("\n\n ======== \n\n")
        
        f.write("google:\n")
        f.write(google_paras[i])
        f.write("\n\n ======== \n\n")
        
        f.write("baidu:\n")
        f.write(baidu[i])
        f.write("\n\n ======== \n\n")
        
        f.write("youdao:\n")
        f.write(youdao[i])
        f.write("\n\n ======== \n\n")
        
        f.write("360:\n")
        f.write(_360[i])
        f.write("\n\n ======== \n\n")
        
        f.write("sogou:\n")
        f.write(sogou[i])
        f.write("\n\n ======== \n\n")
        
        f.write("\n\n ======================== \n\n")