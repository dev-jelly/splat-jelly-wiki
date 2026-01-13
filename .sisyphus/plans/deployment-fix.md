# Splat Jelly Wiki 배포 완료 계획

## 📋 요약

**문제**: 프로젝트가 단 한 번도 배포되지 않음
**원인**: Git 초기화 안됨 → GitHub 리포지토리 없음 → CI/CD 실행 안됨 → 배포 안됨
**목표**: https://sp-wiki.octol.ink 배포 완료
**예상 시간**: 30-45분

---

## ✅ 사전 체크리스트

시작 전에 다음을 확인하세요:

- [ ] GitHub 계정이 있고 로그인 가능
- [ ] Miniflare 클러스터에 접근 가능
- [ ] octol.ink 도메인 관리 권한 있음
- [ ] 프로젝트 폴더: `/Users/jelly/personal/splat-jelly-wiki`
- [ ] Node.js 20+ 설치됨
- [ ] Git 설치됨

---

## 🎯 배포 단계별 가이드

### 단계 1: Git 리포지토리 초기화 (5분)

```bash
cd /Users/jelly/personal/splat-jelly-wiki

# Git 초기화
git init

# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: Splat Jelly Wiki with full Korean documentation"

# main 브랜치 이름 설정
git branch -M main
```

**검증**:
```bash
git status
# Should show: "On branch main" and "nothing to commit, working tree clean"
```

---

### 단계 2: GitHub 리포지토리 생성 (3분)

#### 옵션 A: GitHub 웹에서 생성 (권장)

