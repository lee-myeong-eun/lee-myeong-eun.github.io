---
layout: default
title: C언어 기초문법 정리
permalink: /assignments/c-programming-basics/
---

<style>
  /* Ensure code blocks have a light, readable color on dark backgrounds */
  pre, code, .highlight pre, .highlight code, pre code {
    color: #bae6fd !important;
    background-color: #161b22 !important;
    border-radius: 8px;
  }
  .highlight {
    background-color: #161b22 !important;
    border-radius: 8px;
    padding: 15px;
  }
</style>

## C언어 기초문법 정리

# 1. C언어 개요

C언어는 절차지향 프로그래밍 언어로 시스템, 임베디드, 반도체 장비 제어 등에 사용된다.

## 특징
- 컴파일 언어 (빠른 실행 속도)
- 절차지향 구조
- 하드웨어 제어 가능
- 운영체제 및 장비 소프트웨어 개발에 활용

# 1-2. 프로그램 기본 구조

C 프로그램은 main() 함수에서 시작된다.

구성 요소:
- #include : 헤더 파일
- main() : 실행 시작점
- printf() : 출력
- scanf() : 입력

```c
#include <stdio.h>

int main()
{
    printf("Hello World\n");
    return 0;
}
```

# 2. 변수와 자료형

## 변수
데이터를 저장하는 메모리 공간

## 자료형
데이터 종류를 정의하는 타입

### 기본 자료형
- int : 정수
- float : 실수
- char : 문자

```c
int a = 10;
float b = 3.14;
char c = 'A';
```

# 3. 입출력 (printf / scanf)

- printf : 화면 출력
- scanf : 키보드 입력 (주소 필요)

```c
int a, b;
scanf("%d %d", &a, &b);
printf("%d %d", a, b);
```

# 4. 연산자

## 종류
- 산술: + - * / %
- 증감: ++ --
- 비교: > < == !=
- 삼항 연산자: 조건 ? 참 : 거짓

```c
int a = 5, b = 3;

a++;
printf("%d\n", --a);

int diff = (a > b) ? a - b : b - a;
```

### 📌 핵심 개념

- a++ : 사용 후 증가
- ++a : 증가 후 사용
- --a : 감소 후 사용

# 5. 조건문 (if / switch)

조건에 따라 실행 흐름을 변경하는 구조

```c
if (a > b)
    printf("A가 큼");
else
    printf("B가 큼");
```

```c
switch(num)
{
    case 1:
        printf("One");
        break;
    case 2:
        printf("Two");
        break;
    default:
        printf("Other");
}
```

# 6. 반복문 (for / while)

코드를 반복 실행하는 구조

- for : 횟수 기반
- while : 조건 기반

```c
for(int i=0; i<5; i++)
{
    printf("%d\n", i);
}
```

```c
int i = 0;

while(i < 5)
{
    printf("%d\n", i);
    i++;
}
```

# 7. 배열 (Array)

같은 자료형 데이터를 여러 개 저장하는 구조

## 특징
- 인덱스는 0부터 시작
- 연속된 메모리 구조

```c
int arr[5] = {10,20,30,40,50};
```

📌 활용 (장비제어)
→ 센서 데이터, 공정 값 저장

# 8. 문자열 (String)

문자 배열이며 마지막에 NULL('\0') 포함

```c
char name[10] = "korea";
printf("%s", name);
```

# 9. 함수 (Function)

특정 기능을 수행하는 코드 블록

## 장점
- 재사용
- 구조화
- 유지보수 용이

```c
int add(int a, int b)
{
    return a + b;
}
```

# 10. 포인터 (Pointer)

변수의 메모리 주소를 저장하는 변수

## 핵심
- & : 주소
- * : 값 접근

```c
int a = 10;
int *p = &a;

printf("%d", *p);
```

📌 장비제어 핵심
→ 메모리 직접 접근 / 하드웨어 제어

# 11. 구조체 (struct)

서로 다른 데이터를 하나로 묶는 자료형

```c
struct student {
    char name[20];
    int score;
};
```

# 12. 배열 응용 (최대값 / 탐색)

배열에서 특정 값 탐색 또는 최대값 계산

```c
int num[9] = {3,6,4,2,8,4,9,1,7};

int max = num[0];

for(int i=1; i<9; i++)
{
    if(max < num[i])
        max = num[i];
}
```

# 13. 선택 정렬 (Selection Sort)

가장 작은 값을 찾아 앞으로 이동시키는 정렬 알고리즘

## 특징
- O(n²)
- 구현 단순

```c
for(int i=0; i<n-1; i++)
{
    int min = i;

    for(int j=i+1; j<n; j++)
    {
        if(arr[min] > arr[j])
            min = j;
    }
}
```

# 14. 장비 프로그래밍 응용

C언어는 실제 생산 장비 제어 및 공정 데이터 처리에 사용된다.

## 대표 문제 유형
- 시간 변환 (초 → 시간/분)
- 무게 판별 시스템
- 공정 데이터 필터링
- 조건 기반 선별 시스템

```c
int sec = 3700;

int hour = sec / 3600;
int min = (sec % 3600) / 60;
```

# 15. 전체 정리

C언어 프로그램 구조:

입력 → 처리 → 출력

핵심 요소:
- 변수
- 조건문
- 반복문
- 배열
- 함수
- 포인터
- 구조체
- 알고리즘

