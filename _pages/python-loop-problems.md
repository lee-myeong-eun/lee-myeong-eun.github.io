---
layout: default
title: Python 반복문 문제풀이
permalink: /assignments/python-loop-problems/
---

<style>
  /* Ensure code blocks have a light, readable color on dark backgrounds */
  pre, code, .highlight pre, .highlight code, pre code {
    color: #bae6fd ;
    background-color: #161b22 ;
    border-radius: 8px;
  }
  .highlight {
    background-color: #161b22 ;
    border-radius: 8px;
    padding: 15px;
  }
</style>

## Python 반복문 문제풀이

# WHILE 반복문

# 1. 제곱 출력하기

## 요구 사항
- 사용자로부터 하나의 정수를 입력받는다.  
- 입력된 정수 `num`까지의 숫자에 대해 다음을 수행한다:  
  - `while` 문을 이용하여 1부터 `num`까지 각 수의 제곱을 출력한다.  
  - `for` 문을 이용하여 1부터 `num`까지 각 수의 제곱을 출력한다.  
- 두 반복문 모두 `1^2`, `2^2`, ..., `num^2`까지의 결과를 출력해야 한다.


```python
num = int(input('숫자를 입력하세요.'))
i = 1

while i <= num:
    print(i**2)
    i = i + 1
    
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">1
4
9
16
25
</pre>
</div>

```python
num = int(input('숫자를 입력하세요.'))
for i in range(1,i+1):
    print(i*i)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">1
4
9
16
25
36
</pre>
</div>

# 2. 공 튀기기 시뮬레이션

## 요구 사항
- 사용자로부터 하나의 정수를 입력받는다.  
- 공의 초기 높이는 100cm이다.  
- 공은 한 번 튈 때마다 이전 높이의 3/5만큼 튄다.  
- 입력한 횟수만큼 공이 튄 후, 최종 높이를 출력한다.  
- 최종 출력 형식은 `"최종 높이: ○○"`와 같이 표시한다.


```python
# 사용자로부터 정수 입력
n = int(input("튄 횟수를 입력하세요: "))

# 초기 높이 (cm)
height = 100

# 공 튀기기 시뮬레이션
for _ in range(n):
    height *= (3/5)

# 결과 출력
print(f"최종 높이: {height}")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">최종 높이: 7.775999999999999
</pre>
</div>

# 3. 별찍기 문제
## 요구사항(4입력 예시)
- 패턴 1: 정방향 삼각형
- 패턴 2: 오른쪽 정렬 정방향 삼각형
- 패턴 3: 역삼각형
- 패턴 4: 오른쪽 정렬 역삼각형
- 패턴 5: 피라미드

```python
# 패턴 1
"""
*
**
***
****
"""
num = int(input())
i = 1
while i <= 4:
    print('*'*i)
    i += 1
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">*
**
***
****
</pre>
</div>

```python
# 패턴 2
"""
   *
  **
 ***
****
"""
num = int(input())
i = 1

while i <= num:
    print(' ' * (num - i) + '*' * i)
    i += 1
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">   *
  **
 ***
****
</pre>
</div>

```python
# 패턴 3
"""
****
***
**
*
"""
num = int(input())
i = 4
while i > 0:
    print('*'*i)
    i -= 1
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">****
***
**
*
</pre>
</div>

```python
# 패턴 4
"""
****
 ***
  **
   *
"""
num = int(input())
i = num

while i >= 1:
    print(' ' * (num - i) + '*' * i)
    i -= 1
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">****
 ***
  **
   *
</pre>
</div>

```python
# 패턴 5
"""
   *
  ***
 *****
*******
"""
num = int(input())
i = 1

while i <= num:
    print(' ' * (num - i) + '*' * (2 * i - 1))
    i += 1
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">   *
  ***
 *****
*******
</pre>
</div>

# 4. 커피 자판기 시뮬레이션

## 요구 사항
- 사용자에게 커피 개수를 입력받는다.
- 사용자가 돈을 넣으면 다음 조건에 따라 처리한다:
  - 커피 값은 300원이다.
  - 300원을 넣으면 "커피를 줍니다."를 출력하고 커피를 1개 줄인다.  
  - 300원보다 많이 넣으면 "거스름돈 ○○원을 주고 커피를 줍니다."를 출력하고 커피를 1개 줄인다.  
  - 300원보다 적게 넣으면 "돈을 다시 돌려주고 커피를 주지 않습니다."를 출력하고, 남은 커피 수를 출력한다.  
