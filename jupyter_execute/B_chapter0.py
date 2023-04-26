#!/usr/bin/env python
# coding: utf-8

# # Chapter 0. 프로그래밍 언어와 파이썬
# 
# 이 장에서는 컴퓨터, 프로그래밍 언어, 파이썬에 대해 소개한다.
# 
# 
# 

# :::{admonition} 학습목표와 기대효과 
# :class: info  
# - 학습목표
#   - 컴퓨터의 정의와 프로그래밍 언어의 개념을 이해하자.
#   - 파이썬 언어의 장점을 알아보자.
#   - 파이썬 프로그래밍 개발 환경을 알아보자.
# 
# - 기대효과
#   - 다양한 파이썬 프로그래밍 개발 환경을 이해하고 파이썬 코딩을 위한 환경을 마련할 수 있다.

# ## 컴퓨터
# 
# <!--'컴퓨터(Computer)'는 계산하는 사람 또는 기계를 의미한다. -->
# 
# <strong>컴퓨터(Computer)</strong>의 정의는 시대에 따라 다양하게 변화했지만 오늘날은 데이터와 명령어를 입력하고 저장할 수 있으며, 다양한 프로그램을 통해 신속하고 정확하게 처리하여 인간이 필요한 정보를 출력하는 정보 처리 시스템을 의미한다. 이러한 컴퓨터는 하드웨어와 소프트웨어로 구성된다.
# 
# 

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/HW_SW.png" style="width:700px;"></div>

# ### 하드웨어
# **하드웨어**는 데스크탑, 노트북, 테블릿, 스마트폰 등과 같이 컴퓨터를 구성하고 있는 기계 장치의 총칭으로 크게 본체와 주변 장치로 나뉜다. **본체**는 중앙 처리 장치(CPU, Central Processing Unit)와 주기억 장치(Main memory)로, **주변 장치**는 입·출력 장치, 보조 기억 장치 등으로 구분된다. 
#   - **중앙처리장치**: 컴퓨터 시스템을 통제하고 프로그램의 연산을 실행·처리하는 가장 핵심적인 컴퓨터의 제어 장치, 혹은 그 기능을 내장한 칩이다.
#   - **주기억장치**: 컴퓨터에서 수치·명령·자료 등을 기억하는 컴퓨터 하드웨어 장치이다.
#   - **입·출력장치**: 컴퓨터와 사용자 사이의 정보를 교환할 수 있는 장치이다. 대표적인 입출력 장치로 키보드와 모니터가 있다.
#   - **보조기억장치**: 물리적인 디스크가 연결되어 있는 기억장치이다.
# 주기억장치보다는 느리지만 컴퓨터의 전원을 끄더라도 저장된 데이터가 사라지지 않아 영구적으로 보관할 수 있다.
# 대표적으로 HDD(Hard Disk Driver)와 SSD(Solid State Driver)가 있다.
# 
# 
# 

# ::::{admonition} 참고  
# :class: info
# 개인의 코딩 목적과 프로젝트 크기에 따라 요구되는 컴퓨팅 사양이 다르겠지만,
# 여기에서 다루는 기초적인 코딩을 위해서는 
# - CPU: Dual-Core Processor 급
# - 메모리(RAM): 8GB
# - 저장장치: 250GB 정도면 충분하다.
# ::::

# ### 소프트웨어
# **소프트웨어**는 컴퓨터 하드웨어에게 필요한 기능을 수행할 수 있도록 하는 프로그램이다. **프로그램**은 특정 목적을 위해 **프로그래밍**을 통해 만든 명령어들의 모임이다. 소프트웨어는 크게 시스템 소프트웨어(System software)와 응용 소프트웨어(Application software)로 나뉜다.
#   - **시스템 소프트웨어**는 시스템 운영에 필요한 기본 환경을 제공하는 소프트웨어로, 윈도우, 맥, 리눅스 등의 운영체제(OS)가 있다.
#   - **응용 소프트웨어**는 시스템 소프트웨어 플랫폼 위에 구동되는 프로그램으로 챗팅, 문서작업, 동영상, 게임 등 특정 서비스를 위한 즉, 컴퓨터를 사용하는 목적이 되는 프로그램이다.
# 

