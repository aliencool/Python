import re
import os
import urllib
import urllib2
import random

url = 'http://blog.csdn.net/sinyu890807/article/list/';

class Serach:
    #user_agent
    _header = ['Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30'
          ,'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
          'Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'];
    #pagecount = ����ҳ��
    def __init__(self,url,pagecount):
        self.url = url;
        self.pagecount = pagecount+1;

    def connectURL(self,page):
        print "��������....."

        head = random.choice(self._header);

        req = urllib2.Request(page);

        req.add_header('User-Agent',self._header);
        req.add_header('Host','blog.csdn.net');
        req.add_header('Referer','http://blog.csdn.net/');
        req.add_header('GET',page);
        #ҳ���ȫ������
        return urllib2.urlopen(req).read();
    

    
    def parseTolist(self,info):
        li = [];
        reg = r'<span class="link_title"><a href="(/guolin_blog/article/details/[0-9]+)">([^v]*)(?=</a>)';
        pat = re.compile(reg);#��������
        Blog_Link = re.findall(pat,info);
        #print Blog_Link;
        for i in Blog_Link:
            msg = i[1].replace("\r\n        ","");
            li.append(msg+':'+'http://blog.csdn.net'+i[0]);
        return li;
    
    def wisdomBug(self):
         #��ӡҳ��
        for k in range(1,self.pagecount):
            page = self.url+str(k);
            print '��������:'+page;
            #parese--�����б�
            info = self.connectURL(page);
            li = self.parseTolist(info);
            #save
            for i in li:
                f = open("D:\\python\\link.txt",'a');
                f.write(i+os.linesep*2);
                f.close();

Suceed = Serach(url,2);
Suceed.wisdomBug();
