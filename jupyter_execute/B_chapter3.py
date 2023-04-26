#!/usr/bin/env python
# coding: utf-8

# # Chapter 3. 조건문

# :::{admonition} 학습목표와 기대효과 
# :class: info  
# - 학습목표
#   - 프로그래밍의 제어 구조를 알아보자.
#   - 조건문의 개념을 이해하자.
#   - 들여쓰기의 중요성을 이해하자.
#   - 비교연산자, 논리연산자를 알아보자.
#   - 모듈을 불러와보고 난수에 대해 알아보자.
# 
# - 기대효과
#   - 컴퓨팅 디바이스들이 주어진 조건에 어떤 방식으로 처리를 하는지 이해할 수 있다.

# ## Review & Questions
# 

# Q1. 다음 중 결과가 나오는 번호는?
# 
# A.
# ```python
# x=10
# y=5
# 2x^2 + y
# ```
# B.
# ```python
# x=0 
# x**2 + 10
# ```
# 
# C.
# ```python
# x=0
# 10/x +2
# ```

# Q2. 화씨온도를 입력받아 섭씨온도로 변환하기를 원한다. 코드의 입력값으로 25.5를 넣었을 때 에러가 발생하는 부분, 또는 예상한 결과로 나오지 않은 부분을 모두 찾으시오.
# 
# ```
# c= 5/9*(f-32)
# f = int(input('화씨온도: '))
# print(f'화씨온도 f는 섭씨온도 c이다.')
# ```

# ## 프로그래밍 제어구조
# 

# :::{admonition} 프로그래밍 제어구조
# :class: info  
# 
# 프로그래밍의 제어구조로는 코드의 순서대로 실행하는 순차구조, 조건에 따라 실행을 분기하는 조건구조, 일정 부분을 반복하여 실행하는 반복구조가 있다. 
# 
# 프로그램의 흐름(flow)를 파악하기 위해 차례대로 보기 쉽게 그린 그림을 플로우차트라고 한다.

# <div align="center"><img src="https://haesunbyun.github.io/Basic-Computing/_images/ch03/flow.png" style="width:600px;"></div>
# 
# 앞서 우리는 프로그램의 코드를 순서대로 실행시키는 순차구조에 대해서 익혀왔다. 이번에는 특정 조건에 따라 실행을 분기시키는 조건구조에 대해서 알아보자.

# ## Sample Source Code #1
# 
# ```python
# # This is a guess the number game.
# myName = input('Hello! What is your name?')
# number = 5
# print ( 'Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# 
# guess = int(input('Take a guess.'))
# 
# if guess != number:
#   print ( 'Your guess is wrong.')
# if guess == number:
#   print ( 'Good job, ' + myName + '! You guessed my number!')
# ```

# 샘플 코드를 빈 코드셀에 옮겨 붙인 후 코드를 실행시켜보자. 이 코드에서는 변수 guess와 변수 number를 비교하고 있다.
# 
# 먼저 조건을 비교하기 위해 사용되는 비교연산자, 멤버연산자, 논리연산자부터 알아보자. 

# ## 비교연산자
# 
# 비교연산자는 정수, 문자열, 변수 등의 값을 비교할 때 사용한다. <font color='red'> 비교연산자의 결과는 항상 bool 타입인 True 또는 False로 나온다. </font>
# 
# 비교연산자의 종류는 다음과 같다.

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`>`|크다|`2 > 1`|`True`|
# |`<`|작다|`2 < 1`|`False`|
# |`>=`|크거나 같다|`2 >= 1`|`True`|
# |`<=`|작거나 같다|`2 <= 1`|`False`|
# |`==`|같다|`1 == '1'`|`False`|
# |`!=`|같지 않다|`1 != '1'`|`True`|

# In[1]:


a=10
b=7
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


# :::{admonition} 주의
# :class: warning
# 
# - 비교연산자에서 같은지를 비교할 때에는 `==`와 같이 등호부호(equal sign)를 두 개 쓴다는 것에 주의하자.
# - `>=`, `<=`와 같은 부호는 항상 `>`나 `<`가 `=`보다 앞에 나와야 하며 띄어쓰면 안된다.

# - 문자 비교도 가능하다. 문자비교는 각 문자에 부여되어 있는 unicode값을 비교한다. 알파벳 대문자와 소문자의 unicode는 다르다. 예를 들어 대문자 'H'와 소문자 'h'의 코드값이 다르다. 
# - 만약 첫 글자의 코드 값이 같다면 차례대로 다음 문자를 비교한다. 

