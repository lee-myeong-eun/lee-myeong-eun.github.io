---
layout: default
title: Python 기초 문법 실습 포트폴리오
permalink: /assignments/python-basics/
---

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Header -->
    <div class="animate-fade-in-up delay-100">
      <span class="tech-badge">🐍 Python Study Record</span>
      <h2 class="text-gradient">Python 기초 문법 & 자료형 실습 포트폴리오</h2>
      <hr />
      <p class="lead text-light font-weight-normal">
        반도체 소프트웨어 및 장비 제어 개발을 위해 학습하고 정리한 **파이썬 기초 프로그래밍 논리 및 자료형 제어 실습** 전체 기록입니다.
      </p>
    </div>

    <!-- Contents Grid -->
    <div class="row mt-5 animate-fade-in-up delay-200">
      
      <!-- Left Sidebar Index -->
      <div class="col-lg-3 mb-4">
        <div class="border-0 shadow welcome-box p-3 sticky-top" style="top: 100px; z-index: 10; background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important;">
          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-list-ul mr-2"></i>학습 목차</h4>
          <ul class="list-unstyled small mb-0 pl-1" style="line-height: 2.2;">
            <li><a href="#section1" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-calculator mr-2" style="color: #38bdf8; width: 16px; text-align: center;"></i>1. 변수와 수치 연산</a></li>
            <li><a href="#section2" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-font mr-2" style="color: #fb7185; width: 16px; text-align: center;"></i>2. 문자열(String) 제어</a></li>
            <li><a href="#section3" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-list-ol mr-2" style="color: #34d399; width: 16px; text-align: center;"></i>3. 리스트와 튜플 (List, Tuple)</a></li>
            <li><a href="#section4" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-book-open mr-2" style="color: #a78bfa; width: 16px; text-align: center;"></i>4. 불과 딕셔너리 (Bool, Dict)</a></li>
            <li><a href="#section5" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-code-fork mr-2" style="color: #fb923c; width: 16px; text-align: center;"></i>5. 제어문 (If, Loop)</a></li>
            <li><a href="#section6" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-cube mr-2" style="color: #2dd4bf; width: 16px; text-align: center;"></i>6. 함수와 매개변수 (Functions)</a></li>
            <li><a href="#section7" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-file-text-o mr-2" style="color: #f472b6; width: 16px; text-align: center;"></i>7. 파일 입출력 & 클래스 실습</a></li>
          </ul>
          <hr class="my-3" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <a href="{{ site.baseurl }}/assignments/" class="btn btn-outline-light btn-sm btn-block text-hover-glow">
            <i class="fa fa-arrow-left mr-1"></i>아카이브로 돌아가기
          </a>
        </div>
      </div>

      <!-- Right Detailed Content -->
      <div class="col-lg-9 mb-4">
        <!-- Section: 1. 변수와 수치 연산 -->
        <div id="section1" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #38bdf8; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-calculator"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">1. 변수와 수치 연산</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### Python 기초 문법과 자료형 실습 포트폴리오

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>파이썬(Python)</span>


- 인간다운 언어
- 문법이 쉬워 빠르게 배울 수 있다.
- 무료이지만 강력하다.
- 간결하다.

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>변수(Variable)</span>


값을 저장하는 메모리 공간.
 - 변수 이름과 값을 할당하여 생성한다. ex) a = 10
 - 변수 이름은 식별자로 불리며, 식별자를 통해 변수를 사용할 수 있다.
 - 프로그램 실행 동안, 몇번이고 값이 바뀔 수 있다. (코드 재사용에 필수!)
 - 대소문자 구분 가능 ex) a와 A는 다른 변수
 - 자료형이 자동으로 바뀔 수 있다. 
   →(변수에 타입 지정 x , 값에 따라 자동적으로 결정되는 동적 타이핑 언어)
- 여러 변수 동시에 선언 가능 ex) a , b = 1 , 2



<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

- 변수 이름을 숫자로 시작 불가 (문자/언더스코어로 시작 가능!)
ex) 1a = 10 (X)
- 예약어 사용 불가 
ex) if = 10 (X)



```python
print('안녕하세요.') # print('') 안에 문자열을 넣어 사용

b = 5        # 변수 b에 5를 저장
print(b)     # 변수 b의 현재 값 출력

b = 15       # 변수 b에 15를 저장 (기존 5가 15로 변경됨)
print(b)     # 변수 b의 값 출력

b = 25       # 변수 b에 25를 저장 (기존 15가 25로 변경됨)
print(b)     # 변수 b의 값 출력
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">안녕하세요.
5
15
25</pre>
</div>


### 숫자형 자료형
변수에 저장되는 데이터 형식
- 정수와 실수로 구분
- 연산 결과에 따라 자동 형 변환 발생이 발생함. → 연산 결과의 정확도 유지 , 데이터 손실 방지를 위해 발생

정수형(int)
 - 정수형은 음의 정수, 0, 자연수 등 정수 값을 나타내는 자료형
 - 크기 제한이 거의 없다.
 - 정확한 값 표현이 가능하다.
 - ex) -5, -153, 0, 3, 1456
-----------------------------------
 실수형(float)
 - 정수와 소수점으로 표현되는 모든 값을 나타내는 자료형
 - 지수 표현 가능 (e 사용)
 - ex) -5.0, -123.4, 0.0, 3.12, 532.14

```python
# 변수 선언 : 변수이름 = 값
# 파이썬은 변수가 자료형을 스스로 판단하여 지정한다.
# type() 함수를 사용하여 변수의 자료형을 확인할 수 있다.

x = 50        # 변수 x에 정수 50을 할당한다.
y = 3.1415    # 변수 y에 실수 3.1415를 할당한다.

print(x)      # 변수 x의 값을 출력한다.
print(y)      # 변수 y의 값을 출력한다.

print(type(x))  # 변수 x의 자료형을 확인하고 출력한다.
print(type(y))  # 변수 y의 자료형을 확인하고 출력한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">50
3.1415
<class 'int'>
<class 'float'></pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>연산자</span>

숫자형 자료형을 가공하기 위한 연산자.
- 여러 종류로 구분 (비교, 논리 등)
- 연산 결과는 새로운 값으로 반환된다.

<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

- 문자열과 숫자는 직접 연산 불가
→ 의미와 자료형이 달라 동일한 연산 기준 적용 X

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>복합연산자</span>

산술 연산자( +, - 등 )와 대입 연산자( = )를 합친 것
   ex) +=, -=, *=, /=, //=, %=, **=

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i><사칙연산></span>

 - 덧셈 : + 
 - 뺄셈 : - 
 - 나눗셈 : /
 - 나머지 : %
 - 제곱 : **
 - (나눗셈 후)몫 : //
-------------------------------------
<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>연산자 우선순위</span>

 계산기와 같은 우선순위를 가짐
  1. 제곱 연산자
  2. 곱셈, 나눗셈, 나머지, 몫 연산자
  3. 덧셈, 뺄셈 연산자
  4. 괄호( )를 사용하면 연산자 우선순위를 변경할 수 있음.

```python
a = 10
b = 5

result = a + b      # a(10) + b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다.

result = a - b      # a(10) - b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다.

result = a * b      # a(10) × b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다.

# 다른 연산자는 결과 값이 동일한 자료형으로 나오는데,
# 나눗셈 연산자는 무조건 실수형으로 나온다.
result = a / b      # a(10) / b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다.

result = a % b      # a(10) % b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다. 10 / 5 = 몫:2, 나머지:0
print(10 % 7)       # 10 / 7 = 몫:1, 나머지:3

result = a ** b     # a(10) ** b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다.

result = a // b     # a(10) // b(5)의 값을 result에 저장한다.
print(result)       # result의 값을 출력한다. 10 / 5 = 몫:2, 나머지:0

result = 2 + 3 * 4  # 연산 우선순위에 따라 계산한다.
print(result)       # result의 값을 출력한다.

result = (2 + 3) * 4  # 괄호 우선순위에 따라 계산한다.
print(result)          # result의 값을 출력한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">15
5
50
2.0
0
3
100000
2
14
20</pre>
</div>


          </div>
        </div>

        <!-- Section: 2. 문자열(String) 제어 -->
        <div id="section2" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #fb7185; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-font"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">2. 문자열(String) 제어</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 문자열 자료형(str)
문자들의 집합, 따옴표( ' ', " " )로 표현 가능한 데이터 형식
- 인덱싱, 슬라이싱 가능
- 문자열 연산 및 다양한 함수 사용 가능


4가지의 방법으로 문자열을 생성할 수 있다.

 - '안녕하세요'
 - "안녕하세요"
 - '''안녕하세요'''
 - """안녕하세요"""

## ## ※ 주의할 점
 - 문자열은 수정 불가  → 문자열은 변경불가 자료형이라 생성 후 값 변경 불가능하다.
 - 숫자와 직접 연산 불가  → 문자열과 숫자는 자료형과 의미가 다르기 때문
 - 인덱스 범위를 초과할 경우 에러 발생

```python
a = """나는 생각"했"다"." '집 가고 싶다...'"""
print(a)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">나는 생각"했"다"." '집 가고 싶다...'</pre>
</div>


