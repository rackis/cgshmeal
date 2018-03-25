# 효암 급식봇 - modified by rackis
> 이 소스는 MIT라이선스 하에 자유롭게 이용할 수 있습니다.

### 개발 참고 사이트
* https://github.com/plusfriend/auto_reply
* http://throughkim.kr/2016/07/11/kakao-haksik/
* http://humit.tistory.com/248
* http://sigool.tistory.com/4
* https://github.com/SerenityS/kakaobot_hyoammeal - 효암급식봇
* 기타 많은 사이트들..

### 개발 환경
* PyCharm
* Git
* Raspberry pi 3 model b

### 사용 언어
* Django
* Python + venv

### 필요 모듈
* beautifulsoup4
* urllib
* lxml
* dateutil

# 설치법
## 유의사항
혹시나 아마존 AWS EC2 우분투를 이용하는 경우 로케일 문제로 오류가 잦다.
http://egloos.zum.com/killins/v/3014274를 보고 로케일을 수정하자.

### [설치 전 사전 작업]
<pre>(1). 라즈베리파이용 리눅스 라즈비안(혹은 그외 Raspberry pi에서 사용 가능한 OS) 설치.</pre>
<pre>(2). VNC활성화
라즈베리파이 Configuration에서 인터페이스 탭의 VNC를 allow 하면 작업표시줄에 아이콘이 생긴다.
VNC프로르램을 아이콘을 눌러 실행하고 옵션을 눌러 접속 비밀번호를 설정한다.
전원을 끈 후 리더기로 sd카드를 컴퓨터에 연결하여 boot/config.txt를 수정한다.

# uncomment to force a console size. By default it will be display's size minus
# overscan.
#framebuffer_width=1280
#framebuffer_height=720

에서 framebuffer앞의 #을 지우고 뒤에 해상도 값을 원하는 값으로 변경한다.
그러고 다시 라즈베리파이를 부팅한다.

--VNC로 접속--
데스크탑에서 VNC Viewer을 다운받아 설치한 후
라즈베리파이의 ip로 접속한다.</pre>
<pre>(2). 한글 설치
sudo apt-get install fonts-unfonts-core ibus ibus-hangul -y
설치가 완료되면 라즈베리파이 Configuration에서 로컬라이제이션 탭에서 로케일, 시간, 키보드를 변경한다.
언어 ko (korean)
국가 KR (South Korea) - (UTF-8)
지역 Asia
위치 Seoul
키보드 국가 Korea, Republic of [101/104 key]

설정이 완료되면 재부팅 한다.</pre>


### 1. 기초 패키지 설치
* 업데이트 실시 - 자율 실시
<pre>sudo apt-get update
sudo apt-get upgrade</pre>
* 파이썬 패키지 설치 - 라즈베리파이의 경우 미리 설치되어 있다.
<pre>sudo apt-get install python3 python3-pip python3-venv</pre>
* 깃 클론
<pre>git clone https://github.com/rackis/cgshmeal /home/pi/Desktop/KAKAO

cd /home/pi/Desktop/KAKAO  - 깃 위치로 이동</pre>
* 파이썬 가상화 실행
<pre>python3 -m venv myvenv  - 설치 처음만 실행
source myvenv/bin/activate   - 가상화 시작</pre>
* 가상화된 위치에 필요한 모듈 설치
<pre>pip install Django beautifulsoup4 python-dateutil
pip install lxml
CFLAGS="-O0"  pip install lxml      -   오래걸려도 기다리기

*아래는 lxml 설치 실패시 적용   http://lxml.de/installation.html 참고
sudo apt-get install python3-lxml -y
sudo apt-get install libxml2-dev libxslt-dev python-dev -y
pip install lxml==3.6.0</pre>

### 2. 학교 코드 수정
타학교에서 사용하기 위해선 학교 코드 수정이 필요하다.

