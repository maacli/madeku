
# 爬取豆瓣电影top250的链接、图片、片名、评分


from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error

import sqlite3      #进行sqlite3数据库操作


def main():
    baseurl="https://movie.douban.com/top250"
    #爬取网页
    datalist=getData(baseurl)

    #保存数据
    savepath=".\\豆瓣电影top250.xls"
    #saveData(savepath)

    #askURL("https://movie.douban.com/top250")
#影片链接
findlink=re.compile(r'<a href="(.*?)>')
#影片图片
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)
#影片片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)')
'''
#找到评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片相关内容
findBd=re.compile(r'<p class="">(.*)</p>',re.S)
'''

# 爬取网页
def getData(baseurl):
	datalist=[]
    for i in range(0,10):     #调用获取页面信息的函数，10次
        url=baseurl+str(i*25)
        html=askURL(url)        #保存获取到的网页源码

        # 逐一解析数据
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class="item"):
            data=[]
            item=str(item)
            link=re.findall(findlink,item)[0]
            data.append(link)
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles=re.findall(findTitle,item)
            if(len(titles)==2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')
            rating=re.findall(findRating,item)[0]
            data.append(rating)

            datalist.append(data)


	return datalist


# 保存数据
def saveData(savepath):
    print("save")

# 得到一个指定URL的网页内容
def askURL(url):
	head={			#模拟浏览器头部信息，向豆瓣服务器发送消息
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
	}			#用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器
	request=urllib.request.Request(url,headers=head)

    html = ""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
        print(e.code)
        if hasattr(e,"reason"):
        print(e.reason)

    return html


if __name__ == "__main__":          #当程序执行时
    #调用函数
    main()