```python
"""
여러 줄 주석 예제
여러 줄의 설명이나 메모를 작성할 때 문자열을 사용하면 된다.
"""

# 문자열 안에 ""를 포함하기 위해 ''로 문자열을 구성한다.
greeting1 = 'greeting1, 선생님이 말했다."항상 긍정적으로 생각하라"\n'
print(greeting1)  # greeting1 출력한다.

# 문자열 안에 ''를 포함하기 위해 ""로 문자열을 구성한다.
greeting2 = "greeting2, 친구가 말했다. '포기하지 말자'\n"
print(greeting2)  # greeting2 출력한다.

# ''' '''로 씌어진 문자열은 줄바꿈, '', "" 등 거의 모든 형식을 표현할 수 있다.
greeting3 = '''greeting3, "안녕하세요"
모두 '열심히'
공부합시다!!\n'''
print(greeting3)  # greeting3 출력한다.

# """ """로 씌어진 문자열도 줄바꿈, '', "" 등 거의 모든 형식을 표현할 수 있다.
greeting4 = """greeting4, 오늘 하루도
힘내
세요."""
print(greeting4)  # greeting4 출력한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">greeting1, 선생님이 말했다."항상 긍정적으로 생각하라"

greeting2, 친구가 말했다. '포기하지 말자'

greeting3, "안녕하세요"
모두 '열심히'
공부합시다!!

greeting4, 오늘 하루도
힘내
세요.</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>이스케이프 문자</span>

특수한 문자를 표현하기 위해 사용되는 문자.

백슬래쉬(\\)로 시작하는 문자열.

 - \n, 줄 바꿈 문자
 → 문자열이 여러 개인 경우 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하는 것도 더 깔끔하다.
 - \t, 탭 문자
 - \\\\, 백슬래쉬 문자
 - \\', 작은따옴표 문자
 - \\", 큰따옴표 문자
 - \r, 줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동
 - \f, 폼 피드(커서를 다음 줄로 이동)
 - \a, 벨소리
 - \b, 백 스페이스
 - \000, 널문자

※ 자주 사용하는 코드
→ \n, \t, \\, \', \"

<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

- 출력 시 눈에 안 보일 수도 있음.
→ 문자 대신 동작으로 처리되기때문이다.

 

```python
# \' 작은따옴표 문자를 이용하여 ''로 구성된 문자열 안에서 '사용
a = '선생님은 말했다.\n\'최선을 다하라\''
print(a)

# \t 탭 문자를 사용하여 길이가 다른 두 문자열을 일정한 길이로 유지.
b = "115\t23\t4516"
c = "1\t31255\t456"
print(b)
print(c)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">선생님은 말했다.
'최선을 다하라'
115	23	4516
1	31255	456</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 연산</span>

문자열은 덧셈 연산과 곱셈 연산 사용이 가능하다.

 - 덧셈 : 문자열 + 문자열 -> 문자열이 하나로 합쳐진다.
  ex)  "hello" +"world" → "helloworld"
 - 곱셈 : 문자열 * 숫자 -> 문자열이 숫자만큼 반복된다.
  ex)  "hi" * 3 → "hihihi"

## ## ※ 주의할 점
  - 문자열과 숫자는 직접 연산 불가
  ex) "hi" + 3 → X
  - 반복 연산 시 정수만 가능
  ex) "hi" * 2 → O
    ,  "hi" * 2.5 → X


```python
# 문자열 연산 예제

a1 = "Hello "  # 변수 a1에 문자열 "Hello "를 저장한다.
a2 = "World"   # 변수 a2에 문자열 "World"를 저장한다.

# 문자열 덧셈: "Hello " + "World" = "Hello World"
text = a1 + a2  # a1과 a2를 더해 text에 저장한다.
print(text)     # text를 출력한다.

# 문자열 곱셈: "Hello " * 5 = "Hello Hello Hello Hello Hello "
text1 = a1 * 5  # a1을 5번 반복하여 text1에 저장한다.
print(text1)    # text1을 출력한다.

print(a2 * 3)   # a2를 3번 반복하여 출력한다.

# 문자열 곱셈을 이용하여 '*' 50개 출력하기
print("*" * 50)  # '*' 50개를 출력한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">Hello World
Hello Hello Hello Hello Hello 
WorldWorldWorld
**************************************************</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 인덱싱</span>

문자열의 각 문자에 번호(인덱스)를 붙여 특정 위치의 문자를 가져오는 것

- 인덱스는 0부터 시작한다. 
   ex) "abcd"[0] → 'a'
- 음수 인덱스는 뒤에서부터 시작한다.
   ex) "adcd"[-1] → 'd'
- 문자열은 변경 불가능



<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

- 인덱스 범위를 벗어나면 오류가 발생
- 문자열은 수정이 안되므로 값 변경 시에는 새로운 문자열 만들기


```python
# 문자열 인덱싱 예제 (단어 변경)

msg = "hello world"  # msg 변수에 문자열 "hello world"를 저장한다.

x = msg[0]           # msg의 첫 번째 문자를 x에 저장한다. ("h")
xx = msg[-11]        # msg의 뒤에서 11번째 문자를 xx에 저장한다. ("h")
print(x)             # x를 출력한다.
print(xx)            # xx를 출력한다.

y = msg[5]           # msg의 6번째 문자(공백)를 y에 저장한다.
print(y)             # y를 출력한다.

z = msg[6]           # msg의 7번째 문자 "w"를 z에 저장한다.
zz = msg[-5]         # msg의 뒤에서 5번째 문자 "w"를 zz에 저장한다.
print(z)             # z를 출력한다.
print(zz)            # zz를 출력한다.

# 여러 문자를 더해 새로운 문자열 생성
new_word = msg[0] + msg[1] + msg[2] + msg[3]  # "h"+"e"+"l"+"l" = "hell"
print(new_word)      # new_word를 출력한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">h
h
 
w
w
hell</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 슬라이싱</span>

문자열을 원하는 지점부터 원하는 크기만큼 분해하는 것.
 - 변수명[첫번째항목:마지막항목+1]
 - 인덱스 마지막은 포함되지 않아, 추출하고싶은 마지막항목+1의 값을 지정해주어야함
 - 첫번쨰 인덱스를 공백으로 놓으면, 0번 인덱스부터 추출.
 - 마지막 인덱스를 공백으로 놓으면, 문자열 끝까지 추출.
 - 음수 인덱스 사용 가능

## ## ※ 주의할 점
 - 범위를 초과해도 에러 X  → 가능한 범위까지만 잘라서 반환하도록 설계되어 있기 때문이다.
 - 결과는 새로운 문자열로 생성  → 문자열은 수정이 불가능한 자료형


```python
# ex) 
# a = "python"

# a[0:2] → "py"
# a[:3]  → "pyt"
# a[3:]  → "pon"
# a[-3:] → "hon"
```
```python
# 문자열 슬라이싱 예제

sentence = "hello python world"  # sentence 변수에 문자열을 저장한다.

# "world" 문자 가져오기
print(sentence[13]+sentence[14]+sentence[15]+sentence[16]+sentence[17])  # 개별 문자 더하기
print(sentence[13:18])  # 슬라이싱: 13번부터 17번까지 가져오기
print(sentence[13:])    # 13번부터 끝까지 가져오기

# "hello" 문자 가져오기
print(sentence[0]+sentence[1]+sentence[2]+sentence[3]+sentence[4])  # 개별 문자 더하기
print(sentence[0:5])  # 슬라이싱: 0번부터 4번까지 가져오기
print(sentence[:5])   # 시작 생략 가능, 0번부터 4번까지 가져오기

# "py" 문자 가져오기 (2가지 방법)
print(sentence[6]+sentence[7])  # 개별 문자 더하기
print(sentence[6:8])            # 슬라이싱: 6번부터 7번까지 가져오기
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">world
world
world
hello
hello
hello
py
py</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 포맷팅</span>

문자열에서 변수나 값을 원하는 형식으로 출력하는 방법.
 1. 숫자를 바로 대입하는 방법
 2. 문자열을 바로 대입하는 방법
 3. 변수를 통해 값을 대입하는 방법

- 여러가지 방법 존재 (%방식, format(), f-string)
- 가독성이 좋고 출력 문장을 만들 때 자주 사용
--------------------------------------

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 포맷 코드</span>

문자열 포맷 코드 헷갈리면 무조건 %s 사용!!
 - %s : 문자열(string)
 - %c : 문자 1개(character)
 - %d : 정수(integer)
 - %f : 실수(Floating point)
 - %o : 8진수
 - %x : 16진수

## ## ※ 주의할 점
 - %방식은 자료형을 맞춰야 한다.
 - 따옴표(' ')안에 사용해야 한다.

```python
# 문자열 포맷 코드(%d)에 숫자를 바로 대입하는 방법.
print("고구마 %d 개가 있습니다." % 3)

# 문자열 포맷 코드(%s)에 문자열을 바로 대입하는 방법.
print("제 이름은 %s 입니다." % "이명은")

