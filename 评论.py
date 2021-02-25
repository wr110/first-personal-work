#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#腾讯视频爬取评论
import urllib.request
import re
import urllib.error
import ssl            
ssl._create_default_https_context = ssl._create_unverified_context
 
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0')  #User agent
opener=urllib.request.build_opener()#添加对应的报头信息
opener.addheaders=[headers]
urllib.request.install_opener(opener)
comid='6716721678028090367'
url='https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+comid+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1614215427851'
for i in range(0,10):
     try:
          data=urllib.request.urlopen(url).read().decode()
          patnext='"last":"(.*?)"'
          nextid=re.compile(patnext).findall(data)[0]
          patcom='"content":"(.*?)",'
          comdata=re.compile(patcom).findall(data)     
          for j in range(0,len(comdata)):

               print (eval("u'"+comdata[j]+"'"))   
          url='https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+nextid+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1614215427851'
          with open('comment.json','a',encoding='utf-8') as file:
                 file.write(str(comdata))
     except urllib.error.URLError as e:
          if hasattr(e,'code'): #判断对象是否包含对应属性
               print(e.code)
          if hasattr(e,'reason'):
               print(e.reason)

