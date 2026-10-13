# -*- coding: utf-8 -*-
"""SSEE Lab 홈페이지 생성기 — DATA 영역을 수정한 뒤 `python build.py` 실행하면 모든 html이 갱신됩니다."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
VER = '23'                       # css/js 캐시 갱신용 번호 (디자인 수정 시 올리기)

SITE_URL = ''                    # 홈페이지 주소 (예: 'https://ssee-knu.github.io') — 넣으면 sitemap.xml·robots.txt 자동 생성
GOOGLE_VERIFY = ''               # Google Search Console 'HTML 태그' 인증값 (content="..." 안의 값만)
NAVER_VERIFY = ''                # 네이버 서치어드바이저 'HTML 태그' 인증값 (content="..." 안의 값만)
EMAIL = 'suchanjun@knu.ac.kr'
SCHOLAR = 'https://scholar.google.com/citations?user=8Gv7zDMAAAAJ&hl=ko'                   # Google Scholar 주소
OFFICE_KO = '공대2A호관 206호'     # 연구실·교수실 호실
OFFICE_EN = 'Room 206, Engineering Building 2A'
HERO_IMG = 'hero.jpg'           # 첫 화면 배경 사진 (폴더에 이 이름으로 넣기, 가로 사진 권장 1920×1080)
HERO_CREDIT = ''                 # 사진 설명·출처 (예: '실대형 2층 철골모멘트골조 진동대 실험') — 비우면 표시 안 함
PHONE = '053-950-8541'           # 연구실 전화
PHONE_INTL = '+82-53-950-8541'
MAP_KO = '경북대학교 공대2A호관'   # 지도 검색어

def L(k, e):
    return f'<span class="ko">{k}</span><span class="en">{e}</span>'

def me(s):
    s = s.replace('Su-Chan Jun*', '<b>Su-Chan Jun</b>*')
    if '<b>Su-Chan Jun</b>' not in s:
        s = s.replace('Su-Chan Jun', '<b>Su-Chan Jun</b>')
    return s

# ================================================================
# DATA
# ================================================================
# SCI(E) 국제학술지 — 최신순
# role: 'lead' = 주저자(제1·교신), 'co' = 공동저자 / q, IF, jcr(백분위) 모르면 ''
INTL = [
 dict(date='2026.09.01', authors='Chang-Jun Bae, Cheol-Ho Lee, Su-Chan Jun*, Jin-Won Kim, Ki-Taek Chung',
      title='Experimental Study of Connection and Member Behaviors in a Novel Composite Beam and Column System Developed for Top-Down Construction',
      journal='Journal of Building Engineering', publisher='Elsevier', vol='131', issue='', pages='',
      doi='10.1016/j.jobe.2026.117303', idx='SCIE', q='Q1', IF='8.1', jcr='93.0', role='lead'),
 dict(date='2025.12.01', authors='Su-Chan Jun, Cheol-Ho Lee, Sung-Yong Kim*',
      title='Neural Network-based Hysteresis Modeling for Structural Steel Components',
      journal='Engineering Structures', publisher='Elsevier', vol='344', issue='', pages='121157',
      doi='10.1016/j.engstruct.2025.121157', idx='SCIE', q='Q1', IF='5.6', jcr='90.4', role='lead'),
 dict(date='2025.06.01', authors='Chang-Jun Bae, Su-Chan Jun, Cheol-Ho Lee*',
      title='Evaluation of Seismic Acceleration Amplification Factors for Building Nonstructural Components Based on Coupled Analysis of Structure–Nonstructural 2-DOF System',
      journal='Earthquake Engineering &amp; Structural Dynamics', publisher='Wiley', vol='54', issue='7', pages='1934–1951',
      doi='10.1002/eqe.4346', idx='SCIE', q='Q1', IF='4.3', jcr='86.0', role='co'),
 dict(date='2024.11.01', authors='Su-Chan Jun, Cheol-Ho Lee, Sung-Yong Kim*',
      title='Vibration Mitigation of Modular Structures Supported by Ground-Floor Piloti',
      journal='Journal of Constructional Steel Research', publisher='Elsevier', vol='222', issue='', pages='108965',
      doi='10.1016/j.jcsr.2024.108965', idx='SCIE', q='Q1', IF='4.0', jcr='82.7', role='lead'),
 dict(date='2024.10.25', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Bong-Ho Cho',
      title='Evaluation of Seismic Demand on Nonstructural Elements Based on Shake-Table Testing of Full-Scale 2-Story Steel Moment Frame',
      journal='Journal of Earthquake Engineering', publisher='Taylor &amp; Francis', vol='28', issue='14', pages='4146–4162',
      doi='10.1080/13632469.2024.2370857', idx='SCIE', q='Q2', IF='2.5', jcr='61.8', role='lead'),
 dict(date='2024.06.01', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Gi-Taek Chung',
      title='Experimental Evaluation of Negative Flexural Capacity of Composite Slabs Embedded with Truss Girders',
      journal='International Journal of Steel Structures', publisher='Korean Society of Steel Construction', vol='24', issue='', pages='644–657',
      doi='10.1007/s13296-024-00844-5', idx='SCIE', q='Q3', IF='1.1', jcr='27.7', role='lead'),
 dict(date='2023.10.15', authors='Su-Chan Jun, Dam-I Jung, Cheol-Ho Lee*, Bong-Ho Cho',
      title='Experimental and Numerical Investigation of Seismic Response of Access Floors Based on Shake-Table Tests using 2-Story Steel Moment Frame',
      journal='Journal of Building Engineering', publisher='Elsevier', vol='77', issue='', pages='107474',
      doi='10.1016/j.jobe.2023.107474', idx='SCIE', q='Q1', IF='6.7', jcr='95.3', role='lead'),
 dict(date='2022.02.01', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae',
      title='Shake Table Testing of Braced and Friction-Added Suspended Ceilings and Associated Numerical Study',
      journal='Engineering Structures', publisher='Elsevier', vol='252', issue='', pages='113724',
      doi='10.1016/j.engstruct.2021.113724', idx='SCIE', q='Q1', IF='5.5', jcr='88.55', role='lead'),
 dict(date='2022.07.04', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Kyung-Joo Lee',
      title='Shake-Table Seismic Performance Evaluation of Direct- and Indirect-Hung Suspended Ceiling Systems',
      journal='Journal of Earthquake Engineering', publisher='Taylor &amp; Francis', vol='26', issue='9', pages='4833–4851',
      doi='10.1080/13632469.2020.1845876', idx='SCIE', q='Q1', IF='2.5', jcr='61.8', role='lead'),
 dict(date='2022.03.25', authors='Cheol-Ho Lee, Ji-Hun Park*, Sung-Yong Kim, Dong-Kwan Kim, Su-Chan Jun',
      title='Structural Damage Potentials and Design Implications of 2016 Gyeongju and 2017 Pohang Earthquakes in Korea',
      journal='Earthquakes and Structures', publisher='Techno-Press', vol='22', issue='3', pages='305–318',
      doi='10.12989/eas.2022.22.3.305', idx='SCIE', q='Q3', IF='1.4', jcr='34.3', role='co'),
 dict(date='2018.10.01', authors='Su-Chan Jun, Cheol-Ho Lee*, Kyu-Hong Han, Jin-Won Kim',
      title='Flexural Behavior of High-Strength Steel Hybrid Composite Beams',
      journal='Journal of Constructional Steel Research', publisher='Elsevier', vol='149', issue='', pages='269–281',
      doi='10.1016/j.jcsr.2018.07.020', idx='SCIE', q='Q2', IF='-', jcr='75.40', role='lead'),
]
# 국내학술지 (KCI) — ko: 국문 제목(있으면)
DOM = [
 dict(date='2024.02', authors='Seung-Jun Lee, Su-Chan Jun, Cheol-Ho Lee*', ko='비선형 단자유도 모델을 활용한 마찰감쇠 천장시스템의 해석과 설계',
      title='Seismic Response Analysis and Design of Friction-Added Ceiling System Based on Simplified SDOF Model',
      journal='Journal of Korean Society of Steel Construction', vol='36', issue='1', pages='47–60', doi='10.7781/kjoss.2024.36.1.047'),
 dict(date='2022.12', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae', ko='내진천장시스템 개발을 위한 실대형 2층 철골모멘트골조 진동대 실험',
      title='Development of Seismic Ceiling System Based on Shake Table Test of Full-Scale 2-Story Steel Moment Frame',
      journal='Journal of Korean Society of Steel Construction', vol='34', issue='6', pages='341–352', doi='10.7781/kjoss.2022.34.6.341'),
 dict(date='2022.05', authors='Chang-Jun Bae, Cheol-Ho Lee*, Su-Chan Jun', ko='구조물–비구조요소 2자유도 결합시스템 해석을 통한 비구조요소 내진설계변수 평가',
      title='Evaluation of Seismic Design Parameters for Nonstructural Components Based on Coupled Structure–Nonstructural 2-DOF System Analysis',
      journal='Journal of the Earthquake Engineering Society of Korea', vol='26', issue='3', pages='105–116', doi='10.5000/EESK.2022.26.3.105'),
 dict(date='2021', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae', ko='진동대 실험을 통한 내진 및 비내진 천장시스템의 동적거동 분석',
      title='Analysis of Dynamic Behavior of Seismic and Non-Seismic Suspended Ceiling Systems Based on Shake-Table Testing',
      journal='Journal of Korean Society of Steel Construction', vol='33', issue='2', pages='63–74', doi=''),
 dict(date='2020', authors='Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae', ko='비구조요소의 내진설계를 위한 등가정적 층가속도 평가',
      title='Evaluation of Equivalent-Static Floor Acceleration for Seismic Design of Non-Structural Elements',
      journal='Journal of the Architectural Institute of Korea Structure &amp; Construction', vol='36', issue='3', pages='121–128', doi=''),
 dict(date='2019', authors='Kyu-Hong Han, Jin-Won Kim, Su-Chan Jun, Cheol-Ho Lee*', ko='비대칭 하이브리드 합성보-기둥 접합부 개발 및 내진성능평가',
      title='Development and Seismic Performance Testing of Asymmetric Hybrid Composite Beam-to-Column Connections',
      journal='Journal of Korean Society of Steel Construction', vol='31', issue='1', pages='53–63', doi=''),
 dict(date='2017', authors='Su-Chan Jun, Kyu-Hong Han, Cheol-Ho Lee*, Jin-Won Kim', ko='고강도강재를 적용한 비대칭 하이브리드 합성보의 휨거동 실험',
      title='Flexural Testing of Asymmetric Hybrid Composite Beams Fabricated from High-Strength Steels',
      journal='Journal of Korean Society of Steel Construction', vol='29', issue='3', pages='217–228', doi=''),
]
# 국제학술대회 (year, authors, title, conference, place[, 'upcoming'])
#  — 발표 예정이면 마지막에 'upcoming'을 붙이세요. 발표가 끝나면 지우면 됩니다.
CONF = [
 ('2026.12', 'Chang-Jun Bae, Su-Chan Jun*, Cheol-Ho Lee', 'Seismic and Gravity-Load Performance of Novel Beam-to-Column Assemblies for Top-Down Construction', '27th Japan-Korea-Taiwan Joint Seminar on Earthquake Engineering for Building Structures (SEEBUS)', 'Tainan, Taiwan, Dec. 18–19, 2026', 'upcoming'),
 ('2025', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Jin-Won Kim, Gi-Taek Chung', 'Cyclic Performance of Slim-Floor Composite Beam-Column Connections for Top-Down Construction', '13th Int. Symposium on Steel Structures &amp; 14th Pacific Steel Structures Conference', 'Jeju, Korea'),
 ('2024', 'Su-Chan Jun, Cheol-Ho Lee*, Dam-I Chung, Bong-Ho Cho', 'Experimental and Numerical Study on Seismic Response of Access Floors Based on Shake-Table Tests', '18th World Conference on Earthquake Engineering', 'Milan, Italy'),
 ('2023', 'Su-Chan Jun, Cheol-Ho Lee**, Bong-Ho Cho', 'Experimental and Numerical Seismic Performance Evaluation of Access Floors Based on Shake-Table Testing', '23rd SEEBUS', 'Taipei, Taiwan'),
 ('2023', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Bong-Ho Cho', 'Assessment of Nonstructural Seismic Demands via Full-Scale Shake Table Testing on 2-Story Steel Frame and Associated Numerical Study', '12th Int. Symposium on Steel Structures', 'Jeju, Korea'),
 ('2023', 'Su-Chan Jun, Cheol-Ho Lee*', 'Shake-Table Seismic Performance Evaluation of Braced and Friction-Added Suspended Ceiling Systems', '8th Structural Engineers World Congress', 'Seoul, Korea'),
 ('2023', 'Chang-Jun Bae, Cheol-Ho Lee*, Su-Chan Jun', 'Horizontal Acceleration of Floor-Mounted Nonstructural Components under Rocking Motion', 'Int. Structural Engineering and Construction, 9(1)', 'Chicago, US'),
 ('2022', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Dong-Seob Lee', 'Seismic Performance Evaluation of Braced and Friction-Added Suspended Ceilings Based on Shake Table Testings', '5th Int. Workshop on Seismic Performance of Non-Structural Elements, Stanford University', 'CA, US'),
 ('2022', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Bong-Ho Cho', 'Evaluation of Nonstructural Seismic Demand Based on Shake-Table Testing of Steel Racks Installed on Full-Scale 2-Story Moment Frame', '8th Asia Conference on Earthquake Engineering', 'Taipei, Taiwan'),
 ('2021', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae', 'Shake-Table Testing of Suspended Ceiling Systems with Various Configurations', '11th Int. Symposium on Steel Structures', 'Jeju, Korea'),
 ('2021', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae', 'Shake Table Testing of Braced and Friction-Added Suspended Ceiling Systems', '22nd SEEBUS', 'Seoul, Korea'),
 ('2020', 'Su-Chan Jun, Cheol-Ho Lee*, Chang-Jun Bae, Sung-Yong Kim, Kyung-Joo Lee', 'Seismic Performance Evaluation of Large-Size Suspended Ceiling Using an Array of Shake Tables', '17th World Conference on Earthquake Engineering', 'Sendai, Japan'),
 ('2019', 'Su-Chan Jun, Cheol-Ho Lee*, Sung-Yong Kim, Seung-Ho Lee', 'Evaluation of Equivalent Static and Dynamic Analysis Method for Seismic Design of Non-Structural Elements', '10th Int. Symposium on Steel Structures', 'Jeju, Korea'),
 ('2019', 'Su-Chan Jun, Cheol-Ho Lee*, Seung-Ho Lee, Sung-Yong Kim, Ji-Hun Park', 'Evaluation of Equivalent Static and Dynamic Analysis Method for Seismic Design of Non-Structural Elements', 'Int. Conference in Commemoration of the 20th Anniversary of the 1999 Chi-Chi Earthquake', 'Taipei, Taiwan'),
 ('2019', 'Su-Chan Jun, Cheol-Ho Lee*, Sung-Yong Kim, Ji-Hun Park', 'Evaluation of Equivalent Static Analysis Method for Seismic Design of Non-Structural Elements', '4th Int. Workshop on Seismic Performance of Non-Structural Elements', 'Pavia, Italy'),
 ('2018', 'Su-Chan Jun, Cheol-Ho Lee*, Kyu-Hong Han, Jin-Won Kim', 'Flexural Behavior of High-Strength Steel Asymmetric Hybrid Composite Beams', '1st Workshop of High-Performance Steel Structures Research Council, TU Delft', 'Delft, The Netherlands'),
 ('2017', 'Su-Chan Jun, Kyu-Hong Han, Cheol-Ho Lee*, Jin-Won Kim', 'Flexural Testing of Asymmetric Hybrid Composite Beams Fabricated from High-Strength Steel', '9th Int. Symposium on Steel Structures', 'Jeju, Korea'),
]
# 특허 (등록일, 국문 명칭, 영문 명칭, 등록번호)
PATENTS = [
 ('2024.07', '강판전단벽 코어 시스템 및 모듈러 시스템을 포함하는 건축 구조물', 'Building Structure Comprising Steel Shear Wall Core System and Modular System', '10-2805411'),
 ('2023.10', '면내강성 보강재를 활용한 대공간 천장의 가새시스템', 'Integrated Ceiling Brace System using In-plane Stiffness Reinforcement Members', '10-2587786'),
 ('2023.08', '천장시스템의 내진성능 향상을 위한 마찰감쇠 장치', 'Friction Damping Device to Improve Seismic Performance of Ceiling System', '10-2564927'),
]
BOOKS = [
 ('2022', '비구조요소의 내진설계를 위한 표준상세 지침', '구미서관 · 참여연구원'),
 ('2022', '내진공사 시방서에 따른 비구조요소 표준내진상세', '구미서관 · 참여연구원'),
 ('2022', '비구조요소 내진성능평가 지침', '구미서관 · 참여연구원'),
 ('2022', '건축물 비구조요소의 내진보강 가이드', '구미서관 · 참여연구원'),
]
# 연구과제 (기간, 과제명(영문), 발주·지원(영문), 'PI'면 연구책임자 / 나머지는 Co-Investigator[, 과제명(국문), 발주·지원(국문)])
#  — 국문을 넣으면 한국어 화면에서는 국문, 영어 화면에서는 영문이 보입니다. 없으면 영문만 표시.
PROJECTS = [
 ('2025.03 – 2026.03', 'Expanding steel utilization in the Indonesian construction industry: challenges and practical solutions', 'Indonesian Society of Steel Structures', ''),
 ('2024.08 – 2026.08', 'Development of H-column modular joints', 'Hyundai Engineering', ''),
 ('2024.09 – 2025.09', 'Modularized steel plate shear wall core system for mid-to-high-rise residential modular structures', 'Hyundai Steel', ''),
 ('2024.04 – 2025.04', 'Structural design &amp; performance evaluation guidelines for steel deck systems', 'Korean Society of Steel Construction', ''),
 ('2024.02 – 2025.01', 'Structural performance evaluation of high-load unidirectional composite beam joints', 'POSCO', ''),
 ('2023.12 – 2024.06', 'Development of top-down columns using H-beams', 'Hyundai Steel', ''),
 ('2023.12 – 2024.03', 'Safety inspection manual for structural stability of industrial pipe rack structures', 'KNU Industry-Academic Cooperation Foundation', ''),
 ('2023.09 – 2023.10', 'Safety inspection manual for structural stability of industrial pipe rack structures', 'Chosun Univ. Industry-Academic Cooperation Foundation', ''),
 ('2023.08 – 2024.01', 'Structural performance evaluation of deep-deck floor system under construction load', 'Shinhan S&amp;G', ''),
 ('2023.06 – 2026.05', 'Nonlinear dynamic characteristics and vibration control methods for nonstructural elements', 'National Research Foundation of Korea', 'PI',
  '비구조요소의 비선형 거동특성을 고려한 설계계수 제안 및 제진시스템 개발', '한국연구재단 (창의·도전연구기반지원사업)'),
 ('2023.05 – 2024.04', 'Steel plate shear wall system for mid-to-high-rise modular residential buildings', 'Hyundai Steel', ''),
 ('2022.10 – 2023.03', 'Evaluation of flexural behavior of slim-floor composite beams', 'Shinhan S&amp;G', ''),
 ('2021.03 – 2024.02', 'Seismic design of floor-mounted nonstructural elements based on experimental and analytical study', 'National Research Foundation of Korea', ''),
 ('2020.05 – 2020.12', 'Collaborative round-robin analysis on vibration characteristics of shear wall structures', 'Korea Atomic Energy Research Institute', ''),
 ('2018.04 – 2021.12', 'Seismic performance enhancement methods for nonstructural elements in buildings', 'Ministry of Land, Infrastructure and Transport', ''),
 ('2018.04 – 2018.09', 'Seismic design methods for 5G telecommunication racks', 'SK Telecom', ''),
 ('2017.03 – 2018.02', 'Development of a long-span shear link truss frame', 'POSCO', ''),
 ('2017.02 – 2017.12', 'Seismic design details for steel plant factories', 'POSCO E&amp;C', ''),
 ('2015.06 – 2016.02', 'Development of hybrid composite beams using high-strength steels', 'POSCO', ''),
]
# 소식 (최신순, 홈에는 앞의 4개)
NEWS = [
 ('2026.12', '제27회 SEEBUS (대만 타이난, 12.18–19) 탑다운 보-기둥 접합부 발표 예정', 'Upcoming: top-down beam-to-column study at the 27th SEEBUS, Tainan (Dec. 18–19)'),
 ('2026.09.08', '탑다운 합성 기둥-보 시스템 논문 <i>Journal of Building Engineering</i> 게재 (IF 8.1, JCR 상위 7%)', 'Top-down composite beam–column paper published in <i>Journal of Building Engineering</i> (IF 8.1)'),
]
AREAS = [
 dict(slug='steel', img='img/research-steel.jpg', cap_ko='합성 보-기둥 접합부 반복가력 실험', cap_en='Cyclic test of a composite beam–column joint', figs=[('img/fig-steel-1.jpg', 'H-브라켓·U형 단면 변형률 이력 비교', 'Strain histories: H-bracket vs. U-shaped section'), ('img/fig-steel-2.jpg', '대형 골조 반복가력 실험', 'Large-scale frame cyclic test', 'photo'), ('img/fig-steel-3.jpg', '볼트 보 이음부 휨 실험', 'Flexural test of a bolted beam splice', 'photo'), ('img/fig-steel-4.jpg', '볼트 보 이음부 실험–유한요소해석 비교', 'Bolted beam splice: test vs. FE analysis')], tag='Steel &amp; Composite', ko='강·합성구조', en='Steel &amp; Composite Structures',
  dk='건축물의 고층화·장스팬화와 공기 단축 요구에 따라, 강재와 콘크리트의 장점을 결합한 합성구조의 적용이 확대되고 있습니다. 새로운 강·합성 부재와 접합부의 거동을 실험과 해석으로 규명하고, 이를 설계식으로 정립하여 신기술이 현장에 적용될 수 있는 기반을 마련합니다.',
  de='As buildings grow taller and longer-spanning under tighter construction schedules, composite systems combining steel and concrete are increasingly adopted. We characterize the behavior of new steel and composite members and connections through testing and analysis, and establish design equations that bring these technologies into practice.',
  kw=['하이브리드 합성보', '슬림플로어', '딥데크·트러스거더', '탑다운 공법'], kwe=['Hybrid composite beams', 'Slim-floor', 'Deep deck &amp; truss girders', 'Top-down construction'],
  out=['J. Building Eng. 2026 · top-down composite beam–column system', 'Int. J. Steel Structures 2024 · truss-girder composite slabs', 'J. Constr. Steel Res. 2018 · HSS hybrid composite beams'],
  icon='<path d="M6 10h36M6 38h36M22 10v28M26 10v28"/><path d="M6 24h14M28 24h14" stroke-dasharray="2 3"/>'),
 dict(slug='modular', img='img/research-modular.jpg', cap_ko='모듈러 골조 실대형 실험', cap_en='Full-scale modular frame test', figs=[('img/fig-modular-1.jpg', '모듈러 접합부 유한요소해석 응력 분포', 'FE analysis of a modular joint: von Mises stress'), ('img/fig-modular-2.jpg', '모듈러 골조 접합 시스템', 'A novel connection detail for moudlar structures'), ('img/fig-modular-3.jpg', '건물 바닥 진동 모드 해석', 'Floor vibration mode analysis')], tag='Modular', ko='모듈러 구조', en='Modular Structures',
  dk='모듈러 건축은 공장 제작을 통해 품질 확보와 공기 단축이 가능한 차세대 건축 방식입니다. 모듈 간 접합부와 횡력저항시스템은 모듈러 건축물의 구조 안전성을 좌우하는 핵심 요소로, 연구실은 모듈 단위로 조립된 구조물이 하나의 건축물로서 일체 거동하도록 접합 상세와 시스템 설계 방법을 개발하고 있습니다.',
  de='Modular construction is a next-generation building method that ensures quality and shortens construction time through factory fabrication. Inter-module connections and lateral force-resisting systems govern the structural safety of modular buildings, and we develop connection details and system design methods that ensure modular assemblies perform as a unified structure.',
  kw=['강판전단벽 코어', 'H형강 모듈러 접합부', '필로티 진동 저감'], kwe=['SPSW cores', 'H-column modular joints', 'Piloti vibration mitigation'],
  out=['J. Constr. Steel Res. 2024 · piloti-supported modular structures', 'Patent KR 10-2805411 · SPSW core + modular system'],
  icon='<rect x="8" y="8" width="14" height="14"/><rect x="26" y="8" width="14" height="14"/><rect x="8" y="26" width="14" height="14"/><rect x="26" y="26" width="14" height="14"/>'),
 dict(slug='seismic', img='img/research-seismic.jpg', cap_ko='실대형 2층 철골모멘트골조 진동대 실험', cap_en='Full-scale two-story steel moment frame on the shake table', figs=[('img/fig-seismic-1.jpg', '지반–구조물–비구조요소 지진 증폭 개념', 'Seismic amplification from ground to nonstructural component'), ('img/fig-seismic-2.jpg', '대공간 천장시스템 진동대 실험', 'Large-scale shake-table tests of suspended ceiling system'), ('img/fig-seismic-3.jpg', '천장시스템 보강을 위한 회전형 마찰댐퍼', 'Rotational friction damper for suspended ceiling systems')], tag='Nonstructural', ko='비구조요소 내진·진동제어', en='Nonstructural Seismic &amp; Vibration Control',
  dk='지진 피해의 상당 부분은 천장, 설비, 칸막이 등 비구조요소에서 발생하며, 이는 건축물의 기능을 저하시키는 주요 원인입니다. 구조물 내부에서 비구조요소가 받는 지진하중을 규명하고, 이를 설계에 합리적으로 반영하여 지진 후에도 기능이 유지되는 건축물을 구현하고자 합니다.',
  de='A large share of earthquake damage occurs in nonstructural elements such as ceilings, equipment, and partitions, often delaying the recovery of building function. We quantify the seismic demands these elements experience within structures and translate them into rational design provisions, aiming for buildings that remain functional after earthquakes.',
  kw=['진동대 실험', '천장 시스템', '액세스플로어', '가속도 증폭계수'], kwe=['Shake-table tests', 'Suspended ceilings', 'Access floors', 'Amplification factors'],
  out=['Engineering Structures 2022 · braced &amp; friction-added ceilings', 'J. Building Eng. 2023 · access floors', 'J. Earthquake Eng. 2022, 2024 · ceilings, nonstructural demand', 'Earthquake Eng. Struct. Dyn. 2025 · 2-DOF amplification', 'NRF (PI) 2023–2026 · vibration control of nonstructural elements'],
  icon='<path d="M6 12h36"/><path d="M12 12v6M24 12v6M36 12v6"/><path d="M8 18h32v5H8z"/><path d="M4 40c4-4 6 4 10 0s6 4 10 0 6 4 10 0 6 4 10 0"/>'),
 dict(slug='ai', img='img/research-ai.jpg', cap_ko='신경망 이력모델 예측 결과 (학습·검증 데이터)', cap_en='Neural-network hysteresis prediction against training and test data', img_kind='fig', figs=[('img/fig-ai-1.jpg', '이력 데이터 확보를 위한 부재 반복가력 실험', 'Cyclic member test for hysteresis data')], tag='AI', ko='AI 기반 구조 모델링', en='AI for Structural Modeling',
  dk='구조시스템의 비선형 이력거동을 정밀하게 예측하려면 많은 시간과 비용이 드는 실험이나 고해상도 해석이 필요합니다. AI는 축적된 데이터로부터 복잡한 거동을 빠르고 정확하게 예측할 수 있는 새로운 도구로 주목받고 있으며, 연구실은 실험·해석 데이터를 기반으로 구조물의 주요 거동을 안정적으로 재현하는 데이터 기반 모델을 개발하고 있습니다.',
  de='Accurately predicting the nonlinear hysteretic behavior of structural systems typically requires costly experiments or high-fidelity simulations. AI has emerged as a powerful tool for rapidly and accurately predicting complex behavior from accumulated data, and we develop data-driven models trained on test and analysis data to robustly reproduce hysteretic response.',
  kw=['이력거동 대리모델', '반복하중 응답 예측', '데이터 기반 설계'], kwe=['Hysteresis surrogates', 'Cyclic response prediction', 'Data-driven design'],
  out=['Engineering Structures 2025 · NN-based hysteresis modeling'],
  icon='<circle cx="10" cy="14" r="3"/><circle cx="10" cy="34" r="3"/><circle cx="24" cy="10" r="3"/><circle cx="24" cy="24" r="3"/><circle cx="24" cy="38" r="3"/><circle cx="38" cy="24" r="3"/><path d="M13 14l8-4M13 14l8 10M13 34l8-10M13 34l8 4M27 10l8 14M27 24h8M27 38l8-14"/>'),
]
EDU = [
 ('2022.08', 'Ph.D.', '서울대학교 건축학과', 'Seoul National University, Dept. of Architecture &amp; Architectural Engineering',
  'A Study of Seismic Performance Evaluation and Design of Suspended Ceiling Systems Based on Shake-Table Tests'),
 ('2018.02', 'M.S.', '서울대학교 건축학과', 'Seoul National University, Dept. of Architecture &amp; Architectural Engineering',
  'Flexural Testing of Asymmetric Hybrid Composite Beams Fabricated from High-Strength Steels'),
 ('2016.02', 'B.S.', '고려대학교 건축사회환경공학부', 'Korea University, School of Civil, Environmental &amp; Architectural Engineering', ''),
]
EXP = [  # (기간, 국문, 영문) — 최신순
 ('2026.09 –', '경북대학교 건축공학과 조교수', 'Assistant Professor, Dept. of Architectural Engineering, Kyungpook National University'),
 ('2025.09 – 2026.08', '단국대학교 산학협력단 박사후연구원', 'Postdoctoral Researcher, Dankook University'),
 ('2025.03 – 2026.02', '경희대학교 건축공학과 객원교수', 'Visiting Professor, Dept. of Architectural Engineering, Kyung Hee University'),
 ('2024.09 – 2026.02', '단국대학교 건축학부 강사', 'Lecturer, School of Architecture, Dankook University'),
 ('2024.03 – 2024.06', '서울시립대학교 건축학부 강사', 'Lecturer, School of Architecture, University of Seoul'),
 ('2023.09 – 2025.12', '서울대학교 건축학과 강사', 'Lecturer, Dept. of Architecture &amp; Architectural Engineering, Seoul National University'),
 ('2023.09 – 2024.08', '아주대학교 건축학과 객원조교수', 'Visiting Assistant Professor, Dept. of Architecture, Ajou University'),
 ('2022.09 – 2025.08', '서울대학교 건축학과 박사후연구원 (BK21)', 'Postdoctoral Researcher (BK21), Seoul National University'),
 ('2022.09 – 2023.08', '원광대학교 건축공학과 강사', 'Lecturer, Dept. of Architectural Engineering, Wonkwang University'),
]
# 구성원 — (구분, 이름 국문, 이름 영문, 시작일, 이메일, 사진 경로)
#  구분: 'phd' = 박사과정, 'ms' = 석사과정, 'ug' = 학부연구생  (인원이 없는 구분은 자동으로 숨김)
#  이메일·사진이 없으면 '' — 이메일은 비우면 표시 안 함, 사진은 비우면 이름 첫 글자로 표시
#  사진은 img/members 폴더에 넣기 (증명사진 비율 3:4 권장)
STUDENTS = [
 ('ug', '김지윤', 'Ji-Yoon Kim', '26.09.22', 'rlawldbs0215@naver.com', ''),
 ('ug', '이혜성', 'Hye-Sung Lee', '26.09.28', 'hsl091112@naver.com', 'img/members/lee-hyesung.jpg'),
]

# ================================================================
# TEMPLATE
# ================================================================
N_PROJ = len(PROJECTS)
N_CONF = sum(1 for c in CONF if len(c) < 6 or c[5] != 'upcoming')   # 발표 예정 제외
CUR = ' aria-current="page"'
MARK = '<img class="mark" src="knu-mark.png" alt="" width="40" height="40">'   # 경북대학교 마크
CARET = '<svg class="caret" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'

NAV = [('about', 'About', None), ('people', 'People', [('professor', 'Professor'), ('students', 'Members')]),
       ('publications', 'Publications', None), ('projects', 'Projects', None), ('news', 'News', None), ('contact', 'Contact', None)]

def header(active):
    items = ''
    for key, label, sub in NAV:
        if sub:
            on = active in [s for s, _ in sub]
            cur = ' class="is-cur"' if on else ''
            subs = ''.join(f'<li><a href="{s}.html"{CUR if s == active else ""}>{t}</a></li>' for s, t in sub)
            items += (f'\n        <li class="has-sub"><a href="{sub[0][0]}.html"{cur}>{label}{CARET}</a>'
                      f'<ul class="sub">{subs}</ul></li>')
        else:
            items += f'\n        <li><a href="{key}.html"{CUR if key == active else ""}>{label}</a></li>'
    return f'''<header class="top">
  <div class="wrap bar">
    <a class="brand" href="index.html">{MARK}<span class="brand-t"><b>SSEE Lab</b><small>{L('경북대학교 강구조내진공학 연구실', 'Kyungpook National University')}</small></span></a>
    <nav aria-label="Main"><ul id="menu">{items}
      </ul></nav>
    <div class="tools">
      <button id="langBtn" type="button" aria-label="Switch language">EN</button>
      <button id="themeBtn" type="button" aria-label="Toggle dark mode"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></button>
      <button id="menuBtn" class="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h16" stroke="currentColor" stroke-width="1.6"/></svg></button>
    </div>
  </div>
</header>'''

FOOT_LINKS = ''.join(f'<a href="{k}.html">{t}</a>' for k, t in
                     [('about', 'About'), ('professor', 'Professor'), ('students', 'Members'), ('publications', 'Publications'), ('projects', 'Projects'), ('news', 'News'), ('contact', 'Contact')])
FOOTER = f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <a class="brand" href="index.html">{MARK}<span class="brand-t"><b>SSEE Lab</b><small>Steel Structures &amp; Earthquake Engineering Lab</small></span></a>
      <p class="foot-addr">{L('41566 대구광역시 북구 대학로 80<br>경북대학교 공과대학 건축공학과', 'Dept. of Architectural Engineering, Kyungpook National University<br>80 Daehak-ro, Buk-gu, Daegu 41566, Korea')}</p>
    </div>
    <div class="foot-col"><span class="lbl">Contact</span><span class="sel">{EMAIL}</span><span>{PHONE}</span><a href="contact.html">{L('찾아오는 길', 'Directions')} →</a></div>
    <div class="foot-col foot-links"><span class="lbl">Pages</span>{FOOT_LINKS}</div>
  </div>
  <div class="wrap foot-base"><span>© <span id="yr">2026</span> SSEE Lab · Kyungpook National University</span></div>
</footer>'''

VERIFY = ((f'<meta name="google-site-verification" content="{GOOGLE_VERIFY}">\n' if GOOGLE_VERIFY else '')
          + (f'<meta name="naver-site-verification" content="{NAVER_VERIFY}">' if NAVER_VERIFY else ''))

def page(slug, title, body):
    return f'''<!DOCTYPE html>
<html lang="ko" data-lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="경북대학교 건축공학과 강구조내진공학 연구실 (SSEE Lab, Steel Structures &amp; Earthquake Engineering Lab) — 전수찬 교수 연구실. 강·합성구조, 모듈러 구조, 비구조요소 내진, AI 기반 구조 모델링">
<meta name="keywords" content="경북대학교, 경북대, 강구조내진공학 연구실, 강구조, 내진, 전수찬, SSEE Lab, Kyungpook National University, steel structures, earthquake engineering">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="경북대학교 건축공학과 강구조내진공학 연구실 (SSEE Lab)">
<meta property="og:image" content="{SITE_URL}/knu-mark.png">
{VERIFY}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Noto+Serif+KR:wght@500;600;700&display=swap">
<link rel="stylesheet" href="style.css?v={VER}">
<script>try{{var q=new URLSearchParams(location.search).get('lang'),l=q||localStorage.getItem('lang');if(l==='en'||l==='ko'){{document.documentElement.dataset.lang=l;document.documentElement.lang=l}}var t=localStorage.getItem('theme');if(t==='dark')document.documentElement.dataset.theme='dark'}}catch(e){{}}</script>
</head>
<body>
{header(slug)}
<main>
{body}
</main>
{FOOTER}
<script src="main.js?v={VER}"></script>
</body>
</html>
'''

def phead(eyebrow, k, e, lk='', le=''):
    """페이지 제목 — 영문만 표시. eyebrow가 'People · Professor'처럼 상위 메뉴를 가지면 그 이름만 작게 표시."""
    crumb = f'\n    <p class="eyebrow">{eyebrow.split(" · ")[0]}</p>' if ' · ' in eyebrow else ''
    lead = f'\n    <p class="lead">{L(lk, le)}</p>' if lk else ''
    return f'''<section class="phead">
  <div class="wrap">{crumb}
    <h1>{e}</h1>{lead}
  </div>
</section>'''

def doi_link(d):
    return f'<a class="doi" href="https://doi.org/{d}" target="_blank" rel="noopener">DOI {d} ↗</a>' if d else ''

def src(p):
    s = f'<i>{p["journal"]}</i>'
    if p.get('vol'):
        s += f', {p["vol"]}'
        if p.get('issue'):
            s += f'({p["issue"]})'
    if p.get('pages'):
        s += f', {p["pages"]}'
    return s

def intl_item(p, compact=False):
    tags = [f'<span class="tag tag-idx">{p["idx"]}</span>']
    if p['q']:
        tags.append(f'<span class="tag tag-q">{p["q"]}</span>')
    if p['IF'] and p['IF'] != '-':
        tags.append(f'<span class="tag">IF {p["IF"]}</span>')
    if p['jcr'] and not compact:
        top = 100 - float(p['jcr'])
        tags.append(f'<span class="tag">{L(f"JCR 상위 {top:.1f}%", "JCR " + p["jcr"] + " %ile")}</span>')
    if not compact:
        tags.append(f'<span class="tag tag-role">{L("주저자", "Lead author") if p["role"] == "lead" else L("공동저자", "Co-author")}</span>')
    pub = f' · {p["publisher"]}' if p.get('publisher') and not compact else ''
    doi = '' if compact else doi_link(p['doi'])
    return (f'<li><span class="yr">{p["date"]}</span><div>'
            f'<p class="pt">{p["title"]}</p>'
            f'<p class="pa">{me(p["authors"])}</p>'
            f'<p class="pv">{src(p)}{pub}</p>'
            f'<div class="tags">{"".join(tags)}{doi}</div></div></li>')

def dom_item(p):
    t = L(p['ko'], p['title']) if p['ko'] else p['title']
    sub = f'<p class="pv en-alt ko">{p["title"]}</p>' if p['ko'] else ''
    doi = doi_link(p['doi'])
    return (f'<li><span class="yr">{p["date"]}</span><div><p class="pt">{t}</p>{sub}'
            f'<p class="pa">{me(p["authors"])}</p><p class="pv">{src(p)}</p>'
            f'{wrap_tags(doi)}</div></li>')

def wrap_tags(inner):
    return f'<div class="tags">{inner}</div>' if inner else ''

def news_list(items):
    return '<ul class="news">' + ''.join(f'<li><time>{d}</time><p>{L(k, e)}</p></li>' for d, k, e in items) + '</ul>'

# ---------------- HOME ----------------
area_cards = ''.join(f'''
      <a class="acard" href="about.html#{a['slug']}">
        <svg class="aicon" viewBox="0 0 48 48" aria-hidden="true">{a['icon']}</svg>
        <span class="atag">{a['tag']}</span>
        <h3>{L(a['ko'], a['en'])}</h3>
        <p>{L(a['dk'], a['de'])}</p>
        <span class="alink">{L('자세히', 'Learn more')} <span aria-hidden="true">→</span></span>
      </a>''' for a in AREAS)

CREDIT = f'<p class="hero-credit">{HERO_CREDIT}</p>' if HERO_CREDIT else ''
home = f'''<section class="hero-photo" style="--hero-img:url('{HERO_IMG}')">
  <div class="wrap hero-photo-in">
    <p class="eyebrow">Kyungpook National University</p>
    <h1 class="lab-name">Steel Structures &amp;<br>Earthquake Engineering Lab</h1>
    <p class="lab-name-ko">강구조내진공학 연구실 <span>SSEE Lab</span></p>
    <p class="hero-sub">{L('경북대학교 강구조내진공학 연구실(SSEE Lab)은 새로운 강구조 부재·접합부·시스템을 개발하고, 건축물의 내진 성능 향상에 주력합니다. 실험으로 실제 거동을 규명하고, 해석으로 검증 범위를 확장하며, 축적된 데이터를 바탕으로 설계에 활용 가능한 예측 모델을 구축합니다. 이를 통해 안전하고 지속 가능한 건축 환경을 만드는 연구를 수행하고 있습니다.',
                           'The Steel Structures &amp; Earthquake Engineering Lab (SSEE Lab) at Kyungpook National University develops innovative steel members, connections, and structural systems, with a focus on enhancing the seismic performance of buildings. We investigate structural behavior through experimental testing, extend validation through numerical analysis, and build predictive models from accumulated data for practical design use. Through this work, we pursue research toward safe and sustainable built environments.')}</p>
    <div class="cta">
      <a class="btn btn-light" href="about.html">{L('연구실 소개', 'About the lab')}</a>
      <a class="btn btn-outline-light" href="publications.html">{L('연구성과', 'Publications')}</a>
    </div>
  </div>
  {CREDIT}
</section>

<section class="sec">
  <div class="wrap narrow">
    <div class="sec-h"><h2>News</h2><a class="more" href="news.html">{L('전체', 'All')} →</a></div>
    {news_list(NEWS[:4])}
  </div>
</section>'''

# ---------------- ABOUT ----------------
def rfig(a):
    # 연구 분야 사진 갤러리 — img(대표 사진) + figs(추가 그림, 선택)
    # figs=[('img/파일.jpg', '한글 설명', 'English caption'), ...]  적은 순서대로 썸네일에 표시
    # 실험 사진처럼 꽉 채워 보여줄 그림은 끝에 'photo'를 붙임: ('img/x.jpg', '설명', 'caption', 'photo')
    if not a.get('img'):
        return ''
    items = [(a['img'], a.get('cap_ko', ''), a.get('cap_en', ''), a.get('img_kind', 'photo'))] + [tuple(f) + (('fig',) if len(f) == 3 else ()) for f in a.get('figs', [])]
    main = ''.join(
        f'<figure class="gal-item{" on" if i == 0 else ""}{" fig" if kind != "photo" else ""}">'
        f'<button type="button" class="gal-zoom" aria-label="크게 보기 / Enlarge"><img src="{src}" alt="" loading="lazy"></button>'
        f'<figcaption>{L(ko, en)}</figcaption></figure>'
        for i, (src, ko, en, kind) in enumerate(items))
    thumbs = ''
    if len(items) > 1:
        thumbs = '<div class="gal-thumbs">' + ''.join(
            f'<button type="button" class="gal-th{" on" if i == 0 else ""}" aria-label="{i + 1}"><img src="{src}" alt="" loading="lazy"></button>'
            for i, (src, *_) in enumerate(items)) + '</div>'
    return f'<div class="gal">{main}{thumbs}</div>'
rblocks = ''
for a in AREAS:
    chips = ''.join(f'<li>{L(k, e)}</li>' for k, e in zip(a['kw'], a['kwe']))
    outs = ''.join(f'<li>{o}</li>' for o in a['out'])
    rblocks += f'''
    <article class="rblock" id="{a['slug']}">
      <div class="rblock-h"><svg class="aicon" viewBox="0 0 48 48" aria-hidden="true">{a['icon']}</svg><span class="atag">{a['tag']}</span></div>
      <div class="rblock-b">
        <h2>{L(a['ko'], a['en'])}</h2>
        <p>{L(a['dk'], a['de'])}</p>
        <ul class="chips">{chips}</ul>
        <div class="outs"><span class="lbl">{L('대표 성과', 'Key outputs')}</span><ul>{outs}</ul></div>
      </div>
      {rfig(a)}
    </article>'''
fac = [('Testing', '구조실험', 'Structural testing', '부재·접합부 반복가력 실험과 변형률·변위 계측을 수행합니다. 세부 장비 목록은 추가 예정입니다.', 'Cyclic tests of members and connections with strain and displacement instrumentation. Equipment list to follow.'),
       ('Analysis', '수치해석', 'Numerical analysis', 'Abaqus 기반 비선형 유한요소해석 전용 워크스테이션 (16-core solver).', 'Dedicated Abaqus workstation for nonlinear finite element analysis (16-core solver).'),
       ('Data', '데이터·AI', 'Data &amp; AI', 'GPU 기반 신경망 학습과 실험 데이터 처리 환경.', 'GPU environment for neural-network training and test-data processing.')]
fac_html = ''.join(f'<li><span class="lbl">{a}</span><h3>{L(k, e)}</h3><p>{L(dk, de)}</p></li>' for a, k, e, dk, de in fac)
about = phead('About', '연구실 소개', 'About the Lab',
              '강구조내진공학 연구실(SSEE Lab)은 새로운 강구조 부재·접합부·시스템을 개발하고, 건축물의 내진 성능 향상에 주력합니다. 실험으로 실제 거동을 규명하고, 해석으로 검증 범위를 확장하며, 축적된 데이터를 바탕으로 설계에 활용 가능한 예측 모델을 구축합니다. 이를 통해 지진에 안전하고 지속 가능한 건축 환경을 만드는 연구를 수행하고 있습니다.',
              'The Steel Structures &amp; Earthquake Engineering Lab (SSEE Lab) develops innovative steel members, connections, and structural systems, with a focus on enhancing the seismic performance of buildings. We investigate structural behavior through experimental testing, extend validation through numerical analysis, and build predictive models from accumulated data for practical design use. Through this work, we pursue research toward safe and sustainable built environments against earthquakes.') + f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-h"><h2>Research Areas</h2></div>
    <div class="rblocks">{rblocks}
    </div>
  </div>
</section>
<section class="sec sec-tint" id="facilities">
  <div class="wrap">
    <div class="sec-h"><h2>Facilities</h2></div>
    <ul class="fac">{fac_html}</ul>
  </div>
</section>'''

# ---------------- PROJECTS ----------------
def ptable(rows):
    def ko_en(ko, en):
        return L(ko, en) if ko else en
    body = ''.join(f'<tr><td class="num">{x[0]}</td><td>{ko_en(x[4] if len(x) > 4 else "", x[1])}</td>'
                   f'<td class="sp">{ko_en(x[5] if len(x) > 5 else "", x[2])}</td></tr>'
                   for x in sorted(rows, key=lambda x: x[0][:7], reverse=True))
    return (f'<div class="tscroll"><table class="ptable"><thead><tr><th>{L("기간", "Period")}</th><th>{L("과제명", "Project")}</th>'
            f'<th>{L("발주·지원", "Sponsor")}</th></tr></thead><tbody>{body}</tbody></table></div>')
PI_ROWS = [x for x in PROJECTS if x[3] == 'PI']
CO_ROWS = [x for x in PROJECTS if x[3] != 'PI']
projects = phead('Projects', '연구과제', 'Projects') + f'''
<section class="sec">
  <div class="wrap">
    <div class="sec-h"><h2>Principal Investigator</h2><span class="count">{len(PI_ROWS)} {"project" if len(PI_ROWS)==1 else "projects"}</span></div>
    {ptable(PI_ROWS)}
  </div>
</section>
<section class="sec sec-tint">
  <div class="wrap">
    <div class="sec-h"><h2>Co-Investigator</h2><span class="count">{len(CO_ROWS)} projects</span></div>
    {ptable(CO_ROWS)}
  </div>
</section>'''

# ---------------- PUBLICATIONS ----------------
pat = ''.join(f'<li><span class="yr">{d}</span><div><p class="pt">{L(k, e)}</p><p class="pv en-alt ko">{e}</p>'
              f'<div class="tags"><span class="tag tag-idx">{L("등록특허", "Patent")}</span><span class="tag">KR {n}</span></div></div></li>'
              for d, k, e, n in PATENTS)
bk = ''.join(f'<li><span class="yr">{y}</span><div><p class="pt">{t}</p><p class="pv">{pub}</p></div></li>' for y, t, pub in BOOKS)
UPB = '<div class="tags"><span class="tag tag-up">' + L('발표 예정', 'Upcoming') + '</span></div>'
def conf_item(c):
    y, a, t, cf, pl = c[:5]
    up = len(c) > 5 and c[5] == 'upcoming'
    return (f'<li><span class="yr">{y}</span><div><p class="pt">{t}</p><p class="pa">{me(a)}</p>'
            f'<p class="pv"><i>{cf}</i>, {pl}</p>{UPB if up else ""}</div></li>')
conf = ''.join(conf_item(c) for c in CONF)
SECTIONS = [('intl', 'SCI(E) Journals', 'SCI(E) 국제학술지', len(INTL)), ('domestic', 'Domestic Journals', '국내학술지', len(DOM)),
            ('conf', 'International Conferences', '국제학술대회', len(CONF)), ('patents', 'Patents', '특허', len(PATENTS)), ('books', 'Books', '저서', len(BOOKS))]
toc = ''.join(f'<li><a href="#{k}">{e}<span>{n}</span></a></li>' for k, e, ko, n in SECTIONS)
publications = phead('Publications', '연구성과', 'Publications') + f'''
<section class="sec">
  <div class="wrap pubgrid">
    <nav class="toc" aria-label="Sections"><ul>{toc}</ul>
      <a class="btn btn-ghost btn-sm" href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar ↗</a></nav>
    <div class="pubsecs">
      <section id="intl"><h2>SCI(E) Journals</h2>
        <ol class="plist">{''.join(intl_item(p) for p in INTL)}</ol>
        <p class="fine">{L('IF·JCR 백분위는 게재 연도 기준 JCR 값입니다.', 'IF and JCR percentile follow the JCR of the publication year.')}</p></section>
      <section id="domestic"><h2>Domestic Journals</h2><ol class="plist">{''.join(dom_item(p) for p in DOM)}</ol></section>
      <section id="conf"><h2>International Conferences</h2><ol class="plist">{conf}</ol></section>
      <section id="patents"><h2>Patents</h2><ol class="plist">{pat}</ol></section>
      <section id="books"><h2>Books</h2><ol class="plist">{bk}</ol></section>
    </div>
  </div>
</section>'''

# ---------------- PROFESSOR ----------------
def thesis(th):
    return f'<p class="pv">Thesis: {th}</p>' if th else ''
edu = ''.join(f'<li><span class="yr">{d}</span><div><p class="pt">{deg} · {L(k, e)}</p>{thesis(th)}</div></li>' for d, deg, k, e, th in EDU)
exp = ''.join(f'<li><span class="yr">{d}</span><div><p class="pt">{L(k, e)}</p></div></li>' for d, k, e in EXP)
professor = phead('People · Professor', '지도교수', 'Professor') + f'''
<section class="sec">
  <div class="wrap pi">
    <img class="portrait" src="photo.jpg" alt="전수찬 교수" width="720" height="936">
    <div class="pi-body">
      <p class="eyebrow">Principal Investigator</p>
      <h2 class="pi-name">{L('전수찬', 'Su-Chan Jun')}<small>{L('조교수 · Ph.D.', 'Assistant Professor · Ph.D.')}</small></h2>
      <dl class="contact">
        <div><dt>Email</dt><dd class="sel">{EMAIL}</dd></div>
        <div><dt>{L('전화', 'Phone')}</dt><dd><a href="tel:{PHONE_INTL}">{PHONE}</a></dd></div>
        <div><dt>Office</dt><dd>{L('경북대학교 ' + OFFICE_KO, OFFICE_EN + ', KNU')}</dd></div>
        <div><dt>{L('연구분야', 'Interests')}</dt><dd>{L('강·합성구조 · 내진설계 · 비구조요소 · 진동제어 · 모듈러', 'Steel/composite · Seismic design · Nonstructural elements · Vibration control · Modular')}</dd></div>
      </dl>
    </div>
  </div>
  <div class="wrap cvgrid">
    <div><h3 class="cv-h">Education</h3><ol class="plist tight">{edu}</ol></div>
    <div><h3 class="cv-h">Experience</h3><ol class="plist tight">{exp}</ol></div>
  </div>
</section>'''

# ---------------- MEMBERS ----------------
GROUPS = [('phd', 'Ph.D. Students'), ('ms', 'M.S. Students'), ('ug', 'Undergraduate Researchers')]
def member_card(g, nk, ne, start, mail, ph):
    pic = (f'<img src="{ph}" alt="{nk}" loading="lazy">' if ph
           else f'<span class="mph" aria-hidden="true">{nk[:1]}</span>')
    since = f'<span class="msince">({start} ~ )</span>' if start else ''
    email = f'<span class="mmail sel">{mail}</span>' if mail else ''
    return (f'<li class="mcard"><div class="mpic">{pic}</div>'
            f'<p class="mname"><b>{L(nk, ne)}</b>{since}</p>{email}</li>')
stu = ''
for g, title in GROUPS:
    ms = [m for m in STUDENTS if m[0] == g]
    if ms:
        stu += f'<div class="mgroup"><h2 class="mgh">{title}</h2><ul class="mgrid">' + ''.join(member_card(*m) for m in ms) + '</ul></div>'
if not stu:
    stu = f'<p class="empty">{L("구성원 정보는 곧 업데이트됩니다.", "Member information will be updated soon.")}</p>'
students = phead('People · Members', '구성원', 'Members') + f'''
<section class="sec">
  <div class="wrap">
    {stu}
  </div>
</section>'''

# ---------------- NEWS ----------------
news = phead('News', '소식', 'News') + f'''
<section class="sec"><div class="wrap narrow">{news_list(NEWS)}</div></section>'''

# ---------------- CONTACT ----------------
from urllib.parse import quote
MAP_Q = quote(MAP_KO)
contact = phead('Contact', '연락처', 'Contact') + f'''
<section class="sec">
  <div class="wrap cgrid">
    <dl class="contact big">
      <div><dt>Email</dt><dd class="sel">{EMAIL}</dd></div>
      <div><dt>{L('전화', 'Phone')}</dt><dd><a href="tel:{PHONE_INTL}">{PHONE}</a></dd></div>
      <div><dt>{L('주소', 'Address')}</dt><dd>{L('41566 대구광역시 북구 대학로 80<br>경북대학교 공과대학 건축공학과', 'Dept. of Architectural Engineering<br>Kyungpook National University<br>80 Daehak-ro, Buk-gu, Daegu 41566, Korea')}</dd></div>
      <div><dt>{L('연구실', 'Lab')}</dt><dd>{L('경북대학교 ' + OFFICE_KO, OFFICE_EN + ', KNU')}</dd></div>
    </dl>
    <div class="cards-col">
      <div class="ccard">
        <span class="lbl">{L('지도', 'Map')}</span>
        <h3>{L('찾아오는 길', 'Getting here')}</h3>
        <p>{L('경북대학교 대구캠퍼스 ' + OFFICE_KO, OFFICE_EN + ', Kyungpook National University (Daegu campus)')}</p>
        <div class="maplinks">
          <a class="btn btn-ghost btn-sm" href="https://map.naver.com/p/search/{MAP_Q}" target="_blank" rel="noopener">Naver Map ↗</a>
          <a class="btn btn-ghost btn-sm" href="https://map.kakao.com/?q={MAP_Q}" target="_blank" rel="noopener">Kakao Map ↗</a>
          <a class="btn btn-ghost btn-sm" href="https://www.google.com/maps/search/?api=1&amp;query={MAP_Q}" target="_blank" rel="noopener">Google Maps ↗</a>
        </div>
      </div>
    </div>
  </div>
</section>'''

files = {
 'index.html': page('', 'SSEE Lab · 경북대학교 강구조내진공학 연구실', home),
 'about.html': page('about', 'About · SSEE Lab', about),
 'professor.html': page('professor', 'Professor · SSEE Lab', professor),
 'students.html': page('students', 'Members · SSEE Lab', students),
 'publications.html': page('publications', 'Publications · SSEE Lab', publications),
 'projects.html': page('projects', 'Projects · SSEE Lab', projects),
 'news.html': page('news', 'News · SSEE Lab', news),
 'contact.html': page('contact', 'Contact · SSEE Lab', contact),
}
for n, c in files.items():
    open(os.path.join(OUT, n), 'w', encoding='utf-8').write(c)
# 검색엔진용 sitemap.xml / robots.txt
if SITE_URL:
    import datetime
    base = SITE_URL.rstrip('/')
    today = datetime.date.today().isoformat()
    urls = ''.join(f'<url><loc>{base}/{"" if n == "index.html" else n}</loc><lastmod>{today}</lastmod></url>' for n in files)
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n')
# 이전 구조의 페이지 정리
for old in ['research.html', 'facilities.html', 'people.html']:
    pth = os.path.join(OUT, old)
    if os.path.exists(pth):
        os.remove(pth)
print('built', len(files), 'pages →', OUT)