# :::{admonition} 유니코드
# :class: info
# 
# 유니코드란 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 표준이다. 현재 전 세계의 모든 문자와 이모티콘까지 포함하여 1,114,112개의 코드값이 지정되었고, 이 가운데 한,중,일 한자가 97,058개로 약 87%를 차지한다.(23년 2월 기준)😲

# In[2]:


print('HELLO'=='hello')
print('HELLO'=='Hello')
c='hello'
d='HELLO'
print(c == d)


# - 한글도 비교가 가능하다.
# - 한글은 자음, 모음 각각 unicode가 부여되어 있다.
# - 유니코드 값 확인은 ord() 함수를 통해 가능하다.
# - 반대로 유니코드 값으로 문자를 확인하는 함수로는 chr() 함수가 있다.

# In[3]:


print('서울대'> '고려대')
print('ㅅ' > 'ㄱ')


# In[4]:


print('서', ord('서'))
print('고', ord('고'))
print('ㄱ', ord('ㄱ'))
print('a', ord('a'))
print('A', ord('A'))
print('1', ord('1'))
print('9', ord('9'))


# :::{admonition} 숫자 모양의 문자 비교 시 주의
# :class: warning
# 
# 가끔 입력받은 값의 형 변환을 하지 않아 숫자 모양의 문자를 숫자인줄 알고 비교하는 경우가 있다. 이러한 경우 에러가 발생하지 않고 숫자 모양의 문자 유니코드 값을 비교하니 주의하자.

# In[5]:


print('12'< '123')


# In[6]:


print('123' > '93') 


# - 숫자와 문자는 당연히 같지 않으므로 같다, 같지않다 비교했을 때 비교결과가 나온다. 

# In[7]:


print(5 == '5')
print(5 != '5')


# - 그러나 문자와 숫자간 대소(>, <, >=, <=)는 비교가 불가능하여 에러를 발생시킨다.
# 
# ```python
# print(123>'123') 
# ```
# 
# 

# ## 멤버연산자
# 
# 멤버연산자는 어떤 값이 포함되어 있는지 아닌지를 검사하는 연산자이다. 멤버연산자의 결과는 항상 True 또는 False로 나온다. 

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`in`|포함되어 있다|`'p' in 'python'`|`True`|
# |`not in`|포함되어 있지 않다|`'p' not in 'python'`|`False`|

# In[8]:


print('y' in 'yellow')
print('a' not in 'animal')


# ## 논리 연산자
# 한개 또는 두개 이상의 조건을 비교하여 논리적인 결과를 얻고자 할때 사용한다. 논리연산자의 결과는 항상 True 또는 False로 나온다.  

# |연산 기호|의미|예시|실행 결과|
# |:----------:|:----------:|:----------:|:--------:|
# |`and`|논리곱(그리고)|`True and False`|`False`|
# |`or`|논리합(또는)|`True or False`|`True`|
# |`not`|논리부정(아니다)|`not False`|`True`|

# - 아래의 코드는 논리연산자의 사용을 보여주는 예이다.

# In[9]:


a=10
b=7
c=5
print(a>b and b>c)
print(a>b or b<c)
print(not a>b)


# - and 연산자는 모든 조건이 True일때만 그 결과가 True이다.

# In[10]:


print(True and True)
print(True and False)
print(False and True)
print(False and False)


# - or 연산자는 하나의 조건이라도 True이면 그 결과는 True이다.

# In[11]:


print(True or True)
print(True or False)
print(False or True)
print(False or False)


# - not 연산자는 조건식의 결과를 뒤집는다.

# In[12]:


print(not True)
print(not False)


# - 논리연산자는 not > and > or로 우선순위를 가진다. 우선순위가 동일한 경우에는 왼쪽에서 오른쪽 순서로 실행한다. 

# In[13]:


print(not False or True and False or True )


# :::{admonition} Short Circuit Effect
# :class: warning
# 
# `Short circuit 효과는 짧게 짧게 전기가 흐른다는 뜻`으로 프로그래밍에서는 어떤 경우에는 정상적으로 실행하고 어떤 경우에는 에러가 나오는 경우를 의미한다. 
# 프로그램의 크기가 크고 복잡한 경우에는 이러한 원인을 파악하기 어렵게 만들기도 한다.

