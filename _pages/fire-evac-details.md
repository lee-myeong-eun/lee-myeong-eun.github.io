---
layout: default
title: 실내 화재 대피 유도 시스템 상세 분석
permalink: /projects/fire-evac-safety/
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
    border-color: var(--border-accent);
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
    color: #f43f5e;
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
    background: linear-gradient(145deg, rgba(67, 20, 7, 0.4), rgba(30, 10, 10, 0.4));
    border-left: 4px solid #f97316;
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
    color: #fb923c;
    font-weight: bold;
    margin-right: 10px;
    min-width: 100px;
    display: inline-block;
  }

  /* Highlight text */
  .highlight-text {
    color: var(--text-primary);
    background: rgba(244, 63, 94, 0.15);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
  }
</style>

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Hero Banner -->
    <div class="animate-fade-in-up delay-100 mb-5 text-center" style="background: linear-gradient(135deg, var(--hero-grad-linear-1) 0%, var(--hero-grad-linear-3) 100%); padding: 4rem 2rem; border-radius: 20px; border: 1px solid var(--border-accent); box-shadow: 0 20px 40px var(--shadow-main); position: relative; overflow: hidden;">
      <div style="position: absolute; top: -50px; left: -50px; width: 200px; height: 200px; background: rgba(251, 146, 60, 0.15); border-radius: 50%; filter: blur(40px);"></div>
      <div style="position: absolute; bottom: -50px; right: -50px; width: 200px; height: 200px; background: rgba(244, 63, 94, 0.15); border-radius: 50%; filter: blur(40px);"></div>
      
      <span class="badge badge-danger px-3 py-2 mb-3" style="font-size: 0.9rem; background: var(--border-accent); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.4); border-radius: 20px;">🔥 Safety IoT Project</span>
      <h1 class="text-light font-weight-bold mb-3" style="font-size: 2.2rem; letter-spacing: -0.5px;">실내 화재 대피 유도 시스템</h1>
      <h4 class="text-muted font-weight-normal mb-4">SIGNAL_SPEAK : 동적 대피로 안내 솔루션</h4>
      <div class="d-flex justify-content-center gap-3">
        <span class="text-light mx-3"><i class="fa fa-fire mr-2" style="color: #f97316;"></i>Flame Sensor</span>
        <span class="text-light mx-3"><i class="fa fa-lightbulb-o mr-2 text-warning"></i>WS2812B LED</span>
        <span class="text-light mx-3"><i class="fa fa-microchip mr-2 text-info"></i>ESP32</span>
      </div>
    </div>

    <!-- 1. 프로젝트 배경 및 목표 -->
    <div class="premium-section animate-fade-in-up delay-200" id="section-overview">
      <h2 class="section-title">
        <div class="icon-box" style="background: var(--badge-bg); color: #f43f5e;"><i class="fa fa-flag"></i></div>
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
            <p>연기층 아래인 <span class="highlight-text">바닥 레벨</span>에서 화염 센서를 통해 화재를 실시간 감지하고, <strong>LED 대피 경로 안내, LCD 위치 표출, 부저 경보</strong>를 연동한 직관적인 동적 다중 경보 시스템입니다.</p>
          </div>
        </div>
      </div>
      
      <div class="mt-4 p-4 rounded" style="background: rgba(251, 146, 60, 0.05); border: 1px solid rgba(251, 146, 60, 0.2);">
        <h5 class="text-warning mb-3"><i class="fa fa-bullseye mr-2"></i>최종 목표 요약</h5>
        <ul class="list-unstyled mb-0" style="color: var(--text-body); line-height: 1.8;">
          <li><i class="fa fa-angle-right mr-2 text-warning"></i>여러 방에 설치된 <strong>불꽃 센서의 데이터를 수집</strong>하여 화재를 실시간 감지</li>
          <li><i class="fa fa-angle-right mr-2 text-warning"></i>화재가 감지된 방 번호를 <strong>LCD에 표시</strong>하고 화재 발생 여부에 따라 <strong>출력 내용을 구분</strong></li>
          <li><i class="fa fa-angle-right mr-2 text-warning"></i><strong>LED를 활용한 대피 경로 안내</strong> 및 부저에서 <strong>서로 다른 주파수의 경보음을 순차적으로 출력</strong></li>
        </ul>
      </div>
    </div>

    <!-- 2. 시스템 아키텍처 및 제어 알고리즘 -->
    <div class="premium-section animate-fade-in-up delay-300" id="section-architecture">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(251, 146, 60, 0.1); color: #fb923c;"><i class="fa fa-sitemap"></i></div>
        2. 시스템 아키텍처 및 제어 알고리즘
      </h2>
      
      <div class="row align-items-center">
        <div class="col-lg-5 mb-4">
          <ul class="info-list list-unstyled mb-0">
            <li><span class="info-label">1. 평상시</span>전체 LED 초록색 상시 점등 (Safe Mode)</li>
            <li><span class="info-label">2. 센서 감지</span>여러 방에 설치된 불꽃 센서의 데이터 수집</li>
            <li><span class="info-label">3. 화재 판별</span>화염 센서 신호 입력 시 화재 발생 판단</li>
            <li><span class="info-label">4. 위험 표시</span>화재 발생 인접 LED 빨간색 전환 및 화재 감지 방 번호 LCD 표시</li>
            <li><span class="info-label">5. 경로 유도</span>안전한 방향으로 LED 파도 효과 점등</li>
            <li><span class="info-label">6. 다중 경보</span>부저에서 서로 다른 주파수의 경보음 순차 출력</li>
          </ul>
        </div>
        <div class="col-lg-7 mb-4">
          <div class="p-4 rounded text-center" style="background: var(--bg-terminal-header); border: 1px solid var(--border-subtle);">
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

    <!-- 3. 주요 구현 내용 -->
    <div class="premium-section animate-fade-in-up delay-400" id="section-implementation">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(168, 85, 247, 0.1); color: #a855f7;"><i class="fa fa-cogs"></i></div>
        3. 주요 구현 내용
      </h2>
      <p class="text-muted mb-4" style="font-size: 1.05rem; line-height: 1.7;">
        <strong class="text-light">다중 센서 및 안전 제어 아키텍처:</strong> ESP32를 기반으로 다중 구역 화염 센서 데이터를 실시간 수집하고, 상황별 LCD 안내, WS2812B 동적 LED 대피 경로 유도 및 다중 주파수 부저 경보를 제어하는 핵심 기능입니다.
      </p>

      <div class="row">
        <!-- 1. ESP32 기반 화재 감지 및 데이터 처리 -->
        <div class="col-lg-4 col-md-6 mb-3">
          <div class="overview-card" style="border-top: 3px solid #a855f7;">
            <h5 style="color: #a855f7;"><i class="fa fa-fire mr-2"></i>01. 화재 감지 및 데이터 처리</h5>
            <p>
              여러 방에 분산 설치된 <strong>적외선 불꽃 센서</strong>의 데이터를 ESP32로 실시간 수집합니다. 외란광 노이즈를 차단하기 위한 하드웨어 감도 튜닝 및 소프트웨어 필터링을 적용하고, 외부 전원과의 <strong>공통 접지(Common Ground)</strong>를 결선하여 데이터 무결성을 확보했습니다.
            </p>
          </div>
        </div>

        <!-- 2. LCD를 활용한 화재 발생 위치 표시 -->
        <div class="col-lg-4 col-md-6 mb-3">
          <div class="overview-card" style="border-top: 3px solid #3b82f6;">
            <h5 style="color: #3b82f6;"><i class="fa fa-desktop mr-2"></i>02. LCD 화재 발생 위치 표시</h5>
            <p>
              <strong>I2C 1602 LCD 모듈</strong>을 통해 정상 대기 상태("ALL CLEAR")와 화재 경보 상태를 명확히 구분하여 출력합니다. 화재 감지 시 <strong>발화 구역 방 번호(예: Room 1, Room 2)</strong>를 실시간으로 표시하여 대피자와 소방 인력이 발화 위치를 즉시 파악할 수 있도록 구현했습니다.
            </p>
          </div>
        </div>

        <!-- 3. LED 대피 경로 안내 및 부저 경보 제어 -->
        <div class="col-lg-4 col-md-12 mb-3">
          <div class="overview-card" style="border-top: 3px solid #10b981;">
            <h5 style="color: #10b981;"><i class="fa fa-arrows-alt mr-2"></i>03. LED 경로 안내 및 부저 경보</h5>
            <p>
              <strong>WS2812B 주소지정형 LED 스트립</strong>으로 화재 구역은 적색으로 차단 경고하고, 안전한 비상구 방향으로 <strong>녹색 동적 파도 애니메이션</strong>을 점등합니다. 피에조 부저를 통해 서로 다른 주파수의 경보음을 순차 출력하여 시각 및 청각 경보를 극대화했습니다.
            </p>
          </div>
        </div>

        <!-- 4. 다중 구역 동시 화재 대응 -->
        <div class="col-12 mb-3">
          <div class="overview-card" style="border-left: 4px solid #f43f5e;">
            <h5 style="color: #f43f5e;"><i class="fa fa-shield mr-2"></i>04. 다중 구역 동시 화재 대응 및 복합 위험 제어</h5>
            <p>
              복수의 방에서 동시에 불꽃이 감지되는 복합 재난 상황에서도 센서 신호 누락 없이 즉시 감지하여 화재 구역 목록을 순차 갱신하고, 위험 반경을 우회하는 최적의 안전 대피 경로로 LED 점등과 경보 출력을 안정적으로 제어합니다.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- 4. 핵심 시뮬레이션 코드 -->
    <div class="premium-section animate-fade-in-up delay-500" id="section-code">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(52, 211, 153, 0.1); color: #34d399;"><i class="fa fa-code"></i></div>
        4. 화재 모니터링 시뮬레이션 (Core Code)
      </h2>
      <p class="text-muted mb-3" style="font-size: 1.05rem; line-height: 1.7;">
        <strong class="text-light">화재 감지 및 다중 출력 제어 로직:</strong> 화염 센서 실시간 폴링, 상황별 LCD 방 번호 출력, WS2812B 동적 LED 대피 경로 유도 및 다중 주파수 부저 경보를 통합 제어하는 ESP32 임베디드 펌웨어 코드입니다.
      </p>
      
      <div style="max-height: 400px; overflow-y: auto; border-radius: 8px; border: 1px solid var(--border-medium);">
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

    <!-- 5. 개발 트러블슈팅 -->
    <div class="premium-section animate-fade-in-up delay-600" id="section-troubleshoot">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(217, 70, 239, 0.1); color: #d946ef;"><i class="fa fa-wrench"></i></div>
        5. 개발 트러블슈팅 (Troubleshooting)
      </h2>
      
      <div class="row">
        <div class="col-md-6">
          <div class="ts-card">
            <div class="ts-title"><i class="fa fa-users mr-2"></i>Issue 1: 팀원과의 협업 및 역할 분담</div>
            <p class="ts-problem"><strong>과제:</strong> 4명의 팀원이 센서 입력, LED 제어, LCD 출력 및 부저 경보 기능을 나누어 개발하며 모듈 간 연동 및 시스템 통합 조율이 요구됨.</p>
            <p class="ts-solution"><strong>해결:</strong> LCD 출력 기능을 중심으로 화재 감지 정보와 경보 상태를 표시하도록 개발을 주도하고, 팀원들과 각 기능의 개발 상황 및 동작 결과를 공유하며 시스템 통합 테스트를 성공적으로 진행.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="ts-card" style="border-left-color: #38bdf8;">
            <div class="ts-title"><i class="fa fa-bolt mr-2"></i>Issue 2: 하드웨어 연결 및 시스템 통합 문제</div>
            <p class="ts-problem"><strong>문제:</strong> 개발 초기 전원 공급 문제로 ESP32가 손상되고, LED 스트립 연결 과정에서 공통 접지가 형성되지 않아 오작동과 데이터 신호 왜곡 발생.</p>
            <p class="ts-solution"><strong>해결:</strong> 전원 공급 구조를 재설계하고 ESP32와 외부 전원 장치의 GND를 공통으로 연결하여 기준점을 통일하였으며, 데이터 신호선의 배선 길이를 줄여 연결 구조 개선.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="ts-card" style="border-left-color: #eab308;">
            <div class="ts-title"><i class="fa fa-sun-o mr-2"></i>Issue 3: 불꽃 센서 오작동 문제</div>
            <p class="ts-problem"><strong>문제:</strong> 불꽃 센서가 주변 조명과 실내 온도 등 환경적 요인으로 인해 오작동하는 문제 발생.</p>
            <p class="ts-solution"><strong>해결:</strong> 센서 모듈의 감도를 환경에 맞게 조정하고 소프트웨어 필터링을 적용하여 실제 불꽃 파장에만 정확히 반응하도록 개선.</p>
          </div>
        </div>
        <div class="col-md-6">
          <div class="ts-card" style="border-left-color: #22c55e;">
            <div class="ts-title"><i class="fa fa-bell-o mr-2"></i>Issue 4: 화재 발생 정보 전달 및 사용자 편의성 개선</div>
            <p class="ts-problem"><strong>문제:</strong> 여러 방의 화재 발생 여부와 위치를 사용자가 빠르고 직관적으로 확인하기 어려운 한계.</p>
            <p class="ts-solution"><strong>해결:</strong> 여러 방의 불꽃 센서 데이터를 수집하여 감지된 방 번호를 LCD에 표시하고, 화재 감지 여부에 따라 LCD 출력 내용을 구분하며 부저에서 서로 다른 주파수의 경보음이 순차적으로 출력되도록 구성.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. 담당 역할 -->
    <div class="premium-section animate-fade-in-up delay-700" id="section-role">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(59, 130, 246, 0.1); color: #3b82f6;"><i class="fa fa-id-badge"></i></div>
        6. 담당 역할 (Role & Contribution)
      </h2>
      <p class="text-muted mb-4">본 프로젝트에서 4인 팀 협업을 통해 담당한 핵심 역할 및 기여 내용입니다.</p>

      <div class="row">
        <div class="col-md-6 mb-3">
          <div class="overview-card" style="border-left: 4px solid #3b82f6;">
            <h5 style="color: #3b82f6;"><i class="fa fa-desktop mr-2"></i>LCD 출력 기능 담당</h5>
            <p>I2C LCD 모듈 제어 및 화면 인터페이스 개발을 전담하여 평상시 상태와 비상 화재 상황별 디스플레이 표출 로직을 구현했습니다.</p>
          </div>
        </div>
        <div class="col-md-6 mb-3">
          <div class="overview-card" style="border-left: 4px solid #3b82f6;">
            <h5 style="color: #3b82f6;"><i class="fa fa-fire mr-2"></i>화재 감지 정보 표시</h5>
            <p>각 방의 센서 수집 데이터를 기반으로 화재가 감지된 방 번호 등 핵심 위치 정보를 실시간으로 LCD에 정확히 표시했습니다.</p>
          </div>
        </div>
        <div class="col-md-6 mb-3">
          <div class="overview-card" style="border-left: 4px solid #3b82f6;">
            <h5 style="color: #3b82f6;"><i class="fa fa-exclamation-triangle mr-2"></i>경보 상태 표시</h5>
            <p>화재 발생 여부에 따른 경보 상태를 구분하여 위험 단계 및 대피 안내 문구를 사용자가 직관적으로 인식할 수 있도록 구현했습니다.</p>
          </div>
        </div>
        <div class="col-md-6 mb-3">
          <div class="overview-card" style="border-left: 4px solid #3b82f6;">
            <h5 style="color: #3b82f6;"><i class="fa fa-folder-open-o mr-2"></i>프로젝트 개발 과정 및 구현 자료 관리</h5>
            <p>팀원들과 개발 진행 상황 및 테스트 결과를 공유하며 시스템 통합을 조율하고, 회로 구성 및 제어 코드 등 구현 자료를 체계적으로 문서화 및 관리했습니다.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 7. 최종 완제품 모형 및 패키징 -->
    <div class="premium-section animate-fade-in-up delay-800" id="section-hardware">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(236, 72, 153, 0.1); color: #ec4899;"><i class="fa fa-cubes"></i></div>
        7. 최종 완제품 모형 및 패키징
      </h2>
      
      <div class="row">
        <div class="col-lg-5 mb-4 text-center">
          <div class="p-3" style="background: var(--bg-terminal-header); border-radius: 16px; border: 1px solid var(--border-subtle);">
            <img src="{{ site.baseurl }}/assets/img/fire_evac_hw.png" alt="화재 대피 유도 시스템 축소 모형 완제품" class="img-fluid rounded" style="box-shadow: 0 4px 15px rgba(0,0,0,0.5); max-height: 380px; width: 100%; object-fit: contain;" />
            <p class="text-muted small mt-3 mb-0"><i class="fa fa-search-plus mr-1"></i>화재 감지 시 동적 LED 대피 경로 점등 및 LCD 상황 표시 실물 모형</p>
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

    <!-- 8. 검증 결과 및 향후 기대효과 -->
    <div class="premium-section animate-fade-in-up delay-800 mb-0" id="section-results">
      <h2 class="section-title">
        <div class="icon-box" style="background: rgba(14, 165, 233, 0.1); color: #0ea5e9;"><i class="fa fa-line-chart"></i></div>
        8. 검증 결과 및 향후 기대효과
      </h2>
      
      <div class="row mt-4">
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, var(--bg-card), var(--bg-glass)); border: 1px solid rgba(56, 189, 248, 0.2);">
            <h5 class="text-info mb-3"><i class="fa fa-check-square-o mr-2"></i>통합 시스템 연동 및 검증 완료</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2"><strong>전체 시스템 연동 구현:</strong> 불꽃 센서를 통한 화재 감지부터 ESP32의 데이터 처리, LED 대피 경로 안내, LCD 정보 출력 및 부저 경보까지 연동하여 실내 화재 대피 유도 시스템을 구현했습니다.</li>
              <li class="mb-2"><strong>다중 화재 상황 대응:</strong> 여러 방에서 동시에 화재가 발생하는 상황에서도 시스템 누락 없이 정상적으로 감지하고 신속하게 대응 가능함을 검증했습니다.</li>
              <li><strong>바닥형 시인성 확보:</strong> 상단 비상구 유도등 대비 연기 확산 시에도 가시성을 확보할 수 있는 <strong>바닥 매립형 구조의 월등한 효과</strong>를 입증했습니다.</li>
            </ul>
          </div>
        </div>
        <div class="col-md-6 mb-4">
          <div class="p-4 h-100 rounded" style="background: linear-gradient(145deg, var(--bg-card), var(--bg-glass)); border: 1px solid rgba(16, 185, 129, 0.2);">
            <h5 class="text-success mb-3"><i class="fa fa-globe mr-2"></i>스마트 빌딩 확장 플랜</h5>
            <ul class="text-muted small pl-3 mb-0" style="line-height: 2;">
              <li class="mb-2"><strong>Dijkstra 알고리즘:</strong> 복잡한 실내 구조를 위한 동적 최단 경로 그래프 알고리즘 반영 계획.</li>
              <li><strong>무선 모니터링:</strong> Wi-Fi/BLE를 연동하여 중앙 방재실 모바일 앱에 대피 경로를 실시간 전송.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Demo Video Section -->
      <div class="mt-4 p-4 rounded" style="background: var(--bg-terminal-header); border: 1px solid var(--border-subtle);">
        <h5 class="text-light mb-3"><i class="fa fa-play-circle mr-2" style="color: #f43f5e;"></i>실내 화재 대피 유도 시스템 시연 영상</h5>
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 12px; border: 1px solid var(--border-subtle); box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
          <iframe src="https://www.youtube.com/embed/t4AHV08W0AY" title="실내 화재 대피 유도 시스템 시연 영상" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
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
