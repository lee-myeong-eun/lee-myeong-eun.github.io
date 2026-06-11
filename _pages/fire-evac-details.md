---
layout: default
title: 실내 화재 대피 유도 시스템 상세 분석
permalink: /projects/fire-evac-safety/
---

<style>
  /* 글씨 가독성(간격) 개선을 위한 스타일 */
  .content-body {
    font-size: 1.05rem; 
    line-height: 2.2 !important; /* 줄간격을 대폭 넓혀서 답답함을 해소 */
    word-break: keep-all; 
  }
  .content-body h1, .content-body h2, .content-body h3, .content-body h4 {
    font-weight: bold;
    margin-top: 2rem; /* 소제목 위 간격을 넓혀서 문단 구분 명확히 */
    margin-bottom: 1.2rem;
    padding-bottom: 0.5rem;
    color: #e2e8f0; /* 소제목은 살짝 밝은 원래 톤으로 유지 */
  }
  .content-body ul {
    margin-bottom: 1.8rem; /* 리스트와 다음 문단 사이 간격 확보 */
  }
  .content-body ul li {
    margin-bottom: 1rem; /* 리스트 항목 간의 간격을 넓혀서 읽기 편하게 */
  }
</style>

<div class="row">
  <div class="col-md-12 mb-5">
    
    <!-- Header -->
    <div class="animate-fade-in-up delay-100">
      <span class="tech-badge">🔥 Safety IoT Project</span>
      <h2 class="text-gradient">실내 화재 대피 유도 시스템 (SIGNAL_SPEAK)</h2>
      <hr />
      <p class="lead text-light font-weight-normal">
        위급 상황 발생 시 최적의 대피 경로를 안내하여 인명 피해를 최소화하는 지능형 소방 안전 솔루션 프로젝트 상세 분석 기록입니다.
      </p>
    </div>

    <!-- Contents Grid -->
    <div class="row mt-5 animate-fade-in-up delay-200">
      
      <!-- Left Column: Sidebar Project Metadata & TOC -->
      <div class="col-lg-5 mb-4">
        <!-- Project Info Box -->
        <div class="card border-0 shadow welcome-box p-3 mb-4" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important;">
          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-info-circle mr-2"></i>프로젝트 정보</h4>
          <ul class="list-unstyled small mb-0 text-muted" style="line-height: 2;">
            <li><strong class="text-light">소속 및 팀원:</strong> 전자공학과 SIGNAL_SPEAK 팀 (최성용, 구민서, 이명은, 권은지)</li>
            <li><strong class="text-light">개발 환경:</strong> ESP32 DevKit, C/C++ (Arduino IDE), Jupyter Notebook</li>
            <li><strong class="text-light">핵심 부품:</strong> WS2812B LED 스트립, I2C 1602 LCD 모듈, 적외선 불꽃 감지 센서 등</li>
          </ul>
        </div>

        <!-- Sticky TOC -->
        <div class="card border-0 shadow welcome-box p-3 sticky-top" style="top: 100px; z-index: 10; background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important;">
          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-list-ul mr-2"></i>분석 목차</h4>
          <ul class="list-unstyled small mb-0 pl-1" style="line-height: 2.2;">
            <li><a href="#section1" class="text-info text-hover-glow"><i class="fa fa-flag mr-2" style="color: #38bdf8;"></i>1. 프로젝트 개요</a></li>
            <li><a href="#section2" class="text-info text-hover-glow"><i class="fa fa-sitemap mr-2" style="color: #a78bfa;"></i>2. 시스템 구조 & 알고리즘</a></li>
            <li><a href="#section3" class="text-info text-hover-glow"><i class="fa fa-code mr-2" style="color: #34d399;"></i>3. 실시간 모니터링 시뮬레이션</a></li>
            <li><a href="#section4" class="text-info text-hover-glow"><i class="fa fa-wrench mr-2" style="color: #fb923c;"></i>4. 세부 구현 내용</a></li>
            <li><a href="#section5" class="text-info text-hover-glow"><i class="fa fa-camera mr-2" style="color: #fb7185;"></i>5. 완제품 & 패키징</a></li>
            <li><a href="#section6" class="text-info text-hover-glow"><i class="fa fa-bar-chart mr-2" style="color: #f472b6;"></i>6. 결과 분석 & 기대효과</a></li>
          </ul>
          <hr class="my-3" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <a href="{{ site.baseurl }}/" class="btn btn-outline-light btn-sm btn-block text-hover-glow">
            <i class="fa fa-home mr-1"></i>홈으로 돌아가기
          </a>
        </div>
      </div>

      <!-- Right Column: Case Study Content -->
      <div class="col-lg-7 mb-4">
        <!-- Section 1 -->
        <div id="section1" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #38bdf8; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-flag"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">1. 프로젝트 개요</h3>
              <span class="small text-muted">Fire Evacuation System Overview</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 1.1 개발 배경 및 필요성
