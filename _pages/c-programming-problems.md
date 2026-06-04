---
layout: default
title: C언어 문제정리
permalink: /assignments/c-programming/
---

<style>
  /* Ensure code blocks have a light, readable color on dark backgrounds */
  pre, code, .highlight pre, .highlight code, pre code {
    color: #a3e635 !important;
    background-color: #161b22 !important;
    border-radius: 8px;
  }
  .highlight {
    background-color: #161b22 !important;
    border-radius: 8px;
    padding: 15px;
  }
</style>

## C언어 문제정리

### 증감 연산자 사용에 따른 변수 값 변화 확인

```c
#include <stdio.h>

int main()
{
	int a = 5, b = 3;
	a++;
	printf("a = %d b = %d\n", --a, b++);
	printf("a = %d b = %d", a, b);
}


printf("a = % d원 b = % d원 c = % d원 d = % d원 e = % d원 f = % d원 g = % d원 h = % d원\n", --a, b++, c++, d++, e++, f++, g++, h++);
printf("a = % d원 b = % d원 c = % d원 d = % d원 e = % d원 f = % d원 g = % d원 h = % d원", a, b, c, d, e, f, g, h);

```

### 화폐 단위별 개수 계산

```c
#include <stdio.h>

int main()
{
	int money = 127670  , m50000=0, m10000=0, m5000=0, m1000 =0,  m500=0, m100=0  ,m50=0 ,m10=0;
	m50000 = money / 50000;
	m10000 = (money % 50000) / 10000;
	m5000 = (money % 10000) / 5000;
	m1000 = (money % 5000) / 1000; 
	m500 = (money % 1000) / 500;
	m100 = (money % 500) / 100;	
	m50 = (money % 100) / 50;	
	m10 = (money % 50) / 10;
	printf("%d,%d,%d,%d,%d,%d,%d\n", m50000, m10000, m5000, m1000, m500, m100, m50, m10);
	
	
}
```

### 두 정수의 곱, 합, 차 계산

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a;
	int b;
	printf("두 정수를 공백으로 구분하여 입력하세요.\n");
	scanf("%d %d", &a, &b);

	int c1 = a * b;
	int c2 = a + b;
	int c3 = a - b;
	printf("곱: %d\n합: %d\n차: %d", c1, c2, c3);
}

```

### 생산장비 사용 시간 계산 (1분 미만 절삭)
①입력
②계산
③출력

1시간 = 60분 = 3600초
1분 = 60초 = 60분 = 3600초

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int second;


	printf("생산장비의 사용 시간: \n");
	scanf("%d", &second);

	int hour = second / 3600;
	int minutes = (second % 3600) / 60;
	
	printf("시간:%d\n분:%d\n", hour, minutes);
}

```

### 두 수의 차이 계산

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int a = 10, b = 5, diff;
	diff = a < b ? b - a : a - b;
	printf("두 수의 차는: %d\n", diff);
	printf("두 수의 차는: %d\n", a < b ? b - a : a - b);

}
```

### 미성년자 판별

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int age;
	printf("나이를 입력하세요: \n");
	scanf("%d", &age);
	printf("미성년자이면 0, 성인이면 1을 출력하세요.\n");
	printf("결과:%d\n", age >= 18 ? 0 : 1);
}
```

### 두 정수 중 큰 수 찾기

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num1;
	int num2;
	scanf("%d", &num1);
	scanf("%d", &num2);
	if (num1 > num2) printf("%d", num1);
	else printf("%d", num2);
}
```

### 정수를 입력 받아 "양수","음수","0"을 출력

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num;
	scanf("%d", &num);
	if (num > 0) printf("양수");
	else if (num < 0) printf("음수");
	else printf("0");
}
```

### 세 정수를 입력받아서 가장 큰수 출력

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num1;
	int num2;
	int num3;
	scanf("%d", &num1);
	scanf("%d", &num2);
	scanf("%d", &num3);

	if (num1 > num2 && num1 > num3)
	printf("%d", num1);
	else if (num2 > num1 && num2 > num3)
	printf("%d", num2);
	else if (num3 > num1 && num3 > num2)
		printf("%d", num3);
}
```

### 정량이 아닌 음료 찾기

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int a;
	int b;
	int c;
	
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	if (a == b)
		printf("%d", c);
	else if (b == c)printf("%d", a);
	else printf("%d", b);
}
```