1. [GitHub](https://github.com/new) 접속
2. 리포지토리 이름: `splat-jelly-wiki`
3. 가시성: **Public** (권장, 무료)
4. README 추가: ❌ 체크 해제 (이미 있음)
5. .gitignore 추가: ❌ 체크 해제 (이미 있음)
6. **Create repository** 클릭
7. 리포지토리 URL 복사: `https://github.com/YOUR_USERNAME/splat-jelly-wiki.git`

#### 옵션 B: GitHub CLI로 생성

```bash
gh repo create splat-jelly-wiki --public --source=. --push
```

---

### 단계 3: 코드 GitHub로 푸시 (3분)

```bash
# GitHub 리포지토리를 원격 저장소로 추가
# YOUR_USERNAME을 실제 GitHub 사용자명으로 교체하세요
git remote add origin https://github.com/YOUR_USERNAME/splat-jelly-wiki.git

# GitHub로 푸시
git push -u origin main
```

**검증**:
- GitHub 리포지토리 페이지에서 모든 파일이 표시되는지 확인
- `package.json`, `src/`, `astro.config.mjs` 등이 있는지 확인

---

### 단계 4: Miniflare API 토큰 발급 (5분)

#### 토큰 발급 절차

1. [Miniflare Dashboard](https://dash.miniflare.com) 접속
2. **Settings** 또는 **API Tokens** 메뉴로 이동
3. **Generate New Token** 클릭
4. 토큰 설정:
   - **Name**: `splat-jelly-wiki-deploy`
   - **Scope**: 
     - ✅ Deploy to Miniflare
     - ✅ Access to cluster (기존 클러스터)
   - **Expiration**: 90일 이상 (혹은 Never expire)
5. **Generate Token** 클릭
6. **⚠️ 토큰 즉시 복사** (다시 볼 수 없습니다!)

**예시 토큰 형식**:
```
mfpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 단계 5: GitHub Secrets 설정 (3분)

1. 방금 생성한 GitHub 리포지토리로 이동
2. **Settings** → **Secrets and variables** → **Actions** 클릭
3. **New repository secret** 클릭
4. Secret 추가:
   - **Name**: `MINIFLARE_API_TOKEN`
   - **Secret**: 복사한 Miniflare API 토큰 붙여넣기
   - **Add secret** 클릭

**검증**:
- Secrets 목록에 `MINIFLARE_API_TOKEN`이 표시되는지 확인
- 토큰이 마스킹 (`****`)되어 표시되는지 확인

---

### 단계 6: GitHub Actions 배포 확인 (10분)

#### 자동 트리거 확인

단계 3에서 코드를 푸시했으므로 GitHub Actions가 자동으로 실행되어야 합니다.

1. GitHub 리포지토리 페이지에서 **Actions** 탭 클릭
2. 왼쪽 사이드바에서 **Build and Deploy** 워크플로우 선택
3. 최신 실행(workflow run) 클릭
4. **jobs** → **build-and-deploy** 클릭하여 진행 상황 확인

**예상 동작**:
```
✓ Checkout code
✓ Setup Node.js 20
✓ Install dependencies (npm ci)
✓ Install Miniflare CLI
✓ Build Astro site
✓ Deploy to Miniflare Cluster
```

**빌드 시간**: 약 2-5분

#### 수동 트리거 (필요시)

자동 트리거가 안 된 경우:

1. **Actions** 탭 → **Build and Deploy** 클릭
2. **Run workflow** 드롭다운 클릭
3. **Run workflow** 클릭
4. 실행 상태 모니터링

---

### 단계 7: DNS 설정 (10분)

#### octol.ink 도메인에 CNAME 추가

**옵션 A: octol.ink가 레지스트라에 있는 경우**

1. 도메인 레지스트라 관리 패널 접속 (예: 가비아, 후이즈 등)
2. `octol.ink` 도메인의 **DNS 관리**로 이동
3. 새 레코드 추가:
   - **유형**: `CNAME`
   - **호스트 이름**: `sp-wiki`
   - **값/타겟**: Miniflare에서 제공된 도메인 (아래 참고)
   - **TTL**: `3600` (1시간)
4. 저장

**Miniflare 배포 도메인 확인**:
- GitHub Actions 로그 확인
- "Deployed to: `https://something.pages.dev`"와 같은 메시지 찾기
- 또는 Miniflare Dashboard에서 확인

**완성된 DNS 예시**:
```
타입   이름         값                         TTL
CNAME  sp-wiki      something.pages.dev         3600
```

**옵션 B: Cloudflare에 있는 경우**

1. [Cloudflare Dashboard](https://dash.cloudflare.com) 접속
2. `octol.ink` 도메인 선택
3. **DNS** → **Records**로 이동
4. **Add record** 클릭:
   - **Type**: `CNAME`
   - **Name**: `sp-wiki`
   - **Target**: Miniflare 배포 도메인
   - **Proxy status**: `Proxied` (주황색 구름 아이콘) 권장
5. **Save**

---

### 단계 8: DNS 전파 대기 (5-30분)

DNS 변경사항이 전 세계에 전파될 때까지 기다립니다.

#### DNS 전파 확인

**macOS/Linux**:
```bash
dig sp-wiki.octol.ink +short
# 결과: Miniflare 도메인이 표시되어야 함
```

**Windows**:
```cmd
nslookup sp-wiki.octol.ink
# 결과: Miniflare 도메인이 표시되어야 함
```

**성공 예시**:
```
$ dig sp-wiki.octol.ink +short
your-miniflare-domain.pages.dev.
```

---

### 단계 9: 배포 검증 (5분)

#### 1. 사이트 접속 테스트

```bash
curl -I https://sp-wiki.octol.ink
```

**예상 결과**:
```
HTTP/2 200
content-type: text/html
...
```

#### 2. 브라우저에서 직접 확인

1. [https://sp-wiki.octol.ink](https://sp-wiki.octol.ink) 접속
2. 다음을 확인:

**필수 검증**:
- [x] 홈페이지가 정상 로드됨
- [x] 연어런 NEXT WAVE 제목 표시됨
- [x] 왼쪽 네비게이션 사이드바 표시됨
- [x] 한국어 콘텐츠가 정확히 번역되어 표시
- [x] 모든 스테이지 링크 클릭 가능
- [x] 검색 기능 작동

**추가 검증**:
- [x] 반응형 디자인 (모바일/태블릿)
- [x] HTTPS 연결 (SSL 인증서 유효)
- [x] 빠른 로딩 시간 (<3초)
- [x] 404 페이지 (존재하지 않는 URL 접속 시)

#### 3. 모든 페이지 접근 테스트

다음 URL들이 모두 정상 응답하는지 확인:

```
https://sp-wiki.octol.ink/
https://sp-wiki.octol.ink/stages/
https://sp-wiki.octol.ink/stages/gluttones-valley/
https://sp-wiki.octol.ink/enemies/
https://sp-wiki.octol.ink/enemies/small-fry/
https://sp-wiki.octol.ink/weapons/
https://sp-wiki.octol.ink/special-situations/
https://sp-wiki.octol.ink/events/
```

#### 4. 검색 기능 테스트

1. 홈페이지 우측 상단 검색창 클릭
2. "연어" 입력
3. 결과가 표시되는지 확인
4. 결과 중 하나 클릭하여 페이지 이동 확인

---

## 🚨 문제 해결 가이드

### 문제 1: GitHub Actions 빌드 실패

**증상**: Actions 탭에서 ❌ 빨간색 실패 표시

**진단**:
1. 실패한 스텝 클릭
2. 로그 읽기
3. 에러 메시지 찾기

**일반적인 원인 및 해결**:

| 에러 | 원인 | 해결책 |
|------|------|--------|
| `npm ci` 실패 | `package-lock.json` 없음 | `npm install` 후 `git add . && git commit -m "Add lock file"` |
| `build` 실패 | Astro 설정 오류 | `npm run build` 로컬에서 실행하여 디버깅 |
| `deploy` 실패 | API 토큰 유효하지 않음 | Miniflare 토큰 재발급 후 GitHub Secret 업데이트 |
| `miniflare: command not found` | CLI 설치 실패 | 워크플로우 파일의 `npm install -g miniflare` 확인 |

---

### 문제 2: DNS가 해결되지 않음

**증상**: `curl https://sp-wiki.octol.ink` → "Could not resolve host"

**해결**:

1. **DNS 레코드 확인**:
   ```bash
   dig sp-wiki.octol.ink +short
   # 결과가 없으면 DNS 설정 확인
   ```

2. **TTL 확인**: 5-30분까지 전파 시간 필요

3. **�시 플러시**:
   ```bash
   # macOS
   sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
   
   # Linux
   sudo systemctl flush-dns
   
   # Windows
   ipconfig /flushdns
   ```

4. **다른 네트워크/장치에서 테스트**: 모바일 데이터, VPN 등

---

### 문제 3: 사이트 접속되지만 404 에러

**증상**: 사이트는 열리지만 페이지들 모두 404

**원인**: 배포된 파일이 올바르지 않음

**해결**:

1. **dist 폴더 확인**:
   ```bash
   ls -la dist/
   # index.html이 있는지 확인
   ```

2. **로컬 빌드 테스트**:
   ```bash
   npm run build
   npx serve dist
   # 브라우저에서 http://localhost:3000 접속
   ```

3. **GitHub Actions 재실행**:
   - Actions 탭 → Build and Deploy
   - Run workflow → Run workflow

---

### 문제 4: SSL 인증서 오류

**증상**: 브라우저에서 "연결이 안전하지 않음" 경고

**해결**:

1. **Cloudflare인 경우**:
   - SSL/TLS 탭
   - **Encryption mode**를 **Full** 또는 **Full (strict)**로 설정

2. **기타 레지스트라**:
   - SSL 인증서 자동 발급 확인
   - 10-15분까지 기다리기

---

### 문제 5: 검색 기능 작동 안함

**증상**: 검색창에 입력해도 결과 없음

**해결**:

1. **검색 인덱스 확인**:
   ```bash
   ls dist/pagefind/
   # 여러 파일이 있는지 확인
   ```

2. **개발자 도구 콘솔 확인**:
   - F12 → Console 탭
   - JS 에러가 있는지 확인

3. **�시 지우기**:
   - Ctrl+Shift+R (Windows/Linux)
   - Cmd+Shift+R (macOS)

---

## 🔄 롤백 절차

### 배포 실패 시 롤백

1. **마지막 작동하는 커밋으로 복귀**:
   ```bash
   git log --oneline -5
   # 작동하던 커밋 SHA 찾기
   git reset --hard <COMMIT_SHA>
   git push --force
   ```

2. **수정 후 재배포**:
   ```bash
   # 수정 사항 적용
   git add .
   git commit -m "Fix deployment issue"
   git push
   ```

### 버전 태깅 (권장)

배포마다 태그 생성하여 롤백 용이하게:

```bash
git tag -a v1.0.0 -m "Initial deployment"
git push origin v1.0.0

# 나중에 롤백 시:
git checkout v1.0.0
```

---

## 📊 배포 성공 기준

다음 모든 조건이 충족되면 배포 **성공**으로 간주:

| 항목 | 기준 | 상태 |
|------|------|------|
| 사이트 접속 | https://sp-wiki.octol.ink 200 응답 | ⬜ |
| 홈페이지 | 연어런 NEXT WAVE 표시 | ⬜ |
| 네비게이션 | 사이드바 6개 섹션 표시 | ⬜ |
| 페이지 수 | 22개 페이지 모두 접근 가능 | ⬜ |
| 콘텐츠 | 한국어 번역 정확히 표시 | ⬜ |
| 검색 | 검색창 작동 | ⬜ |
| HTTPS | SSL 인증서 유효 | ⬜ |
| 성능 | 빌드 <60s, 로딩 <3s | ⬜ |
| 모바일 | 반응형 디자인 정상 | ⬜ |

---

## 📝 배포 후 작업

### 1. 모니터링 설정

**Miniflare Dashboard**:
- [ ] Analytics 확인 (트래픽, 에러율)
- [ ] 로그 모니터링 (실시간 에러)

**GitHub Actions**:
- [ ] 워크플로우 성공 모니터링

### 2. 지속적 통합

이제 모든 새 커밋은 자동으로 배포됩니다:

```bash
# 콘텐츠 수정
# 1. 로컬에서 수정
# 2. 테스트 (npm run build)
# 3. 커밋 (git add . && git commit -m "Update content")
# 4. 푸시 (git push)
# 5. GitHub Actions가 자동으로 배포
```

### 3. 주기적 업데이트

일본어 위키 업데이트를 반영:

1. 일본어 위키의 변경사항 확인
2. 콘텐츠 번역 및 수정
3. 로컬 테스트
4. Git 커밋 및 푸시
5. 자동 배포 대기

---

## 🎉 축하합니다!

이 계획을 완료하면:
- ✅ Splat Jelly Wiki가 https://sp-wiki.octol.ink에서 운영
- ✅ 22개 한국어 문서 공개
- ✅ 검색 기능 작동
- ✅ 자동 CI/CD 파이프라인 구축
- ✅ 모든 업데이트는 `git push`로 자동 배포

**다음 단계**: 전체 위키 확장 (500+ 페이지 번역) 계획 실행

---

## 📚 추가 리소스

- [Astro 문서](https://docs.astro.build/)
- [Starlight 문서](https://starlight.astro.build/)
- [Miniflare CLI 문서](https://docs.miniflare.com/)
- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [GitHub Secrets 가이드](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

## 💡 팁

- **SSH Key 설정**: `git push` 비밀번호 입력 피하기
- **Pre-commit hooks**: 푸시 전 자동 빌드 테스트
- **Branch Protection**: main 브랜치 직접 푸시 방지, PR 요구
- **Status Badges**: README에 배포 상태 배지 추가

---

## 📞 도움이 필요하면

문제가 발생하면:
1. GitHub Actions 로그 확인
2. Miniflare Dashboard 확인
3. 이 계획의 **문제 해결** 섹션 참조
