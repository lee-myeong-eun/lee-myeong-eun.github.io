---
layout: default
title: 실내 화재 대피 유도 시스템 (SIGNAL_SPEAK) 코드 리뷰
permalink: /projects/fire-evac-notebook/
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

## 실내 화재 대피 유도 시스템 (SIGNAL_SPEAK) 프로젝트 코드 리뷰

# 실내 화재 대피 유도 시스템

소속 및 팀원: 전자공학과 SIGNAL_SPEAK 팀 (최성용, 구민서, 이명은, 권은지)  
개발 환경: ESP32 DevKit, C/C++ (Arduino IDE), Jupyter Notebook  

## 1. 프로젝트 개요

### 1.1 개발 배경 및 필요성

기존 비상유도등의 시인성 한계: 화재 발생 시 발생하는 치명적인 연기는 상부로 확산되어 벽면 상단에 고정된 기존 비상유도등을 가리게 됩니다. 이로 인해 요구조자의 시야 확보가 어려워져 탈출 골든타임을 놓치는 문제가 지속적으로 발생하고 있습니다. 

정적 안내 시스템의 위험성: 기존 유도등은 화재 위치와 상관없이 항상 일정한 방향만 지시하므로, 오히려 화재가 발생한 위험 구역으로 대피를 유도할 수 있는 치명적인 맹점이 있습니다.  

솔루션 제안: 본 프로젝트는 화재를 실시간으로 감지하고 연기층 아래인 바닥 레벨에서 안전한 최단 탈출 경로를 시각적(동적 LED 파도 효과)·청각적·텍스트로 안내하는 스마트 대피 시스템을 설계 및 구현하였습니다. 

### 1.2 프로젝트 최종 목표
- 화재 발생 시 즉각적으로 위험 구역과 안전 구역을 판별하여 바닥 LED 라인에 동적 애니메이션을 점등합니다.  
- I2C LCD를 통해 정확한 화재 발생 방 번호를 텍스트로 표출하고 부저 경보를 동시에 발령하여 직관성을 극대화합니다.  

## 2. 시스템 구조도 및 알고리즘

### 2.1 시스템 구조도

전체 시스템은 센서 입력부 - ESP32 제어부 - 다중 출력부의 융합 구조로 설계되었으며, 저비용·단순 구성으로 높은 확장성을 가집니다.

[입력부: 불꽃 센서] ──(Digital Input)──> [제어부: ESP32 DevKit] ──(FastLED)──> [출력부: WS2812B LED 스트립]
                                                                ──(I2C Com.)─> [출력부: I2C LCD 16x2]
                                                                ──(PWM/Tone)─> [출력부: 피에조 부저]


### 2.2 메인 제어 알고리즘 흐름도                                       

1. 평상시 (Safe Mode): 전체 LED 인디케이터가 초록색(Green)으로 상시 점등되며 시스템 안정 상태를 유지합니다. 

2. 화재 감지 (Fire Event): 특정 구역의 불꽃 센서 신호가 ESP32로 입력됩니다.  

3. 위험 구역 차단: 화재가 발생한 인접 LED 구간을 빨간색(Red)으로 강제 전환하여 진입을 차단합니다.  

4. 동적 경로 유도: 안전 대피로 방향을 향해 파란색(Blue) LED가 순차적으로 흐르는 '파도 효과(Wave Animation)' 알고리즘을 수행합니다.  

5. 다중 경보 발령: LCD에 "Room 1 Fire" 실시간 텍스트를 출력하고 부저 경보음을 연속 발령합니다.                   

## 3. 실시간 모니터링 시뮬레이션

```c
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <FastLED.h>

// 핀 및 시스템 파라미터 정의
#define LED_PIN       14
#define NUM_LEDS      60
#define FLAME_SENSOR  12
#define BUZZER_PIN    13

CRGB leds[NUM_LEDS];
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(115200);
  pinMode(FLAME_SENSOR, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  lcd.init();
  lcd.backlight();
  
  showNormalStatus();
}

void loop() {
  // 실시간 센서 폴링 모니터링
  int fireDetected = digitalRead(FLAME_SENSOR);
  
  if (fireDetected == HIGH) { 
    triggerFireAlarm();
  } else {
    showNormalStatus();
  }
  delay(30); // 시뮬레이션 루프 주기 최적화
}

// 평상시: 안전 모니터링 상태
void showNormalStatus() {
  lcd.setCursor(0, 0);
  lcd.print("System Stable   ");
  lcd.setCursor(0, 1);
  lcd.print("Safe State      ");
  noTone(BUZZER_PIN);
  
  fill_solid(leds, NUM_LEDS, CRGB::Green); // 안전 구역 초록색 맵핑
  FastLED.show();
}

// 화재 발생 시: 동적 대피 유도 알고리즘 시뮬레이션
void triggerFireAlarm() {
  lcd.setCursor(0, 0);
  lcd.print("WARNING: FIRE!! ");
  lcd.setCursor(0, 1);
  lcd.print("Room 1 Evacuate "); // 화재 위치 정확히 전달
  
  tone(BUZZER_PIN, 1000); // 청각적 경고음 발령
  
  // LED 구간 매핑 및 파도 효과 연출 
  static uint8_t waveIndex = 0;
  waveIndex++;
  
  for (int i = 0; i < NUM_LEDS; i++) {
    if (i < 15) {
      leds[i] = CRGB::Red; // 위험 구간 빨간색 매핑
    } else {
      // 탈출 방향 안내 파란색 파도 효과 (흐름 제어)
      if ((i - 15) % 8 == (waveIndex % 8)) {
        leds[i] = CRGB::Blue;
      } else {
        leds[i] = CRGB::Black; 
      }
    }
  }
  FastLED.show();
  delay(100); // 파도 애니메이션 속도 제어
}
```

