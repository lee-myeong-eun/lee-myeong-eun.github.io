---
layout: default
title: BLE 기반 공사장 안전장비 실시간 감지 시스템 상세 분석
permalink: /projects/ble-safety/
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
      <span class="tech-badge">📶 Capstone Design Project</span>
      <h2 class="text-gradient">BLE 기반 공사장 안전장비 실시간 감지 시스템 (EZ-safe)</h2>
      <hr />
      <p class="lead text-light font-weight-normal">
        산업 현장의 인명 사고를 예방하기 위해 BLE RSSI 거리 인식 및 센서 데이터 판별 알고리즘을 설계하고 하드웨어 모듈을 직접 제작한 캡스톤 디자인 프로젝트 상세 분석 기록입니다.
      </p>
    </div>

    <!-- Contents Grid -->
    <div class="row mt-5 animate-fade-in-up delay-200">
      
      <!-- Left Column: Sidebar Project Metadata & TOC -->
      <div class="col-lg-4 mb-4">
        <!-- Project Info Box -->
        <div class="card border-0 shadow welcome-box p-3 mb-4" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important;">
          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-info-circle mr-2"></i>프로젝트 정보</h4>
          <ul class="list-unstyled small mb-0 text-muted" style="line-height: 2;">
            <li><strong class="text-light">팀 구성:</strong> 최성용, 구민서, 권은지, 이명은</li>
            <li><strong class="text-light">역할 (이명은):</strong> BLE 통신 알고리즘 설계 & 시스템 검증</li>
            <li><strong class="text-light">개발 기간:</strong> 3월 ~ 6월 (16주)</li>
            <li><strong class="text-light">핵심 기술:</strong> ESP32, BLE, FSR Pressure Sensor, PETG 3D Printing</li>
          </ul>
        </div>

        <!-- Sticky TOC -->
        <div class="card border-0 shadow welcome-box p-3 sticky-top" style="top: 100px; z-index: 10; background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important;">
          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-list-ul mr-2"></i>분석 목차</h4>
          <ul class="list-unstyled small mb-0 pl-1" style="line-height: 2.2;">
            <li><a href="#section1" class="text-info text-hover-glow"><i class="fa fa-flag mr-2" style="color: #38bdf8;"></i>1. 프로젝트 개요</a></li>
            <li><a href="#section2" class="text-info text-hover-glow"><i class="fa fa-sitemap mr-2" style="color: #a78bfa;"></i>2. 시스템 구조 & 알고리즘</a></li>
            <li><a href="#section3" class="text-info text-hover-glow"><i class="fa fa-code mr-2" style="color: #34d399;"></i>3. 시뮬레이션 시각화</a></li>
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
      <div class="col-lg-8 mb-4">
        <!-- Section 1 -->
        <div id="section1" class="card border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;">
          <div class="d-flex align-items-center mb-4">
            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: #38bdf8; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
              <i class="fa fa-flag"></i>
            </div>
            <div>
              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">1. 프로젝트 개요</h3>
              <span class="small text-muted">Ez-safe Capstone Design Overview</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
- **팀원**: 최성용(회로/코딩), 구민서(3D 케이스), 권은지(앱 개발/BLE), 이명은(BLE 로직/테스트)
- **개발 기간**: 3월 ~ 6월 (총 16주차)

### 1) 배경 및 필요성
- 공사 현장에서 보호구 미착용으로 인한 추락, 충격 등 인명 사고가 빈번히 발생함.
- 기존의 CCTV 모니터링이나 수동 점검 방식은 실시간 확인이 어렵고 즉각적인 대응에 한계가 있음.

### 2) 프로젝트 목표
- **ESP32**와 다양한 센서(압력, 기울기)를 결합하여 안전모 및 안전조끼의 착용 상태를 실시간 감지.
- **BLE(Bluetooth Low Energy) 통신**의 RSSI(신호 세기) 기반 거리 인식을 통해 미착용 및 이탈 시 즉각적인 경고 시스템 구현.
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
              <span class="small text-muted">EZ-safe Architecture & Flow Logic</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
본 시스템은 **송신기(작업자 장비) -> 수신기(중계기) -> 스마트폰 앱(App Inventor)** 구조로 동작합니다.

1. **RSSI 측정**: 무선 신호 세기를 기반으로 작업자가 일정 거리 이상 이탈했는지 확인합니다.
   - RSSI $\ge$ -30 dBm: 강한 신호 (가까움)
   - RSSI $\le$ -60 dBm: 약한 신호 (멀어짐 / 미착용 의심)