- **기존 비상유도등의 시인성 한계**: 화재 발생 시 발생하는 치명적인 연기는 상부로 확산되어 벽면 상단에 고정된 기존 비상유도등을 가리게 됩니다. 이로 인해 요구조자의 시야 확보가 어려워져 탈출 골든타임을 놓치는 문제가 지속적으로 발생하고 있습니다.
- **정적 안내 시스템의 위험성**: 기존 유도등은 화재 위치와 상관없이 항상 일정한 방향만 지시하므로, 오히려 화재가 발생한 위험 구역으로 대피를 유도할 수 있는 치명적인 맹점이 있습니다.
- **솔루션 제안**: 본 프로젝트는 화재를 실시간으로 감지하고 연기층 아래인 바닥 레벨에서 안전한 최단 탈출 경로를 시각적(동적 LED 파도 효과)·청각적·텍스트로 안내하는 스마트 대피 시스템을 설계 및 구현하였습니다.

### 1.2 프로젝트 최종 목표
- 화재 발생 시 즉각적으로 위험 구역과 안전 구역을 판별하여 바닥 LED 라인에 동적 애니메이션을 점등합니다.
- I2C LCD를 통해 정확한 화재 발생 방 번호를 텍스트로 표출하고 부저 경보를 동시에 발령하여 직관성을 극대화합니다.
          </div>
        </div>

        <!-- Section 2 -->
        <div id="section2" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #a78bfa; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-sitemap"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">2. 시스템 구조도 및 알고리즘</h3>
              <span class="small text-muted">System Architecture & Control Logic</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 2.1 시스템 구조도
전체 시스템은 센서 입력부 - ESP32 제어부 - 다중 출력부의 융합 구조로 설계되었으며, 저비용·단순 구성으로 높은 확장성을 가집니다.

```
[입력부: 불꽃 센서] ──(Digital Input)──> [제어부: ESP32 DevKit] ──(FastLED)──> [출력부: WS2812B LED 스트립]
                                                                ──(I2C Com.)─> [출력부: I2C LCD 16x2]
                                                                ──(PWM/Tone)─> [출력부: 피에조 부저]
```

### 2.2 메인 제어 알고리즘 흐름도
1. **평상시 (Safe Mode)**: 전체 LED 인디케이터가 초록색(Green)으로 상시 점등되며 시스템 안정 상태를 유지합니다. 
2. **화재 감지 (Fire Event)**: 특정 구역의 불꽃 센서 신호가 ESP32로 입력됩니다.  
3. **위험 구역 차단**: 화재가 발생한 인접 LED 구간을 빨간색(Red)으로 강제 전환하여 진입을 차단합니다.  
4. **동적 경로 유도**: 안전 대피로 방향을 향해 파란색(Blue) LED가 순차적으로 흐르는 '파도 효과(Wave Animation)' 알고리즘을 수행합니다.  
5. **다중 경보 발령**: LCD에 "Room 1 Fire" 실시간 텍스트를 출력하고 부저 경보음을 연속 발령합니다.
          </div>
        </div>

        <!-- Section 3 -->
        <div id="section3" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #34d399; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-code"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">3. 실시간 모니터링 시뮬레이션</h3>
              <span class="small text-muted">Core Simulation Code</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
<p class="small text-muted mb-3">화재 감지 및 동적 대피 유도를 위한 아두이노 기반 제어 코드 스니펫입니다.</p>

