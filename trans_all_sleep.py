#coding:utf-8
import json
import urllib.request
import execjs
import json
import time
import random
class Yuguii():

    def __init__(self):
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 

        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 

        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 

    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)

def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data

def get_result(ps):
    a = json.loads(ps)
    res = ""
    for d in a[0][:-1]:
        res += d[0]
    return res

def google_trans(content):
    time.sleep(random.randint(0,3))
    js = Yuguii()
    if len(content) > 4891:
        print("翻译文本超过限制！")
        return
    tk  = js.getTk(content)
    content = urllib.parse.quote(content)
    # print(content)
    url = "http://translate.google.com/translate_a/single?client=t" \
          "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)

    result = open_url(url)
    result = get_result(result)
    # if end > 4:
    #     print(result[4:end])
    return result
with open('squad.json', 'r') as f:
    data = json.load(f)
data = data['data']
trans_data={}
trans_data['version']='1.1'

tran_d = []
i=0
for d in data:
    print(i)
    i += 1
    art={}
    title = d['title']
    paras = d['paragraphs']
    art['title'] = title
    paras_tr = []
    for p in paras:
        p_={}
        context = p['context']
        qas = p['qas']
        p_['context'] = google_trans(context)
#         print(p_['context'])
        qas_=[]
        for q in qas:
            q_ = {}
            question = q['question']
            id_ = q['id']
            ans = q['answers']
            q_['question'] = google_trans(question)
#             print(q_['question'])
            q_['id'] = id_
            ans_=[]
            for a in ans:
                a_={}
                ans_start = a['answer_start']
                ans_text = a['text']
                a_['answer_start'] = ans_start
                a_['text'] = google_trans(ans_text)
#                 print(a_['text'])
                ans_.append(a_)
            q_['answers'] = ans_
            qas_.append(q_)
        p_['qas'] = qas_
        paras_tr.append(p_)
    art['paragraphs'] = paras_tr
    json_str = json.dumps(art)
    with open("%d.json"%(i), 'w') as f:
        json.dump(json_str, f)
    tran_d.append(art)
trans_data['data'] = tran_d
json_str = json.dumps(trans_data)
with open("total.json", 'w') as f:
    json.dump(json_str, f)