### 4개 중 무게가 다른 탁구공 찾기

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int a;
	int b;
	int c;
	int d;

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	scanf("%d", &d);

	if (a == b && a == c)
	printf("%d", d);
	else if (a == b && a == d)
	printf("%d", c);
	else if (a == c && a == d)
	printf("%d", b);
	else
	printf("%d", a);

}
```

### 50부터 100까지 수 중에서 5의 배수

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char ch = 'b';
	switch (1 + 1)   //  변수,연산식 가능 but 실수 불가능
		                 // case문은 선택이 많을	때 사용,  if문은 선택이 적을 때 사용(참이거나 거짓이 명확할 때)
	{
	case 'a': printf("1\n");
	case 'b':printf("2\n");
		printf("2A\n");
	case 'c':printf("3\n");
	{
		printf("3A\n");
		break;
		printf("3B\n");
	}
	default:printf("D");
	}
```

### 무한연산 코드

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int i = 0;
	for (int i = 0, j = 0; i < 3; ++i)         //++i와 i++는 같다.
	{
		printf("%d\n", i);
	}
	printf("종료 i=%d\n", i);
} 
```

### 50~100 사이의 3의 배수 개수

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int count =0;
	for (int i = 50; i < 100; ++i) //++i와 i++는 같다.
		if (!(i % 3)) count++;
			
		
		printf("i =%d\n",count);
	}
```

### 1~100까지 합

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int sum = 0;
	for (int i = 0; i <= 100; ++i)   //++i와 i++는 같다.
	sum = sum + i;
	printf("i=%d\n", sum);
}
```

### 5개의 정수data를 입력 받아 홀수 출력

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a = 0;
	for (int i = 0; i < 5; i++)
	{
		scanf("%d", &a);
		if (a % 2 == 1)
			printf("%d\n", a);
	}
}
```

### 두 정수 m,n입력받아서 m~n까지 합 

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int M = 0;
	int N = 0;
	int sum = 0;
	scanf("%d", &M);
	scanf("%d", &N);
	
	for (int i = M; i <= N; i++)
		sum += i;
	printf("%d", sum);
	
}
```

### 구구단 출력

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int N = 0;
	scanf("%d", &N);

	
	for (int i = 1;  i<= 9; i++)
	printf("%d*%d=%10d\n", N,i,N*i);
	
}
```

### 기부금 총액 및 평균 계산

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int N = 0;
	int sum = 0;
	int avg = 0;
	
	for (int i = 0; i < 10; i++)
	{
		scanf("%d", &N);
		sum += N;
		avg = sum / 10;
	}
		printf("%d\n", sum);
		printf("%d", avg);
	
}
```

### 출하 가능 돼지의 수와 무게 출력 (출하 대상 돼지는 60KG ~ 80KG)

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int weight = 1;  
	int total = 0;  
	int count = 0; 

	while ( total <  5000 && weight !=0)
	{
		printf("돼지의 무게를 입력하시오: ");
		scanf_s("%d", &weight);

			while (weight >= 60 && weight <= 80)
			{
				total += weight;
				count++;
				break;
			}
	}
	printf("출하가능한 돼지 수 :%d", count);
	printf("출하가능한 돼지의 총 무게 :%d", total);

}

```

### 배열 크기

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int arr[8];
	int var = 10;
	int size = sizeof(arr);
	int length = size / sizeof(int);
	printf("arr = %p\n", arr);
	printf("var = %d\n", var);

	printf("배열의 크기:%d \r\n배열의 길이:%d", size, length);
}
```

### 문자 세로로 출력

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main()
{
	

	char str[] = "C Programming for the fisrt time";
	int slen = sizeof(str) / sizeof(str[0]) - 1;
	for (int i = 0; i < slen; i++)
		printf("str[%d] = %c\n",i, str[i]);
}
```

###  <3,6,4,2,8,4,9,1,7 중에 제일 큰 값 찾기>

```c
// 1

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main()
{

	int num[9] = { 3,6,4,2,8,4,9,1,7 };
	int max = 0;
	for (int i = 0; i < 9; i++)
	{
		if (max < num[i])
		{
			max = num[i];
		}
	}
	printf("%d", max);
}
```