# ## 프로그래밍 언어와 파이썬
# 
# 소프트웨어는 프로그래밍을 통해 만들어진다. 
# 
# **프로그래밍**은 수식이나 작업을 컴퓨터가 수행하기 알맞게 순서를 정하고 컴퓨터 명령 코드인 프로그래밍 언어를 이용하여 <strong>코딩(Coding)</strong>하는 작업을 총칭하여 쓰는 말이다. 구체적으로 문법(Statement, Keyword, Expression)를 이용해서 값(Data, Value)를 입력 받고, 계산/변환하고, 출력하는 흐름을 만드는 일이다. 
# 
# **코딩**은 **프로그래밍 언어**를 사용하여 프로그램의 코드를 작성하는 일, 
# 또는 알고리즘을 프로그래밍 언어로 변환하는 작업을 말한다.

# ::::{admonition} 참고  
# :class: info
# 첨언하자면, 1980년대까지는 코드를 옮겨주는 사람, 즉, 코더라는 직업이 있었고 코더가 하는 일을 코딩이라고 했으나 요즘에는 프로그래밍, 코딩 용어가 특별한 구분없이 사용된다.
# ::::

# ### 프로그래밍 언어
# **프로그래밍 언어**는 프로그램을 만들 때 사용하는 언어이다. 세상에는 영어, 중국어, 한국어, 일본어 등 수 많은 자연어가 존재하듯, 프로그래밍 언어 또한 기계어, 어셈블리어, 포트란(Fortran), 코볼(Cobol), C, C++, 자바(JAVA), 파이썬(Python) 등 수많은 프로그래밍 언어가 존재한다.
# 
# 그 가운데 파이썬 프로그래밍 언어는 2000년대 들어서 점점 인기가 높아지기 시작했으며 프로그래밍 및 컴퓨터 공학 입문용으로 가장 널리 활용되고 있다. 파이썬은 네덜란드 출신인 귀도 반 로섬에 의해 개발되었으며 로고는 뱀 두마리가 형상화되어 있다.

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_logo.png" style="width:200px;"></div>

# ### 파이썬
# 
# **파이썬**은 많은 장점을 가지고 있다. 
# - 배우기 쉽다.
# - 간결한 문법과 풍부한 표준 라이브러리를 가지고 있다.
# - 풍부한 표준 라이브러리를 소스나 바이너리 형태로 파이썬 웹 사이트에서 무료로 제공하고 있으며 자유롭게 배포가능하다.
# - 자료 구조들과 객체 지향 프로그래밍에 대해 간단하고도 효과적인 접근법을 제공한다.
# - ......
# 
# 

# ::::{admonition} 참고  
# :class: info
# 1990년대에 포트란, 코볼부터 다뤄봤던 나는 파이썬이라는 언어를 처음 접했을때 '세상에 이런 언어가 있다니!' 하면서 굉장히 놀라지 않을 수 없었다. 파이썬은 다른 언어에 비해 매우 직관적이며 배우기 쉬울뿐만 아니라 필요한 대부분의 기능들이 구현되어 있어서 초보자뿐만 아니라 전공자들이 사용하기에도 부족함이 없는 언어이다.
# ::::

# 파이썬은 웹 어플리케이션의 개발 언어로도 많이 사용되고 있으며, 데이터 분석에 장점을 가진 스크립트 언어이다. 기계학습 등 인공지능의 개발에도 많이 사용되고 있는 등 웹/앱에서 인공지능까지 인기가 급상승하며 주목받는 언어이다. 
# 
# 파이썬 언어의 인기는 프로그래밍 언어들의 인기도를 측정하는 TIOBE https://www.tiobe.com/tiobe-index/ 에서 확인할 수 있다. 
# 

