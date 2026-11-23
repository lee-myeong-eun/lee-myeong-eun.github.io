---
layout: default
title: BLE 기반 공사장 안전장비 실시간 감지 시스템 상세 분석
permalink: /projects/ble-safety/
---

<style>
  /* Premium Design System Styles */
  .premium-section {
    background-color: var(--bg-card);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 2.5rem;
    margin-bottom: 2.5rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .premium-section:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    border-color: rgba(56, 189, 248, 0.2);
  }
  
  .section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-heading);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    border-bottom: 2px solid var(--border-subtle);
    padding-bottom: 1rem;
  }
  
  .icon-box {
    width: 45px;
    height: 45px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 15px;
    font-size: 1.3rem;
  }
  
  /* Overview Cards */
  .overview-card {
    background: var(--bg-glass);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 1.5rem;
    height: 100%;
  }
  .overview-card h5 {
    color: #38bdf8;
    font-weight: 600;
    margin-bottom: 1rem;
    font-size: 1.1rem;
  }
  .overview-card p {
    color: var(--text-body);
    line-height: 1.7;
    font-size: 0.95rem;
    margin-bottom: 0;
  }

  /* Troubleshooting Cards */
  .ts-card {
    background: linear-gradient(145deg, var(--bg-glass), var(--bg-input));
    border-left: 4px solid #fb923c;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
  }
  .ts-title {
    color: var(--text-body);
    font-weight: bold;
    margin-bottom: 0.8rem;
  }
  .ts-problem { color: #f87171; font-size: 0.9rem; margin-bottom: 0.5rem; }
  .ts-solution { color: #34d399; font-size: 0.9rem; margin-bottom: 0; }

  /* Info List */
  .info-list li {
    padding: 0.8rem 0;
    border-bottom: 1px dashed var(--border-medium);
    color: var(--text-body);
    line-height: 1.6;
  }
  .info-list li:last-child {
    border-bottom: none;
  }
  .info-label {
    color: #a78bfa;
    font-weight: bold;
    margin-right: 10px;
    min-width: 100px;
    display: inline-block;
  }

  /* Highlight text */
  .highlight-text {
    color: var(--text-primary);
    background: rgba(56, 189, 248, 0.15);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
  }
</style>

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Hero Banner -->
    <div class="animate-fade-in-up delay-100 mb-5 text-center" style="background: linear-gradient(135deg, var(--hero-grad-linear-1) 0%, var(--hero-grad-linear-3) 100%); padding: 4rem 2rem; border-radius: 20px; border: 1px solid var(--border-accent); box-shadow: 0 20px 40px var(--shadow-main); position: relative; overflow: hidden;">
      <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: var(--badge-bg); border-radius: 50%; filter: blur(40px);"></div>
      <div style="position: absolute; bottom: -50px; left: -50px; width: 200px; height: 200px; background: var(--badge-bg); border-radius: 50%; filter: blur(40px);"></div>
      
      <span class="badge badge-primary px-3 py-2 mb-3" style="font-size: 0.9rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 20px;">📶 Capstone Design Project</span>
      <h1 class="text-light font-weight-bold mb-3" style="font-size: 2.2rem; letter-spacing: -0.5px;">BLE 기반 공사장 안전장비 실시간 감지 시스템</h1>
      <h4 class="text-muted font-weight-normal mb-4">EZ-safe : 지능형 스마트 안전모 솔루션</h4>
      <div class="d-flex justify-content-center gap-3">
        <span class="text-light mx-3"><i class="fa fa-microchip mr-2 text-info"></i>ESP32</span>
        <span class="text-light mx-3"><i class="fa fa-bluetooth mr-2 text-primary"></i>BLE / RSSI</span>
        <span class="text-light mx-3"><i class="fa fa-mobile mr-2 text-success"></i>App Inventor</span>
      </div>
    </div>

    <!-- 1. 프로젝트 개요 -->
    <div class="premium-section animate-fade-in-up delay-200" id="section-overview">
      <h2 class="section-title">
        <div class="icon-box" style="background: var(--badge-bg); color: #38bdf8;"><i class="fa fa-flag"></i></div>
        1. 프로젝트 배경 및 목표
      </h2>
      
      <div class="row">
        <div class="col-md-4 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-warning mr-2"></i>건설 현장의 한계</h5>
            <p>기존 안전관리는 수동 점검이나 CCTV 모니터링에 의존하여 사각지대가 발생하고, 안전모·조끼 미착용을 실시간으로 적발하여 즉각 대응하기가 매우 어렵습니다.</p>
          </div>
        </div>
        <div class="col-md-4 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-heartbeat mr-2"></i>중대재해 예방</h5>
            <p>소규모 공사장일수록 안전장비 미착용에 의한 추락, 낙상 사고 발생률이 높습니다. 사고 발생 시 <span class="highlight-text">골든타임을 확보</span>할 수 있는 자동화 인프라가 필수적입니다.</p>
          </div>
        </div>
        <div class="col-md-4 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-lightbulb-o mr-2"></i>솔루션 제안 (EZ-safe)</h5>
            <p>ESP32와 <span class="highlight-text">BLE(저전력 블루투스)</span> 통신을 활용해 작업자의 안전 상태를 실시간으로 감지하고, RSSI 신호 세기 측정과 MPU6050 가속도 센서를 통해 착용 상태를 판별하여 모바일 앱으로 즉시 확인할 수 있는 시스템입니다.</p>
          </div>
        </div>
      </div>
      
      <div class="mt-4 p-4 rounded" style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2);">
        <h5 class="text-success mb-3"><i class="fa fa-check-circle mr-2"></i>최종 목표 요약</h5>
        <ul class="list-unstyled mb-0" style="color: var(--text-body); line-height: 1.8;">
          <li><i class="fa fa-angle-right mr-2 text-success"></i>BLE 신호를 10회 측정하여 평균 RSSI를 계산하고 <strong>기준값(-55) 기반으로 신호 상태를 판별</strong>하는 시스템 구축</li>
          <li><i class="fa fa-angle-right mr-2 text-success"></i>MPU6050 가속도 센서를 통한 <strong>작업자 움직임 감지 및 착용불량 판별 알고리즘</strong> 구현</li>
          <li><i class="fa fa-angle-right mr-2 text-success"></i>Bluetooth Serial 통신 기반의 MIT App Inventor 모바일 앱 연동 및 작업자별 실시간 모니터링 구축</li>
        </ul>
      </div>
    </div>

    <!-- 2. 시스템 구조도 -->
    <div class="premium-section animate-fade-in-up delay-300" id="section-architecture">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(167, 139, 250, 0.1); color: #a78bfa;"><i class="fa fa-sitemap"></i></div>
        2. 시스템 아키텍처 및 알고리즘
      </h2>
      
      <div class="row align-items-center">
        <div class="col-lg-5 mb-4">
          <ul class="info-list list-unstyled mb-0">
            <li><span class="info-label">1. 초기화</span>ESP32 가동 후 BLE 스캔 시작 및 MPU6050 가속도 센서 초기화</li>
            <li><span class="info-label">2. 신호 측정</span>BLE 신호를 <span class="text-info">10회 측정</span>하고 평균 RSSI 계산, 기준값 <span class="text-danger">-55 이하</span> 시 약한 신호로 판단하여 부저 작동</li>
            <li><span class="info-label">3. 움직임 감지</span>시작 후 3초간 판정 유예, 초기 가속도값 대비 <span class="text-danger">변화량 0.3 초과</span> 시 움직임 판단, 1분 이상 미감지 시 착용불량 처리</li>
            <li><span class="info-label">4. 데이터 전달</span>작업자별 MAC 주소 기반 데이터 구분, <span class="text-info">Bluetooth Serial</span>로 모바일 앱에 상태 전달</li>
          </ul>
        </div>
        <div class="col-lg-7 mb-4">
          <div class="p-4 rounded text-center" style="background: var(--bg-terminal-header); border: 1px solid var(--border-subtle);">
            <h5 class="text-muted mb-4 small text-uppercase tracking-widest">System Flow</h5>
            <!-- Mermaid Diagram for beautiful flowchart -->
            <div class="mermaid text-center">
              graph TD
                A["👷 안전모 노드<br><small>(ESP32 + MPU6050)</small>"]:::node
                B(("📡 BLE 무선 통신<br><small>(RSSI 신호 측정)</small>")):::ble
                C["📱 모니터링 앱<br><small>(MIT App Inventor)</small>"]:::app
                
                A -->|RSSI + 가속도 데이터| B
                B -->|Bluetooth Serial| C
                C -.->|작업자별 상태 표시| C
                
                classDef node fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
                classDef ble fill:#312e81,stroke:#a78bfa,stroke-width:2px,color:#f8fafc;
                classDef app fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 주요 구현 내용 -->
    <div class="premium-section animate-fade-in-up delay-350" id="section-implementation">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(16, 185, 129, 0.1); color: #10b981;"><i class="fa fa-list-ol"></i></div>
        3. 주요 구현 내용
      </h2>
      <p class="text-muted mb-4" style="font-size: 1.05rem; line-height: 1.7;">
        <strong class="text-light">센서 데이터 기반 실시간 안전 상태 판별 시스템:</strong> ESP32와 BLE, MPU6050 가속도 센서를 연동하여 RSSI 신호 세기 및 작업자 움직임을 정밀 측정하고, Bluetooth Serial 통신을 통해 관리자 모바일 앱으로 실시간 모니터링 데이터를 전송합니다.
      </p>
      
      <div class="row">
        <!-- 1. BLE 신호 세기 기반 감지 -->
        <div class="col-lg-4 col-md-6 mb-3">
          <div class="overview-card" style="border-top: 3px solid #10b981;">
            <h5 style="color: #10b981;"><i class="fa fa-bluetooth-b mr-2"></i>01. BLE 신호 세기 기반 감지</h5>
            <p>
              ESP32의 BLE 통신으로 신호를 <strong>총 10회 연속 측정</strong>하여 평균 RSSI 값을 산출합니다. 평균 RSSI가 <strong>기준값 -55 dBm 미만</strong>으로 감쇠될 경우 신호 미약 및 작업 구역 이탈 상태로 판정하고 즉시 부저 경보를 울립니다.
            </p>
          </div>
        </div>

        <!-- 2. MPU6050 기반 작업자 움직임 판별 -->
        <div class="col-lg-4 col-md-6 mb-3">
          <div class="overview-card" style="border-top: 3px solid #38bdf8;">
            <h5 style="color: #38bdf8;"><i class="fa fa-heartbeat mr-2"></i>02. MPU6050 기반 움직임 판별</h5>
            <p>
              MPU6050 6축 센서의 X, Y, Z축 가속도 데이터를 수집합니다. 초기 오판정 방지를 위해 시작 후 <strong>3초간 판정을 유예</strong>하며, 가속도 변화량이 <strong>0.3 초과</strong> 시 움직임으로 인정하고, <strong>1분 이상 움직임이 없을 경우</strong> 착용불량 상태로 자동 처리합니다.
            </p>
          </div>
        </div>

        <!-- 3. 작업자별 안전 상태 데이터 처리 -->
        <div class="col-lg-4 col-md-12 mb-3">
          <div class="overview-card" style="border-top: 3px solid #a855f7;">
            <h5 style="color: #a855f7;"><i class="fa fa-mobile mr-2"></i>03. 작업자별 상태 데이터 처리</h5>
            <p>
              작업자별 <strong>고유 MAC 주소</strong>를 활용해 다중 디바이스 데이터를 안정적으로 구분합니다. 수집된 안전 상태는 <strong>Bluetooth Serial 통신</strong>을 통해 MIT App Inventor로 개발한 스마트폰 앱으로 실시간 전송되어 모니터링 화면에 표시됩니다.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 4. 핵심 시뮬레이션 코드 -->
    <div class="premium-section animate-fade-in-up delay-400" id="section-code">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(52, 211, 153, 0.1); color: #34d399;"><i class="fa fa-code"></i></div>
        4. 실시간 모니터링 시뮬레이션 (Core Code)
      </h2>
      <p class="text-muted mb-3" style="font-size: 1.05rem; line-height: 1.7;">
        <strong class="text-light">센서 데이터 수집 및 상태 판별 제어 로직:</strong> ESP32 하드웨어 모듈로부터 전송되는 BLE 서비스 및 MPU6050 센서 데이터를 실시간 처리하고, 착용 상태 및 낙상 위험을 판별하여 Bluetooth 통신으로 전송하는 코어 알고리즘 코드입니다.
      </p>
      
      <div style="max-height: 400px; overflow-y: auto; border-radius: 8px; border: 1px solid var(--border-medium);">
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

// ... (초기화 코드 생략) ...

void loop() {
  int fsrValue = analogRead(FSR_PIN);
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // 3축 가속도 벡터 합성값 계산
  float totalAccel = sqrt(pow(a.acceleration.x, 2) + pow(a.acceleration.y, 2) + pow(a.acceleration.z, 2));
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

  // BLE 데이터 송신
  if (deviceConnected) {
    pCharacteristic->setValue(statusPayload.c_str());
    pCharacteristic->notify();
  }
  delay(100);
}
```
      </div>
    </div>

    <!-- 5. 개발 트러블슈팅 -->
    <div class="premium-section animate-fade-in-up delay-500" id="section-troubleshoot">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(251, 146, 60, 0.1); color: #fb923c;"><i class="fa fa-wrench"></i></div>
        5. 개발 트러블슈팅 (Troubleshooting)
      </h2>
      
      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-users mr-2"></i>Issue 1: 팀원과의 협업 및 역할 분담</div>
        <p class="ts-problem"><strong>상황:</strong> 4명의 팀원이 센서 데이터 수집, ESP32 제어, BLE 통신 및 모바일 앱 구현 등의 기능을 분담하여 개발을 진행했습니다.</p>
        <p class="ts-solution"><strong>해결:</strong> 각 기능의 진행 상황과 동작 결과를 주기적으로 공유하면서 전체 시스템을 통합했습니다. 기능 간 인터페이스를 사전에 정의하여 통합 과정에서의 충돌을 최소화했습니다.</p>
      </div>

      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-signal mr-2"></i>Issue 2: BLE 신호 세기 변동 및 감지 안정성 문제</div>
        <p class="ts-problem"><strong>문제:</strong> 주변 환경과 장치 간 거리에 따라 RSSI 값이 불규칙하게 달라져 신호 상태를 안정적으로 판단하기 어려웠습니다.</p>
        <p class="ts-solution"><strong>해결:</strong> BLE 신호를 10회 측정한 후 평균 RSSI를 계산하도록 구현했습니다. 평균값을 기준값 -55와 비교하여 신호 상태를 판단하도록 개선하여 안정성을 확보했습니다.</p>
      </div>

      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-tachometer mr-2"></i>Issue 3: 작업자 움직임 감지 및 착용 상태 판별 문제</div>
        <p class="ts-problem"><strong>문제:</strong> 초기 센서값과 일시적인 움직임 변화로 인한 오판정이 발생하여 착용 상태를 정확히 판별하기 어려웠습니다.</p>
        <p class="ts-solution"><strong>해결:</strong> 시스템 시작 후 3초간 판정을 유예하고 초기 가속도값을 기준으로 변화량을 비교하도록 구성했습니다. 변화량 0.3 초과 시 움직임으로 판단하고 1분 이상 움직임이 없으면 착용불량 상태로 처리했습니다.</p>
      </div>

      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-exchange mr-2"></i>Issue 4: 작업자별 데이터 구분 및 모바일 앱 연동 문제</div>
        <p class="ts-problem"><strong>문제:</strong> 여러 작업자의 센서 데이터를 구분하지 못해 개별 작업자의 안전 상태를 정확하게 파악할 수 없었습니다.</p>
        <p class="ts-solution"><strong>해결:</strong> 작업자별 MAC 주소를 등록하고 수신 장치의 MAC 주소를 비교하여 데이터를 구분했습니다. 이후 작업자별 상태 메시지를 생성하고 Bluetooth Serial 통신으로 모바일 앱에 전달하도록 구성했습니다.</p>
      </div>
    </div>

    <!-- 6. 담당 역할 -->
    <div class="premium-section animate-fade-in-up delay-550" id="section-role">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(99, 102, 241, 0.1); color: #818cf8;"><i class="fa fa-user"></i></div>
        6. 담당 역할
      </h2>
      
      <div class="row">
        <div class="col-md-6 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-mobile mr-2"></i>모바일 앱 개발</h5>
            <p>MIT App Inventor를 활용하여 모바일 앱의 UI를 설계하고 블루투스 장치 검색 및 연결 기능을 구현했습니다.</p>
          </div>
        </div>
        <div class="col-md-6 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-database mr-2"></i>수신 데이터 처리</h5>
            <p>ESP32로부터 Bluetooth Serial 통신을 통해 수신한 데이터를 처리하고 작업자별 안전 상태 표시 화면을 구현했습니다.</p>
          </div>
        </div>
      </div>
      
      <div class="mt-3 p-4 rounded" style="background: rgba(99, 102, 241, 0.05); border: 1px solid rgba(99, 102, 241, 0.2);">
        <h5 style="color: #818cf8;" class="mb-3"><i class="fa fa-tasks mr-2"></i>세부 담당 내역</h5>
        <ul class="list-unstyled mb-0" style="color: var(--text-body); line-height: 1.8;">
          <li><i class="fa fa-angle-right mr-2" style="color: #818cf8;"></i>MIT App Inventor를 활용한 모바일 앱 UI 및 기능 개발</li>
          <li><i class="fa fa-angle-right mr-2" style="color: #818cf8;"></i>블루투스 장치 검색 및 연결 기능 구현</li>
          <li><i class="fa fa-angle-right mr-2" style="color: #818cf8;"></i>수신 데이터 처리 및 파싱</li>
          <li><i class="fa fa-angle-right mr-2" style="color: #818cf8;"></i>작업자별 안전 상태 표시 화면 구현</li>
        </ul>
      </div>
    </div>

    <!-- 7. 완제품 패키징 -->
    <div class="premium-section animate-fade-in-up delay-600" id="section-hardware">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(251, 113, 133, 0.1); color: #fb7185;"><i class="fa fa-camera"></i></div>
        7. 최종 완제품 및 패키징
      </h2>
      
      <div class="row">
        <div class="col-lg-6 mb-4 text-center">
          <div class="p-3" style="background: var(--bg-terminal-header); border-radius: 16px; border: 1px solid var(--border-subtle);">
            <img src="{{ site.baseurl }}/assets/img/ez_safe_hw.png" alt="EZ-safe 완제품" class="img-fluid rounded" style="box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
            <p class="text-muted small mt-3 mb-0"><i class="fa fa-search-plus mr-1"></i>안전모 패키징 외관 및 배선 일체화</p>
          </div>
        </div>
        <div class="col-lg-6 mb-4 d-flex flex-column justify-content-center">
          <h4 class="text-light mb-3" style="font-size: 1.2rem;">IoT 안전 시스템 하드웨어 구성</h4>
          <p class="text-muted" style="line-height: 1.8;">
            ESP32와 MPU6050 가속도 센서, BLE 통신 모듈을 활용하여 작업자의 안전 상태를 실시간으로 감지하는 하드웨어 시스템을 구성했습니다. 센서 데이터는 <span class="highlight-text">Bluetooth Serial 통신</span>을 통해 MIT App Inventor 모바일 앱으로 전달되어 작업자별 안전 상태를 확인할 수 있습니다.
          </p>
          
          <div class="mt-3 p-3 rounded" style="background: rgba(255,255,255,0.02); border-left: 3px solid #fb7185;">
            <strong class="d-block text-light mb-2">핵심 파트 리스트 (BOM)</strong>
            <p class="small text-muted mb-0" style="line-height: 1.6;">
              ESP32 Wi-Fi+BLE 보드, MPU6050 6축 가속도 센서, BLE 통신 모듈, Bluetooth Serial 통신, 액티브 능동 부저, MIT App Inventor 모바일 앱
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 8. 결과 분석 및 기대효과 -->
    <div class="premium-section animate-fade-in-up delay-700 mb-0" id="section-results">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(244, 114, 182, 0.1); color: #f472b6;"><i class="fa fa-rocket"></i></div>
        8. 결과 검증 및 향후 기대효과
      </h2>

      <!-- 시현 영상 -->
      <div class="mb-4">
        <h5 class="text-light mb-3"><i class="fa fa-play-circle mr-2 text-danger"></i>프로젝트 시현 영상</h5>
        <div class="embed-responsive embed-responsive-16by9" style="border-radius: 12px; overflow: hidden; border: 1px solid var(--border-subtle);">
          <iframe class="embed-responsive-item" src="https://www.youtube.com/embed/Gf-O3V0Eyr0" allowfullscreen></iframe>
        </div>
      </div>
      
      <div class="row mt-4">
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, var(--bg-card), var(--bg-glass)); border: 1px solid rgba(56, 189, 248, 0.2);">
            <h5 class="text-info mb-3"><i class="fa fa-bar-chart mr-2"></i>테스트 최종 검증</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2">BLE 신호 10회 측정 후 평균 RSSI 계산을 통한 <strong>신호 상태 판별 정상 동작</strong> 확인.</li>
              <li class="mb-2">MPU6050 가속도 변화량 기반 <strong>움직임 감지 및 착용불량 판별</strong> 알고리즘 정상 동작 검증 완료.</li>
              <li>작업자별 MAC 주소 구분 및 Bluetooth Serial 통신을 통한 <strong>모바일 앱 실시간 상태 확인</strong> 성공.</li>
            </ul>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, var(--bg-card), var(--bg-glass)); border: 1px solid var(--border-accent);">
            <h5 class="text-primary mb-3"><i class="fa fa-lightbulb-o mr-2"></i>스마트 건설 인프라의 미래</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2"><strong>중앙 집중형 모니터링:</strong> 관리자 앱 하나로 원격 실시간 모니터링을 지원하여 안전 사각지대 원천 차단.</li>
              <li class="mb-2"><strong>BLE Mesh 확장:</strong> 1:1 통신을 넘어 다중 노드 네트워킹을 통한 대규모 인력 동시 모니터링 게이트웨이 구축 예정.</li>
              <li><strong>GPS 연동:</strong> 스마트폰 GPS 데이터 융합으로 낙상 시 정확한 위치 좌표를 전송하는 방재 시스템 고도화 가능.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- Initialize Mermaid -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: (localStorage.getItem('theme') === 'light' ? 'default' : 'dark') });
</script>
