#!/usr/bin/env python
# coding: utf-8

# # Chapter 2. 입출력과 타입변환
# 
# 이 장에서는 주석을 처리하는 방법, 데이터를 입력하고, 출력하는 방법, 데이터 타입을 변환하는 방법에 대해 알아본다. 

# :::{admonition} 학습목표와 기대효과 
# :class: info  
# - 학습목표
#   - 주석을 달아보자.
#   - 결과를 출력하는 print() 함수에 대해 배워보자.
#   - 데이터를 입력받는 input() 함수에 대해 배워보자.
#   - 형변환 함수에 대해 알아보자.
# 
# - 기대효과
#   - 데이터를 입,출력할 수 있으며 데이터의 특성을 이해하고 타입을 변환할 수 있다.
# ::: 

# ## Sample Source Code
# 
# ```python
# # This program says hello and asks for my name.
# print('Hello world!')
# print('Input your name. ') 
# myName = input()
# print ('Welcome, ' + myName + '.' )
# ```
# 
# 

# In[ ]:





# 샘플 코드를 빈 코드셀에 옮겨 붙인 후 코드를 실행시켜보자.
# 두 줄의 문장이 출력된 이후에 커서가 깜박이고 있을 것이다. 
# 커서가 깜박이는 곳에 이름을 입력하고 엔터를 치면 Welcome, 다음에 입력한 이름이 출력된다.

# 방금 실행시켜 본 것이 바로 **파이썬 프로그램**이다. 
# 프로그램을 만들기 위해 채워 넣는 코드를 보통 **소스 코드**라 부른다.
# 소스코드는 여러번 실행시켜도 항상 똑같이 동작한다. 
# 
# 컴퓨터는 동일한 소스 코드를 항상 같은 방식으로 읽는다. 
# 여기에는 몇몇 원칙들이 적용된다.
# - 소스 코드는 맨 윗줄부터 순서대로 읽는다.
# - 언제나 한 줄의 코드를 다 실행한 후 다음 줄로 이동한다. 
# 
# 동일한 소스 코드를 항상 같은 방식으로 읽기 때문에 매 번 반복하기 번거로운 작업을 프로그램으로 만들어 두면 그 이후로는 편하게 실행 시켜서 결과를 얻을 수 있다.

# ## comment
# **주석**은 프로그램 또는 소스코드의 부연 설명이다. 소스코드 한 줄을 주석으로 처리하기 위해서는 #(pound) 기호를 문장의 맨 앞에 붙인다. # 기호를 문장의 중간에 붙이면 # 기호부터 그 줄의 마지막까지 주석으로 처리된다. 
# 
# 주석으로 처리된 코드는 프로그램의 실행에 전혀 영향을 미치지 않으므로 소스코드의 일부를 실행시키고 싶지 않을 때도 사용한다. 
# 또한 이 코드를 읽을 사람을 위해 붙이기도 한다.

# In[1]:


# This program says hello and asks for my name.
#print('Hello world!')
print('Input your name. ') # Ask your name


# :::{admonition} Tip  
# :class: tip 
# 
# 여러줄을 한꺼번에 주석처리 하려면 주석처리 할 여러 줄을 블럭설정한 후(드래그) `ctrl + /`를 누른다. ctrl + /를 한번 더 누르면 주석이 해제된다. 
# ctrl + a를 누르면 현재 셀의 모든 코드를 한꺼번에 블럭설정 할 수 있다.
# 
# 멀티라인 스트링 기호를 써서 여러 줄을 문자열로 묶어 주석처럼 사용하기도 한다.
# :::  

# In[2]:


# This program says hello and asks for my name.
print('Hello world!')
'''
print('Input your name. ')
멀티라인 스트링 기호를 써서 
여러 줄을 주석으로 처리할 수도 있다. 
'''
print('Welcome!!')


# ## print()
# print()는 문자열, 변수, 연산의 결과를 표준출력장치인 화면에 출력하는 함수이다. 
# 

# - 출력하기 위해서는 출력하고자 하는 내용을 print() 함수의 괄호안에 넣어주면 된다.

# In[3]:


print(123)
print('hello')
print(50/9)
print('hello! ' + 'sunny')
print('hello! ''sunny')
name = 'sunny'
print(name)
print('hello! ' + name)


# :::{admonition} Tip  
# :class: tip 
# 
# - 소수점 이하 원하는 자릿수까지만 표현하기 위한 두 가지 방법을 소개한다.
#   - round(value, n), n은 자릿수이다. n을 생략하면 반올림하여 정수로 출력한다. 
#   - f'{value:.nf}', n은 자릿수이며 생략할 수 없다. 정수로 출력하고 싶다면 n자리에 0을 넣는다. :::
#    

# In[4]:


print(round(3.141592, 3))
print(round(3.141592))
print(round(3.541592))


