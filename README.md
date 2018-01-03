# Final-assignment
#期末作业
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re



user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }

for i in range(2,60):
    url = 'http://www.neihan8.com/article/index_'+str(i)+'.html'



    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()

    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
       

all_pattern = re.compile('<span>.*?<a target="_blank" title="(.*?)".*?<span class="t2">.*?>(.*?)</a>.*?<span class="t3"(.*?)</span>.*?<span class="t4"(.*?)</span>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "title:" + item[0]
    print "content:" + item[1]
    print "Point of praise:" + item[2].strip()
    print "Step number:" + item[3]
    print "Browse count:" + item[4]
    
    
    print "-----------------"

    

    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break
