#!/usr/bin/env python
# coding: utf-8

# # Chapter 4. 반복문
# 
# 반복(iteration)문은 동일한 문장을 반복해서 실행하는 구조이다. 이 장에서는 반복문 while과 for에 대해서 알아본다.

# :::{admonition} 학습목표와 기대효과 
# :class: info  
# - 학습목표
#     - 반복문의 개념과 동작원리를 이해하고 반복 패턴을 찾아보자. 
#     - 반복문 while를 배워보자.
#     - 반복문 for를 배워보자.
# 
# - 기대효과
#   - 컴퓨팅 디바이스들이 어떻게 반복적인 일을 계속 할 수 있는지 이해할 수 있다.
#   
# :::

# ## While loop
# 
# 먼저, while문에 대해 알아보자. 

# ### while statement
# while문의 형식은 다음과 같다. 조건 뒤에는 반드시 콜론(:)이 있어야 하며, 조건이 True인 동안 while문 안에 있는 실행 문장을 실행한다. 이때 실행 문장은 반드시 들여쓰기가 되어 있어야 한다.
# 
# ```
# while 조건:
#     실행 문장1
#     실행 문장2
#     ...
# ```

# - 예를 통해서 while문을 이해해보자.
# - 아래 코드에서는 반복을 위한 조건변수로 count를 활용했다. 
# - 변수를 조건에 활용하기 위해서는 반드시 while문 이전에 어디에선가 미리 정의되어 있어야 한다. 이 예에서는 while문 이전에 변수 count를 1로 정의하였다.
# - 변수 count는 while문 안에서 반복할 때마다 1씩 증가한다.
# - 그러다가 count가 5보다 크면, 즉 6이 되면, `count <= 5` 조건이 False가 되어 반복을 멈춘다.

# In[1]:


count = 1
while count <= 5:
    print(f'재미있는 파이썬:{count}')
    count=count+1
        
print(f'count={count}')


# - 조건변수로 사용한 count의 초기값은 프로그래머가 설정해주면 된다. 
# - 예를 들어, count=0으로 했다면 while문 안에서 count를 먼저 증가시킨다. 
# - 또한 5번 반복하고 빠져나와야 하므로 `count < 5`와 같이 조건식도 달라지며, count가 5일때 while문을 빠져나온다.

# In[2]:


count = 0
while count < 5:
    count=count+1  
    print(f'재미있는 파이썬:{count}')
        
print(f'count={count}')


# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. 다음과 같이 출력하는 코드를 while문을 이용해 작성해 보시오.
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```
# 나무를 1그루 심었습니다. 싹!
# 나무를 2그루 심었습니다. 싹!싹!
# 나무를 3그루 심었습니다. 싹!싹!싹!
# 나무를 4그루 심었습니다. 싹!싹!싹!싹!
# 나무를 5그루 심었습니다. 싹!싹!싹!싹!싹!
# ```
# :::

# ### break

# - while문의 조건 부분에 조건식이 아닌 True 또는 1 등을 넣어줄 수도 있다. 
# - 이 경우에는 `while True:` 또는 `while 1:` 이므로 조건이 항상 True가 되어 무한 반복하게 된다. 
# - 따라서 무한반복문의 경우 반드시 반복문을 탈출하는 break를 반복문 안 어딘가에 있어야 한다.
# 
# 

# In[3]:


count = 0
while True :
    print(f'무야호~:{count}')
    count = count + 1
    if count == 5:
       break
print(f'count={count}')


# :::{admonition} 프로그래밍 제어구조
# :class: info  
# 프로그래밍에서 True는 1의 값을 가지며, False는 0의 값을 가진다. 엄밀히 말하면 False와 0을 제외한 모든 값은 True의 의미를 가진다. 따라서 while 'a': 와 같이 적어도 무한 반복된다.

# ### Sample Source Code #4
# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄 반복하여 기회주기
# ^^^
# 
# - TODO-1: while문을 이용하여 number를 맞히지 못했을 때는 guess 기회를 계속 주도록 수정해보세요.
# - TODO-2: 맞혔을 때에는 Good job~문 출력 후 I'm happy를 출력해주세요.
# 
# ```python
# # This is a guess the number game.
# import random
# myName = input('Hello! What is your name?')
# number = random.randint(1,20)
# print ( f'Well, {myName} I am thinking of a number between 1 and 20.')
# 
# guess = int(input('Take a guess.'))
# 
# if guess> number:
#     print('your guess is too high')
# elif guess < number:
#     print('your guess is too  low')
# else:
#     print ( f'Good job, {myName}! You guessed my number!')
# 
# ```