number = 5
# 문자열 포맷 코드에 변수를 대입하는 방법.
print("고구마 %d 개가 있습니다." % number)

# 2개 이상의 문자열 포맷 코드 % (a, b)의 형식으로 사용
fruit = ""
number = 5
print("저는 %d개의 %s고구마가 있습니다." %(number, fruit))

# %d를 %s로 바꾸어도 상관없음.
print("저는 %s개의 %s고구마가 있습니다." %(number, fruit))
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">고구마 3 개가 있습니다.
제 이름은 이명은 입니다.
고구마 5 개가 있습니다.
저는 5개의 고구마가 있습니다.
저는 5개의 고구마가 있습니다.</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 관련 함수</span>

 - LEN : 문자열 길이 구하기
 - COUNT : 특정 문자 수 세기
 - UPPER : 모든 문자 대문자로 변경
 - LOWER : 모든 문자 소문자로 변경
 - STRIP : 양쪽 공백 지우기
 - LSTRIP : 왼쪽 공백 지우기
 - RSTRIP : 오른쪽 공백 지우기
 - SPLIT : 문자열 원하는 형식으로 나누기
 - REPLACE : 문자열 원하는 문자열로 바꾸기
 - JOIN : 문자열 사이사이에 문자 삽입

## ### LEN( )
 공백, 이스케이프 문자를 포함한 문자열의 길이를 구하는 함수
 - 문자열, 리스트, 튜플 등 다양한 자료형에 사용 가능
 - 결과는 정수형(int)으로 반환됨.
 - ex) len("hello")  → 5
 - ex) len([1,2,3])  → 3

## ## ※ 주의할 점
 - 함수이기 때문에 괄호( )는 필수
 - 공백도 하나의 문자로 표함됨.
   → ex) len("hi there")  → 8
 - 문자열 길이 = 문자 개수
   → ex) len("a/n")  → 2 (줄바꿈도 문자로 포함)

```python
# len() 함수를 이용하여 문자열의 길이 구하기
# \t와 같은 이스케이프 문자열도 1개의 문자로 취급한다.

# 함수 -> 특정한 기능을 하는 코드
text = "i love\tpython."
print(text)
print(len(text))      # text 변수의 길이를 구해서 출력한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">i love	python.
14</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>COUNT()</span>

문자열에 속한 특정 문자의 개수를 세는 함수
- 문자열( str ), 리스트( list ) 모두 사용 가능
 → 둘 다 여러 값의 집합(시퀀스)이라 count와 같은 기능 사용 가능하다.
- 결과는 정수형(int)으로 반환됨.
- 대소문자 구분 가능
- 없는 값에는 0 반환

```python
text = "python is very nice"
print(text.count('o'))      # text 변수 안에 저장되어있는 문자열 중 소문자 o의 개수 세기
print(text.count('a'))      # 문자열에 문자가 존재하지 않으면, 0을 반환한다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1
0</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>JOIN()</span>

문자열 사이사이에 특정 문자를 삽입하는 함수
- 결과는 하나의 문자열(str)로 반환됨.
- 문자열 자료형, 리스트, 튜플 모두 입력으로 사용 가능


```python
text = "python is very nice"

# text 문자열의 모든 문자 사이사이에 ,를 삽입한다.
print(','.join(text))
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">p,y,t,h,o,n, ,i,s, ,v,e,r,y, ,n,i,c,e</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>UPPER()</span>

문자열을 모두 대문자로 변경하는 함수
→ 문자열이 대문자라면 아무런 변화 X



```python
text1 = "python is nice"
text2 = "Python Is Good"

print(text1.upper())
print(text2.upper())
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">PYTHON IS NICE
PYTHON IS GOOD</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>LOWER()</span>

문자열을 모두 소문자로 변경하는 함수

```python
text1 = "PYTHON IS NICE"
text2 = "Python Is Good"

print(text1.lower())
print(text2.lower())
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">python is nice
python is good</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>STRIP()</span>

양쪽 공백을 지우는 함수 (한 칸 이상의 연속된 공백 모두 지우기)


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>LSTRIP()</span>

왼쪽 공백을 지우는 함수


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>RSTRIP()</span>

오른쪽 공백을 지우는 함수

```python
text = "  bye  "

print(text)
print(text.strip())
print(text.lstrip())
print(text.rstrip())
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">bye  
bye
bye  
  bye</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>SPLIT()</span>

문자열을 특정 기준에 따라 분리하는 함수
 - 형식을 지정하지 않으면 공백, TAB, 엔터로 분리가 됨.
 - 분리된 결과는 리스트의 형식으로 저장됨.
 - 괄호 안에 특정 값이 있을 경우 괄호 안의 값을 구분자로 하여 문자열을 나눠준다.

```python
text = "python is excellent"
print(text.split())       # 형식을 지정하지 않아 공백으로 분리됨.

text1 = "a,b,c,d,e"
print(text1.split(','))    # 구분자를 ','로 직접 지정
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">['python', 'is', 'excellent']
['a', 'b', 'c', 'd', 'e']</pre>
</div>



<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 바꾸기 - replace</span>

● replace 함수는 replace(바뀔_문자열, 바꿀_문자열)처럼 사용하여 문자열 안의 특정한 값을 다른 값으로 치환

```python
# 예시

a = "a:b:c:d"   
a. replace("a:b:c:d", "a#b#c#d")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">'a#b#c#d'</pre>
</div>


```python
text = "python is excellent"
print("원래 단어: "+text+"\n바뀐 단어: "+text.replace("good", "bad"))
print("\n원래 단어: "+text+"\n바뀐 단어: "+text.replace("python is", "I am"))
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">원래 단어: python is excellent
바뀐 단어: python is excellent

원래 단어: python is excellent
바뀐 단어: I am excellent</pre>
</div>


### 사용자 입력 : INPUT()
사용자에게 값을 입력받는 함수
- 변수 = input('문자열을 입력하세요: ')
- 문자열 외의 다른 자료형을 사용하기 위해 자료형 변환을 사용해아 한다.

```python
# int
# float
a = int(input('숫자를 입력하세요:'))
b = float(input('소수 값을 입력하세요:'))

print(a + b)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">2.0</pre>
</div>


```python

# 문자열 입력
username = input('이름을 입력해주세요: ')          # 문자열로 저장

# 정수 입력
age = int(input('나이를 입력해주세요: '))         # 정수로 저장

# 실수 입력
height = float(input('키(cm)를 입력해주세요: '))   # 실수로 저장

future_age = age + 5
height_m = height / 100  # cm → m 변환

print(f"{username}님, 5년 후 나이는 {future_age}세이고, 키는 {height_m}cm입니다.")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">이명은 님, 5년 후 나이는 29세이고, 키는 160.0cm입니다.</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>제곱 문제</span>

사용자에게 입력받은 수의 제곱을 계산하여 출력하는 코드를 작성하시오.

- a=4, 결과 -> 16 출력.
- b=6, 결과 -> 36 출력.

```python
a = int(input())

print(a*a)
print(a**2)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">16
16</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>문자열 인덱싱&슬라이싱 문제</span>

문자열 인덱싱 또는 슬라이싱을 사용하여 년 월 일 계절을 출력하시오.

text = '20030820summer'
 - year = '2003'
 - month = '08'
 - day = '20'
 - weather = 'summer'


```python
text = '20220114fall'
# [2][0][2][2][0][1][1][4][f][a][l][l]
# [0][1][2][3][4][5][6][7][8][9][10][11]

year = text[0:4]
month = text[4:6]
day = text[6:8]
season = text[8:]

# print 함수는 문자열을 출력하는 함수.
# 문자열 덧셈 연산을 할 시에, 문자열이 이어진다.
print(year+'년 '+month+'월 '+day+'일\n계절 : '+season)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">2022년 01월 14일
계절 : fall</pre>
</div>


          </div>
        </div>

        <!-- Section: 3. 리스트와 튜플 (List, Tuple) -->
        <div id="section3" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #34d399; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-list-ol"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">3. 리스트와 튜플 (List, Tuple)</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 리스트 자료형(list)
모든 종류의 자료형을 자유로게 묶어서 사용할 수 있는 자료형의 묶음.
 - list = [3, "이명은", -0.5, '안녕']
- 대괄호[]로 표현
- 서로 다른 자료형과 함께 저장 가능
- 리스트 안에 리스트도 가능
  a = [1, [2,3]]


```python
# 비어 있는 리스트 생성
a = list()
a = []

# 리스트를 직접 선언
b = [3, "이명은", -0.5, '안녕']

# b리스트를 c에 복사
c = list(b)

print(a)
print(b)
print(c)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[]
[3, '이명은', -0.5, '안녕']
[3, '이명은', -0.5, '안녕']</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>리스트 인덱싱</span>

리스트도 문자열과 유사하게 인덱싱 및 슬라이싱이 가능하다.

단, 문자열이나, 리스트 내부의 리스트도 하나의 요소로 취급한다.
 - a = [1, "고구마", -0.5, '맛있다']
 - a[0] = 1
 - a[1] = "고구마"
 - a[2] = -0.5
 - a[3] = '맛있다'

