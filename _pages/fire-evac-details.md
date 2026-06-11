---
layout: default
title: 실내 화재 대피 유도 시스템 상세 분석
permalink: /projects/fire-evac-safety/
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
    border-color: rgba(244, 63, 94, 0.2);
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
    color: #f43f5e;
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
    background: linear-gradient(145deg, rgba(67, 20, 7, 0.4), rgba(30, 10, 10, 0.4));
    border-left: 4px solid #f97316;
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
    color: #fb923c;
    font-weight: bold;
    margin-right: 10px;
    min-width: 100px;
    display: inline-block;
  }

  /* Highlight text */
  .highlight-text {
    color: #f1f5f9;
    background: rgba(244, 63, 94, 0.15);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
  }
</style>

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Hero Banner -->
    <div class="animate-fade-in-up delay-100 mb-5 text-center" style="background: linear-gradient(135deg, #1e0b16 0%, #4a0404 100%); padding: 4rem 2rem; border-radius: 20px; border: 1px solid rgba(244, 63, 94, 0.2); box-shadow: 0 20px 40px rgba(0,0,0,0.4); position: relative; overflow: hidden;">
      <div style="position: absolute; top: -50px; left: -50px; width: 200px; height: 200px; background: rgba(251, 146, 60, 0.15); border-radius: 50%; filter: blur(40px);"></div>
      <div style="position: absolute; bottom: -50px; right: -50px; width: 200px; height: 200px; background: rgba(244, 63, 94, 0.15); border-radius: 50%; filter: blur(40px);"></div>
      
      <span class="badge badge-danger px-3 py-2 mb-3" style="font-size: 0.9rem; background: rgba(244, 63, 94, 0.2); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); border-radius: 20px;">🔥 Safety IoT Project</span>
      <h1 class="text-white font-weight-bold mb-3" style="font-size: 2.2rem; letter-spacing: -0.5px;">실내 화재 대피 유도 시스템</h1>
      <h4 class="text-muted font-weight-normal mb-4">SIGNAL_SPEAK : 동적 대피로 안내 솔루션</h4>
      <div class="d-flex justify-content-center gap-3">
        <span class="text-light mx-3"><i class="fa fa-fire mr-2" style="color: #f97316;"></i>Flame Sensor</span>
        <span class="text-light mx-3"><i class="fa fa-lightbulb-o mr-2 text-warning"></i>WS2812B LED</span>
        <span class="text-light mx-3"><i class="fa fa-microchip mr-2 text-info"></i>ESP32</span>
      </div>
    </div>

    <!-- 1. 프로젝트 개요 -->
    <div class="premium-section animate-fade-in-up delay-200" id="section-overview">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(244, 63, 94, 0.1); color: #f43f5e;"><i class="fa fa-flag"></i></div>
        1. 프로젝트 배경 및 목표
      </h2>
      
      <div class="row">
        <div class="col-md-4 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-eye-slash mr-2"></i>기존 유도등의 한계</h5>
            <p>화재 시 발생하는 연기는 상부로 확산되어 상단에 고정된 기존 비상유도등을 가립니다. 이로 인해 요구조자의 <strong>시야 확보가 어려워져</strong> 골든타임을 놓치는 문제가 지속 발생합니다.</p>
          </div>
        </div>
        <div class="col-md-4 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-warning mr-2"></i>정적 안내의 치명적 오류</h5>
            <p>기존 유도등은 화재 발생 위치와 상관없이 <strong>항상 일정한 방향만</strong> 지시하므로, 오히려 불이 난 위험 구역으로 대피를 유도할 수 있는 치명적인 맹점이 있습니다.</p>
          </div>
        </div>
        <div class="col-md-4 mb-3">
          <div class="overview-card">
            <h5><i class="fa fa-lightbulb-o mr-2"></i>동적 대피 시스템 제안</h5>
            <p>연기층 아래인 <span class="highlight-text">바닥 레벨</span>에서 화재를 실시간으로 감지하고 안전한 최단 탈출 경로를 <strong>시각적(LED 파도 효과)·청각적·텍스트</strong>로 안내하는 솔루션입니다.</p>
          </div>
        </div>
      </div>
      
      <div class="mt-4 p-4 rounded" style="background: rgba(251, 146, 60, 0.05); border: 1px solid rgba(251, 146, 60, 0.2);">
        <h5 class="text-warning mb-3"><i class="fa fa-bullseye mr-2"></i>최종 목표 요약</h5>
        <ul class="list-unstyled mb-0" style="color: #cbd5e1; line-height: 1.8;">
          <li><i class="fa fa-angle-right mr-2 text-warning"></i>즉각적으로 위험/안전 구역을 판별하여 <strong>바닥 LED 라인에 동적 애니메이션(파도 효과)</strong> 점등</li>
          <li><i class="fa fa-angle-right mr-2 text-warning"></i>I2C LCD를 통해 화재 발생 위치(방 번호)를 명확한 <strong>텍스트로 표출</strong></li>
          <li><i class="fa fa-angle-right mr-2 text-warning"></i>동시에 <strong>부저 경보</strong>를 발령하여 시스템의 직관성을 극대화</li>
        </ul>
      </div>
    </div>

    <!-- 2. 시스템 구조도 -->
    <div class="premium-section animate-fade-in-up delay-300" id="section-architecture">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(251, 146, 60, 0.1); color: #fb923c;"><i class="fa fa-sitemap"></i></div>
        2. 시스템 아키텍처 및 제어 알고리즘
      </h2>
      
      <div class="row align-items-center">
        <div class="col-lg-5 mb-4">
          <ul class="info-list list-unstyled mb-0">
            <li><span class="info-label">1. 평상시</span>전체 LED 인디케이터 초록색 상시 점등 (Safe Mode)</li>
            <li><span class="info-label">2. 화재 감지</span>특정 구역의 <span class="text-danger">불꽃 센서 신호</span> 입력</li>
            <li><span class="info-label">3. 위험 차단</span>화재 발생 인접 LED를 <span class="text-danger">빨간색 강제 전환</span></li>
            <li><span class="info-label">4. 경로 유도</span>안전한 방향을 향해 <span class="text-info">파란색 파도 효과(Wave)</span> 점등</li>
            <li><span class="info-label">5. 다중 경보</span>LCD에 실시간 텍스트 출력 및 부저 작동</li>
          </ul>
        </div>
        <div class="col-lg-7 mb-4">
          <div class="p-4 rounded text-center" style="background: #0d1117; border: 1px solid rgba(255,255,255,0.05);">
            <h5 class="text-muted mb-4 small text-uppercase tracking-widest">Hardware Architecture</h5>
            <!-- Mermaid Diagram for beautiful flowchart -->
            <div class="mermaid text-center">
              graph TD
                A["🔥 불꽃 센서<br><small>(입력부)</small>"]:::input
                B(("⚡ ESP32 DevKit<br><small>(제어부)</small>")):::controller
                C["✨ WS2812B LED<br><small>(바닥 유도선)</small>"]:::output_led
                D["📟 I2C 16x2 LCD<br><small>(위치 텍스트)</small>"]:::output_lcd
                E["🔔 피에조 부저<br><small>(경고음)</small>"]:::output_snd
                
                A -->|Digital Input| B
                B -->|FastLED| C
                B -->|I2C Com.| D
                B -->|PWM Tone| E
                
                classDef input fill:#450a0a,stroke:#ef4444,stroke-width:2px,color:#f8fafc;
                classDef controller fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
                classDef output_led fill:#082f49,stroke:#0ea5e9,stroke-width:2px,color:#f8fafc;
                classDef output_lcd fill:#14532d,stroke:#22c55e,stroke-width:2px,color:#f8fafc;
                classDef output_snd fill:#4a044e,stroke:#d946ef,stroke-width:2px,color:#f8fafc;
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 핵심 시뮬레이션 코드 -->
    <div class="premium-section animate-fade-in-up delay-400" id="section-code">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(52, 211, 153, 0.1); color: #34d399;"><i class="fa fa-code"></i></div>
        3. 화재 모니터링 시뮬레이션 (Core Code)
      </h2>
      <p class="text-muted mb-3">센서 폴링 및 동적 대피 유도 애니메이션을 처리하는 아두이노 기반 제어 코드입니다.</p>
      
      <div style="max-height: 400px; overflow-y: auto; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);">