```c
// 2

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main()
{

	int num[9] = { 3,6,4,2,8,4,9,1,7 };
	int max = 0;
	for (int i = 0; i < 9; i++)
	{
		while (max <= num[i])
		{
			max = num[i];
			break;
		}
	}
	printf("%d", max);
}

```

### 임의의 수보다 큰 수의 개수를 구하는 코드

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{

	int num[9] = { 3,2,4,2,3,2,9,5,7 };
	int number = 0;
	int count = 0;
	printf("수를 입력하세요.");
	scanf_s("%d", &number);
	for (int i = 0; i < 9; i++)
	{
		if (number < num[i])
		{
			count++;
		}
	}
	printf("%d", count);
}
```

### 점수가 다음과 같이 저장
score = {30,60,40,20,80,40,90,10,70}
점수별로 석차 출력.

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int score[] = { 30,60,40,20,80,40,90,10,70 };
	int rank;
	for (int i = 0; i < sizeof(score)/sizeof(int); i++)
	{
		rank = 1;
		for (int j = 0; j < sizeof(score) / sizeof(int); j++)
			if (score[i] < score[j]) rank++;
			printf("\nscore[%d]=%d점 석차는 %d", i, score[i],rank);
		}
	}
```

### 5명의 학생의 이름과 점수를 배열에 입력받아서, 학생들의 이름과 석차를 출력.

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
		char name[5][15];
		int score[5];
		int rank;

	for (int i = 0; i < 5; i++)
	{
		printf("이름이 뭐에요?\n");
		scanf("%s", name[i]);
		printf("점수는?\n");
		scanf("%d", &score[i]);
	}
	for (int i = 0; i < 5; i++)
	{
		rank = 1;
		for (int j = 0; j < 5; j++)
		{
			if (score[i] < score[j])
				rank++;
		}
		printf("\n학생이름:%s 점수는 %d 석차는 %d", name[i], score[i], rank);
	}
}
```

### 두 정수를 입력받아서 변수 Large에는 큰 수를 Small에는 작은 수를 저장하고 출력하는 코드 작성.

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int large;
	int small;
	int temp;

	printf("정수를 입력하세요");
	scanf("%d %d", &large, &small);
	if (large < small)
	{
		temp = small;
		small = large;
		large = temp;
	}
		printf("\nLarge:%d , Small:%d", large, small);
}

	int large;
	int small;
	int temp;

	printf("정수를 입력하세요");
	scanf("%d %d", &large, &small);
	if (large < small)
	{
		temp = small;
		small = large;
		large = temp;
	}
		printf("\nLarge:%d , Small:%d", large, small);
}
```

### 사칙연산

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

add()
{
	int a, b;
	printf(" 두 정수를 입력하세요.");
	scanf_s("%d %d", &a, &b);
	printf(" %d + %d = %d\n", a, b, a + b);
}

sub()
{
	int a, b;
	printf(" 두 정수를 입력하세요.");
	scanf_s("%d %d", &a, &b);
	printf(" %d - %d = %d\n", a, b, a - b);
}
div()
{
	int a, b;
	printf(" 두 정수를 입력하세요.");
	scanf_s("%d %d", &a, &b);
	if (b == 0)
		printf(" 0으로 나눌 수 없음..\n");
	else
		printf(" %d / %d = %d\n", a, b, a / b);
}
mul()
{
	int a, b;
	printf(" 두 정수를 입력하세요.");
	scanf_s("%d %d", &a, &b);
	printf(" %d * %d = %d\n", a, b, a * b);
}
main()
{
	int select = menu();
	while (select != 4)
	{
		switch (select)
		{
		case 1:
			add();
			break;
		case 2:
			sub();
			break;
		case 3:
			div();
			break;
                case 4:
			mul();
			break;
		}
select = menu();
}
}
int menu()
{
	int select;
	printf("\n 1.뺄셈");
	printf("\n 2.덧셈");
	printf("\n 3.나눗셈");
         printf("\n 4.곱셈");
	printf("\n 5.종료");
	printf("\n메뉴선택하려면 번호를 누르세요.");
	scanf_s("%d", &select);
	return select;
}
```

### Switch문을 이용한 메뉴 선택 프로그램

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

main()
{
	int select = menu();
	while (select != 5)
	{
		switch (select)
		{
		case 1:
			printf("\n덧셈\n");
                break;
		case 2:
			printf("\n뺄셈\n");
            break;
		case 3:
			printf("\n나눗셈\n");
            break;
		case 4:
			printf("\n곱셈\n");
            break;
		default:
			break;
		}
select = menu();
}
}
menu()
{
	int select;
	printf("\n 1.덧셈");
	printf("\n 2.뺄셈");
	printf("\n 3.나눗셈");
	printf("\n 4.곱셈");
	printf("\n 5.종료");
	printf("메뉴선택하려면 번호를 누르세요.");
	scanf("%d", &select);
	return select;
}

```