# ### while ~ else
# - while문에도 else가 있다. 
# - while문의 else 파트는 while문이 정상적으로 모든 반복을 다 한 경우에만 실행한다. 
# - 즉, while문의 조건식이 False가 되서 빠져나오는 경우에만 실행하며, break를 통해서 while문을 빠져나온 경우에는 else문이 실행되지 않는다.
# 
# 
# ```python
# count = 0
# while count < 5 :
#     pw=input('password')
#     if pw=='pythonisfun':
#        print('로그인 되었습니다.')
#        break
#     count = count + 1    
# else:
#     print ('로그인에 실패했습니다.')
# ```
# 
# 

# ### Sample Source Code #5
# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄 기회 횟수 제한하기: Sample Source Code #4에서 수정한 코드를 복사하여 붙여넣은 후 아래 TODO와 같이 수정해 주세요.
# ^^^
# 
#  - TODO: guess할 기회를 5번만 주고 5번안에 맞히지 못하면 반복문을 빠져나와 `f'oops! The number I was thinking of was {number}.'` 와 같이 메시지를 출력해주세요.
#  - 5번 이내에 number를 맞혔다면 맞혔을 때의 문장을 출력 후 반복문을 빠져나오도록 해야 합니다.
# 
# 

# In[ ]:





# ### continue
# 반복문에서 continue를 만나면 continue 아래쪽에 있는 모든 코드는 실행하지 않고 while문이 있는 라인으로 이동한다.
# 

# In[4]:


count = 0
while count < 31:
    count += 1
    if '3' in str(count):
      print(f'{"👏"*count}') #https://www.emojiengine.com/ko/keyboard/
      continue
    
    print(f'{count}')


# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. 위 코드를 수정하여 3, 6, 9 게임을 완성해보세요. 3,6,9가 문자열에 들어 있는 경우에는 박수를 숫자만큼 출력하도록 수정하시오.
# ^^^
# 
# ```
# 1 
# 2
# 👏👏👏
# 4
# 5
# 👏👏👏👏👏👏
# 7
# 8
# 
# ......
# 28 
# 👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏
# ......
# ```
# 
# 
# :::

# ### while 중첩문
# 
# 중첩 while문은 while문 안에 다른 while문이 들어 있는 것을 말한다. 

# In[5]:


out_count = 0
while out_count<5:
  in_count = 1
  while in_count <= out_count+1:
    print('🍩', end='')
    in_count += 1
  print()
  out_count += 1


# ## for loop
# while문이 주어진 조건에 대해 반복하는 것이였다면 for문은 주어진 범위에 대해 순회한다. 

# ### for statements
# 
# ```
# for 변수 in 범위(반복가능한 것들):
#     statements
# next_statements
# ```
# - while문에서는 조건에 사용될 변수를 while문 전에 미리 정의해야 했다. 그러나 for문에서는 for 다음에 바로 정의하면 된다. 
# - 범위에는 range, 문자열, 리스트, 튜플, 딕셔너리 등  반복가능한 데이터 타입(iterable data type)들이 올 수 있다.
# 

# - for문과 함께 유용하게 사용되는 range() 함수를 먼저 알아보자. 
# - range() 함수는 일정한 규칙에 따라 나열된 수열을 생성한다.
# 
# ```
# range(start, stop, step)
# ```
# - start: 범위의 시작 값이며, 생략하면 0이다.
# - stop: 범위의 끝값 + 1이다.
# - step: 범위의 간격이며, 생략하면 1이다.
# 
# 

# - range() 함수의 예를 살펴보자. 
# - `range(1, 10)`은 1부터 9까지 수열을 생성한다.
# - `range(10)`은 시작 값 생략으로 0부터 9까지 수열을 생성한다.
# - `range(3, 10, 3)`은 3부터 9까지 3씩 간격으로 수열을 생성한다.
# - `range(10, 3, -3)`은 10부터 2까지 -3씩 간격으로 수열을 생성한다.

# In[6]:


range(1, 10) 
range(10)   
range(3, 10, 3) 
range(10, 3, -3)


# - `범위에 range()`를 넣어보자.
# - 1부터 10까지 범위를 변수 count가 그 값을 순서대로 저장하면서 반복한다.
# - 비슷한 출력결과를 while문에서도 해봤을 것이다. for문이 while문보다는 코드가 간결한 것을 알 수 있다.