```python
a = [1, "고구마", -0.5, '맛있다']
print("a[0]: "+ str(a[0]))        # 정수 1을 문자열 "1"로 자료형 변환
print("a[1]: "+ a[1])
print("a[2]: "+ str(a[2]))
print("a[3]: "+ a[3])

# a[1] = "고구마"
print("a[1][0]: "+ a[1][0])   # a[1][0] = "문"
print("a[1][1]: "+ a[1][1])   # a[1][1] = "자"
print("a[1][2]: "+ a[1][2])   # a[1][2] = "열"
print()

b = [1, 2, [3, 4, 5]]
print("b[0]: "+ str(b[0]))     # 1
print("b[1]: "+ str(b[1]))     # 2
print("b[2]: "+ str(b[2]))     # [3,4,5]
print("b[2][0]: "+ str(b[2][0]))  # 3
print()

# c리스트 안에 있는 요소 'b'에 접근하는 방법.
c = [1, 2, 3, ['python', 'is', 'nice', ['a', 'b', 'c']]]
print(c[3][1][0])
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">a[0]: 1
a[1]: 고구마
a[2]: -0.5
a[3]: 맛있다
a[1][0]: 고
a[1][1]: 구
a[1][2]: 마

b[0]: 1
b[1]: 2
b[2]: [3, 4, 5]
b[2][0]: 3

i</pre>
</div>


```python
# c리스트 안에 있는 요소 'b'에 접근하는 방법.
c = [1, 2, 3, ['python', 'is', 'nice', ['a', 'b', 'c']]]
print(c[3][0][3])
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">h</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>리스트 슬라이싱</span>

 - 문자열과 동일한 방법으로 리스트 슬라이싱 할 수 있다.
 - 리스트가 중복 되었을 때에는, 인덱싱한 후 슬라이싱을 해야한다.

```python
b = [1, 2, 3, ['python', 'is', 'nice', ['a', 'b', 'c', 'd']]]

# 1, 2, 3을 가져오고 싶으면
print(b[0:3])

# ['python', 'is', 'nice'] 을 가져오고 싶으면
print(b[3][0:3])

# ['a', 'b', 'c','d']를 가져오고 싶으면
print(b[3][3])
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[1, 2, 3]
['python', 'is', 'nice']
['a', 'b', 'c', 'd']</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>리스트 뎃셈과 곱셈</span>

리스트 덧셈 : 두개의 리스트를 합쳐 하나의 리스트로 만드는 연산 (+는 2개의 리스트를 합치는 기능)
- ※ 숫자처럼 계산되는 것 아님

리스트 곱셈 : 리스트를 지정한 횟수만큼 반복하여 새로운 리스트를 만드는 연산 
- ※ 정수만 곱셈 가능

```python
a = [1, 2, 3]
b = [4, 5, 6]

# 리스트 덧셈
c = a + b     # a리스트와 b리스트가 합쳐져 변수 c에 저장됨
print(c)

# 리스트 곱셈
print(a*3)
print(b*4)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>리스트 관련 함수</span>

 - LEN() : 리스트의 길이 구하기
 - APPEND() : 리스트에 요소 추가
 - SORT() : 리스트 정렬
 - REVERSE() : 리스트 뒤집기
 - INDEX() : 요소의 위치 찾기
 - INSERT() : 요소 삽입하기
 - REMOVE() : 요소 제거하기
 - POP() : 요소 추출하기
 - COUNT() : 요소의 개수 세기

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>LEN()</span>

리스트의 길이를 구하는 
- 문자열, 리스트, 튜플, 딕서녀리에도 사용 가능

```python
b = [1, 2, 3, ['python', 'is', 'nice', ['a', 'b', 'c']]]

print(len(b))     # ['python', 'is', 'nice', ['a', 'b', 'c']] -> 1개의 요소로 취급.
print(len(b[3]))  # ['a', 'b', 'c'] -> 1개의 요소로 취급.
print(len(b[3][0]))   # 'python'
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">4
4
6</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>리스트 요소 수정 삭제 및 추가</span>

수정 : 리스트의 요소에 직접 접근하여 수정한다.

삭제 : del 키워드로 요소 삭제한다.

추가 : append() 함수를 사용한다. ( append( x ) 리스트의 맨 마지막에 x를 추가하는 함수)

```python
aa = [10, 20, 30, 40, 50]
print(a)  # 초기 리스트 출력

a[3] = 35      # 3번 인덱스 값 변경
print(a)

del a[1]       # 1번 인덱스 요소 삭제
print(a)

del a[2:]      # 2번 인덱스부터 끝까지 삭제
print(a)

a.append(45)           # 한 요소 추가
print(a)

a.append([55, 65, 75]) # 리스트 자체를 요소로 추가
print(a)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[2, 3, 4, [5, 6, 7, 8]]
[2, 3, 4, 35]
[2, 4, 35]
[2, 4]
[2, 4, 45]
[2, 4, 45, [55, 65, 75]]</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>SORT()</span>

리스트를 오름차순으로 정렬시키는 함수
(문자도 알파벳 순서로 정렬 가능)


```python
aa = [9, 3, 8, 1, 5, 2, 7]
print(a)  # 초기 숫자 리스트

a.sort()  # 오름차순 정렬
print(a)

b = ['d', 'x', 'c', 'a', 'm', 'b']
print(b)  # 초기 문자 리스트

b.sort()  # 알파벳 순 정렬
print(b)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
['d', 'x', 'c', 'a', 'm', 'b']
['a', 'b', 'c', 'd', 'm', 'x']</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>REVERSE()</span>

리스트를 역순으로 뒤집기, 리스트의 첫번째 요소부터 마지막 요소까지 순서를 뒤바꾸는 함수
- ※ reverse를 사용할 때는 sort 후 실행해야 가능함.


```python
a = [10, 20, 30, 40, 50]
b = ['h', 'e', 'l', 'l', 'o']

print(a)  # 초기 숫자 리스트
a.reverse()  # 리스트 순서 뒤집기
print(a)

print(b)  # 초기 문자 리스트
b.reverse()  # 리스트 순서 뒤집기
print(b)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[10, 20, 30, 40, 50]
[50, 40, 30, 20, 10]
['h', 'e', 'l', 'l', 'o']
['o', 'l', 'l', 'e', 'h']</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>INDEX()</span>

문자열, 리스트에서 원하는 요소의 위치를 찾는 함수
 - 리스트 내부에 같은 값이 존재할 때, 가장 앞에 있는 요소의 위치를 반환
 - 리스트 내에 없는 값을 찾을 시 에러가 발생한다.
 - 0부터 시작


```python
a = [5, 7, 9, 5, 2, 1]
print(a.index(9))  # 9의 위치인 2번 인덱스 반환

print(a.index(5))  # 5는 여러 개 있지만 가장 앞의 0번 인덱스 반환

# print(a.index(10))
# ValueError: 10 is not in list (리스트에 없는 값이라 오류 발생)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">2
0</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>INSERT()</span>

리스트의 원하는 위치에 값을 삽입하는 함수

```python
# insert(위치, 값)으로 원하는 위치에 값을 삽입한다.

a = [10, 20, 30, 40, 50]
print(a)

a.insert(1, 15)  # 1번 인덱스 위치에 15 삽입
print(a)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[10, 20, 30, 40, 50]
[10, 15, 20, 30, 40, 50]</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>리스트 요소 제거 - remove</span>

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>remove는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수</span>

● a가 1이라는 값을 2개 가지고 있는 경우, 첫 번째 1만 제거
● 만약, 1이라는 값을 3개 가지고 있을 경우에는 remove 두번 사용

```python
a = [1,1,1,2,2,3,3,3,4,4,5]

a.remove(1)
a
a.remove(1)
a
a.remove(2)
a
a.remove(3)
a
a.remove(3)
a
a.remove(4)
a
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[1, 2, 3, 4, 5]</pre>
</div>


```python
a = [1, 2, 3, 1, 4, 5]
print(a)

if 1 in a:
    a.remove(1)  # 값이 있을 때만 제거
print(a)

if 3 in a:
    a.remove(3)
print(a)

if 3 in a:
    a.remove(3)  # 없으면 실행 안 해서 오류 방지
print(a)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[1, 2, 3, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 1, 4, 5]
[2, 1, 4, 5]</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>POP()</span>

리스트의 원하는 위치에 있는 요소 '추출'하기
- 인덱스를 지정하면 해당 위치의 요소는 삭제
- 삭제된 값을 반환

```python
a = [10, 20, 30, 40, 50]
print(a)

b = a.pop(1)  # pop으로 1번 인덱스(20)를 추출하여 b에 저장
print(a)
print(b)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[10, 20, 30, 40, 50]
[10, 30, 40, 50]
20</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>COUNT()</span>

리스트에 있는 원하는 요소의 개수 세기
- 같은 값이 여러 개 있을 때 사용

```python
a = [5, 1, 3, 5, 7, 5, 9, 2, 5]
print(a)

