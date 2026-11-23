---
layout: default
title: BLE 기반 공사장 안전장비 실시간 감지 시스템 코드 리뷰
permalink: /projects/ble-notebook/
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

# BLE 기반 공사장 안전장비 실시간 감지 시스템 (EZ-safe)

소속 및 팀원: 전자공학과 최성용, 구민서, 권은지, 이명은  
개발 환경: ESP32 DevKit, C/C++ (Arduino IDE), MIT App Inventor  

---

## 1. 프로젝트 개요

### 1.1 개발 배경 및 필요성

- **건설 현장 안전관리의 한계**: 기존 공사장 안전관리는 주로 관리자의 수동 육안 점검이나 고정식 CCTV 모니터링에 의존하여 사각지대가 발생하며, 작업자의 안전모·안전조끼 미착용 상태를 실시간으로 즉각 적발하여 대응하기 어렵습니다.
- **중대재해 예방의 중요성**: 소규모 공사장일수록 안전장비 미착용으로 인한 추락, 낙상 등 인명 사고 발생률이 높으며, 사고 발생 시 골든타임을 확보할 수 있는 자동화된 실시간 감지 인프라가 필수적입니다.
- **솔루션 제안 (EZ-safe)**: 작업자가 착용하는 안전모와 안전조끼에 ESP32 MCU와 다중 센서(MPU6050 가속도 센서, FSR 압력 센서)를 결합하여 착용 여부 및 낙상(Fall) 상태를 실시간 감지하고, 저전력 BLE 통신 및 Bluetooth Serial을 통해 관리자 및 작업자 모바일 앱으로 즉시 경고를 전송하는 지능형 안전 시스템을 설계하였습니다.

### 1.2 프로젝트 최종 목표

- **BLE 신호 세기(RSSI) 기반 감지**: BLE 신호를 10회 연속 측정하여 평균 RSSI를 산출하고, 기준값(-55 dBm) 기반으로 작업 구역 이탈 및 신호 상태를 정밀 판별.
- **MPU6050 기반 움직임 및 착용 상태 판별**: 3축 가속도 변화량(0.3 기준) 분석 및 1분 이상 무움직임 감지 시 착용불량(UNWORN) 자동 처리.
- **모바일 앱 실시간 모니터링**: 작업자별 고유 MAC 주소 기반 데이터 구분 및 Bluetooth Serial 통신을 통해 MIT App Inventor 안드로이드 앱으로 상태 실시간 동기화.

---

## 2. 시스템 구조도 및 알고리즘

### 2.1 시스템 구조도 (System Architecture)

전체 시스템은 디바이스 노드(안전모/안전조끼) - 무선 통신 레이어(BLE / BT Serial) - 모니터링 애플리케이션(App)의 3-Tier 아키텍처로 구성됩니다.

```text
[안전모 노드: ESP32 + MPU6050 가속도 + FSR 압력] 
                       │
              (BLE / BT Serial 무선 통신)
                       ▼
[모니터링 앱: MIT App Inventor 기반 안드로이드 UI] ──> [실시간 상태 표시 및 긴급 경고 팝업]
```

### 2.2 핵심 알고리즘 및 판별 기준

| 구분 | 주요 동작 및 판별 기준 | 상세 설명 |
| :--- | :--- | :--- |
| **초기화 및 판정 유예** | 전원 인가 후 **3초간 판정 유예** | 센서 초기 구동 노이즈 및 착용 준비 시간을 고려하여 오판정 방지 |
| **BLE RSSI 신호 측정** | **10회 연속 측정 후 평균값 산출** | 순간적인 신호 감쇠 노이즈를 필터링하여 안정적인 수신 감도 확보 |
| **신호 상태 판단** | 평균 RSSI **기준값 -55 dBm** | -55 dBm 미만 시 작업 구역 이탈 또는 약한 신호로 판단하여 로컬 부저 경보 발령 |
| **작업자 움직임 감지** | 가속도 변화량 **0.3 초과** | MPU6050 X, Y, Z축 데이터 변화량이 0.3을 초과하면 정상 작업 활동으로 인정 |
| **착용불량 상태 처리** | 움직임 미감지 지속 시간 **1분 이상** | 1분 동안 가속도 변화가 없을 시 장비 미착용 또는 의식 상실 상태로 판단하여 경보 |
| **작업자 데이터 구분** | **디바이스 고유 MAC 주소** 매핑 | 다중 작업자가 동시 작업하는 현장에서도 개별 작업자의 안전 상태를 독립 식별 |