```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <FastLED.h>

#define LED_PIN       14
#define NUM_LEDS      60
#define FLAME_SENSOR  12
#define BUZZER_PIN    13

CRGB leds[NUM_LEDS];
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  pinMode(FLAME_SENSOR, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  lcd.init();
  lcd.backlight();
  showNormalStatus();
}

void loop() {
  int fireDetected = digitalRead(FLAME_SENSOR);
  if (fireDetected == HIGH) { 
    triggerFireAlarm();
  } else {
    showNormalStatus();
  }
  delay(30);
}

void triggerFireAlarm() {
  lcd.setCursor(0, 0); lcd.print("WARNING: FIRE!! ");
  lcd.setCursor(0, 1); lcd.print("Room 1 Evacuate "); 
  tone(BUZZER_PIN, 1000); 
  
  static uint8_t waveIndex = 0; waveIndex++;
  for (int i = 0; i < NUM_LEDS; i++) {
    if (i < 15) {
      leds[i] = CRGB::Red; // 위험 구간 차단
    } else {
      // 안전 구역을 향한 파도 애니메이션
      if ((i - 15) % 8 == (waveIndex % 8)) {
        leds[i] = CRGB::Blue;
      } else {
        leds[i] = CRGB::Black; 
      }
    }
  }
  FastLED.show();
  delay(100); 
}
```
      </div>
    </div>

    <!-- 4. 세부 구현 내용 (트러블슈팅) -->
    <div class="premium-section animate-fade-in-up delay-500" id="section-troubleshoot">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(217, 70, 239, 0.1); color: #d946ef;"><i class="fa fa-wrench"></i></div>
        4. 개발 트러블슈팅 (Troubleshooting)
      </h2>
      
      <div class="row">
        <div class="col-md-6">
          <div class="ts-card">
            <div class="ts-title"><i class="fa fa-bolt mr-2"></i>Issue 1: 전압 변동에 의한 MCU 손상</div>
            <p class="ts-problem"><strong>문제:</strong> 초기 5V 전원 어댑터 전류가 ESP32 인가단 전압 변동을 일으켜 기기가 소손됨.</p>
            <p class="ts-solution"><strong>해결:</strong> 5V 전원을 LED에 직접 바이패스하고, ESP32의 Vin 레귤레이터로 안전하게 들어가도록 전원 분배 재설계.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="ts-card" style="border-left-color: #38bdf8;">
            <div class="ts-title"><i class="fa fa-random mr-2"></i>Issue 2: 공통 접지(Ground) 노이즈</div>
            <p class="ts-problem"><strong>문제:</strong> LED 색상 데이터가 제어되지 않거나 노이즈가 튀는 현상 발생.</p>
            <p class="ts-solution"><strong>해결:</strong> 제어부와 외부 전원 간의 모든 GND 라인을 공통 결선(Common Ground)하여 데이터 기준점 무결성 확보.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="ts-card" style="border-left-color: #eab308;">
            <div class="ts-title"><i class="fa fa-signal mr-2"></i>Issue 3: 긴 대피로 데이터 신호 감쇠</div>
            <p class="ts-problem"><strong>문제:</strong> LED 스트립 연장 시 후반부 라인의 신호 왜곡 및 품질 저하.</p>
            <p class="ts-solution"><strong>해결:</strong> 데이터 신호선 배선을 최소화하고 분기점 회로를 물리적으로 개선.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="ts-card" style="border-left-color: #22c55e;">
            <div class="ts-title"><i class="fa fa-sun-o mr-2"></i>Issue 4: 외란광 노이즈 오작동</div>
            <p class="ts-problem"><strong>문제:</strong> 태양광/조명의 적외선 파장으로 화재가 없음에도 센서가 반응.</p>
            <p class="ts-solution"><strong>해결:</strong> 모듈 가변저항을 통한 감도 튜닝 및 S/W 필터링을 거쳐 확실한 불꽃 파장에만 반응하도록 셋업.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 5. 완제품 패키징 -->
    <div class="premium-section animate-fade-in-up delay-600" id="section-hardware">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(236, 72, 153, 0.1); color: #ec4899;"><i class="fa fa-cubes"></i></div>
        5. 최종 완제품 모형 및 패키징
      </h2>
      
      <div class="row">
        <div class="col-lg-5 mb-4 text-center">
          <div class="p-3" style="background: #0d1117; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05);">
            <!-- Mockup Image placeholder since real image wasn't provided directly in notebook -->
            <div style="background: #1e293b; height: 250px; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-direction: column; border: 1px dashed rgba(255,255,255,0.2);">
               <i class="fa fa-building-o" style="font-size: 3rem; color: #475569; margin-bottom: 10px;"></i>
               <span class="text-muted small">80x80cm 모형 축소 구조물</span>
            </div>
            <p class="text-muted small mt-3 mb-0"><i class="fa fa-search-plus mr-1"></i>동적 애니메이션 속도 정밀 조정 완료</p>
          </div>
        </div>
        <div class="col-lg-7 mb-4 d-flex flex-column justify-content-center">
          <h4 class="text-light mb-3" style="font-size: 1.2rem;">구조적 매립형 인클로저</h4>
          <p class="text-muted" style="line-height: 1.8;">
            실제 실내 환경을 축소한 <strong>80x80cm 폼보드 모델</strong>을 기반으로 시스템을 일체화했습니다. 하드웨어 데이터선 및 전원 배선이 노출될 경우 미관을 저해하고 쇼트 위험이 있으므로, <span class="highlight-text">구조적 홀링 및 내장형 매립 케이스</span>를 통해 안전하게 마감 처리하였습니다.
          </p>
          
          <div class="mt-3 p-3 rounded" style="background: rgba(255,255,255,0.02); border-left: 3px solid #ec4899;">
            <strong class="d-block text-light mb-2">핵심 부품 내역 (총 17만원 예산 지원)</strong>
            <p class="small text-muted mb-0" style="line-height: 1.6;">
              ESP32 DevKit, WS2812B 고밀도 LED 스트립(1M 144LED 및 5M), I2C 1602 LCD 모듈, 적외선 불꽃 감지 센서 확장 모듈, 피에조 부저, DC 5V 8A 고용량 전원장치.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. 결과 분석 및 기대효과 -->
    <div class="premium-section animate-fade-in-up delay-700 mb-0" id="section-results">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(14, 165, 233, 0.1); color: #0ea5e9;"><i class="fa fa-line-chart"></i></div>
        6. 검증 결과 및 향후 기대효과
      </h2>
      
      <div class="row mt-4">
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, rgba(13, 17, 23, 0.8), rgba(22, 27, 34, 0.8)); border: 1px solid rgba(56, 189, 248, 0.2);">
            <h5 class="text-info mb-3"><i class="fa fa-check-square-o mr-2"></i>테스트 100% 성공</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2">화재 감지 ➡️ ESP32 ➡️ LED 안내선 ➡️ 경보에 이르는 전체 시나리오 정상 작동 확인.</li>
              <li>상단 비상구 유도등 대비 <strong>바닥 매립형 구조의 월등한 가시성</strong> 입증.</li>
            </ul>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, rgba(13, 17, 23, 0.8), rgba(22, 27, 34, 0.8)); border: 1px solid rgba(16, 185, 129, 0.2);">
            <h5 class="text-success mb-3"><i class="fa fa-globe mr-2"></i>스마트 빌딩 확장 플랜</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2"><strong>Dijkstra 알고리즘:</strong> 복잡한 실내 구조를 위한 동적 최단 경로 그래프 알고리즘 반영 계획.</li>
              <li><strong>무선 모니터링:</strong> Wi-Fi/BLE를 연동하여 중앙 방재실 모바일 앱에 대피 경로를 실시간 전송.</li>
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