# In[5]:


print(f'{3.141592:.0f}')


# - 아래의 코드처럼 print() 함수를 쓰지 않아도 결과가 나온다. 이는 단지 코랩에서 제공해주는 기능으로 실행시키는 셀의 마지막 라인을 결과로 되돌려주기 때문이다. 

# In[6]:


'Hello world'


# - 만약 아래의 코드처럼 여러줄을 print()없이 썼다면 전체 문장을 출력하는 것이 아니라 가장 마지막 줄만 출력한다.

# In[7]:


'Hello world'
'How are you?'
'Nice to meet you'


# - 따라서 세 줄 모두 출력하려면 아래와 같이 각각을 print() 괄호안에 넣어주거나 또는 하나의 print() 괄호안에 멀티라인 스트링으로 넣어준다.

# In[8]:


print('Hello world')
print('How are you?')
print('Nice to meet you')

print('''Hello world
How are you?
Nice to meet you''')


# - print() 괄호안에 아무런 내용없다면 한 줄 공백을 출력한다. 
# 

# In[9]:


print('Hello')
print( )
print('Nice to meet you')


# - 여러개의 결과를 나열하여 출력하려면 콤마(,)로 구분한다. 콤마는 문자열과 숫자를 나열하여 출력할 때 매우 유용하다. print() 괄호안에 콤마가 있으면 콤마 자리마다 기본으로 한칸 띄어쓰기(공백)가 된다.

# In[10]:


print('내 나이는', 20, '살이야')


# In[11]:


age = 20
print('10년 후의 나이는', age+10, '살이야')


# - 한칸 띄어쓰기를 없애고 싶으면 옵션 sep을 변경하면 된다.
# - sep는 seperation의 약자로 결과를 분리시킨다는 의미이다.
# - 한칸 띄어쓰기 대신에 다른 구분자를 넣을때도 sep 옵션을 사용할 수 있다.

# In[12]:


print('내 나이는', 20, '살이야', sep='')
print(2323,18549, sep='-')


# - print() 괄호안에 f-string과 함께 사용하면 띄어쓰기, 데이터타입 등을 고민 할 필요없이 수월하게 출력할 수 있다.

# In[13]:


name = "민지"
age = 20
print(f'{name}는 {age}살이야')


# - print() 함수는 줄바꿈(\n) 기능이 포함되어 있다. 줄바꿈 기능을 바꾸고 싶다면 옵션 end를 변경하면 된다. \t는 일정한 간격으로 분리해주는 tab 기능이다.
# 

# In[14]:


print('나','너','우리', end='\t')
print('나','너','우리', end='^^;')


# - help()함수는 함수나 클래스의 옵션이나 사용방법에 도움을 주는 함수이다. help() 괄호안에 알고자 하는 함수명, 변수명, 클래스명을 넣어주면 된다. 
# - print() 함수의 다양한 옵션과 활용방법을 알고 싶다면 help(print)를 외쳐라.

# In[15]:


help(print)


# ### 연습문제

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제 1. 변수를 활용하여 아래와 같은 결과가 나오도록 코드를 작성해 보세요. '딱!' 문자열이 age+number만큼 출력되어야 합니다.
# ^^^
# 
# ```python
# a = '딱!'
# age = 21
# number = 10
# # TODO
# ```
# Output:
# 
# 10년후에, 너의 나이는 딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱!딱! 31살이 될꺼야.
# :::
# 
# 
# 
# 

# ## input()
# 
# input() 함수는 프로그램 실행 중에 표준입력장치인 키보드로부터 데이터를 입력받는 함수이다. 프로그램 실행중에 input() 코드를 만나면 그 아래 입력박스가 생기면서 커서가 깜박이며 입력을 기다린다.
# 그 박스안에 데이터를 입력하고 엔터를 치면된다. 
# 
# 입력 받은 데이터는 일반적으로 변수에 저장한다. 
# 만약, 변수에 저장없이 input()만 있다면 데이터는 입력 받지만 저장되지는 않는다.
# 
# 아래의 코드를 실행시켜보자.
# - 'Input your name.'을 출력한다.
# - 입력으로 'sunny'를 입력하면 변수 myName에 'sunny'가 저장된다.
# - Welcome, sunny.가 출력된다.
# 
# ``` python
# print ('Input your name.')
# myName = input()
# print (f'Welcome, {myName}.')
# ```
# ```
# Input your name.
# sunny
# Welcome, sunny.
# ```

# In[ ]:





# - 아래 코드를 실행시켜 'Alice'를 입력해보자. 
# - Welcome, sunny.가 출력된다.
# - 왜 컴퓨터는 Alice를 입력했는데도 sunny만 환영해줄까?
# 
# ```python
# input()
# print (f'Welcome, {myName}.')
# ```
# ```
# Alice
# Welcome, sunny.
# ```
# 
# 