print(a.count(5))  # 리스트 안에 있는 요소 5의 개수를 세서 출력
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[5, 1, 3, 5, 7, 5, 9, 2, 5]
4</pre>
</div>


### 튜플 자료형(tuple)
여러 개의 데이터를 순서대로 저장하는 자료형.
- 리스트와 마찬가지로, 모든 자료형을 담을 수 있는 자료형.

- 튜플은 한 번 생성하면 값의 변경, 삭제가 불가능하다.

※ 리스트와는 다르게 append 등 사용 불가 

```python
# 모든 자료형을 담을 수 있는 자료형.
t1 = (1, 2, 3, ('python', 'is', 'nice', ('a', 'b', 'c')))
print(t1)

# 튜플 내부에 요소가 하나만 존재할 때 맨 뒤에 ,를 붙인다.
t2 = (2,)
print(t2)

#튜플 생성시 괄호()를 생략해도 상관없다.
t3 = 1, 2, 3
print(t3)

# 1. 튜플 인덱싱
# 2. 튜플 슬라이싱
# 3. 튜플 더하기
# 4. 튜플 곱하기
# 5. LEN() 함수
# 위와 같은 기능을 사용할 수 있다.
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">(1, 2, 3, ('python', 'is', 'nice', ('a', 'b', 'c')))
(2,)
(1, 2, 3)</pre>
</div>


          </div>
        </div>

        <!-- Section: 4. 불과 딕셔너리 (Bool, Dict) -->
        <div id="section4" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #a78bfa; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-book-open"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">4. 불과 딕셔너리 (Bool, Dict)</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 불 자료형(BOOL)
True(참), False(거짓)의 값만을 갖는 자료형.

```python
a = True
b = False

print(type(a))  
print(type(b))  

print(a)  
print(b) 
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;"><class 'bool'>
<class 'bool'>
True
False</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>비교 연산자</span>

두 값의 비교하여 True, False의 값을 반환하는 연산자.
- 조건문(if)에서 자주 사용
- 숫자뿐 아니라 문자열도 비교 가능

```python
# 비교 연산자 : < > == != <= >=
# = : 대입 연산자
# == : 같다
# != : 다르다

x = 1
y = 2

print("x==y: "+str(x == y))       # 1 과 2는 같은가?
print("x!=y: "+str(x != y))       # 1 과 2는 다른가?
print("x>y: "+str(x > y))        # 1 > 2?
print("x<y: "+str(x < y))        # 1 < 2?
print("x<=y: "+str(x <= y))      # 1 <= 2?
print("x>=y: "+str(x >= y))       # 1 >= 2?
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">x==y: False
x!=y: True
x>y: False
x<y: True
x<=y: True
x>=y: False</pre>
</div>


### 논리 연산자
여러 조건을 결합하여 하나의 Ture / False 결과를 만드는 연산자
- and, or, not 세 가지 존재

<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

- and는 앞이 False면 뒤는 실행 X
- or은 앞이 True면 뒤는 실행 X
- 우선순위가 존재함. (not > and > or)

```python
# 논리 연산자   and, or, not
a = True
b = False


# and 연산자 : a와 b모두 True일 때만, True
print("True and True: "+str(a and a))
print("True and False: "+str(a and b))
print("False and True: "+str(b and a))
print("False and False: "+str(b and b))

# or 연산자 : a와 b모두 False일 때만, False
print("True or True: "+str(a or a))
print("True or False: "+str(a or b))
print("False or True: "+str(b or a))
print("False or False: "+str(b or b))

# not 연산자
print("not True: "+str(not a))
print("not False: "+str(not b))
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">True and True: True
True and False: False
False and True: False
False and False: False
True or True: True
True or False: True
False or True: True
False or False: False
not True: False
not False: True</pre>
</div>


### 딕셔너리 자료형
사전, key와 Value를 한 쌍으로 데이터를 저장하는 자료형.
 - 순차적으로 접근하지 않고, 오직 Key를 통해서 Value값에 접근.
 - 순서가 없기 때문에, 인덱싱 및 슬라이싱이 불가능.
 - Key값은 고유한 값이므로, 중복되는 Key값을 사용하면 안됨.
 - 중괄호 { }로 표현