# - 1/0은 0으로 나누는 연산으로 division by zero error가 발생하는 것이 맞다.
# 
# ```python
# 1/0
# ---------------------------------------------------------------------------
# ZeroDivisionError                         Traceback (most recent call last)
# <ipython-input-13-9e1622b385b6> in <module>
# ----> 1 1/0
# 
# ZeroDivisionError: division by zero
# ```
# 
# 

# - 그런데 아래의 코드는 1/0 연산이 포함되어 있음에도 불구하고 에러를 발생하지 않는다. 그 이유는 a>b 조건식의 결과가 True이고 그 다음 연산자가 or이므로 그 다음의 조건의 결과와 상관없이 전체 결과는 True이기 때문이다. 

# In[14]:


a=10
b=7
print (a>b or 1/0)


# - 아래 코드 또한 마찬가지다. 변수 muyaho가 앞에서 전혀 정의된 적이 없음에도 불구하고 i%2 != 0 조건식의 결과가 False이고 그 다음 연산자가 and이므로 그 다음의 조건과 상관없이 전체 결과는 False이면서 에러를 발생시키지 않는다.
# - 그러나 변수 i의 값이 11이라면 에러가 발생한다. 
# - 이와 같이 경우에 따라서 에러가 발생하기도 하고 발생하지 않기도 하는 것을 short circuit 효과라고 한다.

# In[15]:


i=10
print (i%2 != 0 and muyaho == 0)


# ## if statements
# 
# if문은 조건에 따라 실행을 분기시키는 문으로 if문, if ~ else문, if ~ elif ~ else문이 있다. 
# - 조건식의 끝에는 반드시 콜론(:)을 붙여야 한다.
# - 조건식에 변수가 들어간다면 반드시 미리 정의되어 있어야 한다.
# - 조건에 의해서 실행되는 문장들은 반드시 들여쓰기(Indentation)을 해야 한다.

# ### if 문
# - 비교해야 할 조건식이 하나라면 if문으로 충분하다.

# In[16]:


score = 75
if score >= 75:
  print("success!")


# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. 입력받은 점수가 80점 이상이면 'Pass!'를 출력하는 코드를 작성하세요.
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```python
# 점수: 90
# Pass!
# ```
# <font color='blue'>`test case-2`</font>
# ```python
# 점수: 70
# ```

# ### if ~ else 문
# - 비교해야 할 조건식이 True일때와 False일때를 분기하여 실행해야 한다면 if ~ else문이 적합하다.
# - 아래 코드에서 print('Happy')는 조건에 의해 실행되는 문장이 아니다. 따라서 들여쓰기가 되어 있지 않다.

# In[17]:


state = 'Hit'
if state == 'Hit':
  print("Homerun!")
else:
  print("Strike!")

print("Happy")


# - 중첩 if문이란 if문 안에 또 다른 if문이 있는 것을 말한다. 중첩 if뿐만 아니라 중첩 if ~ else문도 가능하다. 
# - 그러나 중첩 if, 중첩 if ~ else문은 코드가 길어지거나 중첩 레벨에 따라 들여쓰기가 단계별로 깊어지므로 코드가 자칫 복잡해질 수 있다.

# In[18]:


a=10
b=7
c=3
query=5
if query>a:
  print("가장 큰 수 이다.")
else:
  if query>b:  
    print("두 번째로 큰 수 이다.")
  else:
    if query>c:
      print("세 번째로 큰 수 이다.")
    else:
      print("가장 작은 수 이다.")


# ### if ~ elif ~ else 문(다중 if문)
# - 중첩 if ~ else문 대신에 다중 if문(if ~ elif ~ elif ~ else)으로 코드를 간결화 할 수 있다.
# - 다중 if문은 조건식이 True인 조건을 만날 때 까지 비교하면서 내려온다. 
# - 조건식이 True인 조건을 만나면 그 조건에 해당하는 실행문장을 실행한 후, 다음 elif문의 조건을 비교하지 않고 다중 if문 전체를 벗어난다.
# - `else:`없이 `elif 조건:`으로 끝날 수도 있으나 일부 컴파일러에서는 에러로 인식하기도 한다.

# In[19]:


a=10
b=7
c=3
query=5
if query>a:
  print("가장 큰 수 이다.")