# In[ ]:





# 사용자에게 무엇을 입력받을 때에는 다짜고짜 입력하라고 하지말고 무엇을 입력할것인지를 알려주는 것이 좋다. 즉, 질문을 주고 입력을 받아야 한다. 질문을 넣어주려면 input() 괄호안에 넣어주면 된다. 이때 입력박스는 질문 오른쪽에 생긴다.
# 
# ```python
# myName = input('Input your name.') 
# print (f'Welcome, {myName}.')
# ```
# ```
# Input your name.Alice
# Welcome, Alice.
# ```

# In[ ]:





# input() 함수에는 절대 잊어서는 안될 중요한 특징 하나가 있다. <font color='red'>입력받은 모든 데이터를 문자열로 처리된다는 것이다.</font> 숫자를 입력해도 문자열로 처리된다. 아래 코드에서 변수 age에는 문자열이 들어 있으므로 문자열과 변수를 더해도 에러가 발생하지 않는다.
# 
# ```python
# age = input('How old are you? ')
# print ('You are '  + age + ' years old.') 
# ```
# ```
# How old are you? 20
# You are 20 years old.
# ```
# 

# In[ ]:





# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄Quiz 1. 입력값 100을 주었다면 출력결과는?
# ^^^
# ```python
# a = input() + '5'
# print (a)
# ```
# :::
# 
# 
# 
# 

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄Quiz 2. 입력값 100을 주었다면 출력결과는?
# ^^^
# ```python
# a = input() + 'Hello'
# print (a)
# ```
# :::
# 
# 
# 
# 

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄Quiz 3. 입력값 100을 주었다면 출력결과는?
# ^^^
# ```python
# a = input() + 100
# print (a)
# ```
# :::
# 
# 
# 
# 

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄Quiz 4. 입력값 20을 주었다면 출력결과는?
# ^^^
# ```python
# age = input('How old are you?')
# age = age + 10  
# print (f'Ten years later, you will be {age} years old.')
# ```
# :::
# 
# 
# 
# 

# ### 연습문제

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제 2. 다음과 같이 출력결과가 나오도록 코드를 작성해 보세요.
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```
# 요구르트에 김치 말아먹기 vs 라면에 초콜릿 넣기: 라면에 초콜릿 넣기
# 당신은 라면에 초콜릿 넣기를 선택하셨군요!
# ```
# 
# <font color='blue'>`test case-2`</font>
# ```
# 요구르트에 김치 말아먹기 vs 라면에 초콜릿 넣기: 둘 다 싫어
# 당신은 둘 다 싫어를 선택하셨군요!
# ```
# :::
# 
# 
# 
# 

# In[ ]:





# ## Data type 확인과 변환
# 
# **형 변환**은 데이터의 타입을 변환하는 것으로, 형 변환이 필요한 이유는 데이터가 어떤 타입이냐에 따라 지원하는 연산도 다르기 때문이다. 예를 들어, input() 함수로 입력 받은 데이터는 문자열로 처리되는데 입력 받은 데이터와 숫자 연산을 하려면 데이터의  타입을 정수형 또는 실수형으로 변환해주어야 한다. 

# - 먼저 데이터의 타입을 확인해보자. type()함수는 데이터의 타입을 확인할 때 사용한다.
# 
# ```python
# height = 180
# type(height)
# int
# ```
# ```python
# height = '180'
# type(height)
# str
# ```
# ```python
# height = 180.3
# type(height)
# float
# ```

# ### int()
# 파이썬에서는 다양한 형 변환 함수를 제공한다.
# int()는 정수로 변환해주는 함수이다.

# In[16]:


print(int(42))
print(int(3.5))
print(int('42'))
print(int('    42   '))


# :::{admonition} 참고  
# :class: warning
# 
# int()함수는 정수모양이 아닌 문자열은 변환하지 못한다. 예를 들어, '3.5'나 'forty-two'를 변환하려고 하면 에러를 발생시킨다.
# 
# 
# ```python
# print(int('3.5'))
# print(int('forty-two'))
# ```
# :::
# 

# In[ ]:





# - 입력을 받은 값에 대해서 바로 형 변환을 하려면 int(input('체온을 입력하세요. '))와 같이 함수를 중첩하여 쓰면된다.
# - 아래 예제의 경우, 체온으로 정수 35를 입력했다면 정상적으로 실행된다.
# - 그러나 실수값 36.5를 입력했다면 input() 함수에 의해 실수값은 문자열 '36.5'가 되어 int()함수에 의해 에러가 발생한다.
# 
# ```python
# num=int(input('체온을 입력하세요. '))
# print(num)
# ```

# In[ ]:





# ### float()
# float()은 실수형으로 변환해주는 함수이다. int()와 달리 제약이 없다.

# In[17]:


