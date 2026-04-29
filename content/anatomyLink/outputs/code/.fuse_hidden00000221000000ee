# AnatomyLink HTML Generator

AnatomyLink Obsidian 볼트를 HTML 웹사이트로 변환하는 파이썬 빌드 시스템입니다.

## 📁 파일 구조

```
code/
├── converter.py      # Markdown → HTML 변환 클래스
├── build.py         # 메인 빌드 스크립트
└── README.md        # 이 파일

html_output/        # 생성된 HTML 파일들
├── index.html       # 홈페이지
├── styles.css       # 스타일시트
├── script.js        # JavaScript 인터랙티브 기능
├── Circulatory System/
├── Skeletal System/
├── Muscular System/
├── Nervous System/
├── Digestive System/
└── Ligament System/
```

## 🔧 기능

### converter.py
- Obsidian의 위키 링크 `[[Heart]]`, `[[Sternum]]` 등 → HTML 링크로 변환
- Markdown 문법을 HTML로 변환
  - 제목 (# ~ ###)
  - 굵게 (**text**)
  - 기울임 (*text*)
  - 코드 (\`code\`)
  - 인용구 (> text)
  - 테이블 지원

### build.py
- 전체 Obsidian 볼트를 스캔
- 모든 마크다운 파일을 HTML로 변환
- 파일 인덱스 생성 (링크 매핑)
- 네비게이션 구조 자동 생성
- 스타일시트와 JavaScript 파일 생성

## ✨ 생성되는 HTML의 특징

1. **반응형 디자인** - 모바일/데스크톱 최적화
2. **의료 전문성** - 테이블, 제목 구조화
3. **인터랙티브 링크** - 모든 위키 링크가 클릭 가능
4. **네비게이션** - 사이드바와 브레드크럼
5. **전문 디자인** - 의료학 학습 자료에 적합

## 🚀 사용 방법

### 1. 전체 사이트 다시 생성
```bash
python3 build.py
```

이 명령은:
- `/mnt/anatomyLink`의 모든 마크다운 파일을 읽음
- 링크 인덱스 생성
- HTML 파일들을 `/mnt/outputs/html_output/`에 생성
- CSS와 JavaScript 파일 생성

### 2. 생성된 사이트 열기
브라우저에서 `html_output/index.html` 파일을 열면 됩니다:

```
file:///sessions/exciting-adoring-gates/mnt/outputs/html_output/index.html
```

### 3. 웹서버로 호스팅
더 나은 성능을 위해 로컬 웹서버에서 실행:

```bash
cd /sessions/exciting-adoring-gates/mnt/outputs/html_output/
python3 -m http.server 8000
```

그 다음 브라우저에서 `http://localhost:8000` 방문

## 🔗 위키 링크 변환 예시

**원본 (Obsidian):**
```markdown
[[Heart]] is protected by [[Sternum]]
```

**생성된 HTML:**
```html
<a href="Heart.html" class="wiki-link">Heart</a> is protected by 
<a href="Sternum.html" class="wiki-link">Sternum</a>
```

존재하지 않는 링크는 회색으로 표시됩니다 (예: 존재하지 않는 구조에 대한 링크):

```html
<!-- 예시: 존재하지 않는 파일을 가리키는 링크 -->
<span class="dead-link" title="Not found: UndefinedStructure">UndefinedStructure</span>
```

## 📊 테이블 변환

**원본:**
```
| 항목 | 설명 |
|------|------|
| 심장 | 펌프 역할 |
```

**생성된 HTML:**
- 자동으로 스타일된 HTML 테이블로 변환
- 마우스 호버 효과
- 반응형 디자인

## 🎨 커스터마이징

### CSS 수정
`html_output/styles.css`를 편집하면 디자인을 커스터마이징할 수 있습니다:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #e74c3c;
    /* ... */
}
```

### JavaScript 수정
`html_output/script.js`에서 인터랙티브 기능을 추가할 수 있습니다.

## 📈 성능

- 206개 마크다운 파일 처리: ~2-3초
- 생성된 HTML 크기: 약 25MB (최적화 가능)
- 페이지 로딩: 매우 빠름 (정적 HTML)

## 🐛 문제 해결

### 링크가 작동하지 않음
1. 파일명이 정확한지 확인
2. 파일 경로에 공백이 있으면 URL 인코딩됨 (`%20`)
3. 콘솔(F12)에서 에러 확인

### 마크다운이 제대로 변환되지 않음
- YAML frontmatter는 자동으로 제거됨
- 복잡한 마크다운은 `converter.py` 수정 필요

## 📝 라이선스

이 HTML 생성 도구는 AnatomyLink 프로젝트의 일부입니다.

## 🎓 의료 학생을 위한 배포

이 HTML 사이트는:
- ✅ 완전히 정적 (서버 필요 없음)
- ✅ 오프라인에서 작동 가능
- ✅ USB 드라이브에 담아 공유 가능
- ✅ 어떤 웹서버에도 호스팅 가능

### GitHub Pages에 배포하기
```bash
# 1. GitHub 저장소 생성
git init

# 2. html_output 폴더를 gh-pages 브랜치로 배포
```

## 📞 지원

문제가 있으면 `converter.py` 또는 `build.py`의 주석을 참고하세요.