2. **센서 데이터 수집**: 안전모 내부의 압력 센서와 기울기 센서 값을 측정하여 실제 착용 여부 및 낙상(이상 상태)을 감지합니다.
3. **경고 출력**: 조건 만족 시 현장 부저(Buzzer) 경고음 발생 및 스마트폰 앱으로 실시간 데이터 전송.
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
              <span class="small text-muted">Python Simulated BLE Receiver Core Code</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
            <p class="small text-muted mb-3">ESP32 하드웨어 모듈로부터 전송되는 BLE 문자열 스트림 패킷을 파싱하여 실시간으로 작업자의 안전/이탈/위험 상황을 추론하고 경고 버저 출력을 결정하는 수신기 제어 핵심 파이썬 알고리즘 모형입니다.</p>
```python
import time
import pandas as pd
import random

# 1. ESP32로부터 들어오는 가상의 BLE 데이터 스트림 생성 함수
def generate_mock_ble_data():
    # 데이터 포맷: "작업자번호,RSSI,압력센서값,기울기센서값"
    # 압력 1: 착용, 0: 미착용 / 기울기 1: 정상, 0: 낙상(기울어짐)
    worker_id = random.choice([1, 2, 3])
    rssi = random.randint(-70, -25)
    pressure = random.choice([0, 1, 1, 1]) # 착용 확률 높게 설정
    tilt = random.choice([0, 1, 1, 1, 1, 1]) # 낙상 확률 낮게 설정
    
    return f"{worker_id},{rssi},{pressure},{tilt}"

# 2. 수신 데이터 파싱 및 실시간 상태 판별 함수
def parse_and_check_safety(raw_string):
    tokens = raw_string.split(',')
    worker_id = tokens[0]
    rssi = int(tokens[1])
    pressure = int(tokens[2])
    tilt = int(tokens[3])
    
    status = "정상 착용"
    alert = False
    
    # 위험 조건 검사 (로직 반영)
    if pressure == 0:
        status = "안전모 미착용!"
        alert = True
    elif rssi <= -60:
        status = "작업장 이탈 위험 (신호 약함)"
        alert = True
    elif tilt == 0:
        status =  "낙상 발생 의심!"
        alert = True
        
    return {
        "작업자 ID": worker_id,
        "RSSI (dBm)": rssi,
        "착용 여부": "착용" if pressure == 1 else "미착용",
        "자세 상태": "정상" if tilt == 1 else "기울어짐(낙상)",
        "최종 상태": status,
        "부저 알림 작동": "ON" if alert else "OFF"
    }

# 3. 5회 실시간 모니터링 시뮬레이션 작동
print("====== EZ-safe 공사장 안전장비 실시간 감지 시스템 ======")
results = []
for _ in range(5):
    raw_data = generate_mock_ble_data()
    parsed_info = parse_and_check_safety(raw_data)
    results.append(parsed_info)
    print(f"[수신 Raw 데이터]: {raw_data} -> [판단]: {parsed_info['최종 상태']} (부저: {parsed_info['부저 알림 작동']})")
    time.sleep(0.5)

# 결과를 DataFrame으로 변환하여 주피터 상에서 깔끔하게 표로 출력
df = pd.DataFrame(results)
df
```

            <!-- Output Console Box -->
            <div class="terminal-output mt-3 mb-2" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
              <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">
                <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>
                <span class="badge badge-success" style="padding: 3px 6px; font-weight: 600; border-radius: 4px;">Success</span>
              </div>
              <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: 'Fira Code', 'Courier New', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">====== EZ-safe 공사장 안전장비 실시간 감지 시스템 ======
[수신 Raw 데이터]: 2,-62,1,1 -> [판단]: 작업장 이탈 위험 (신호 약함) (부저: ON)
[수신 Raw 데이터]: 2,-69,1,1 -> [판단]: 작업장 이탈 위험 (신호 약함) (부저: ON)
[수신 Raw 데이터]: 3,-65,1,1 -> [판단]: 작업장 이탈 위험 (신호 약함) (부저: ON)
[수신 Raw 데이터]: 1,-48,1,1 -> [판단]: 정상 착용 (부저: OFF)
[수신 Raw 데이터]: 2,-53,0,0 -> [판단]: 안전모 미착용! (부저: ON)