```cpp
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
          </div>
        </div>

        <!-- Section 4 -->
        <div id="section4" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #fb923c; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-wrench"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">4. 세부 구현 내용</h3>
              <span class="small text-muted">Implementation Details & Troubleshooting</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
1. **전원 공급 문제로 인한 MCU 손상 및 전원 분배 재설계**
   - **문제**: 프로젝트 초기 5V 전원 어댑터 전류가 ESP32(내부 로직 3.3V) 인가단 전압 변동을 일으켜 MCU 기기 2대가 손상되는 문제 발생.
   - **해결**: 외부 5V 전원을 LED 스트립에 직접 바이패스하고, ESP32의 Vin 레귤레이터 핀으로 안전하게 인가되도록 전원 분배 라인을 분리 및 재설계하여 해결함.

2. **공통 접지(Common Ground) 노이즈에 의한 LED 오작동**
   - **문제**: 테스트 중 LED 색상 데이터가 튀거나 제어되지 않는 노이즈 현상 발생.
   - **원인**: ESP32와 외부 LED 전원 공급 장치 간의 신호 기준점이 불일치하는 공통 접지 미형성 문제.
   - **해결**: 회로 상의 모든 GND 라인을 공통으로 결선(Common Ground)하여 신호 기준점을 일치시킴으로써 데이터 무결성 확보.

3. **긴 대피로 인스턴스에서의 데이터 신호 감쇠**
   - **문제**: 스트립 연장 시, 전반부 LED는 정상 작동하나 후반부 LED 라인의 데이터 왜곡 및 품질 저하 발견.
   - **해결**: 신호선 배선 길이를 최소화하고 분기점 회로를 개선하는 구조적 배선 최적화를 통해 데이터 품질 확보.

4. **외란광 노이즈로 인한 불꽃 센서 오작동 정밀 튜닝**
   - **문제**: 주변 태양광 및 실내 조명등의 적외선 파장 노이즈로 인해 화재가 없음에도 센서가 오작동함.
   - **해결**: 불꽃 센서 모듈의 가변저항을 통한 하드웨어 감도 튜닝 및 소프트웨어 필터링을 통해 확실한 화재 불꽃 파장 대역에만 반응하도록 설정
          </div>
        </div>

        <!-- Section 5 -->
        <div id="section5" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #fb7185; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-camera"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">5. 최종 완제품 및 하드웨어 패키징</h3>
              <span class="small text-muted">Final Product & Enclosure Optimization</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 5.1 하드웨어 인클로저 및 배선 최적화
- **외관 개선**: 실제 실내 환경을 축소한 80x80cm 구조물 폼보드 모델 기반으로 시스템을 일체화하였습니다. 시연 중 요구조자의 인지성을 높이기 위해 LED 흐름 애니메이션 속도를 최적 정밀 조정하였습니다.
- **패키징 수정 사항**: 축소 모형 구현 시 데이터 및 전원 배선이 외부로 노출되어 미관 저해 및 쇼트 위험이 있어, 배선이 노출되지 않도록 구조적 케이스 홀링 및 내장형 매립 케이스 구조로 하드웨어 패키징을 최종 보완하였습니다.

### 5.2 완제품 사양 및 파트리스트
- **총 소요 예산**: RISE 사업단 일반형 캡스톤디자인 과제비 지원 (총액: 171,120원)   
- **핵심 부품 내역**: ESP32 DevKit, WS2812B 고밀도 LED 스트립(1M 144LED 및 5M 스트립 교차 검증), I2C 1602 LCD 모듈, 적외선 불꽃 감지 센서 확장 모듈, 피에조 부저, DC 5V 8A 고용량 직류전원장치.
          </div>
        </div>

        <!-- Section 6 -->
        <div id="section6" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #f472b6; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-bar-chart"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">6. 결과 분석 및 기대효과</h3>
              <span class="small text-muted">Test Results & Future Work</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 6.1 프로젝트 최종 결과 분석
- 축소 구조물 모델 환경에서 화재 감지 ──> ESP32 신호 처리 ──> 동적 LED 파도 안내선 점등 ──> LCD/부저 다중 경보로 이어지는 임베디드 소방 안전 시나리오 동작에 **100% 성공**하였습니다.
- 바닥 매립형 LED 구조로 연기가 가득 찬 모의 환경에서도 상단 비상구 유도등 대비 **월등한 가시성과 최단 탈출 경로 시인성**을 확인하였습니다.

### 6.2 기대효과 및 향후 개선 과제
- **스마트 빌딩 소방 안전성 확보**: 저비용·단순 구성의 하드웨어 융합 시스템으로 실제 복잡한 복도나 다중이용시설에 도입 시 인명 피해를 획기적으로 줄일 수 있습니다.
- **향후 개선사항 (고도화 알고리즘 적용)**: 대규모 복잡 건물 구조에 대응하기 위해 고정 경로 외에 그래프 기반 최단 경로 탐색 알고리즘(Dijkstra, A* 알고리즘)을 소프트웨어에 추가 반영할 계획입니다.
- **무선 모니터링 연동**: ESP32의 내장 Wi-Fi/BLE 통신 기능을 활성화하여, 화재 발생 시 건물 중앙 방재실 모니터링 시스템 및 요구조자 모바일 앱으로 대피 경로를 실시간 원격 전송하는 통합 IoT 인프라로 고도화가 가능합니다.
          </div>
        </div>

      </div>
    </div>
  </div>
</div>