### Num_arr = [6,8,2,9,4,7]를 선택정렬 알고리즘을 이용해 오름차순 정렬

```c
// 1
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int round;
int Nums[] = { 6,8,2,9,4,7 };
int legth = sizeof(Nums) / sizeof(int);

void SelectionSort();

int main(void)
{
	printf("정렬 전 배열: ");
	for (int i = 0; i < legth; i++) printf("%d ", Nums[i]);
	printf("\n ==========================\n");
	SelectionSort();
	printf("\n\n");
	return 0;
}

void SelectionSort()
{
	int i, j, temp;

	for (i = 0; i < legth - 1; i++)
	{
		for (j = i + 1; j < legth; j++)
		{
			if (Nums[i] > Nums[j])
			{
				temp = Nums[i];
				Nums[i] = Nums[j];
				Nums[j] = temp;
			}
		}
	}
	for (i = 0; i < legth; i++)
	{
		printf("%d ", Nums[i]);
	}
	printf("\n");
}

```

```c
// 2

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int round;
int Nums[] = { 6,8,2,9,4,7 };
int legth = sizeof(Nums) / sizeof(int);

void SelectionSort();

int main(void)
{
	printf("정렬 전 배열: ");
	for (int i = 0; i < legth; i++) printf("%d ", Nums[i]);
	printf("\n ==========================\n");
	SelectionSort();
	printf("\n\n");
	return 0;
}

void SelectionSort()
{
	int i, j, temp,min_index;

	for (i = 0; i < legth - 1; i++)
	{
		min_index = i;
		for (j = i + 1; j < legth; j++)
		{
			if (Nums[min_index] > Nums[j])
			{
				min_index = j;
			}
		}
				temp = Nums[i];
				Nums[i] = Nums[min_index];
				Nums[min_index] = temp;
	}
	for (i = 0; i < legth; i++)
	{
		printf("%2d ", Nums[i]);
	}
	printf("\n");
}

```

### 이름과 과목 A,B의 점수를 입력받아서 총점이 높은 순서대로 (Sort) 출력

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

char name[2][15];
int score[2];
int subject[2];
int total[2];
int legth = sizeof(score) / sizeof(score[0]);  // 학생 수

void SlectionSort();

int main(void)
{
	for (int i = 0; i < legth; i++)
	{
	printf("학생 이름을 입력하세요.");
	scanf("%s" ,name[i]);
	printf("두개의 과목 점수를 입력하세요.");
	scanf("%d %d", &score[i], & subject[i]);
	total[i] = score[i] + subject[i];
	}
	SlectionSort();   //정렬함수 호출 (총점 기준으로 내림차순 정렬)
	return 0;
}


void SlectionSort()
{
	int i, j, max;
	int temp;
	char tempName[15];

		for (i = 0; i < legth - 1; i++)
		{
			max = i;
			for (j = i + 1; j < legth; j++)
			{
				if (total[max] < total[j])
				{
					max = j;
				}
			}

		temp = total[i];
		total[i] = total[max];
		total[max] = temp;

		temp = score[i];
		score[i] = score[max];
		score[max] = temp;

		temp = subject[i];
		subject[i] = subject[max];
		subject[max] = temp;

		strcpy(tempName, name[i]);  //name[i]의 값을 tempName에 복사,  (name변수가 있어서 tempName으로 변수 지정)
		strcpy(name[i], name[max]);
		strcpy(name[max], tempName);
}
		for (i = 0; i < legth; i++)
		{
			printf("%s %d %d %d\n", name[i], score[i], subject[i], total[i]);
		}
}
```

