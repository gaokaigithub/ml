import requests
import jieba
from bs4 import BeautifulSoup
import numpy as np

def get_urls():
    urls = []
    for i in range(1,11):
        url = 'http://yangmaojie.com/?page='+str(i)
        urls.append(url)
    return urls

def get_titles():
    urls = get_urls()
    titles = {}
    for url in urls:
        html = requests.get(url).text
        bsj = BeautifulSoup(html,'lxml')
        h2s = bsj.find_all('h2',{'class':'title'})
        for h2 in h2s:
            a1 = h2.find_all('a')[0].get_text().strip()
            a2 = h2.find_all('a')[1].get_text().strip()
            titles.setdefault(a2,'')
            titles[a2]+=a1
    print('。。。。。。。。。。。获取论坛数据完毕。。。。。。。。。')
    return titles

titles = get_titles()
#获取论坛标题的词频
def get_cipin(ti):
    all_words = {}
    tis = jieba.cut(ti)
    test_words = {}
    for t in tis:
        all_words.setdefault(t,0)
        test_words.setdefault(t,0)
        all_words[t]+=1
    return all_words,test_words
#计算余弦值
def get_cos(x,y):
    x = np.array(x)
    y = np.array(y)
    c1 = np.sum(x*y)
    c2 = np.sqrt(np.sum(x**2))
    c3 = np.sqrt(np.sum(y**2))
    cos = c1/float(c2*c3)
    return cos
#获取测试标题的词频
def get_newcipin(t1,t2):
    t2 = t2.strip()
    t2_seg = jieba.cut(t2)
    for w in t2_seg:
        if w in t1:
            t1[w]+=1
    return t1
testt = '		微博红包，试试 '
gou,gou1 = get_cipin(titles['购物活动'])
hao,hao1 = get_cipin(titles['好价'])
xin,xin1 = get_cipin(titles['信用卡'])
you,you1 = get_cipin(titles['有奖活动'])
mao,mao1 = get_cipin(titles['毛友交流'])

gou2 = get_newcipin(gou1,testt)
hao2 = get_newcipin(hao1,testt)
xin2 = get_newcipin(xin1,testt)
you2 = get_newcipin(you1,testt)
mao2 = get_newcipin(mao1,testt)

#获取相似度（余弦值）
def near(x1,x2):
    y1 = []
    y2 = []
    for k in x1.keys():
        y1.append(x1[k])
        y2.append(x2[k])
    return get_cos(y1,y2)

g = near(gou,gou2)
h = near(hao,hao2)
x = near(xin,xin2)
y = near(you,you2)
m = near(mao,mao2)
print(g)
print(h)
print(x)
print(y)
print(m)