[DataFrame 테이블 출력 결과]
작업자 ID | RSSI (dBm) | 착용 여부 | 자세 상태 | 최종 상태 | 부저 알림 작동
-------|------------|-------|-------|-------|---------
2 | -62 | 착용 | 정상 | 작업장 이탈 위험 (신호 약함) | ON
2 | -69 | 착용 | 정상 | 작업장 이탈 위험 (신호 약함) | ON
3 | -65 | 착용 | 정상 | 작업장 이탈 위험 (신호 약함) | ON
1 | -48 | 착용 | 정상 | 정상 착용 | OFF
2 | -53 | 미착용 | 기울어짐(낙상) | 안전모 미착용! | ON</pre>
            </div>
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
              <span class="small text-muted">Hardware BOM & Software Architecture</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 1) 하드웨어 구성 (HW BOM)
- **컨트롤러**: ESP32 개발 보드 (내장 BLE 모듈 활용)
- **센서류**: 압전 센서(FSR RA12P)를 통한 착용 압력 감지, 기울기 센서를 통한 낙상 감지
- **전원 및 출력**: 3.7V 리튬 배터리, TP4056 충전 모듈, MT3608 승압 컨버터, 3V 능동 부저
- **외관 케이스**: 현장 환경을 고려해 높은 강도, 내열성, 내습성, 유연성을 가진 **PETG 필라멘트**를 사용하여 3D 프린팅 설계 및 제작

### 2) 소프트웨어 및 앱 개발
- **ESP32 코딩**: 센서 입력값 판별 ➡️ 문자열 형태 변환 ➡️ BLE 통신 송출 로직 설계
- **앱 인벤터(App Inventor)**: BLE로 중계기 데이터를 받아 스플릿/파싱하여 각 작업자의 착용 상태를 UI에 실시간 시각화 구현
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
              <span class="small text-muted">EZ-safe 3D Packaging Enclosure</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
            <!-- Centered beautiful device display image -->
            <div class="text-center mb-4">
              <div class="img-wrapper d-inline-block shadow" style="border-radius: 12px; overflow: hidden; border: 2px solid rgba(56, 189, 248, 0.2); max-width: 100%;">
                <img src="{{ site.baseurl }}/assets/img/ez_safe_hw.png" alt="EZ-safe 최종 완제품" class="img-fluid" style="max-height: 450px;" />
              </div>
              <p class="text-muted small mt-2"><i class="fa fa-info-circle mr-1"></i>3D 프린팅(PETG) 케이스 제작 및 기판 회로도 전원 절연 처리 완료</p>
            </div>
실제 산업 현장에서 사용할 수 있도록 내구성과 실용성을 고려하여 하드웨어를 최종 패키징하였습니다.





### 🛠️ 하드웨어 패키징의 주요 특징
1. **현장 맞춤형 3D 케이스 설계**: 
   - 공사 현장의 거친 환경을 고려하여 내열성, 내습성, 그리고 충격 유연성이 뛰어난 **PETG 필라멘트**를 채택하여 케이스를 직접 출력 및 가공했습니다.
   - 안전모의 곡률과 구조를 반영하여 작업자의 착용감에 방해가 되지 않도록 컴팩트하게 설계했습니다.
2. **안정적인 전원 및 출력부 통합**:
   - 내부에는 3.7V 리튬 배터리와 함께 전압 강하를 방지하는 **MT3608 승압 컨버터**를 내장하여 능동 부저가 항상 일정한 광량/음량으로 경고를 보낼 수 있도록 회로를 안정화했습니다.
   - 기판 후면은 **절연 처리**를 통해 현장 조립 중 발생할 수 있는 쇼트(Short) 오작동을 원천 차단했습니다.
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
              <span class="small text-muted">Test Evaluation & Future Extensions</span>
            </div>
          </div>
          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />
          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">
### 1) 테스트 결과
- 실전 시연을 통해 짧은 반응 속도와 안정적인 작동성 검증 완료.
- 수동 점검 방식 대비 자동화 시스템 구축으로 휴먼 에러 차단 가능.
- 아두이노 및 기성 센서 기반으로 제작되어 기존 고가 시스템 대비 **저전력/저비용**으로 즉시 도입 가능함.

### 2) 향후 발전 방향
- 현재 구축된 BLE 인프라에 추가로 **GPS 및 RFID** 모듈을 연동한다면 단순 착용 감지를 넘어 **정밀 위치 기반 관제 시스템**으로 확장 가능함.
          </div>
        </div>

      </div>
    </div>
  </div>
</div>