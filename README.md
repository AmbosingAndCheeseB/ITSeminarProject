# SALES COMBINE  
*****
## Feature
sales combine은 직구 세일 정보나 하드웨어 세일 정보를 한 곳에 모아 놓은 사이트입니다.    
sales combine에서 크롤링한 사이트들은 시간 한정 특가인 경우와 할인 코드를 모아놓은 사이트들이 대부분입니다.  
평소에 사고 싶은 것이 있었던 사람들은 이번 기회에 직구를 통해서나 타임 세일로 저렴하게 구매해봅시다!    
운영체제 환경은 Ubuntu 16.04로 진행했습니다.    
*****  
  
   
## Bulit With
 - Python3
 - MySQL
 - PHP
 - Shell script  
  
  
  
*****
## Installation  
  
  
#### Server install  






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
  
  
  
   
#### Python Module Installation 
  
 - 여기에 제공된 크롤러를 사용하려면 설치해야할 모듈들이 존재한다. 
   
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

####  
- 크롤링을 할 때에 동적 크롤링을 해야할 때가 있는데 이 때 selenium과 phantom.js가 필요하다.   
####  
####  
5. selenium install   
 ```sh
$ pip3 install selenium
```  
####  
6. phantom.js install   
 ```sh
$ apt-get install -y wget libfontconfig
$ mkdir -p /home/root/src && cd $_
$ wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
$ tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
$ cd phantomjs-2.1.1-linux-x86_64/bin/
$ cp phantomjs /usr/local/bin/ 
```
*****  
## How to use?  
1. 위의 설치해야할 것들을 먼저 다 설치한 후 python 문서에 대해서 수정할 것이 있습니다.  
   `pymysql.connect(host = 'localhost',port = 3306, user = 'user_name', password = 'password', db = 'db_name', charset='utf8')`   
<p><br></p>
`webdriver.PhantomJS('phantomjs가 있는 경로/phantomjs')`  
<p><br></p>
   - 이 내용을 자신의 데이터베이스에 맞게 수정해 주세요.  
<p><br></p>
   - phantomjs 경로를 잘 설정하지 않으면 crontab으로 주기적인 실행할 때 오류가 발생할 수 있습니다.
<p><br></p>
2. DB Schema를 생성하세요.  
 - 우리가 사용한 DB Schema  

3. python3 code를 쉘 스크립트로 실행  
```sh
$ sh forWeb.sh
```  
 - 이 안에 python code들을 실행하는 Shell Script가 들어있습니다.  
<p><br></p>
 4. Webpage 구성  
<p><br></p>  
 - apach2/html/ <-- 이곳에 웹페이지 코드들을 넣어주세요.  
<p><br></p>
 - 그 외에 필요한 이미지 파일 등은 경로를 잘 설정해주세요.  
<p><br></p>
 5. crontab 설정  
<p><br></p>
- root 권한에서  
<p><br></p>  
```sh
$ crontab -e
```  
<p><br></p>
  
`0 */6 * * * /쉘 스크립트 경로/example.sh >> /로그를 남기고 싶은 경로/status_check.log 2>&1`  
  
- 이 프로젝트는 6시간마다 크롤링을 반복하게 만들었습니다.  
*****  
  
## Author
 - Kim SeongYeon  
 - Yang JiWon  
  
*****
## Site
 - http://106.10.37.140/
 - 서버는 불안정합니다. 😭😭😭😭😭😭😭😭😭