# In[7]:


for count  in range(1, 11):
    print(f'🌳를 {count}그루 심었습니다. {"🌳"*count}')
print('아~ 공기좋다~~~')


# In[8]:


for count  in range(1, 11, 2):
    print(f'🌳를 {count}그루 심었습니다. {"🌳"*count}')
print('아~ 공기좋다~~~')


# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. 다음과 같이 출력하는 코드를 for문을 이용해 작성해 보시오.
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```
# 나무를 1그루 심었습니다. 싹!
# 나무를 2그루 심었습니다. 싹!싹!
# 나무를 3그루 심었습니다. 싹!싹!싹!
# 나무를 4그루 심었습니다. 싹!싹!싹!싹!
# 나무를 5그루 심었습니다. 싹!싹!싹!싹!싹!
# ```
# :::

# :::{grid} 1
# :::{grid-item-card}
# :class-header: bg-light
# 
# 😄문제. for문을 이용하여 구구단 2단을 출력해보세요.
# ^^^
# 
# <font color='blue'>`test case-1`</font>
# ```
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# ```
# :::

# - 반복문안에서 값을 누적시키기 위해서는 누적을 위한 변수를 반복문 밖 위쪽에 정의해야 한다. 
# - 아래 코드에서 total은 처음에 0이였지만 반복할 때마다 total = total + i에 의해
#  1=0+1, 3=1+2, 6=3+3, 10=6+4.....로 누적값을 가진다.

# In[9]:


total=0
for i in range(1,11): 
  total = total+i   
  print(total)

print("The total is", total)


# - `범위에 문자열`을 넣을 수 있다. 문자열의 경우 변수 i가 한 글자씩 순회한다.

# In[10]:


for i in 'Hello World':
    print (i)


# - `범위에 리스트`를 넣을 수 있다. 리스트의 경우 변수 i가 리스트내 아이템(원소, 요소, 엘리먼트)를 하나씩 순회한다. 
# - 리스트는 아직 안 배웠으니 ['programming', 'pasta', 'spam', 'play park'] 이러한 구조가 리스트라는 것만 눈에 익혀두자.

# In[11]:


for i in ['programming', 'pasta', 'spam', 'play park']:
    print (i)


# - `범위에 딕셔너리`를 넣을 수 있다. 딕셔너리의 경우 변수 i가 딕셔너리의 key를 하나씩 순회한다. 
# - 딕셔너리 또한 아직 안 배웠으니 {'2323-12345':'가영', '2323-12346':'나영'} 이러한 구조가 딕셔너리라는 것만 눈에 익혀두자.

# In[12]:


for i in {'2323-12345':'가영', '2323-12346':'나영'}:
    print (i)


# ### for~else
# for문에도 else가 있다. while ~ else와 마찬가지로 for문이 정상적으로 모든 반복을 다 한 경우에만 실행한다.
# 
# ```
# for 변수 in 리스트(or 문자열 등) :
#     statements1
#     if 조건: 
#         if_statements
#         break
#     statements2
# else: 
#     else_statements
# next_statements
# ```

# In[13]:


a = 'computer'
letter = 'u'

for i in a:
    if i == letter:
        print(f'{letter}가 검색되었습니다.')
        break
else:
    print(f'{letter}는 검색되지 않았습니다.')
print('END')


# ### for 중첩문
# 
# 중첩 for문은 for문 안에 다른 for문이 들어 있는 것을 말한다. 

# In[14]:


for dan in range(2,10):
    print(f'{dan}단')
    for num in range(1,10):
        print(f'{dan}*{num}={dan*num}')
    print()


# ## 마무리
# 
# - 반복구조는 조건 또는 범위에 따라 실행문장을 반복한다. 
# - while문은 조건비교 결과가 True인 동안 블록 소스코드를 반복 수행한다.
# - for문은 범위의 처음부터 끝까지 차례대로 반복한다. 
# - for문의 in 연산자 뒤에는 반복가능한 데이터타입인 숫자, 리스트, 문자열, 딕셔너리, 튜플, 셋 등이 올 수 있다.
# - for 다음의 변수는 in 뒤에 있는 자료값을 하나씩 차례대로 저장한다.
# - for문은 숫자값의 범위를 만들어주는 range()함수를 유용하게 활용한다.
# 
