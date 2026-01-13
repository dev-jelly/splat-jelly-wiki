# DNS 설정 안내 - sp-wiki.octol.ing

## 현재 상태

✅ **GitHub Pages 배포 완료**
- 사이트가 gh-pages 브랜치로 성공적으로 배포됨
- 모든 22개 페이지가 포함됨
- CNAME 파일 설정됨: `sp-wiki.octol.ing`
- .nojekyll 파일로 Jekyll 비활성화됨

⏳ **DNS 설정 필요**
- sp-wiki.octol.ing 도메인이 GitHub Pages를 가리키도록 설정 필요
- 현재 상태: DNS 레코드 미설정

## DNS 설정 단계

### 1. GitHub Pages CNAME 확인

GitHub Pages에서 제공하는 DNS 타겟:
```
dev-jelly.github.io
```

### 2. DNS 레코드 추가

octol.ing 도메인의 DNS 관리자에서 다음 CNAME 레코드를 추가하세요:

| 타입 | 이름 | 값/타겟 | TTL |
|------|------|----------|-----|
| CNAME | sp-wiki | dev-jelly.github.io | 3600 (또는 1시간) |

### 3. DNS 설정 방법

#### 옵션 A: Cloudflare DNS (권장)

Cloudflare Dashboard에서:

1. [Cloudflare Dashboard](https://dash.cloudflare.com) 접속
2. `octol.ing` 도메인 선택
3. **DNS** → **Records** 이동
4. **Add Record** 클릭:
   - Type: `CNAME`
   - Name: `sp-wiki`
   - Target: `dev-jelly.github.io`
   - Proxy status: `Proxied` (오렌지 아이콘) 또는 `DNS only` (회색 아이콘)
   - TTL: Auto
   - Save 클릭

#### 옵션 B: Namecheap

1. Namecheap Dashboard 접속
2. Domain List → octol.ing → **Manage**
3. **Advanced DNS** 탭
4. **Add New Record**:
   - Type: `CNAME Record`
   - Host: `sp-wiki`
   - Value: `dev-jelly.github.io`
   - TTL: `Automatic`
5. **Save All Changes**

#### 옵션 C: GoDaddy

1. GoDaddy Dashboard 접속
2. My Products → octol.ing → **DNS Management**
3. **Add** 버튼:
   - Type: `CNAME`
   - Name: `sp-wiki`
   - Value: `dev-jelly.github.io`
   - TTL: `1 Hour`
4. **Save**

### 4. DNS 전파 확인

DNS 레코드가 전파되는 데 5분~24시간 소요될 수 있습니다.

#### 확인 방법:

**macOS/Linux:**
```bash
dig sp-wiki.octol.ing
```

**Windows:**
```cmd
nslookup sp-wiki.octol.ing
```

**예상 출력:**
```
; ANSWER SECTION:
sp-wiki.octol.ing.  3600  IN  CNAME  dev-jelly.github.io.
```

### 5. 도메인 확인 (GitHub)

GitHub에서 도메인 소유권을 확인합니다:

1. [GitHub Repository Settings](https://github.com/dev-jelly/splat-jelly-wiki/settings/pages) 접속
2. Pages 섹션에서 `sp-wiki.octol.ing`가 표시되는지 확인
3. 상태가 `Active`로 변경될 때까지 기다림
4. 필요한 경우 GitHub에서 제공하는 DNS 확인 TXT 레코드를 추가

## 배포 검증

DNS가 설정되고 전파된 후 다음 URL에서 사이트 접속 가능:

**프로덕션 URL:**
```
https://sp-wiki.octol.ing
```

**GitHub Pages 대체 URL (DNS 전파 전):**
```
https://dev-jelly.github.io/splat-jelly-wiki/
```

## 검증 체크리스트

### DNS 설정
- [ ] CNAME 레코드 생성됨
- [ ] Name: sp-wiki
- [ ] Target: dev-jelly.github.io
- [ ] TTL 설정됨 (3600 또는 Auto)

### 사이트 접속
- [ ] https://sp-wiki.octol.ing 접속 가능
- [ ] 홈페이지 정상 로딩
- [ ] 네비게이션 사이드바 표시
- [ ] 모든 페이지 접근 가능 (22개 페이지)
- [ ] 검색 기능 작동
- [ ] HTTPS 연결 (보안 잠금장 아이콘)

### GitHub Pages 상태
- [ ] GitHub Pages status: Active
- [ ] Custom domain: sp-wiki.octol.ing
- [ ] DNS checks passed
- [ ] Build status: Latest deployment successful

## 문제 해결

### 사이트 접속 불가 (DNS 전파 중)

**증상:**
```
ERR_NAME_NOT_RESOLVED 또는 NXDOMAIN
```

**해결:**
1. DNS 레코드가 올바르게 설정되었는지 확인
2. DNS 전파 대기 (5분~24시간)
3. 다음 명령어로 전파 확인: `dig sp-wiki.octol.ing`
4. 브라우저 캐시 삭제 및 DNS 캐시 플러시

### GitHub Pages 상태가 "Errored"

**원인:**
- DNS 레코드가 올바르지 않거나
- GitHub에서 도메인 확인이 안됨

**해결:**
1. DNS 레코드 확인 (GitHub가 제공하는 TXT 레코드 추가 필요할 수 있음)
2. [Repository Settings](https://github.com/dev-jelly/splat-jelly-wiki/settings/pages)에서
   "Custom domain" 섹션 확인
3. GitHub에서 제공하는 DNS 확인 지침 따르기

### 404 에러

**원인:**
- 사이트가 빌드되지 않았거나
- 잘못된 경로로 접근

**해결:**
1. [GitHub Pages 배포 로그](https://github.com/dev-jelly/splat-jelly-wiki/actions/workflows/github-pages.yml) 확인
2. gh-pages 브랜치에 index.html 있는지 확인
3. 최신 커밋 확인

### HTTPS 비활성화

**원인:**
- DNS 레코드가 Cloudflare Proxy를 통과하지 않거나
- SSL 인증서가 발급되지 않음

**해결:**
1. GitHub Pages에서 자동 SSL 활성화 대기 (최대 24시간)
2. Cloudflare를 사용하는 경우 SSL/TLS 설정을 "Full"로 변경
3. Edge Certificates 탭에서 "Always Use HTTPS" 활성화

## 모니터링

### 사이트 상태 확인

**GitHub Actions:**
```
https://github.com/dev-jelly/splat-jelly-wiki/actions
```

**GitHub Pages:**
```
https://github.com/dev-jelly/splat-jelly-wiki/settings/pages
```

### 로그 확인

배포 문제 발생 시:
1. [Actions](https://github.com/dev-jelly/splat-jelly-wiki/actions)에서 최신 워크플로우 확인
2. 실패한 단계의 로그 자세히 확인
3. 오류 메시지 기록하여 문제 해결

## 업데이트 방법

사이트 콘텐츠 업데이트 시:

1. 로컬에서 콘텐츠 수정 (`src/content/**/*.mdx`)
2. 로컬 빌드 테스트: `npm run build`
3. Git 커밋: `git add . && git commit -m "Update ..."`
4. GitHub에 푸시: `git push origin main`
5. 자동 배포 대기 (약 1-2분)
6. 사이트 접속하여 변경사항 확인

## 완료 기준

배포가 완료되었다고 간주할 때:

1. ✅ DNS 레코드 올바르게 설정
2. ✅ DNS 전파 완료 (dig/nslookup로 확인)
3. ✅ https://sp-wiki.octol.ing 접속 가능
4. ✅ GitHub Pages status: Active
5. ✅ HTTPS 연결 작동 (보안 잠금장 아이콘)
6. ✅ 모든 22개 페이지 정상 로딩
7. ✅ 검색 기능 작동
8. ✅ 네비게이션 사이드바 작동

---

**다음 단계:** DNS 설정을 완료하고 사이트 접속 테스트를 진행하세요!
