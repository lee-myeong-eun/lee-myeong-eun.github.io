---
layout: default
title: C# 기초 문법 실습
permalink: /assignments/c-sharp-basics/
---

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Header -->
    <div class="animate-fade-in-up delay-100">
      <span class="tech-badge">💻 C# Study Record</span>
      <h2 class="text-gradient">C# 기초 문법 및 객체지향 프로그래밍 실습</h2>
      <hr />
      <p class="lead text-light font-weight-normal">
        반도체 장비 GUI 및 제어 개발을 위해 학습하고 정리한 **C# 기초 및 메모리/객체지향 구조** 기록입니다.
      </p>
    </div>

    <!-- Contents Grid -->
    <div class="row mt-5 animate-fade-in-up delay-200">
      
      <!-- Left Sidebar Index -->
      <div class="col-lg-4 mb-4">
        <div class="border-0 shadow welcome-box p-3 sticky-top" style="top: 100px; z-index: 10; background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) ;">
          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-list-ul mr-2"></i>학습 목차</h4>
          <ul class="list-unstyled small mb-0 pl-1" style="line-height: 2.2;">
            <li><a href="#section1" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-terminal mr-2" style="color: #38bdf8; width: 16px; text-align: center;"></i>1. C# 프로그램의 기본 규칙 및 표준 출력</a></li>
            <li><a href="#section2" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-cube mr-2" style="color: #fb7185; width: 16px; text-align: center;"></i>2. 변수와 C# 데이터형 체계</a></li>
            <li><a href="#section3" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-microchip mr-2" style="color: #34d399; width: 16px; text-align: center;"></i>3. 메모리 아키텍처: 값 타입(Value) vs 참조 타입(Reference)</a></li>
            <li><a href="#section4" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-code-fork mr-2" style="color: #a78bfa; width: 16px; text-align: center;"></i>4. 제어문과 다중 배열 구조</a></li>
            <li><a href="#section5" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-cubes mr-2" style="color: #fb923c; width: 16px; text-align: center;"></i>5. 구조체(Struct)와 클래스(Class) 차이</a></li>
            <li><a href="#section6" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-warning mr-2" style="color: #2dd4bf; width: 16px; text-align: center;"></i>6. 런타임 예외 처리 아키텍처</a></li>
            <li><a href="#section7" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-object-group mr-2" style="color: #f472b6; width: 16px; text-align: center;"></i>7. 객체지향 프로그래밍</a></li>
            <li><a href="#section8" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa fa-sitemap mr-2" style="color: #818cf8; width: 16px; text-align: center;"></i>8. 클래스의 확장: 상속과 다형성 입문</a></li>
          </ul>
          <hr class="my-3" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <a href="{{ site.baseurl }}/assignments/" class="btn btn-outline-light btn-sm btn-block text-hover-glow">
            <i class="fa fa-arrow-left mr-1"></i>아카이브로 돌아가기
          </a>
        </div>
      </div>

      <!-- Right Detailed Content -->
      <div class="col-lg-8 mb-4">
        <!-- Section: 1. C# 프로그램의 기본 규칙 및 표준 출력 -->
        <div id="section1" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #38bdf8; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-terminal"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">1. C# 프로그램의 기본 규칙 및 표준 출력</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

C# 프로그래밍을 시작할 때 반드시 준수해야 하는 가장 기초적인 구문 규칙과 표준 출력의 제어 방식

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">문장과 세미콜론:</span> C#의 모든 실행 코드는 문장의 끝에 반드시 세미콜론(;)을 붙여 컴파일러에게 문장의 종료를 알려야 함.

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">대소문자 구분:</span> 동일한 알파벳이라도 대소문자를 다르게 작성하면 컴파일러는 이를 완전히 다른 식별자(Identifier)로 인식

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">표준 콘솔 출력 메서드:</span> 

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">Console.Write():</span> 지정한 데이터를 출력한 후 줄바꿈(개행)을 수행하지 않고 다음 출력과 연결

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">Console.WriteLine():</span> 데이터를 출력한 후 자동으로 줄바꿈을 수행하여 다음 행으로 커서를 이동

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">이스케이프 시퀀스(Escape Sequence):</span> 문자열 내부에서 특수한 제어를 하기 위해 역슬래시(\)와 결합하는 문자입니다. 대표적으로 \n(줄바꿈)과 \t(일정 간격 띄우기)가 있다.
          </div>
        </div>

        <!-- Section: 2. 변수와 C# 데이터형 체계 -->
        <div id="section2" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #fb7185; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-cube"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">2. 변수와 C# 데이터형 체계</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