print(float(42))
print(float(3.5))
print(float('3'))
print(float('3.6'))


# ### str()
# str()은 문자열로 변환해주는 함수이다. 이 또한 제약이 없다.

# In[18]:


print(str(42))
print(str(3.5))
print(str('42'))
print(str('3.5'))


# :::{admonition} 참고
# :class: info
# 
# 아래와 같이 입력받아서 변수 num에 저장한 후, 다음 라인에서 형변환을 했다. 그런 후에 type(num)을 통해 변수 num의 타입을 확인해보면 어떤 타입으로 나올까?
# 그리고 그 타입으로 나오는 이유가 무엇인지 생각해보자.
# ```python
# num = input() 
# int(num)
# type(num)
# ```

# ## print()에서 덧셈기호(+)와 콤마(,)와 f-string의 사용의 출력결과 비교
# 
# 형변환까지 배웠으니 마지막으로 print()에서 
# - +를 사용하여 출력하는 것
# - ,를 사용하여 출력하는 것
# - f-string을 사용하여 출력하는 것을 비교해보자.

# 
# ```
# name='홍길동'
# age=20
# ```
# 
# - `홍길동님의 나이는 20살입니다.` 이와 같이 정확하게 출력하기를 바란다고 하자.
# 

# - '+'연산자를 사용하는 경우, 변수 age가 정수형이므로 문자열과 더하기 위해서는 변수 age를 str()로 타입변환을 해줘야 한다.
# - `나이는` 다음에 공백까지 생각해줘야 한다.
# 
# 

# In[19]:


name='홍길동'
age=20
print(name+'님의 나이는'+str(age)+'살 입니다.')
print(name+'님의 나이는 '+str(age)+'살 입니다.')


# - 콤마(,)를 사용하는 경우, 콤마 있는 부분이 자동 한칸 띄어쓰기가 되므로 `20살`과 같이 나오게 하려면 `sep=''` 옵션을 줘서 띄어쓰기를 없애줘야 한다. 
# - 이때 올바르게 띄어써준 부분까지 없어지기 때문에 그 부분에는 일부러 공백을 넣어줘야 한다.

# In[20]:


print(name, '님의 나이는', age, '살 입니다.')
print(name, '님의 나이는', age, '살 입니다.', sep='')
print(name, '님의 나이는 ', age, '살 입니다.', sep='')


# - f-string으로 처리하는 것이 가장 편하다.
# - 출력하고자 하는 형태 그대로 만들고, `변수명`이나 `연산식` 또는 `함수호출` 등이 들어가야 할 자리에 {}를 씌어 넣어주면 된다.

# In[21]:


print(f'{name}님의 나이는 {age}살입니다.')
print(f'{name}님의 나이는 {age}살입니다.')


# ## 종합 연습문제

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제 1. 두 개의 정수를 입력 받아 덧셈 연산을 실행한 후에, 연산 결과를 화면에 출력하는 프로그램을 작성하시오.
# 
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```
# 첫 번째 정수를 입력하세요: 100
# 두 번째 정수를 입력하세요: 200
# 
# 100+200의 결과는 300입니다.
# ```
# 
# <font color='blue'>`test case-2`</font>
# ```
# 첫 번째 정수를 입력하세요: 300
# 두 번째 정수를 입력하세요: 500
# 
# 300+500의 결과는 800입니다.
# ```
# :::

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제 2. 온도를 입력받아 계산한 후 출력하는 프로그램을 작성하시오.
# ^^^
# 
# 섭씨온도공식 = 5/9*(화씨온도-32.0)
# 
# 화씨온도공식 = 9/5*섭씨온도+32.0
# 
# <font color='blue'>`test case-1`</font>
# ```
# 온도 변환 프로그램
# 화씨 온도를 입력하세요: 50
# 섭씨 온도는 10.0 입니다.
# 
# 섭씨 온도를 입력하세요: 50
# 화씨 온도는 122.0 입니다.
# ```
# :::

# ## 마무리
# - ‘#’은 주석처리 기호이며, 주석은 프로그램과 소스코드에 대한 부연 설명으로 프로그램의 실행에 영향을 미치지 않는다. 
# - print ( ) 함수는 표준출력장치인 스크린에 값을 출력하는 함수이며, 출력하고자 하는 내용을 괄호 안에 넣어주면 된다.
# - input( ) 함수는 프로그램 실행 중에 값을 입력 받는 함수다. 입력 받은 데이터는 모두 문자열 처리된다.
# - 데이터 타입에 따라 지원하는 연산(기능)이 다르다. 연산을 위해 데이터 타입을 변환해야 할 수도 있다.
# - int ( )함수는 정수로 변환하는 함수이다.
# - str ( ) 함수는 문자열로 변환하는 함수이다.
# - float ( ) 함수는 실수타입으로 변환하는 함수이다.