# 아래 그래프에서 확인할 수 있듯이, 파이썬의 인기는 2000년대 들어서부터 점차 상승하였으며, 2018년부터 가장 인기있는 프로그래밍 언어로 부동의 1위 자리를 유지하고 있다.(2023년 2월 기준)
# 
# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_pop_graph.png" style="width:700px;"></div>
# 
# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/pl_pop_list.png" style="width:700px;"></div>
# 
# Source: www.tiobe.com

# ### 파이썬 학습 사이트
# 
# 파이썬을 학습하기에 가장 좋은 방법은 바로 튜토리얼이다. 파이썬 튜토리얼은 다음 링크에서 확인할 수 있다.
# - https://docs.python.org/ko/3/tutorial/index.html  
# 
# 점프투파이썬도 초보자가 학습하기 좋은 사이트이다.
# - https://wikidocs.net/book/1 
# 
# 오픈튜토리얼 생활코딩도 도움이 많이 된다.
# - https://opentutorials.org/course/1

# ## 파이썬 프로그래밍 개발 환경
# 
# 파이썬 인기에 발맞춰 파이썬 프로그래밍 언어를 이용하여 프로그램을 개발할 수 있는 다양한 개발 환경이 제공되고 있다.
# - Python IDLE
# - Jupyter Notebook
# - Google Colab
# - Visual Studio code(VS code)
# - PyCharm
# - ...
# 
# 여기에서는 가장 기본적인 파이썬 IDLE, 개발 환경으로 인기가 많은 구글 코랩(Google Colab)에 대해서 소개한다. 참고로, 이 강좌에서는 구글 코랩 기준으로 설명한다.

# ### 구글 Colab

# **구글 코랩**은 브라우저 내에서 파이썬 스크립트를 작성하고 실행할 수 있도록 구글에서 제공하는 에디터이다. 주피터 노트북기반으로 제공하므로 주피터 노트북을 사용해본 개발자라면 구글 코랩도 쉽게 익힐 수 있다. 
# 구글 코랩은 이름에서 알 수 있듯이, 구글에서 구글 클라우드 서비스를 기반으로 무료로 리소스(RAM, Disk)를 제공하며 구글 아이디만 있으면 사용할 수 있다. 개인의 PC 보다 접근성이 좋으며 링크하나로 다른 사용자들과의 공유와 협업도 용이하다는 장점이 있다.
# 

# #### 코랩 실행하기
# 
# 웹브라우저에서 https://colab.research.google.com/ 링크로 코랩에 접속해보자. 코랩에 접속하면 코랩에 대한 간단한 소개글 페이지가 열린다. 코랩 사용법을 정리해둔 문서이니 필요하다면 읽어보길 바란다. 코랩 노트에서는 아래 그림과 같이, 코드에 대한 설명, 결과 내용, 그림, 링크 등을 넣는 **텍스트 셀**, 코드를 넣는 **코드 셀**, 그리고 코드를 실행하면 **결과**까지 바로 볼 수 있다.
# 

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/colab_1.png" style="width:700px;"></div>
# <br>
# <br>

# 이제 **파일** 메뉴에서 **새 노트**를 클릭하여 새 노트를 만들어보자. 구글에 로그인이 되어있지 않다면 먼저 로그인을 해야 한다.  
# 
# 새 노트가 열리면 아래와 같이 회색의 셀이 보인다. 이 셀을 **코드셀**이라고 하는데 코드셀은 코드를 작성할 때 사용하는 셀이다. 코드셀안에 다음과 같이 코드를 쓰고 셀을 실행해보자.
# 

# In[1]:


print('Hello World!')


# 셀을 실행하는 방법은 셀 앞에 플레이 버튼처럼 생긴 실행버튼을 눌러도 되고, 아래의 단축키를 사용해도 된다. 
# 
# - **Ctrl + Enter** : 셀 실행 후 커서는 방금 실행한 셀에 있음
# - **Shift + Enter** : 셀 실행 후 커서가 다음 셀로 넘어감. 다음 셀이 없을 경우, 새로운 셀이 만들어짐.
# 
# 코드의 결과는 실행시킨 코드셀 아래에 출력된다. 
# 
# 코드셀은 코랩 메뉴 아래에 '+코드'를 클릭하거나, 추가하고자 하는 셀 위아래 중간쯤에 마우스를 움직이면 '+코드', '+텍스트' 버튼이 나타나는데 여기에서 '+코드'를 클릭하여 추가할 수 있다.

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/colab_3.png" style="width:200px;"></div>