```python
# 딕셔너리 예제
dic = {'cat': '고양이', 'dog': '강아지', 'bird': '새'}
dic1 = {1: 'hello', 2: [10, 20, 30], '3': 100}

print(dic)   # dic 출력
print(dic1)  # dic1 출력
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">{'cat': '고양이', 'dog': '강아지', 'bird': '새'}
{1: 'hello', 2: [10, 20, 30], '3': 100}</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>딕셔너리 추가 및 삭제</span>



<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>딕셔너리 쌍 추가</span>

딕셔너리의 키와 값을 변수에 그대로 대입한다.
 - 변수명[Key] = Value

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>딕셔너리 요소 삭제</span>

del 키워드를 사용하여 요소를 삭제한다.
 - del 변수명[Key]

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>딕셔너리 사용 방법</span>

 예를 들면, 4명의 사람이 있다고 가정하고 각자의 특기를 표현할 수 있는 좋은 방법에 대해서 생각해보면
 리스트나 문자열로는 표현하기가 까다롭지만, 
 파이썬의 딕셔너리를 사용하면 쉽게 표현 가능하다.

ex)

```python
{"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}
```
이렇게 사람 이름과 특기를 한 쌍으로 묶으면 딕셔너리를 간펀하게 사용할 수 있다.

```python
# 딕셔너리 생성
dic = {'a': 100, 'b': 200}
print(dic)

# 딕셔너리 추가
dic['c'] = 300
print(dic)

# 딕셔너리 삭제
del dic['b']
print(dic)

# Key를 통해 Value값 얻기
print(dic['a'])  # 'a' 키의 값 출력

# Key 중복 시 마지막 값만 유효
test_dic = {'x': 1, 'y': 2, 'y': 20, 'z': 3, 'z': 30}
print(test_dic)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">{'a': 100, 'b': 200}
{'a': 100, 'b': 200, 'c': 300}
{'a': 100, 'c': 300}
100
{'x': 1, 'y': 20, 'z': 30}</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>딕셔너리 관련 함수</span>

 - keys() : key 리스트 만들기
 - values() : value 리스트 만들기
 - items() : key, value 쌍 리스트 얻기(튜플값)
 - clear() : key: value 쌍 모두 지우기
 - get() : key값을 통해 value값 얻기
 - in : key가 딕셔너리에 있는지 찾아보기(true, false)



```python
# 딕셔너리 생성
dic = {'cat': '고양이', 'dog': '강아지', 'bird': '새'}

# key, value, (key, value) 조회
print(dic.keys())     # key 리스트
print(dic.values())   # value 리스트
print(dic.items())    # (key, value) 튜플 리스트

# 특정 key의 value 조회
print(dic.get('dog'))   # 'dog'의 value 출력
print(dic.get('lion'))  # 존재하지 않는 key 조회, None 반환

# key 존재 여부 확인
print('cat' in dic)    # True
print('lion' in dic)   # False

# 딕셔너리 초기화
dic.clear()
print(dic)             # {}
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">dict_keys(['cat', 'dog', 'bird'])
dict_values(['고양이', '강아지', '새'])
dict_items([('cat', '고양이'), ('dog', '강아지'), ('bird', '새')])
강아지
None
True
False
{}</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>Q1</span>

홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
- 국어 : 80점
- 영어 : 75점
- 수학 : 55점

```python
a = 80
b = 75
c = 55
print((a + b + c) / 3)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">70.0</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>Q2</span>

[1,3,5,4,2]리스트를 [5,4,3,2,1]로 만들어보자.

```python
a = [1, 3, 5, 4, 2]


a.sort()
a
a.reverse()
a

```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[5, 4, 3, 2, 1]</pre>
</div>


          </div>
        </div>

        <!-- Section: 5. 제어문 (If, Loop) -->
        <div id="section5" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #fb923c; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-code-fork"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">5. 제어문 (If, Loop)</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### if문 (조건문)
조건이 참(True)일 때만 특정 코드르 실행하는 문장
- 조건식은 True or False로 판단
- 들여쓰기 필수 → python은 들여쓰기로 코드 블록을 구분하기 때문이다.
- elif, else와 함께 사용 가능
- 파이썬 문법 구조에 맞게 조건문 뒤에는 반드시 콜론:이 붙는다.

```python
## if문의 기본 구조 

#- if 조건문:
    #수행할_문장1
    #수행할_문장2
    #...
#- else:
    #수행할_문장A
    #수행할_문장B
    #...
```
```python
x = int(input("숫자를 입력하세요: "))

if x > 0:
    print("양수입니다")       # x가 0보다 크면 실행
elif x == 0:
    print("0입니다")         # x가 0이면 실행
else:
    print("음수입니다")       # x가 0보다 작으면 실행
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">양수입니다</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>들여쓰기</span>

- 들여쓰기는 같은 깊이로 해야한다. (오류발생)
- 공백문자와 탭 문자 2가지를 혼용해서 사용하지 않기.
 → 탭이나 공백은 눈으로 보이지 않아 혼용해서 사용하면 오류의 원인
- 일반적으로 공백 문자 4개 사용

### 비교연산자

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i><비교연산자 정리></span>

- x < y	x가 y보다 작다.
- x > y	x가 y보다 크다.
- x == y	x와 y가 같다.
- x != y	x와 y가 같지 않다.
- x >= y	x가 y보다 크거나 같다.
- x <= y	x가 y보다 작거나 같다.




### in
특정 값이 문자열, 리스트 등에 포함되어 있는지 확인하는 연산자
- 포함되어 있으면 True, 없으면 False을 반환
- 문자열, 리스트, 튜플, 딕셔너리에서 사용 가능
- ※ 딕셔너리는 key 기준으로 검사

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("사과가 있다.")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">사과가 있다.</pre>
</div>


```python
numbers = [1, 3, 5, 7, 9]

for i in range(10):
    if i in numbers:
        print(i, "있음")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1 있음
3 있음
5 있음
7 있음
9 있음</pre>
</div>


### not in
특정 값이 포함되어 있지 않은지 확인하는 연산자
- 포함되어 있지 않으면 True, 있으면 False 반환

```python
fruits = ["apple", "banana", "cherry"]

if "grape" not in fruits:
    print("포도는 없다.")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">포도는 없다.</pre>
</div>


```python
menu = ["커피", "차", "주스"]

choice = input("메뉴 선택: ")

if choice not in menu:
    print("없는 메뉴입니다.")
else:
    print("주문 완료!")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">주문 완료!</pre>
</div>


### elif (else if)
여러 조건을 순차적으로 검사할 때 사용하는 조건문
  (앞의 if 조건이 거짓일 경우에만 다음 조건 검사)
- 조건은 위 → 아래 순으로 실행된다.
- 하나라도 참이라면 그 아래부터는 실행되지 않는다.
- ※ 마지막은 보통 else를 사용한다
   (모든 조건이 거짓일 경우)

```python
score = 95

if score >= 70:
    print("C")
elif score >= 90:
    print("A")
    
    # 결과가 C (잘못됨)
    # → 위 조건이 먼저 참으로 나와서 끝남
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">C</pre>
</div>


<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>2. 중복 조건 주의!</span>


```python
x = 10

if x > 5:
    print("조건1")
elif x > 3:
    print("조건2")
    
    # X > 3은 의미가 없음!! (이미 조건1에서 걸림)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">조건1</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>3. 불필요한 elif 줄이기</span>


```python
# ❌ 비효율적
if x == 1:
    print("1")
elif x == 2:
    print("2")
elif x == 3:
    print("3")

# ✅ 더 좋은 방법
if x in [1, 2, 3]:
    print("1~3 중 하나")
    
    # in을 사용하면 더 깔끔하다.
```
### 조건부 표현식
한 줄로 조건문을 작성할 수 있는 문법
 → if-else를 간단하게 줄인 형태

```python
# 기본구조

결과값1 if 조건 else 결과값2
```
```python
# 예시

x = 10

result = "양수" if x > 0 else "음수 또는 0"
print(result)

```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">양수</pre>
</div>


```python
score = 85
print("시험 결과:", "합격" if score >= 60 else "불합격")  # 60점 이상이면 합격, 아니면 불합격

num = 7
print("숫자 판별:", "짝수" if num % 2 == 0 else "홀수")  # 2로 나눈 나머지로 짝수/홀수 판단

battery = 30
print("배터리:", "충전 필요" if battery < 50 else "충분")  # 50% 미만이면 충전 필요, 아니면 충분

hour = 14
print("시간:", "오전" if hour < 12 else "오후")  # 12시 이전이면 오전, 아니면 오후

password = "1234"
print("로그인:", "접속 성공" if password == "1234" else "접속 실패")  # 비밀번호 일치 여부 확인

speed = 80
print("속도:", "과속" if speed > 60 else "정상")  # 제한속도 60 초과면 과속, 아니면 정상
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">시험 결과: 합격
숫자 판별: 홀수
배터리: 충전 필요
시간: 오후
로그인: 접속 성공
속도: 과속</pre>
</div>


### 

### while문
조건이 참(True)인 동안 반복 실행되는 반복문이다.  (조건이 거짓(False)이 되면 반복은 종료됨.)
1. 조건 기간 반복
- 반복 횟수를 미리 모를 때 사용
2. 무한 루프 가능 (서버, 이벤트 처리, 입력 대기 상황 등)

3. break /  continue 사용 가능
- break → 반복 종료
- continue → 아래 코드를 건너뛰고 다음 반복



<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>기본 구조</span>

- while 조건:
    - 반복 실행 코드
- → 조건이 True동안 반복, 조건이 False가 되면 종료


```python
# 1부터 5까지 출력
i = 1
while i <= 5:
    print(i)  # 현재 값 출력
    i += 1   # i 증가, 조건이 False 되면 반복 종료
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1
2
3
4
5</pre>
</div>


```python
# while -else문 예시

# 1부터 5까지 출력 후 else 실행
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("반복 종료")  # while 조건이 거짓일 때 실행

```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1
2
3
4
5
반복 종료</pre>
</div>


```python
# while_else + break문 예시

i = 1
while i <= 5:
    print(i)
    if i == 3:
        print("반복 강제 종료")
        break  # break로 종료하면 else 실행 안됨
    i += 1
else:
    print("반복 정상 종료")  # break 없이 끝나야 실행
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1
2
3
반복 강제 종료</pre>
</div>


```python
# 중첩 while문 예제
i = 1
while i <= 2:  # i는 1~2 반복
    j = 1
    while j <= 4:  # j는 1~4 반복
        print(f"i={i}, j={j}, 합={i+j}")  # i+j 값도 함께 출력
        j += 1
    i += 1
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">i=1, j=1, 합=2
i=1, j=2, 합=3
i=1, j=3, 합=4
i=1, j=4, 합=5
i=2, j=1, 합=3
i=2, j=2, 합=4
i=2, j=3, 합=5
i=2, j=4, 합=6</pre>
</div>


### for문
시퀀스 자료형의 각 요소를 순회하며 반복할 때 사용
1. 반복 횟수를 미리 알 수 있을 때 효율적 
- ex) 1~100까지 반복, 리스트 요소 순회

2. 시퀀스 순회 반복
- 리스트, 문자열, 튜플, 딕서녀리(key)등 활용 가능

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>기본 구조</span>

- for 변수 in 시퀀스:
    - 반복 실행 코드
- → 시퀀스의 각 요소를 변수에 순차적으로 할당하며 반복
- → 반복이 끝나면 자동 종료


```python
# 간단한 예제
fruits = ["사과", "바나나", "체리"]

for fruit in fruits:
    print(fruit)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">사과
바나나
체리</pre>
</div>


```python
# 리스트 순회

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(f"{num}은 짝수")
    else:
        print(f"{num}은 홀수")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1은 홀수
2은 짝수
3은 홀수
4은 짝수
5은 홀수</pre>
</div>


```python
# for-else문 예제

for i in range(1, 4):
    print(i)
else:
    print("반복 정상 종료")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1
2
3
반복 정상 종료</pre>
</div>


```python
# for문과 continue문 예제

scores = [75, 58, 89, 42, 90]  # 학생 점수 리스트

student_no = 0
for score in scores:
    student_no += 1  # 학생 번호 증가
    if score < 60:
        continue  # 60점 미만은 다음 반복으로 건너뜀
    print(f"{student_no}번 학생 축하합니다! 합격입니다.")  # 합격 메시지 출력
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1번 학생 축하합니다! 합격입니다.
3번 학생 축하합니다! 합격입니다.
5번 학생 축하합니다! 합격입니다.</pre>
</div>


```python
# range 함수 예제

# 1부터 20까지 합 계산
total = 0  # 합계 초기화

for num in range(1, 21):  # 1~20 반복
    total += num  # 현재 수를 합계에 더함

print("1부터 20까지 합:", total)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1부터 20까지 합: 210</pre>
</div>


```python
# enumerate 함수 예제

fruits = ["사과", "바나나", "체리"]

for idx, fruit in enumerate(fruits, start=1):  # start=1: 인덱스 1부터 시작
    print(f"{idx}번째 과일은 {fruit}입니다.")

```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1번째 과일은 사과입니다.
2번째 과일은 바나나입니다.
3번째 과일은 체리입니다.</pre>
</div>


```python
#zip 함수로 여러 리스트 함께 순회하기

products = ["사과", "바나나", "체리"]
prices = [1000, 1500, 2000]

for product, price in zip(products, prices):
    # f-string 대신 format() 사용
    print("{}의 가격은 {}원입니다.".format(product, price))
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">사과의 가격은 1000원입니다.
바나나의 가격은 1500원입니다.
체리의 가격은 2000원입니다.</pre>
</div>


          </div>
        </div>

        <!-- Section: 6. 함수와 매개변수 (Functions) -->
        <div id="section6" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #2dd4bf; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-cube"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">6. 함수와 매개변수 (Functions)</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 함수