elif query>b:
  print("두 번째로 큰 수 이다.")
elif query>c:
  print("세 번째로 큰 수 이다.")
else: #없을수도 있음
  print("가장 작은 수 이다.")

print('End')


# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. 변수 number와 같은 수, 큰 수, 작은 수를 출력하고 싶었다. 무엇이 문제인지 찾아보시오.
# ^^^
# 
# ```python
# number = 75
# if number == 75:
#   print ( '같다.')
# if number > 75:
#   print ( '크다.')   
# else:
#   print('작다.')
# ```

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. 눈으로 살펴보고 Case-1과 Case-2의 결과가 어떻게 나올지 예상해보세요.
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```python
# score = 75
# if score >= 90:
#     print ('A입니다. ' )
# elif score >= 80 :
#     print ('B입니다.' )
# elif score >= 70 :
#     print ('C입니다.' )
# elif score >= 60 :
#     print ('D입니다.' )
# else:
#     print ('F입니다.' )
# ```
# 
# <font color='blue'>`test case-2`</font>
# ```python
# score = 75
# if score >= 90:
#     print ('A입니다. ' )
# if score >= 80 :
#     print ('B입니다.' )
# if score >= 70 :
#     print ('C입니다.' )
# if score >= 60 :
#     print ('D입니다.' )
# else:
#     print ('F입니다.' )
# ```

# ## Indentation
# 동일 조건하에 실행해야 할 문장들을 블럭으로 만들어 줘야 하며, 동일 블럭은 들여쓰기의 깊이가 같다. 주로 조건문, 반복문 등을 작성하거나 함수, 클래스 등을 정의할 때 들여쓰기를 한다.
# 
# - 키보드의 space bar를 눌러 들여쓰기를 할 수도 있지만 tab 키를 눌러 들여쓰면 편하다. shift + tab은 반대로 내어쓰기가 된다. 
# - 코랩의 `설정>편집기>들여쓰기 가이드 표시`를 선택해 놓으면 들여쓰기 구분이 쉽다.
# - 또한 `설정>편집기>편집기에서 코드폴딩을 사용설정합니다.`를 선택해 놓으면 들여쓰기 단위로 코드를 접어 놓을 수 있다.
# 

# <div align="center"><img src="https://haesunbyun.github.io/AISW/_images/ch03/block.png" style="width:600px;"></div>

# - 동일 블럭에서 들여쓰기가 달라 Indentation error가 발생한다.
# 
# 
# ```python
# score = 90
# if score >= 90 :
#   print ('합격입니다.') 
#  print ('A 등급입니다.')  
#     print ('장학금도 받을 수 있습니다.')      
#   print ('효도하시는군요!') 
# ```
# 
# 

# - 아래 코드는 들여쓰기가 다르지만 서로 다른 블럭이므로 정상 실행된다. 그렇지만 블럭에 레벨에 따라 가급적 들여쓰기 깊이를 동일하게 주는 것을 권장한다. 

# In[20]:


score = 80
if score >= 90 :
  print ('합격입니다.')
  print ('A 등급입니다.')
  print ('장학금도 받을 수 있습니다.')
  print ('효도하시는군요!') 
else :
       print ('다음학기를 노려보세요.')


# - 블럭에 들어가야 할 코드가 한줄도 없는 경우에도 Indentation error가 발생한다. 
# 
# ```python
# if score >= 70:
#  
# else:
#     print('다음학기를 노려보세요.')    
# print("end")
# ```
# ```
# File "<ipython-input-12-01b624ec0bbe>", line 3
#     else:
#     ^
# IndentationError: expected an indented block
# ```

# - 블럭안에 들어가야 할 코드를 아직 생각하지 못했다면 키워드 pass를 넣어주면 된다. 

# In[21]:


if score >= 70:
  pass
else:
    print('다음학기를 노려보세요.')    
print("end")


# ## Sample Source Code #2
# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄 다음 코드를 아래의 세가지 조건으로 실행되도록 비교파트를 수정해보세요.
# ^^^
# 
# - (조건1) guess가 number보다 크면 'Your guess is high.'
# - (조건2) guess가 number보다 작으면 'Your guess is low.'
# - (조건3) guess와 number가 같으면 지금 메시지 그대로
# 
# 
# ```python
# # This is a guess the number game.
# myName = input('Hello! What is your name?')
# number = 5
# print ( 'Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# 
# guess = int(input('Take a guess.'))
# 
# if guess != number:
#  print ( 'Your guess is wrong.')
# if guess == number:
#  print ( 'Good job, ' + myName + '! You guessed my number!')
# ```