- 커피가 0개가 되면 "커피가 다 떨어졌습니다. 판매를 중지합니다."를 출력하고 반복을 종료한다.


```python
coffee = int(input('개수를 입력해주세요.'))
while coffee > 0:
    money = int(input('돈을 넣어주세요.'))
    if money == 300:
        print('커피를 줍니다.')
        coffee = coffee - 1
    elif money > 300:
        print('거스름돈 %d을 주고 커피를 줍니다.' % (money-300))
        coffee = coffee - 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
        print('남은 커피의 양은 %d개입니다.' % coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지 합니다.')
        break
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">거스름돈 200을 주고 커피를 줍니다.
커피를 줍니다.
거스름돈 200을 주고 커피를 줍니다.
거스름돈 200을 주고 커피를 줍니다.
돈을 다시 돌려주고 커피를 주지 않습니다.
남은 커피의 양은 1개입니다.
커피를 줍니다.
커피가 다 떨어졌습니다. 판매를 중지 합니다.
</pre>
</div>

# FOR 반복문

# 1. 문자열 내 알파벳 빈도수 출력

## 요구 사항
- 사용자로부터 문자열을 입력받는다.  
- 입력된 문자열에서 알파벳(a~z, A~Z)의 빈도수를 출력한다.  
- 대소문자는 구분하지 않는다.  
- 알파벳이 아닌 문자는 무시한다.  
- 알파벳은 오름차순으로 정렬하여 출력한다.

### 예시 입력
Hello, Python!

### 예시 출력
- e: 1
- h: 2
- l: 2
- n: 1
- o: 2
- p: 1
- t: 1
- y: 1

```python
text = input().lower()  # 소문자로 변환

count = {}

for ch in text:
    if ch.isalpha():  # 알파벳만 체크
        count[ch] = count.get(ch, 0) + 1

# 알파벳 순서대로, 모든 항목 동일하게 '- ' 포함
for key in sorted(count):
    print(f"- {key}: {count[key]}")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">- e: 1
- h: 1
- l: 2
- o: 1
</pre>
</div>

# 2. 계단식 숫자 출력

## 요구 사항
- 사용자로부터 정수 n을 입력받는다.  
- `for` 반복문을 이용해 다음과 같은 숫자 계단을 출력한다.  
- 각 줄에는 1부터 해당 줄 번호까지의 숫자를 공백과 함께 출력한다. 단, 마지막에는 공백이 있어선 안된다.
- 줄 수는 입력한 정수만큼 출력한다.

### 예시 출력 (입력: 5)
- 1
- 1 2
- 1 2 3
- 1 2 3 4
- 1 2 3 4 5

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end='')  # 마지막 숫자는 공백 없이
        else:
            print(j, end=' ')
    print()  # 줄 바꿈
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
</pre>
</div>

# 3. 1부터 500까지 3과 5의 공배수 출력

## 요구 사항
- 1부터 500까지 숫자 중에서 **3과 5의 공배수**만 출력한다.  
- 출력 결과는 한 줄에 5개씩 출력되도록 한다.  
- 줄바꿈은 5개를 출력할 때마다 적용한다.  
- 각 숫자는 가독성을 위해 일정한 간격으로 정렬한다.

### 예시 출력
15 30 45 60 75

90 ...

```python
num = 0
for i in range(1,500):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end=' ')
        num += 1
        
        if num % 5 == 0:
            print()
        
    
        
        
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">15 30 45 60 75 
90 105 120 135 150 
165 180 195 210 225 
240 255 270 285 300 
315 330 345 360 375 
390 405 420 435 450 
465 480 495 </pre>
</div>

# 4. 구구단 2단부터 9단까지 출력하기

## 요구 사항
- `for` 반복문을 중첩 사용하여 **2단부터 9단까지**의 구구단을 출력한다.  
- 각 단은 `단 제목`을 먼저 출력한 후, 그 단의 곱셈 결과를 1부터 9까지 출력한다.  
- 출력 형식은 `2 x 1 = 2`, `3 x 2 = 6`과 같은 형태로 출력한다.

```python
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end ='')
    print('')
    
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 ;">24681012141618
369121518212427
4812162024283236
51015202530354045
61218243036424854
71421283542495663
81624324048566472
91827364554637281
</pre>
</div>