# In[2]:


a=10
b=20


# #### 텍스트셀과 마크다운
# 

# **텍스트셀**은 목차 만들기, 코드에 대한 설명, 이미지, 링크, 코드 형식 넣기 등 텍스트를 넣을 때 사용한다. 
# 텍스트셀은 **마크다운** 형식을 지원한다. 

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/colab_4.png" style="width:200px;"></div>

# - **마크다운**이란 읽고, 쓰고, 편집하기 쉬운 목적으로 만들어진 문서 작성을 위한 문법을 의미한다. README 파일이나 온라인
# 문서, 혹은 일반 텍스트 편집기로 문서 양식을 편집할 때 쓰인다. 
# - 마크다운을 이용해 작성된 문서는
# 쉽게 HTML, PDF, Word등 다른 문서형태로 변환이 가능해서 많은 프로그래밍 보고서를 마크다운으로 작성하기도 한다.
# - 직관적으로 읽기 쉽다는 장점이 있으며, 대표적으로 GitHub에서 README.md 파일을 작성할 때 자주 사용한다. 
# 
# - 코랩에서 제공하는 마크다운에 대한 설명은 다음 사이트를 참고하면 된다.
# https://colab.research.google.com/notebooks/markdown_guide.ipynb

# `제목만들기`
# - `#`표시가 앞에 붙으면 제목이 생성된다. #의 개수가 늘어날 수록 글자 크기가 작은 제목이 만들어진다.
# - 텍스트셀의 아이콘은 가장 왼쪽에 있는 **T**이다.

# `글자를 진하게`
# - `** **`를 붙이면 글자를 진하게 표현할 수 있다.
# - 텍스트셀의 아이콘은 두 번째 있는 **B**이다.

# `글자 기울이기`
# - 글자를 이텔릭체(기울임꼴)로 만들어준다.
# - 텍스트셀의 아이콘은 세 번째 $I$이다.

# `코드블럭`
# - 코드 형식으로 보이도록 만들어준다.
# - 텍스트셀의 아이콘은 **<>**이다.
# 
# 
# ```python
# print('Hello python')
# ```

# `링크 달기`
# - 보통 홈페이지의 링크, 코드의 출처, 자료의 출처를 표기할 때 이용한다.
# - 텍스트셀의 아이콘은 다섯 번째 클립모양이다.

# `이미지 첨부`
# 
# ![이미지](http://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
# 
# - 이미지의 경우 이미지 자체를 바로 불러오기 보다는 이미지가 들어있는 링크를 넣어주는 것이 좋다.

# `들여쓰기`
# 
# > 일정한 간격만큼 들여쓰여 보여진다.
# >> 오른쪽 꺽새 기호의 갯수에 따라 더 들어간다.
# 
# 

# `번호매기기 목록추가`
# 
#   1.   항목에 번호를 매길 수 있다.
#   2.   항목 추가
# 
# 

# `글머리기호 목록추가`
# 
# *   항목에 글머리기호를 달 수 있다.
#   - 들어간 글머리 기호
# 

# `수평선 긋기`
# - 코드를 분리할 때 주로 사용한다.
# ---  

# #### 파일명 변경하기
# 파일의 이름을 변경하기 위해서는 코랩 마크 옆에 Untitled0.ipynb 부분을 클릭하여 변경할 수 있다. 코랩이나 주피터 노트북에서 작성한 코드는 .ipynb라는 확장자를 갖는다. 확장자는 파일의 성격을 구분짓기 위한 구분자로 ipynb는 Interactive Python Notebook의 약자이다. 
# 
# 코랩은 구글 드라이브와 연동되며 여러분이 저장한 노트는 구글 드라이브의 **Colab Notebooks** 폴더에 자동 저장된다.

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/colab_2.png" style="width:300px;"></div>

