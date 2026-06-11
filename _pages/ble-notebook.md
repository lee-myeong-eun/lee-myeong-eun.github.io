---
layout: default
title: BLE 기반 공사장 안전장비 실시간 감지 시스템 코드 리뷰
permalink: /projects/ble-notebook/
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

## BLE 기반 공사장 안전장비 실시간 감지 시스템

```cpp
# BLE 기반 공사장 안전장비 실시간 감지 시스템 (EZ-safe)

소속 및 팀원: 전자공학과 최성용, 구민서, 권은지, 이명은
개발 환경: ESP32 DevKit, C/C++ (Arduino IDE), MIT App Inventor
```

## 1. 프로젝트 개요

1.1 개발 배경 및 필요성

- 건설 현장 안전관리의 한계: 기존의 공사장 안전관리는 주로 관리자의 수동 점검이나 CCTV 모니터링에 의존하고 있어, 사각지대가 발생하거나 작업자의 안전모·안전조끼 미착용 상태를 실시간으로 즉각 적발하여 대응하기 어렵습니다.

- 중대재해 예방의 중요성: 소규모 공사장일수록 안전장비 미착용으로 인한 추락, 낙상 등 인명 사고 발생률이 높으며, 사고 발생 시 골든타임을 확보할 수 있는 자동화된 실시간 감지 인프라가 필수적입니다.

- 솔루션 제안: 본 프로젝트는 작업자가 착용하는 안전모와 안전조끼에 ESP32 MCU와 다중 센서(압력, 자이로)를 결합하여 착용 여부 및 낙상(Slam) 상태를 실시간 감지하고, BLE(Bluetooth Low Energy) 통신을 통해 관리자 및 작업자 스마트폰 앱으로 즉시 경고를 전송하는 지능형 안전모 시스템을 설계하였습니다.


1.2 프로젝트 최종 목표

- 압력 센서(FSR) 및 고휘도 LED, 부저를 활용한 안전장비 착용/미착용 실시간 로컬 경고 시스템 구축.

- 6축 가속도 자이로 센서(MPU6050)를 통한 작업자 낙상(Wreck/Fall) 알고리즘 구현.

- 저전력 BLE 통신 기반의 안드로이드 애플리케이션 연동 및 다중 작업자 실시간 모니터링 시뮬레이션.

## 2. 시스템 구조도 및 알고리즘

2.1 시스템 구조도 (System Architecture)

전체 시스템은 디바이스 노드(안전모/안전조끼) - 무선 통신 레이어(BLE) - 모니터링 애플리케이션(App)의 3-Tier 아키텍처로 구성됩니다.


[안전모 노드: ESP32 + FSR 압력 + MPU6050 자이로] 
                       │
             (BLE 저전력 무선 통신)
                       ▼
[모니터링 앱: MIT App Inventor 기반 안드로이드 UI] ──> [실시간 알림 및 경고 팝업]


2.2 핵심 알고리즘 흐름도

1. 초기화: ESP32 가동 후 I2C 통신(MPU6050) 및 BLE 가속도 서비스 비콘을 브로드캐스팅합니다.

2. 착용 감지 단계: 안전모 내부 정수리에 배치된 압력 센서(FSR)의 아날로그 데이터가 설정 임계값(Threshold)을 넘지 못하면 미착용으로 판단, 로컬 부저 경보와 동시에 BLE로 Unworn 데이터를 전송합니다.

3. 낙상 감지 알고리즘: MPU6050의 3축 가속도 벡터 합성값($\sqrt{x^2+y^2+z^2}$)의 급격한 변동(자유낙하 및 충격 임계값 초과)과 임계 시간 이상의 기울기 변화를 분석하여 낙상 발생 여부를 최종 판별합니다.

## 3. 실시간 모니터링 시뮬레이션

```cpp
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

// UUID 정의 (App Inventor 연동 규격)
#define SERVICE_UUID        "4fafc201-75d5-4b36-91e2-575e0d0d3b14"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

#define FSR_PIN             34  // 압력 센서 아날로그 핀
#define BUZZER_PIN          25  // 경고 부저
#define LED_PIN             26  // 경고 LED

Adafruit_MPU6050 mpu;
BLECharacteristic *pCharacteristic;
bool deviceConnected = false;

class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) { deviceConnected = true; };
    void onDisconnect(BLEServer* pServer) { deviceConnected = false; }
};

void setup() {
  Serial.begin(115200);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  // MPU6050 자이로 센서 초기화 (I2C)
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
  }
  mpu.setHighPassFilter(MPU6050_HIGHPASS_0_5HZ);

  // BLE 장치 서버 설정
  BLEDevice::init("EZ-Safe_Helmet_01");
  BLEServer *pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());
  
  BLEService *pService = pServer->createService(SERVICE_UUID);
  pCharacteristic = pService->createCharacteristic(
                      CHARACTERISTIC_UUID,
                      BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
                    );
                    
  pService->start();
  pServer->getAdvertising()->start();
}

void loop() {
  int fsrValue = analogRead(FSR_PIN);
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // 3축 가속도 벡터 합성값 계산
  float totalAccel = sqrt(a.acceleration.x * a.acceleration.x + 
                          a.acceleration.y * a.acceleration.y + 
                          a.acceleration.z * a.acceleration.z);

  String statusPayload = "SAFE";

  // Case 1: 안전모 미착용 판별 (임계값 미달)
  if (fsrValue < 500) { 
    statusPayload = "UNWORN";
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 800);
  } 
  // Case 2: 낙상 사고 감지 (가속도 임계값 초과 비정상 거동)
  else if (totalAccel > 25.0 || totalAccel < 2.0) { 
    delay(500); // 일시적 노이즈 방지 윈도우
    mpu.getEvent(&a, &g, &temp);
    if (abs(a.acceleration.z) < 5.0) { // 충격 후 누워있는 상태 체크
      statusPayload = "FALL";
      digitalWrite(LED_PIN, HIGH);
      tone(BUZZER_PIN, 1200);
    }
  } else {
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);
  }

  // BLE 데이터 송신을 통한 실시간 앱 모니터링 시뮬레이션
  if (deviceConnected) {
    pCharacteristic->setValue(statusPayload.c_str());
    pCharacteristic->notify();
    Serial.println("Sent Status: " + statusPayload);
  }
  delay(100);
}
```