변수는 데이터를 저장하는 메모리 공간의 이름입니다. C#은 강력한 형식 안정성(Type Safety)을 지닌 언어로, 변수 선언 시 데이터의 종류와 크기를 명확히 규정해야 함.


<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>기본 자료형(Primitive Types) 분류</span>

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">정수형:</span> int (4바이트 정수형, 가장 보편적), long (8바이트 큰 정수 표현)

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">실수형:</span> double (8바이트 부동소수점 실수, 기본값), float (4바이트 실수, 값 뒤에 접미사 f 또는 F 명시 필요)

문자형/문자열: char (2바이트 단일 문자, 작은따옴표 ' ' 사용), string (참조 타입 문자열, 큰따옴표 " " 사용)

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">논리형:</span> bool (true와 false 두 가지 상태값만 가짐)

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>암시적 타입 지정 (var)</span>

메서드 내부에서 선언하는 지역 변수에 한해 사용할 수 있으며, 컴파일러가 대입 연산자 우항의 리터럴 자료형을 분석하여 컴파일 타임에 타입을 자동으로 확정해 주는 편리한 문법이다.

          </div>
        </div>

        <!-- Section: 3. 메모리 아키텍처: 값 타입(Value) vs 참조 타입(Reference) -->
        <div id="section3" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #34d399; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-microchip"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">3. 메모리 아키텍처: 값 타입(Value) vs 참조 타입(Reference)</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

프로그램의 성능과 최적화를 이해하는 데 가장 중요한 스택(Stack)과 힙(Heap) 메모리 관리 구조의 차이점

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>값 타입 (Value Type)</span>

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">할당 공간:</span> 시스템의 스택(Stack) 메모리 영역에 실제 데이터가 직접 저장

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">특징:</span> 변수 선언 시 메모리 크기가 정적으로 결정되며, 선언된 코드 블록(Scope)을 벗어나면 메모리에서 즉시 자동 소멸합니다. 다른 변수에 대입할 때 '실제 값의 복사(Copy by Value)'가 일어난다.

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">해당 타입:</span> 기본 숫자 자료형, bool, char, 그리고 구조체(struct)

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>참조 타입 (Reference Type)</span>

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">할당 공간:</span> 실제 데이터 객체는 동적 공간인 힙(Heap) 메모리 영역에 생성되고, 스택 변수에는 해당 힙 객체의 메모리 주소(참조값)만 저장

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">특징:</span> 대입 연산 시 주소가 복사되므로, 여러 변수가 동일한 힙 객체를 가리키는 현상(Copy by Reference)이 발생합니다. 더 이상 참조하는 변수가 없는 힙 데이터는 .NET의 가비지 컬렉터(Garbage Collector, GC)가 백그라운드에서 추적하여 주기적으로 자동 수거

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">해당 타입:</span> 클래스(class), 배열(array), 문자열(string)
          </div>
        </div>

        <!-- Section: 4. 제어문과 다중 배열 구조 -->
        <div id="section4" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #a78bfa; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-code-fork"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">4. 제어문과 다중 배열 구조</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>조건문과 반복문</span>

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">조건 분기:</span> 관계/논리 연산자의 결합을 통해 다중 조건을 비교하는 if-else 구조와, 특정 변수의 정적 값에 매핑하여 분기하는 switch 구조가 있음.

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">반복 제어:</span> 횟수 제어에 유리한 for, 조건 만족 시 지속하는 while, 그리고 인덱스 초과 에러(IndexOutOfRangeException)를 구조적으로 예방하며 컬렉션을 순회하는 C# 특유의 foreach문이 있음.

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>다차원 배열과 가변 배열</span>

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">2차원 배열 (정방형):</span> 대괄호 내에 콤마를 사용하는 [,] 형태로 선언되며, 모든 행의 열 크기가 격자 형태로 고정된 구조입니다. 연속된 메모리 블록을 사용한다.

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">가변 배열 (Jagged Array):</span> 대괄호를 연속으로 사용하는 [][] 형태로 선언되며, '배열을 요소로 갖는 배열'입니다. 행마다 가리키는 열 배열의 크기를 완전히 다르게 구성할 수 있어 메모리 낭비를 방지한다.
          </div>
        </div>

        <!-- Section: 5. 구조체(Struct)와 클래스(Class) 차이 -->
        <div id="section5" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #fb923c; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-cubes"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">5. 구조체(Struct)와 클래스(Class) 차이</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">구조체 (struct):</span> 값 타입(Value Type)으로 스택에 할당됩니다. 크기가 작고 수명이 짧은 경량 데이터를 제어할 때 오버헤드가 적어 성능상 유리하며, 상속을 지원하지 않는다.

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">클래스 (class):</span> 참조 타입(Reference Type)으로 힙에 할당됩니다. 객체지향 프로그래밍의 핵심 도구로서 복잡한 논리 구조를 설계할 때 쓰이며, 상속과 다형성을 완벽히 지원
          </div>
        </div>

        <!-- Section: 6. 런타임 예외 처리 아키텍처 -->
        <div id="section6" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #2dd4bf; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-warning"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">6. 런타임 예외 처리 아키텍처</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