# 이 강좌에서는 코랩 기준으로 진행하므로 아래 내용부터는 관심있으면 추가적으로 살펴보기 바란다.

# ### 파이썬 IDLE

# #### 파이선 IDLE 설치하기
# 
# 파이썬 IDLE은 파이썬 공식사이트인 http://www.python.org 에서 다운로드 받을 수 있다. IDLE은 Interactive DeveLopment Environment의 약자로 대화형 개발 환경을 의미한다. 
# 
# Downloads 메뉴에는 Windows, macOS, Other platforms 등 운영체제별로 다운로드 받을 수 있는 설치파일이 존재한다.

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_site.png" style="width:700px;"></div>

# 현재의 버전은 2023년 2월 기준 Python 3.11.2이다. 설치하는 과정은 매우 간단하다. Windows 버전으로 설명하자면, 다운로드 받은 설치 파일을 실행하여 특별히 설정해줄 옵션없이 Next> 버튼만 눌러주면 쉽게 설치완료된다. 
# 
# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_idle_1.png" height="250" width="300">  <img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_idle_2.png" height="250" width="300"></div>

# #### 파이썬 IDLE 실행하기
# 
# 설치가 완료되었다면 파이썬 IDLE을 실행시켜보자. 윈도우 시작버튼을 클릭하여 Python 3.11 목록을 펼친 후 IDLE을 클릭하면
# **Python 대화형모드**가 열린다. 이 모드에서는 기본 프롬프트 <font color='red'>**>>>**</font>를 표시해서 다음 명령을 요청한다. 
# 기본 프롬프트 옆에 
# 
# ```
# print('Hello') 
# ```
# 
# 코드를 입력하고 엔터를 눌러보자. 그 결과가 아래에 출력된다.
# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_idle_3.png" height="250" width="200">  <img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_idle_4.png" width="450"></div>

# 그런데 이와 같이 파이썬 대화형모드에서는 길고 복잡한 코드(특히 함수를 정의할때)를 작성 또는 수정하기에는 매우 번거롭다. 그래서 간단한 코드가 아니고서는 일반적으로 파이썬 **편집기모드**로 코드를 작성한다. 파이썬 편집기모드는 **File** 메뉴에서 **New File**을 클릭하면 메모장과 비슷하게 생긴 윈도우가 열린다. 편집기모드에서는 여러줄의 코드를 한번에 작성할 수 있고 수정도 쉽다.
# 
# 편집기모드에서 작성한 코드를 실행시킬때에는 **Run** 메뉴에서 **Run Module**을 클릭하거나 단축기 F5를 누른다. 코드를 실행시키면 대화형모드의 윈도우에 그 결과가 출력된다.
# 

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch01/python_idle_5.png" style="width:700px;"></div>

# ## 마무리
# 이 장에서는 컴퓨터의 정의와 파이썬 프로그래밍 언어의 특징, 파이썬 프로그래밍 개발 환경에 대해서 살펴보았다.
# - 컴퓨터는 하드웨어와 소프트웨어로 구성되어 있다.
# - 소프트웨어(프로그램)는 프로그래밍을 통해 만들어진다.
# - 프로그래밍을 하기 위해서는 프로그래밍 언어를 알아야 한다.
# - 다양한 프로그래밍 언어가 있지만, 이 가운데 파이썬은 매우 직관적이며 배우기 쉬울뿐만 아니라 필요한 대부분의 기능들이 구현되어 있어서 초보자뿐만 아니라 전공자들이 사용하기에도 부족함이 없는 언어이다.
# - 파이썬 프로그래밍 언어를 활용하여 프로그램을 개발하기 위한 환경으로 구글 코랩이 많이 이용되고 있다.
# 
# 다음 장부터 본격적으로 구글 코랩 환경에서 파이썬 프로그래밍을 시작해보자.