입력값(input)을 받아 처리를 수행한 후 출력값(output)을 내보내는 것


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>함수를 사용하는 이유</span>

1. 코드 재사용성
- 반복되는 코드를 하나의 함수로 묶으면 재사용 가능
→ ex) 덧셈, 곱셈, 문자열 처리 등

2. 프로그램 구조화
- 입력값이 여러 함수를 거쳐 결과를 내는 구조로 만들면, 프로그램의 흐름을 명확히 이해 가능 (오류 발생 위치 찾기 용이)
  


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>함수 구조</span>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>입력값이 있는 함수</span>

값을 받아서 처리하는 함수 (입력값에 따라 결과가 달라짐.)

- def 함수_이름(매개변수):
    - 수행할_문장1
    - 수행할_문장2
   - ...
   - return 반환값

```python
def greet(name):
    return f"안녕하세요, {name}님!"

# 함수 호출
result = greet("명은")
print(result)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">안녕하세요, 명은님!</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>반환값이 없는 함수</span>

결과를 돌려주지 않고, 대신 어떤 동작(출력 등)만 수행하는 함수
- 반환값은 return 명령어로만 반환 가능

```python
def add(a, b):
    print(f"{a} + {b} = {a + b}")

# 함수 호출
add(3, 4)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">3 + 4 = 7</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>입력값,반환값 둘 다 없는 함수</span>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>예제를 보면, 입력 인수를 받는 매개변수도 없고 return문도 없어 입력값,반환값 모두 없다.</span>


```python
# 예제
def say_hello():
    print("안녕하세요!")

# 함수 호출
say_hello()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">안녕하세요!</pre>
</div>


### 키워드 매개변수, kwargs
함수 호출 시 키워드=값 형태로 전달된 인수들을 딕셔너리로 받는 매개변수
- 키워드 매개변수를 사용할 때에는 매개변수 앞에 별 2개(**)를 붙인다.

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i><특징></span>

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>1. 입력 개수 제한 없음</span>


```python
def info(**kwargs):
    print(kwargs)

info(a=1)
info(a=1, b=2, c=3)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">{'a': 1}
{'a': 1, 'b': 2, 'c': 3}</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>2. 딕셔너리로 처리됨</span>


```python
def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

info(name="김철수", age=25)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">name 김철수
age 25</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>3. 가독성이 좋음</span>


```python
def create_user(name, age, city):
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"도시: {city}")

# 함수 호출 (가독성 좋게)
create_user(name="김철수", age=20, city="서울")
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">이름: 김철수
나이: 20
도시: 서울</pre>
</div>


<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

1. 반드시 key=값 형태로 전달

2. 매개변수 순서가 중요 ( 일반 -> args -> kwargs )

3. 키 이름 중복 주의

```python
# kwargs 예제

def create_profile(**kwargs):  # 키워드 인수들을 딕셔너리 형태로 받는 함수 정의
    print("=== 프로필 ===")  # 제목 출력
    for key, value in kwargs.items():  # 딕셔너리의 키와 값을 하나씩 꺼내 반복
        print(f"{key}: {value}")  # 키와 값을 "key: value" 형태로 출력

create_profile(  # 함수 호출 시작
    name="김영희",   # name이라는 키에 "홍길동" 값 전달
    age=30,         # age라는 키에 30 값 전달
    job="개발자",   # job이라는 키에 "개발자" 값 전달
    hobby="독서"    # hobby라는 키에 "독서" 값 전달
)  # 함수 호출 끝
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">=== 프로필 ===
name: 김영희
age: 30
job: 개발자
hobby: 독서</pre>
</div>


### 함수의 반환값과 return

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>1.  파이썬 함수의 반환값은 항상 하나이다.</span>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>2. 여러 값을 반환하는 것처럼 보일 경우, 실제로는 튜플 형태로 묶여 하나의 값으로 반환된다.</span>



```python
def add_and_mul(a, b):
    return a + b, a * b

result = add_and_mul(3, 4)  # (7, 12)
```
<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>3. 튜플 반환값은 언패킹을 통해 각각의 변수로 나눠 받을 수 있다.</span>


```python
x, y = add_and_mul(3, 4)  # x=7, y=12
```
<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>4. return문은 실행되는 즉시 함수가 종료되며, 이후 코드는 실행되지 X</span>


```python
def add_and_mul(a, b):
    return a + b
    return a * b  # 실행되지 않음
```
<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>5. return은 값을 반환하지 않고 함수를 종료하는 용도로도 사용된다.</span>


```python
def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick}입니다.")
```
<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>매개변수 초깃값 미리 설정하기 (Default Parameter)</span>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>1. 함수 정의 시 매개변수에 기본값을 설정할 수 있다.</span>


```python
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
```
```python
say_myself("김철수", 27)       # man은 기본값 True 사용
say_myself("김철수", 27, True) # man에 True 명시
say_myself("김철용", 27, False)# man에 False 명시
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">나의 이름은 김철수 입니다.
나이는 27살입니다.
남자입니다.
나의 이름은 김철수 입니다.
나이는 27살입니다.
남자입니다.
나의 이름은 김철용 입니다.
나이는 27살입니다.
여자입니다.</pre>
</div>


<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>※ 주의할 점</span>

기본값이 있는 매개변수는 항상 뒤쪽에 배치한다

### 함수 안에서 선언한 변수의 효력 범위 ( 지역 변수 vs 전역 변수 )
- 함수 안에서 선언된 변수는 함수 안에서만 유효하다.
- 함수 밖의 동일한 이름의 변수와는 완전히 별개의 변수이다.
- 함수 안에서 선언된 변수 = 지역 변수
- 함수 밖에서 선언된 변수 = 전역 변수

```python
# 전역 변수
x = 10

def my_function():
    # 지역 변수
    y = 5
    print("함수 안에서 x (전역 변수):", x)  # 전역 변수 접근 가능
    print("함수 안에서 y (지역 변수):", y)

my_function()

print("함수 밖에서 x (전역 변수):", x)  # 10
# print("함수 밖에서 y (지역 변수):", y)  # ❌ 오류 발생, y는 지역 변수
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">함수 안에서 x (전역 변수): 10
함수 안에서 y (지역 변수): 5
함수 밖에서 x (전역 변수): 10</pre>
</div>


### 함수 안에서 함수 밖의 변수 변경하는 방법

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>return</span>

- retirn문을 사용하면 함수 안 계산 결과를 밖으로 전달할 수 있다.
- 함수 안의 매개변수는 여전히 지역 변수이며, 함수 밖의 변수와 이름이 같아도 독립적이다.

```python
# 예시
a = 1  # 전역 변수

def vartest(a):  # 매개변수 a는 지역 변수
    a = a + 1
    return a     # 계산 결과를 반환

a = vartest(a)   # 반환값으로 전역 변수 a 갱신
print(a)         # 출력: 2
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">2</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>global</span>

- global 키워드 사용하면 함수 안에서 전역 변수에 직접 접근하여 값을 변경하 수 있다.

```python
# 예제
a = 1  # 전역 변수

def vartest():
    global a       # 함수 안에서 전역 변수 a 사용
    a = a + 1

vartest()
print(a)           # 출력: 2
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">2</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>변경 가능한 자료형</span>

- 리스트, 딕셔너리 등 mutable 자료형은 함수 안에서 변경하면 원본에도 영향을 줌.


```python
# 예제
def change_list(my_list):
    my_list.append(4)  # 리스트에 값 추가

a = [1, 2, 3]
change_list(a)
print(a)  # 출력: [1, 2, 3, 4]
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">[1, 2, 3, 4]</pre>
</div>


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>iambda 예약어</span>

- 간단한 함수를 한 줄로 정의할 때 사용하는 예약어
- def와 동일한 역햘을 하지만, 표현식 한 줄만 사용 가능
- return 명령어 없이도 표현식의 결과를 자동으로 반환



```python
# 예제
# lambda 함수
add = lambda a, b: a + b
result = add(3, 4)
print(result)  # 출력: 7

# 일반 def 함수와 동일한 기능
def add_def(a, b):
    return a + b

result2 = add_def(3, 4)
print(result2)  # 출력: 7
```
<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>독스트링(Docstring)</span>

- 함수에 대한 설명을 문서화하는 방법
- 함수 정의 첫 줄에 삼중 따옴표(""" """)로 문자열 작성
- 함수 사용법, 매개변수, 반환값 등을 명확히 기록 가능



<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>특징</span>

- add._doc_를 통해 문서 문자열 확인 가능
- 코드 유지보수,협업,자동 문서화에 유용