## 4. 세부 구현 내용

1. BLE 신호 감쇠 및 앱 연동 데이터 누락 현상

문제: 공사장 환경을 모사한 거리 테스트 시, 장애물이나 배터리 전압 강하로 인해 BLE Advertising 패킷이 유실되거나 앱 화면이 간헐적으로 멈추는 현상이 발생함.

해결: 통신 패킷 전송 방식을 효율화하고 MIT App Inventor 단의 타이머 클럭 주기를 ESP32 폴링 주기와 동기화(100ms)시켜 데이터 버퍼 오버플로우를 해결함.

2. 리튬이온 배터리 정격 전압(3.7V)과 회로 승압 구조 최적화

문제: 18650 리튬이온 배터리(3.7V) 구동 시, 가속도 센서와 고휘도 LED 소자가 요구하는 안정적인 전압 레벨 유지 불능으로 인한 오작동 확인.

해결: MT3608 DC-DC 승압 부스터 스텝업 컨버터를 설계 단에 추가 배치하여 전체 센서 보드 로직에 안정적인 5V 전원을 유지하고, TP4056 충전 모듈을 연동하여 휴대성과 안전성을 동시 확보함.

3. 압력 센서(FSR) 아날로그 전압 분배기(Voltage Divider) 노이즈

문제: 작업자가 안전모를 착용했음에도 신호 기준값(Float 상태)이 흔들려 오작동 경보음이 발생하는 현상 발생.

해결: 하드웨어 회로 내에 10kΩ 풀다운 막대 저항을 결선하여 전압 분배 회로를 확립함으로써, 완벽한 디지털 로직 레벨 변환을 유도함.

## 5. 최종 완제품 및 하드웨어 패키징

5.1 하드웨어 컴팩트 패키징 및 내장화

- 외관 및 안전성 개선: 실제 작업용 백색 안전모 내부에 센서 부품들이 직접 노출될 경우 작업자의 이물감 유발 및 두피 부상 위험이 있었습니다.

- 패키징 보완: 하드웨어 모듈 회로를 전용 소형 기판(FR-4)에 땜납 처리하여 고정하고, 배선 꼬임 방지를 위해 점퍼 와이어 라인을 일체화했습니다. 최종적으로 배터리, MCU, 컨버터 회로 전반을 헬멧 외부에 안정적으로 마운팅할 수 있는 보호 인클로저 구조로 마감하여 실용성을 극대화하였습니다.


5.2 프로젝트 예산 및 파트리스트 (BOM)

- 총 소요 예산: RISE 사업단 일반형 캡스톤디자인 과제비 지원 (총 171,120원 규모)

- 핵심 부품 사양: ESP32 Wi-Fi+Bluetooth 일체형 개발보드, MPU-6050 6축 가속도 자이로 센서, FSR RA12P 압력 힘 센서, TP4056 배터리 충전 모듈, MT3608 승압 컨버터, 18650 보호회로 내장 리튬배터리, 고휘도 3색 LED 및 액티브 능동 부저.

## 6. 결과 분석 및 기대효과

6.1 프로젝트 최종 결과 분석

- 실제 완제품 안전모 착용 테스트 결과, 안전모 미착용 시 1초 이내로 스마트폰 모니터링 앱 화면에 UNWORN 적색 경고 팝업이 활성화되었으며 안전모 외부 LED/부저가 정상 작동하였습니다.

- 안전모를 착용한 채 강한 물리적 충격과 측면 기울임(낙상 모사)을 인가했을 때 가속도 합성 벡터 연산을 통해 정확히 관리자 앱으로 FALL 긴급 SOS 알림이 전송됨을 검증하였습니다.


6.2 기대효과 및 향후 개선 과제

- 스마트 건설 현장 인프라 혁신: 현장 관리자가 수많은 작업자의 안전 장구 착용 현황을 관리 동선 낭비 없이 중앙 앱 하나로 원격 실시간 모니터링할 수 있어 안전 사각지대를 원천 차단합니다.

- 향후 고도화 계획: 1. 다중 노드 네트워킹: 현재 1:1 BLE 매핑 방식을 넘어, BLE Mesh 네트워킹 기술을 소프트웨어에 추가 반영하여 현장 내 수십 명의 안전모 데이터를 동시 수집하는 게이트웨이 구조로 고도화할 예정입니다.

- GPS 위치 추적 연동: 스마트폰의 GPS 센서 데이터와 임베디드 장치를 연동하여 낙상 사고 발생 시 요구조자의 정확한 현장 내 위치 좌표를 구조대에 즉각 전송하는 원스톱 방재 시스템으로 확장이 가능합니다.

## 7. 최종 완제품 및 시연 사진

![최종 완제품 및 안전모 패키징 외관](./images/KakaoTalk_20260528_164647377.jpg)