# ## 모듈과 모듈 불러오기
# **모듈**은 서로 관련있는 함수들을 모아 놓은 집합이다. 파이썬에는 random, math, sys, ... 등 수 많은 모듈들이 정의되어 있고 필요할 때 불러서 쓸 수 있다. 모듈은 한번만 불러오면 현재 소스코드 파일을 닫을 때까지 사용할 수 있으므로 여러 번 불러올 필요가 없다. 따라서 일반적으로 모듈을 불러오는 코드는 소스코드의 맨 위에 모아 놓는다.
# 
# 모듈을 불러오는 키워드는 import이다.
# 모듈을 불러오는 방법은 두 가지가 있는데, 
# - 첫 번째는 `import 모듈명`으로 불러온다. 
# 예를 들어, random 모듈을 불러오려면
# ```python
# import random
# ```
# 이라고 쓰면 된다. random 모듈안에 다양한 함수들, 예를 들어 randint(), seed(), sample(), ..., 등 이 있는데 `모듈명.함수명()`의 형식으로 불러와 사용한다.
# ```python
# import random
# print(random.randint(1,100))
# print(random.sample(range(100), 2))
# ```
# - 두 번째는 `from 모듈명 import *`로 불러온다. 예를 들어,
# ```python
# from random import *
# ```
# 이라고 쓰면 된다. 여기서의 *은 모든 것이라는 의미를 담고 있는데 즉, random 모듈안에 모든 것을 불러온다는 뜻이다. 만약, random 모듈안에 randint() 함수만 불러오려면 
# ```python
# from random import randint
# ```
# 와 같이 쓴다.
# 'from 모듈명 import'방식으로 불러온 경우에는 <font color='red'>모듈명.함수명()이 아니라 함수명()만 쓴다.</font>
# ```python
# from random import *
# print(randint(1,100))
# print(sample(range(100), 2))
# ```
# 
# 

# - 여기에서는 random 모듈안에 들어있는 함수중에 randint() 함수만 알아보자.
# - randint() 함수는 함수명에서도 추측할 수 있듯이 정수인 난수를 발생시키는 함수이다.
# - randint() 괄호안에 시작 수와 끝 수를 명시해주면 그 범위 안에서 난수를 발생시킨다.
# - `randint(시작 수, 끝 수)`
# - 끝수는 시작 수보다 같거나 커야 한다.
# - 범위에는 끝수까지 포함한다.
# 
# 

# In[22]:


import random
random.randint(1, 100)


# - 아래의 코드는 에러가 발생한다. 그 이유를 생각해보자.
# 
# ```python
# num = input( )
# random.randint(1, num)
# ```
# 
# 

# In[ ]:





# ## Sample Source Code #3
# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄 number의 값을 랜덤수로 수정하세요.
# ^^^
# 
# - TODO-1: number = 5 대신에 1부터 20 사이의 랜덤 수를 number에 저장하세요.
# - TODO-2: Sample Source Code #2에서 여러분이 작성한 비교파트 코드를 #TODO-2 아래에 넣어주세요.
# 
# ```python
# # This is a guess the number game.
# myName = input('Hello! What is your name?')
# number = 5
# print ( 'Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# 
# guess = int(input('Take a guess.'))
# 
# # TODO-2
# 
# ```

# ## 마무리
# - 프로그래밍 제어 구조는 순차, 선택, 반복 구조가 있다.
# - 선택구조는 조건에 따라 실행문장을 다르게 분기 시켜 준다.
# - 조건문은 비교할 때 사용하는 문으로 if문, if ~ else문, if ~ elif ~ else문이 있다.
# - 비교연산자는 if문, while문 등에서 수, 문자열, 변수 등의 값을 비교할 때 사용한다.
# - 비교연산자에는 >, < , >=, <=, ==, != 연산자가 있다.
# - 논리연산자에는 and, or, not 연산자가 있다.
# - 멤버연산자에는 in, not in 연산자가 있다.
# - 비교, 논리, 멤버연산자의 결과 값은 bool 타입으로 True 아니면 False로 산출된다.
# - import는 모듈을 소스코드 내에서 사용할 수 있도록 포함시키는 키워드다.
# 