프로그램 실행 중에 발생할 수 있는 데이터 오류, 인덱스 초과, 무선 통신 단절 등의 시스템 크래시(다운 현상)를 방지하는 고신뢰성 제어 문법

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">try 블록:</span> 예외(Exception)가 발생할 가능성이 있는 불안정한 논리 코드를 격리하는 영역

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">catch 블록:</span> try 내부에서 에러가 던져졌을 때(Throw), 해당 에러 객체를 인터셉트하여 로그를 남기거나 프로그램을 안전하게 우회 제어하는 예외 핸들러 영역

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">finally 블록:</span> 예외 발생 여부와 전혀 상관없이, 프로그램이 최종적으로 무조건 실행하도록 보장하는 영역입니다. 통신 포트나 메모리 자원을 안전하게 해제(Dispose)하는 셧다운 코드가 위치한다.
          </div>
        </div>

        <!-- Section: 7. 객체지향 프로그래밍 -->
        <div id="section7" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #f472b6; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-object-group"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">7. 객체지향 프로그래밍</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>프로퍼티 (Property)</span>

멤버 필드를 외부에 노출하는 public 선언을 지양하고, private으로 숨겨진 필드에 안전하게 접근하기 위해 사용하는 C# 고유의 제어 프레임워크

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">get 접근자:</span> 필드의 데이터를 외부로 읽어갈 때 트리거되는 영역

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">set 접근자:</span> 외부에서 데이터를 필드에 대입할 때 트리거되는 영역으로, 내부에 조건문(유효성 검증 필터링)을 삽입하여 잘못된 범위의 데이터가 내부로 진입하는 것을 원천 차단한다.

<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>생성자 오버로딩 (Constructor Overloading)</span>

new 키워드를 통해 객체가 인스턴스화될 때 내부 멤버를 초기화하는 생성자 메서드를, 매개변수의 개수, 타입, 순서를 다르게 하여 여러 개 정의하는 문법입니다. 이를 통해 개발자는 객체의 초기 진입 상태를 다양하게 동적 설계할 수 있다.
          </div>
        </div>

        <!-- Section: 8. 클래스의 확장: 상속과 다형성 입문 -->
        <div id="section8" class="mb-5" style="padding: 1rem 0;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #818cf8; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-sitemap"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">8. 클래스의 확장: 상속과 다형성 입문</h3>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: var(--text-body);">

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">상속성 (Inheritance):</span> 공통된 성격을 가진 기본 클래스(Base Class)의 필드와 메서드를 파생 클래스(Derived Class)가 그대로 물려받아 코드를 재사용하고 생산성을 높이는 기술

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">base 키워드:</span> 자식 클래스 내부에서 부모 클래스의 생성자나 멤버 변수를 명시적으로 가리키고 인자를 전달할 때 사용하는 지시어

<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">메서드 오버라이딩 (Method Overriding):</span> 부모 클래스에 선언된 메서드를 자식 클래스의 특성에 맞게 새로 재정의하는 기술입니다. 부모 클래스에는 virtual 키워드를, 자식 클래스에는 override 키워드를 매핑하여 다형성(Polymorphic) 아키텍처의 기틀을 완성한다.
          </div>
        </div>

      </div>
    </div>
  </div>
</div>
