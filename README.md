# SALES COMBINE  
*****

sales combine은 직구 세일 정보나 하드웨어 세일 정보를 한 곳에 모아 놓은 사이트다.  
github에 제공된 코드들은 python3와 php, mysql를 사용하여 만들었다.  
운영체제 환경은 Ubuntu 16.04로 진행했다.  
*****
#
#
#
#### 서버 설치  






1.  apache2 install  
```sh
$ apt install apache2
```



2. mysql-server install  
```sh
$ apt install mysql-server install
```


3. php install
```sh
$ apt install php-mysql
```
#
#
*****
   
#### 파이썬 모듈 설치  
#
 - 여기에 제공된 크롤러를 사용하려면 설치해야할 모듈들이 존재한다. 
 #
1. pip3 install  
 ```sh
$ apt-get install python3-pip
```
2. request install  
 ```sh
$ apt-get install python3-pip
```
3. HTMLParser install  
 ```sh
$ apt-get install HTMLParser
```
   
- python과 db를 연동할 것이기에 pymysql도 설치한다.  
4. pymysql install  
 ```sh
$ pip3 install PyMySQL
```

#
- 크롤링을 할 때에 동적 크롤링을 해야할 때가 있는데 이 때 selenium과 phantom.js가 필요하다.   
#
#
5. selenium install   
 ```sh
$ pip3 install selenium
```  
#
6. phantom.js install   
 ```sh
$ apt-get install -y wget libfontconfig
$ mkdir -p /home/root/src && cd $_
$ wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
$ tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
$ cd phantomjs-2.1.1-linux-x86_64/bin/
$ cp phantomjs /usr/local/bin/ 
```