## 3. 실시간 모니터링 시뮬레이션

```c
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

---

## 4. 세부 구현 내용 및 회로 최적화

### 4.1 BLE 신호 감쇠 및 앱 연동 데이터 누락 현상
- **문제**: 공사장 환경을 모사한 거리 테스트 시, 장애물이나 배터리 전압 강하로 인해 BLE Advertising 패킷이 유실되거나 앱 화면이 간헐적으로 멈추는 현상이 발생함.
- **해결**: 통신 패킷 전송 방식을 효율화하고 MIT App Inventor 단의 타이머 클럭 주기를 ESP32 폴링 주기와 동기화(100ms)시켜 데이터 버퍼 오버플로우를 해결함.

### 4.2 리튬이온 배터리 정격 전압(3.7V)과 회로 승압 구조 최적화
- **문제**: 18650 리튬이온 배터리(3.7V) 구동 시, 가속도 센서와 고휘도 LED 소자가 요구하는 안정적인 전압 레벨 유지 불능으로 인한 오작동 확인.
- **해결**: MT3608 DC-DC 승압 부스터 스텝업 컨버터를 회로에 추가 배치하여 센서 보드 로직에 안정적인 5V 전원을 유지하고, TP4056 충전 모듈을 연동하여 휴대성과 안전성을 동시 확보함.

### 4.3 압력 센서(FSR) 아날로그 전압 분배기(Voltage Divider) 노이즈
- **문제**: 작업자가 안전모를 착용했음에도 신호 기준값(Float 상태)이 흔들려 오작동 경보음이 발생하는 현상 발생.
- **해결**: 하드웨어 회로 내에 10kΩ 풀다운 저항을 결선하여 전압 분배 회로를 확립함으로써, 명확한 디지털 로직 레벨 변환을 유도함.

---

## 5. 나의 역할 및 문제 해결 과정

### 5.1 담당 역할: MIT App Inventor 기반 모바일 앱 개발 및 블루투스 연동
본 프로젝트에서 저는 **사용자 및 현장 관리자용 안드로이드 애플리케이션의 프론트엔드 UI 디자인 및 백엔드 블록 코딩**을 전담하여 하드웨어와 앱 간의 무선 데이터 연동을 성공시켰습니다.

- **App Inventor 기반 UI 기획 및 레이아웃 설계**: 건설 현장이라는 특수 환경을 고려하여 시인성 높은 직관적인 대시보드 화면을 기획하고, 스마트폰 화면 크기에 맞춰 반응형 정렬 구조를 구축했습니다.
- **블루투스 장치 검색 및 연결**: ESP32 서버의 서비스 UUID와 커랙터리스틱 UUID를 MIT App Inventor의 BluetoothLE 확장 컴포넌트와 매핑하여 끊김 없는 양방향 통신을 구현했습니다.
- **수신 데이터 파싱 및 작업자별 상태 표시**: 개별 기기의 고유 MAC 주소로 데이터를 식별하고, 실시간 안전 상태(`SAFE` / `UNWORN` / `FALL`)를 대시보드에 즉각 시각화하였습니다.

### 5.2 문제 해결 과정 (Troubleshooting)

**🛠️ 트러블슈팅: 앱 표지(스플래시 화면) 레이아웃 컴포넌트 밀림 현상 해결**
- **문제점**: 앱 인벤터로 앱 표지(스플래시 화면)의 로고와 텍스트를 배치하는 과정에서, 특정 기기나 화면 회전 시 컴포넌트 정렬이 아래로 밀리거나 화면 바깥으로 튀어나가는 현상 발생.
- **원인 분석**: Screen 속성의 Scrollable 옵션과 수평/수직 정렬 속성이 컴포넌트의 고정 픽셀(Pixel) 크기와 충돌하여 발생한 문제.
- **해결 방법**: 
  1. 컴포넌트의 크기 단위를 픽셀(Pixel)에서 상대값(`Fill Parent` 또는 `Percent%`)으로 전면 수정하여 모든 해상도에 유연하게 대응하도록 설계.
  2. 표지 화면의 수직/수평 정렬을 Center(가운데)로 고정하고, `Horizontal/Vertical Arrangement` 컨테이너 박스로 감싸 안아 화면 크기에 구애받지 않는 정중앙 스플래시 화면 완성.

---

## 6. 결과 분석 및 기대효과

### 6.1 프로젝트 최종 결과 분석
- **착용/미착용 감지 검증**: 실제 완제품 안전모 착용 테스트 결과, 안전모 미착용 시 1초 이내로 스마트폰 모니터링 앱 화면에 `UNWORN` 적색 경고 팝업이 활성화되었으며 안전모 외부 LED/부저가 정상 작동하였습니다.
- **낙상(Fall) 사고 감지 검증**: 안전모를 착용한 채 강한 물리적 충격과 측면 기울임을 인가했을 때 가속도 합성 벡터 연산을 통해 관리자 앱으로 `FALL` 긴급 SOS 알림이 정확히 전송됨을 확인하였습니다.

### 6.2 기대효과 및 향후 개선 과제
- **스마트 건설 현장 인프라 혁신**: 현장 관리자가 수많은 작업자의 안전 장구 착용 현황을 중앙 앱 하나로 원격 실시간 모니터링할 수 있어 안전 사각지대를 원천 차단합니다.
- **향후 고도화 계획**:
  1. **다중 노드 네트워킹**: 1:1 BLE 매핑 방식을 넘어 BLE Mesh 네트워킹 기술을 적용하여 현장 내 수십 명의 안전모 데이터를 동시 수집하는 게이트웨이 구조로 고도화.
  2. **GPS 위치 추적 연동**: 스마트폰의 GPS 센서 데이터와 연동하여 낙상 사고 발생 시 요구조자의 정확한 현장 내 위치 좌표를 구조대에 즉각 전송하는 원스톱 방재 시스템 구축.

---

## 7. 최종 완제품 및 하드웨어 패키징 (EZ-safe 외관)

실제 산업 현장에서 사용할 수 있도록 내구성과 실용성을 고려하여 하드웨어를 최종 패키징하였습니다.

![EZ-safe 완제품]({{ site.baseurl }}/assets/img/ez_safe_hw.png)  
*그림: 스마트 안전모 및 안전조끼 하드웨어 모듈 일체형 완제품 외관*

### 7.1 하드웨어 컴팩트 패키징 및 내장화
1. **현장 맞춤형 3D 케이스 설계**:
   - 공사 현장의 거친 환경을 고려하여 내열성, 내습성, 충격 유연성이 뛰어난 **PETG 필라멘트**를 채택하여 케이스를 직접 모델링 및 3D 출력 가공.
   - 안전모의 곡률과 구조를 반영하여 작업자의 착용감에 방해가 되지 않도록 컴팩트하게 설계.
2. **안정적인 전원 및 출력부 통합**:
   - 3.7V 리튬 배터리와 함께 전압 강하를 방지하는 **MT3608 승압 컨버터**를 내장하여 능동 부저와 LED가 항상 일정한 출력으로 경고를 보낼 수 있도록 회로 안정화.
   - 기판 후면은 **절연 처리**를 통해 현장 조립 및 착용 중 발생할 수 있는 쇼트(Short) 오작동을 원천 차단.

### 7.2 프로젝트 예산 및 파트리스트 (BOM)
- **총 소요 예산**: RISE 사업단 일반형 캡스톤디자인 과제비 지원 (총 171,120원 규모)
- **핵심 부품 사양**: ESP32 Wi-Fi+Bluetooth 일체형 개발보드, MPU-6050 6축 가속도 자이로 센서, FSR RA12P 압력 힘 센서, TP4056 배터리 충전 모듈, MT3608 승압 컨버터, 18650 보호회로 내장 리튬배터리, 고휘도 3색 LED 및 액티브 능동 부저.