```python
# 예제
def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """
    return a + b

# 독스트링 확인
print(add.__doc__)
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">두 숫자를 더하는 함수

Parameters:
a (int, float): 첫 번째 숫자
b (int, float): 두 번째 숫자

Returns:
int, float: 두 숫자의 합</pre>
</div>


          </div>
        </div>

        <!-- Section: 7. 파일 입출력 & 클래스 실습 -->
        <div id="section7" class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #f472b6; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-file-text-o"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">7. 파일 입출력 & 클래스 실습</h3>
              <span class="small text-muted">Python Core Grammar Study Record</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 파일 입출력
프로그램이 파일에 데이터를 저장(출력)하거나 파일에서 데이터를 읽어오는(입력)작업

### 파일 생성하기
- open( 파일_이름, 파일_열기_모드)을 사용
- 쓰기 모드(w)로 열었을 때 파일이 없으면 새로 만들고 있으면 내용이 지워짐.
- f.open과 f.close는 무조건 같이 사용!!
- 경로 작성 시 / or \ or r""을 사용

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>파일 열기 모드</span>

- r → 읽기 모드 : 파일을 읽기만 할 때 사용
- w → 쓰기 모드 : 파일에 내용을 쓸 때 사용
- a → 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>특징</span>

- 파일을 열면 파일 객체가 생성
- close()로 닫지 않으면, 데이터 손실 또는 오류 발생


```python
#f.open(파일이름,파일 열기 모드(w:write),쓰기 모드로 열기)
f = open("새로운 파일.txt", 'w')
f.close()
```
```python
# 다른 디렉토리에 있는 파일을 열 때에는 경로를 직접 지정
f = open("새로운 폴더 / 새로운 파일.txt",'w')
f.close()
```
### 파일을 쓰기 모드로 열어 내용 쓰기
- 파일에 데이터 작성 가능
 ( wirte()함수 사용해 내용 입력 )
 - 문자열만 저장 가능 
  ( 숫자는 문자열로 변환 필요 )
- 인코딩 설정 가능
 ( 한글 처리 )

 


```python
# 1. 동일 디렉토리에 있는 새파일.txt 모드로 열기
f = open('새로운 파일.txt','w')

#반복문 실행
for i in range(1,11):
    #date에 값 넣기
    #data = f"(i)번째 줄입니다.\n"
    data = str (i) +'번째 줄입니다.\n'
    print(data)
    f.write(data)
    
    print("문자열 파일에 쓰기")
    f.write("문자열 파일에 쓰기")
    f.close
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">1번째 줄입니다.

문자열 파일에 쓰기
2번째 줄입니다.

문자열 파일에 쓰기
3번째 줄입니다.

문자열 파일에 쓰기
4번째 줄입니다.

문자열 파일에 쓰기
5번째 줄입니다.

문자열 파일에 쓰기
6번째 줄입니다.

문자열 파일에 쓰기
7번째 줄입니다.

문자열 파일에 쓰기
8번째 줄입니다.

문자열 파일에 쓰기
9번째 줄입니다.

문자열 파일에 쓰기
10번째 줄입니다.

문자열 파일에 쓰기</pre>
</div>


### 파일을 읽는 여러 가지 방법

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>readline 함수</span>

- readline()은 한 줄씩 읽는다.
- 반복문과 함께 사용 가능
- readline()은 파일의 모든 줄을 리스트로 반환
- 파일을 읽을 때에는 for문을 사용해야 한다.
- 반복 호출 시 다음 줄 읽음

```python
# 파일 생성
f = open("test.txt", "w")  # 쓰기 모드로 열면 새 파일 생성
f.write("첫 번째 줄\n두 번째 줄\n세 번째 줄\n")
f.close()
```
```python
# readline 기본 구조 코드

f = open("test.txt", "r")

while True:
    line = f.readline()
    
    if not line:
        break
    
    print(line.strip())  # 줄 끝 \n 제거

f.close()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">첫 번째 줄
두 번째 줄
세 번째 줄</pre>
</div>


### read
- read()는 파일 전체 내용을 한 번에 읽어 문자열로 

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>특징</span>

- 전체 내용을 한 번에 읽음 → 메모리 사용량 증가 가능
- 줄바꿈(\n)포함
- 문자열 형태 변환

```python
# read 기본 구조 예제

# 파일 열기
f = open("test.txt", "r")  # 읽기 모드

# 파일 전체 내용 읽기
data = f.read()

# 읽은 내용 출력
print(data)

# 파일 닫기
f.close()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">첫 번째 줄
두 번째 줄
세 번째 줄</pre>
</div>


### for문과 함께 사용하기
- 파일 객체는 반복 가능한 객체
- for line in f : 구조 사용하면 파일을 한 줄씩 순차적으로 읽음.
- readline과 비슷하지만 코드가 더 간결하고, 메모리가 효율적이다.

```python
# test.txt' 파일을 읽기 모드로 열기
f = open("test.txt", 'r')  

# 파일 객체 f를 반복(iterable)로 사용하여 한 줄씩 읽기
for line in f:  
    # 읽은 한 줄을 출력, strip()으로 줄 끝의 \n 제거
    print(line.strip())  

# 파일 닫기
f.close()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">첫 번째 줄
두 번째 줄
세 번째 줄</pre>
</div>


```python
# 파일을 읽기 모드로 열고 with 문 사용
with open("test.txt", 'r') as f:
    for line in f:
        print(line.strip())  # 줄 끝의 \n 제거 후 출력
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">첫 번째 줄
두 번째 줄
세 번째 줄</pre>
</div>


### 파일에 새로운 내용 추가하기
- 'a'모드로 열면 기존 내용 뒤에 추가된다.

```python
f =open('my_log.txt','a')
f.write()
for i in range(11,20):
    data = f"번째 줄입니다.\n"
    f.write(data)
    
    f.close()
```
### with문과 함께 사용하기
- with open()을 사용하면 close()를 따로 호출하지 않아도 된다.

```python
# with문 사용 예제

with open("test.txt", "r") as f:
    while True:
        line = f.readline()
        
        if not line:
            break
        
        print(line.strip())
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">첫 번째 줄
두 번째 줄
세 번째 줄</pre>
</div>


```python
# with문 사용 예제

# 'test.txt' 파일을 읽기 모드('r')로 열고, 파일 객체를 f에 할당
with open("test.txt", "r") as f:  
    # 파일 전체 내용을 읽어 문자열로 변수 data에 저장
    data = f.read()  
    
    # 읽어온 파일 내용을 화면에 출력
    print(data)
    
# with 문을 벗어나면 파일이 자동으로 닫힘
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">첫 번째 줄
두 번째 줄
세 번째 줄</pre>
</div>


### API
서로 다른 소프트웨어 시스템 간에 정보를 주고받거나 기능을 사용할 수 있도록 도와주는 서비스
- 요청하면 필요한 데어티를 보내주는 자동화 시스템 
- 딕셔너리와 같은 구조
- 딕셔너리에 vaule와 같은 구조로 접근
- dupms 사용하면 가독성있게 표현 가능


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>아침 루틴 만들기(Routine 클래스의 routine 메소드)</span>

1. 랜덤 고양이 사진 보여주기(메소드)
2. 오늘 서울 날씨 알려주기(메소드)
3. 오늘의 명언 출력하기(메소드)
4. 추가 기능 제공(자율)

```python
# 1
import requests
from IPython.display import Image, display

def routine():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    cat_url = data[0]['url']
    print("오늘의 고양이 사진:")
    display(Image(url=cat_url, width=500))  # 너비 500px로 지정

routine()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">오늘의 고양이 사진:</pre>
</div>


```python
# 2
import requests
from datetime import datetime

def today_seoul_weather():
    latitude = 37.5665
    longitude = 126.9780
    today = datetime.utcnow().date()
    
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FSeoul"
    )
    
    response = requests.get(url)
    data = response.json()
    
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']
    
    for date in dates:
        if date == str(today):
            i = dates.index(date)
            print(f"오늘({today}) 서울 날씨")
            print(f"- 최고 기온: {max_temps[i]}°C")
            print(f"- 최저 기온: {min_temps[i]}°C")
            break

# 함수 호출
today_seoul_weather()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">오늘(2026-03-26) 서울 날씨
- 최고 기온: 14.6°C
- 최저 기온: 2.3°C</pre>
</div>


```python
# 3
import requests
import json

url = "https://zenquotes.io/api/random"
response = requests.get(url)

data = response.json()

print("=== JSON 데이터 ===")
print(json.dumps(data, indent=3))

quote = data[0]['q']
author = data[0]['a']

print("\n오늘의 명언:",f'"{quote}" — {author}')
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">=== JSON 데이터 ===
[
   {
      "q": "Everybody has talent, but ability takes hard work.",
      "a": "Michael Jordan",
      "h": "<blockquote>&ldquo;Everybody has talent, but ability takes hard work.&rdquo; &mdash; <footer>Michael Jordan</footer></blockquote>"
   }
]

오늘의 명언: "Everybody has talent, but ability takes hard work." — Michael Jordan</pre>
</div>


```python
import requests
from datetime import datetime

def morning_routine_time():
    try:
        url = "http://worldtimeapi.org/api/timezone/Asia/Seoul"
        response = requests.get(url, timeout=5)
        data = response.json()
        current_time = data['datetime']
    except:
        current_time = datetime.now()
    
    print("현재 시각:", current_time)

# 실행
morning_routine_time()
```

<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
    <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
  </div>
  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">현재 시각: 2026-03-26 15:41:43.237803</pre>
</div>


          </div>
        </div>

      </div>
    </div>
  </div>
</div>