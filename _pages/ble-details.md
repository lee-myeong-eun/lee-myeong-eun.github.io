---
layout: default
title: BLE 기반 공사장 안전장비 실시간 감지 시스템 상세 분석
permalink: /projects/ble-safety/
---

<style>
  /* Premium Design System Styles */
  .premium-section {
    background-color: #161b22;
    border: 1px solid rgba(255, 255, 255, 0.05);
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
    color: #e2e8f0;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    border-bottom: 2px solid rgba(255,255,255,0.05);
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
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
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
    color: #94a3b8;
    line-height: 1.7;
    font-size: 0.95rem;
    margin-bottom: 0;
  }

  /* Troubleshooting Cards */
  .ts-card {
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.4), rgba(15, 23, 42, 0.4));
    border-left: 4px solid #fb923c;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1rem;
  }
  .ts-title {
    color: #cbd5e1;
    font-weight: bold;
    margin-bottom: 0.8rem;
  }
  .ts-problem { color: #f87171; font-size: 0.9rem; margin-bottom: 0.5rem; }
  .ts-solution { color: #34d399; font-size: 0.9rem; margin-bottom: 0; }

  /* Info List */
  .info-list li {
    padding: 0.8rem 0;
    border-bottom: 1px dashed rgba(255,255,255,0.1);
    color: #cbd5e1;
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
    color: #f1f5f9;
    background: rgba(56, 189, 248, 0.15);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
  }
</style>

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Hero Banner -->
    <div class="animate-fade-in-up delay-100 mb-5 text-center" style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); padding: 4rem 2rem; border-radius: 20px; border: 1px solid rgba(167, 139, 250, 0.2); box-shadow: 0 20px 40px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
      <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: rgba(56, 189, 248, 0.1); border-radius: 50%; filter: blur(40px);"></div>
      <div style="position: absolute; bottom: -50px; left: -50px; width: 200px; height: 200px; background: rgba(244, 63, 94, 0.1); border-radius: 50%; filter: blur(40px);"></div>
      
      <span class="badge badge-primary px-3 py-2 mb-3" style="font-size: 0.9rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 20px;">📶 Capstone Design Project</span>
      <h1 class="text-white font-weight-bold mb-3" style="font-size: 2.2rem; letter-spacing: -0.5px;">BLE 기반 공사장 안전장비 실시간 감지 시스템</h1>
      <h4 class="text-muted font-weight-normal mb-4">EZ-safe : 지능형 스마트 안전모 솔루션</h4>
      <div class="d-flex justify-content-center gap-3">
        <span class="text-light mx-3"><i class="fa fa-microchip mr-2 text-info"></i>ESP32 DevKit</span>
        <span class="text-light mx-3"><i class="fa fa-bluetooth mr-2 text-primary"></i>BLE 통신</span>
        <span class="text-light mx-3"><i class="fa fa-mobile mr-2 text-success"></i>App Inventor</span>
      </div>
    </div>

    <!-- 1. 프로젝트 개요 -->
    <div class="premium-section animate-fade-in-up delay-200" id="section-overview">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(56, 189, 248, 0.1); color: #38bdf8;"><i class="fa fa-flag"></i></div>
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
            <p>안전모에 다중 센서를 결합해 착용 여부 및 낙상(Slam)을 실시간 감지하고, <span class="highlight-text">BLE(저전력 블루투스)</span>를 통해 스마트폰 앱으로 즉시 경고를 전송합니다.</p>
          </div>
        </div>
      </div>
      
      <div class="mt-4 p-4 rounded" style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2);">
        <h5 class="text-success mb-3"><i class="fa fa-check-circle mr-2"></i>최종 목표 요약</h5>
        <ul class="list-unstyled mb-0" style="color: #cbd5e1; line-height: 1.8;">
          <li><i class="fa fa-angle-right mr-2 text-success"></i>압력 센서(FSR) 및 고휘도 LED, 부저를 활용한 <strong>착용/미착용 실시간 로컬 경고 시스템</strong> 구축</li>
          <li><i class="fa fa-angle-right mr-2 text-success"></i>6축 가속도 자이로 센서(MPU6050)를 통한 <strong>작업자 낙상(Wreck/Fall) 알고리즘</strong> 구현</li>
          <li><i class="fa fa-angle-right mr-2 text-success"></i>저전력 BLE 통신 기반의 안드로이드 애플리케이션 연동 및 실시간 모니터링 구축</li>
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
            <li><span class="info-label">1. 초기화</span>ESP32 가동 후 I2C 통신(MPU6050) 및 BLE 가속도 서비스 비콘 브로드캐스팅</li>
            <li><span class="info-label">2. 착용 감지</span>안전모 정수리의 압력 센서(FSR) 데이터가 임계값 미달 시 <span class="text-danger">Unworn(미착용)</span> 전송 및 경보</li>
            <li><span class="info-label">3. 낙상 감지</span>3축 가속도 벡터 합성값($\sqrt{x^2+y^2+z^2}$)의 변동 및 기울기를 분석하여 <span class="text-danger">Fall(낙상)</span> 판별</li>
          </ul>
        </div>
        <div class="col-lg-7 mb-4">
          <div class="p-4 rounded text-center" style="background: #0d1117; border: 1px solid rgba(255,255,255,0.05);">
            <h5 class="text-muted mb-4 small text-uppercase tracking-widest">System Flow</h5>
            <!-- Mermaid Diagram for beautiful flowchart -->
            <div class="mermaid text-center">
              graph TD
                A["👷 안전모 노드<br><small>(ESP32 + FSR + MPU6050)</small>"]:::node
                B(("📡 BLE 무선 통신<br><small>(저전력 비콘)</small>")):::ble
                C["📱 모니터링 앱<br><small>(App Inventor UI)</small>"]:::app
                
                A -->|센서 데이터 송출| B
                B -->|실시간 파싱| C
                C -.->|경고 팝업 발생| C
                
                classDef node fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
                classDef ble fill:#312e81,stroke:#a78bfa,stroke-width:2px,color:#f8fafc;
                classDef app fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 핵심 시뮬레이션 코드 -->
    <div class="premium-section animate-fade-in-up delay-400" id="section-code">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(52, 211, 153, 0.1); color: #34d399;"><i class="fa fa-code"></i></div>
        3. 실시간 모니터링 시뮬레이션 (Core Code)
      </h2>
      <p class="text-muted mb-3">ESP32 하드웨어 모듈로부터 전송되는 BLE 서비스 및 센서 판별 코어 파트입니다.</p>
      
      <div style="max-height: 400px; overflow-y: auto; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
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

    <!-- 4. 세부 구현 내용 (트러블슈팅) -->
    <div class="premium-section animate-fade-in-up delay-500" id="section-troubleshoot">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(251, 146, 60, 0.1); color: #fb923c;"><i class="fa fa-wrench"></i></div>
        4. 개발 트러블슈팅 (Troubleshooting)
      </h2>
      
      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-bug mr-2"></i>Issue 1: BLE 신호 감쇠 및 데이터 누락 현상</div>
        <p class="ts-problem"><strong>문제:</strong> 공사장 환경 모사 테스트 시, 장애물이나 전압 강하로 인해 BLE 패킷이 유실되거나 앱 화면이 멈추는 현상 발생.</p>
        <p class="ts-solution"><strong>해결:</strong> 통신 패킷 전송 방식을 효율화하고 MIT App Inventor의 타이머 클럭 주기를 ESP32 폴링 주기와 동기화(100ms)하여 버퍼 오버플로우를 해결함.</p>
      </div>

      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-bolt mr-2"></i>Issue 2: 리튬 배터리 정격 전압과 승압 최적화</div>
        <p class="ts-problem"><strong>문제:</strong> 18650 배터리(3.7V) 구동 시 가속도 센서와 고휘도 LED가 요구하는 안정적인 전압 유지가 불가능하여 오작동 발생.</p>
        <p class="ts-solution"><strong>해결:</strong> MT3608 DC-DC 승압 부스터 컨버터를 추가 배치하여 5V 전원을 안정적으로 유지하고, TP4056 모듈을 연동해 휴대성과 충전 안정성을 동시 확보함.</p>
      </div>

      <div class="ts-card">
        <div class="ts-title"><i class="fa fa-wave-square mr-2"></i>Issue 3: 압력 센서 아날로그 전압 노이즈</div>
        <p class="ts-problem"><strong>문제:</strong> 안전모를 착용했음에도 신호 기준값이 흔들려 오작동 경보음이 무작위로 발생함 (Float 상태).</p>
        <p class="ts-solution"><strong>해결:</strong> 하드웨어 회로 내에 10kΩ 풀다운 저항을 결선해 전압 분배 회로를 확립, 완벽한 디지털 로직 레벨 변환을 유도함.</p>
      </div>
    </div>

    <!-- 5. 완제품 패키징 -->
    <div class="premium-section animate-fade-in-up delay-600" id="section-hardware">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(251, 113, 133, 0.1); color: #fb7185;"><i class="fa fa-camera"></i></div>
        5. 최종 완제품 및 패키징
      </h2>
      
      <div class="row">
        <div class="col-lg-6 mb-4 text-center">
          <div class="p-3" style="background: #0d1117; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
            <img src="{{ site.baseurl }}/assets/img/ez_safe_hw.png" alt="EZ-safe 완제품" class="img-fluid rounded" style="box-shadow: 0 4px 15px rgba(0,0,0,0.5);" />
            <p class="text-muted small mt-3 mb-0"><i class="fa fa-search-plus mr-1"></i>안전모 패키징 외관 및 배선 일체화</p>
          </div>
        </div>
        <div class="col-lg-6 mb-4 d-flex flex-column justify-content-center">
          <h4 class="text-light mb-3" style="font-size: 1.2rem;">컴팩트 패키징 및 내장화 설계</h4>
          <p class="text-muted" style="line-height: 1.8;">
            실제 작업용 안전모 내부에 부품이 노출될 경우 <strong>작업자의 이물감 유발 및 두피 부상 위험</strong>이 존재했습니다. 이를 방지하기 위해 회로를 전용 소형 기판(FR-4)에 납땜 고정하고 점퍼 라인을 일체화했습니다. 최종적으로 헬멧 외부에 마운팅 가능한 <span class="highlight-text">보호 인클로저 구조</span>로 마감하여 실용성을 극대화했습니다.
          </p>
          
          <div class="mt-3 p-3 rounded" style="background: rgba(255,255,255,0.02); border-left: 3px solid #fb7185;">
            <strong class="d-block text-light mb-2">핵심 파트 리스트 (BOM)</strong>
            <p class="small text-muted mb-0" style="line-height: 1.6;">
              ESP32 Wi-Fi+BLE 보드, MPU-6050 6축 센서, FSR RA12P 압력 센서, TP4056 충전 모듈, MT3608 승압 컨버터, 18650 리튬배터리, 고휘도 3색 LED 및 액티브 능동 부저. (총 17만원 규모 예산)
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. 결과 분석 및 기대효과 -->
    <div class="premium-section animate-fade-in-up delay-700 mb-0" id="section-results">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(244, 114, 182, 0.1); color: #f472b6;"><i class="fa fa-rocket"></i></div>
        6. 결과 검증 및 향후 기대효과
      </h2>
      
      <div class="row mt-4">
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, rgba(13, 17, 23, 0.8), rgba(22, 27, 34, 0.8)); border: 1px solid rgba(56, 189, 248, 0.2);">
            <h5 class="text-info mb-3"><i class="fa fa-bar-chart mr-2"></i>테스트 최종 검증</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2">안전모 미착용 시 1초 이내 앱 화면에 <strong><span class="text-danger">UNWORN</span></strong> 적색 경고 팝업 활성화 및 로컬 부저 작동 성공.</li>
              <li>강한 충격과 측면 기울임(낙상 모사) 인가 시 가속도 합성 벡터 연산을 통해 관리자에게 <strong><span class="text-danger">FALL</span></strong> 긴급 SOS 알림 전송 검증 완료.</li>
            </ul>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, rgba(13, 17, 23, 0.8), rgba(22, 27, 34, 0.8)); border: 1px solid rgba(167, 139, 250, 0.2);">
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
  mermaid.initialize({ startOnLoad: true, theme: 'dark' });
</script>