hyoammeal/views.py를 열어보자.
```python
# 타학교에서 이용시 수정
regionCode = 'gne.go.kr'
schulCode = 'S100000492'
```
라는 코드를 발견할 수 있다.
여기서 regionCode는 각 시도교육청의 주소이며, schulCode는 [링크](http://weezzle.tistory.com/559) 를 참조하도록 하자.

### 3. 급식 정보 받아오기
* 아래 코드 입력시 급식 정보 파일 생성
<pre>python3 hyoammeal/crawl.py</pre>

* crontab을 통한 crawl.py의 주기적 실행
<pre>터미널 창에 crontab -e 입력</pre>
```
crontab -e
# 매주 일요일 0시 0분에 crawl.py 실행
0 0 * * 7 cd ~/Desktop/KAKAO/data/mealdb && /usr/bin/python3 ~/Desktop/KAKAO/cgsh/crawl.py
```

### 3-1. 시간표 출력하기
* 시간표 파일은 자신이 직접 입력해야 한다.(/data/schedb)
* 처음 해보는 거라 코드가 엉망이고, 제대로 구현하지도 못해서 3학년 5반 - 7반(이과반) 까지만 시간표를 제공할 수 있다.

### 3-2. 학사일정 출력하기
* 학사일정 파일도 자신이 직접 입력해야 한다.(/data/calendardb)
* 나이스 파싱을 하는법을 모르겠어서 그냥 txt파일로 직접 만들었다.

### 4. 마이그레이션, 서버 실행
<code>python3 manage.py migrate</code>

<code>python3 manage.py runserver 라즈베리파이아이피주소:8000</code>

아래와 같이 뜬다면 정상적으로 실행된 것이다.
<pre><code>Performing system checks...
System check identified no issues (0 silenced).
July 19, 2017 - 19:18:53
Django version 1.11.3, using settings 'kakaobot.settings'
Starting development server at http://host-ip:8000/
Quit the server with CONTROL-C.</code></pre>
여의치 않다면 127.0.0.1 루프백으로 두고 실행해서 테스트해도 된다.

**앞으로 서버 재실행시에는 터미널에서 아래 코드를 한꺼번에 붙여넣어 편리하게 사용하자.
<pre>cd /home/pi/Desktop/KAKAO
source myvenv/bin/activate
./Start.sh</pre>

### 5. 동작 확인
카카오톡 플러스친구 자동등답 API에선 http://host-ip:8000/keyboard/에 대한 반응을 필수로 요구한다.

터미널에 <code>curl -XGET 'http://host-ip:8000/keyboard/'</code>를 입력해보자.
<pre><code>serenitys@serenitys-X34:~$ curl -XGET 'http://host-ip:8000/keyboard/'
{"type": "buttons", "buttons": ["\uc870\uc2dd", "\uc911\uc2dd", "\uc11d\uc2dd", "\ub0b4\uc77c\uc758 \uc870\uc2dd", "\ub0b4\uc77c\uc758 \uc911\uc2dd", "\ub0b4\uc77c\uc758 \uc11d\uc2dd"]}</code></pre>
정상적으로 작동한다면 이와 같은 정보가 오는것을 확인할 수 있다.

또한 keyboard에서 선택한 메뉴의 응답으로 message를 반환하는데 POST형태로 서버로 요구사항을 전달하고  GET으로 정보를 받는다.
 
터미널에 
```
curl -XPOST 'http://host-ip:8000/message' -d '{ "user_key": "encryptedUserKey", "type" : "text", "content": "중식"}'
```
  를 입력해보자.
  
  <pre>serenitys@serenitys-X34:~$ curl -XPOST (생략)
{"keyboard": {"type": "buttons", "buttons": ["\uc870\uc2dd", "\uc911\uc2dd", "\uc11d\uc2dd", "\ub0b4\uc77c\uc758 \uc870\uc2dd", "\ub0b4\uc77c\uc758 \uc911\uc2dd", "\ub0b4\uc77c\uc758 \uc11d\uc2dd"]}, "message": {"text": "07\uc6d4 19\uc77c \uc218\uc694\uc77c \uc911\uc2dd \uba54\ub274\uc785\ub2c8\ub2e4. \n \n\ub098\ubb3c\ube44\ube54\ubc25/\uc57d\uace0\ucd94\uc7a5\n\uac10\uc790\ub41c\uc7a5\uad6d\n\uc18c\uc13</pre>
와 같이 반환됨을 확인함으로서 정상 작동함을 알 수 있다.

### 6. 카카오톡 플러스 친구와 연동
타게시물들을 참조하도록 하자.

## 작동 화면