## 4. 세부 구현 내용


1. 전원 공급 문제로 인한 MCU 손상 및 전원 분배 재설계
- 문제: 프로젝트 초기 5V 전원 어댑터 전류가 ESP32(내부 로직 3.3V) 인가단 전압 변동을 일으켜 MCU 기기 2대가 손상되는 문제 발생.  
- 해결: 외부 5V 전원을 LED 스트립에 직접 바이패스하고, ESP32의 Vin 레듈레이터 핀으로 안전하게 인가되도록 전원 분배 라인을 분리 및 재설계하여 해결함. 

2. 공통 접지(Common Ground) 노이즈에 의한 LED 오작동
- 문제: 테스트 중 LED 색상 데이터가 튀거나 제어되지 않는 노이즈 현상 발생.  
- 원인: ESP32와 외부 LED 전원 공급 장치 간의 신호 기준점이 불일치하는 공통 접지 미형성 문제. 
- 해결: 회로 상의 모든 GND 라인을 공통으로 결선(Common Ground)하여 신호 기준점을 일치시킴으로써 데이터 무결성 확보.  

3. 긴 대피로 인스턴스에서의 데이터 신호 감쇠
- 문제: 스트립 연장 시, 전반부 LED는 정상 작동하나 후반부 LED 라인의 데이터 왜곡 및 품질 저하 발견.  
- 해결: 신호선 배선 길이를 최소화하고 분기점 회로를 개선하는 구조적 배선 최적화를 통해 데이터 품질 확보.  

4. 외란광 노이즈로 인한 불꽃 센서 오작동 정밀 튜닝
- 문제: 주변 태양광 및 실내 조명등의 적외선 파장 노이즈로 인해 화재가 없음에도 센서가 오작동함.  
- 해결: 불꽃 센서 모듈의 가변저항을 통한 하드웨어 감도 튜닝 및 소프트웨어 필터링을 통해 확실한 화재 불꽃 파장 대역에만 반응하도록 설정


## 5. 최종 완제품 및 하드웨어 패키징

### 5.1 하드웨어 인클로저 및 배선 최적화

외관 개선: 실제 실내 환경을 축소한 80x80cm 구조물 폼보드 모델 기반으로 시스템을 일체화하였습니다. 시연 중 요구조자의 인지성을 높이기 위해 LED 흐름 애니메이션 속도를 최적 정밀 조정하였습니다. 

패키징 수정 사항: 축소 모형 구현 시 데이터 및 전원 배선이 외부로 노출되어 미관 저해 및 쇼트 위험이 있어, 배선이 노출되지 않도록 구조적 케이스 홀링 및 내장형 매립 케이스 구조로 하드웨어 패키징을 최종 보완하였습니다.


### 5.2 완제품 사양 및 파트리스트
총 소요 예산: RISE 사업단 일반형 캡스톤디자인 과제비 지원 (총액: 171,120원)   

핵심 부품 내역: ESP32 DevKit, WS2812B 고밀도 LED 스트립(1M 144LED 및 5M 스트립 교차 검증), I2C 1602 LCD 모듈, 적외선 불꽃 감지 센서 확장 모듈, 피에조 부저, DC 5V 8A 고용량 직류전원장치.  

## 6. 결과 분석 및 기대효과

### 6.1 프로젝트 최종 결과 분석

- 축소 구조물 모델 환경에서 화재 감지 ──> ESP32 신호 처리 ──> 동적 LED 파도 안내선 점등 ──> LCD/부저 다중 경보로 이어지는 임베디드 소방 안전 시나리오 동작에 100% 성공하였습니다.  

- 바닥 매립형 LED 구조로 연기가 가득 찬 모의 환경에서도 상단 비상구 유도등 대비 월등한 가시성과 최단 탈출 경로 시인성을 확인하였습니다.  


### 6.2 기대효과 및 향후 개선 과제

- 스마트 빌딩 소방 안전성 확보: 저비용·단순 구성의 하드웨어 융합 시스템으로 실제 복잡한 복도나 다중이용시설에 도입 시 인명 피해를 획기적으로 줄일 수 있습니다.  

- 향후 개선사항 (IoT 확장성): 1. 고도화 알고리즘 적용: 대규모 복잡 건물 구조에 대응하기 위해 고정 경로 외에 그래프 기반 최단 경로 탐색 알고리즘(Dijkstra, A* 알고리즘)을 소프트웨어에 추가 반영할 계획입니다.

- 무선 모니터링 연동: ESP32의 내장 Wi-Fi/BLE 통신 기능을 활성화하여, 화재 발생 시 건물 중앙 방재실 모니터링 시스템 및 요구조자 모바일 앱으로 대피 경로를 실시간 원격 전송하는 통합 IoT 인프라로 고도화가 가능합니다.








