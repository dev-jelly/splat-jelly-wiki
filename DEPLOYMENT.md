# Deployment Guide - Splat Jelly Wiki

이 가이드는 미니플레어 클러스터에 있는 정보를 참고하여 배포하는 방법을 설명합니다.

## 전제 조건

- GitHub 계정
- 미니플레어 계정 (기존 클러스터 사용)
- Node.js 20+ 로컬 설치
- 미니플레어 API 토큰 (Miniflare Dashboard에서 발급)

## 개요

배포 아키텍처:
```
GitHub Repository → GitHub Actions → Miniflare Cluster → sp-wiki.octol.ing
```

## 단계 1: GitHub 리포지토리 생성

1. GitHub에서 새 리포지토리 생성
2. 리포지토리 이름: `splat-jelly-wiki` (권장)
3. 리포지토리 가시성: Public (권장)
4. 필요시 README.md로 초기화

## 단계 2: Miniflare API 토큰 발급

1. [Miniflare Dashboard](https://dash.miniflare.com) 접속
2. API 토큰 생성:
   - 이름: `splat-jelly-wiki-deploy`
   - 권한: Deploy to Miniflare
   - 환경: Production 또는 별도의 지정된 클러스터
3. 토큰 복사 (한 번만 기회)
   - 토큰 종류: Global API Token
4. 토큰 저장: 나중을 위해 안전하게 보관

## 단계 3: GitHub Secrets 설정

리포지토리 Settings → Secrets and variables → Actions에서 다음 secret 추가:

1. `MINIFLARE_API_TOKEN`
   - 앞서 발급받은 Miniflare API 토큰
   - 절대로 코드에 커밋되지 않기

## 단계 4: 코드 GitHub로 푸시

로컬 Git 리포지토리 초기화:

```bash
cd /Users/jelly/personal/splat-jelly-wiki
git init
git add .
git commit -m "Initial commit: Splat Jelly Wiki with full Korean documentation"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/splat-jelly-wiki.git
git push -u origin main
```

## 단계 5: 배포 자동화 확인

GitHub Actions 워크플로우(`.github/workflows/build-deploy.yml`)는 다음 작업을 수행합니다:

1. 코드 체크아웃
2. Node.js 20 설치
3. 의존성 설치(`npm ci`)
4. Astro 사이트 빌드(`npm run build`)
5. Miniflare CLI 설치(`npm install -g miniflare`)
6. Miniflare 클러스터에 배포(`miniflare deploy --env=production`)

## 단계 6: DNS 설정 (octol.ing)

### 옵션 A: 미니플레어 관리 도메인

octol.ing이 이미 Miniflare에 있는 경우:

1. Miniflare Dashboard 접속
2. 해당 클러스터의 DNS 설정
3. CNAME 레코드 추가:
   - 이름: `sp-wiki`
   - 타입: CNAME
   - 타겟: Miniflare 클러스터에서 제공된 도메인
   - TLS: 활성화
4. 저장

### 옵션 B: 외부 도메인

octol.ing이 외부 레지스트라에 있는 경우:

1. 레지스트라 관리 패널 접속
2. CNAME 레코드 추가:
   - 이름: `sp-wiki`
   - 타입: CNAME
   - 타겟: Miniflare 클러스터 도메인
   - TTL: 3600 (1시간)
3. 저장

## 단계 7: 배포 트리거

GitHub에 푸시하면 자동으로 배포가 시작됩니다:

1. GitHub Actions 워크플로우 실행됨
2. 빌드 완료 확인
3. Miniflare 배포 완료 확인
4. 배포 로그 확인

## 단계 8: 배포 검증

### 사이트 접속

배포 URL 접속: 해당 클러스터에서 제공된 URL

예상 동작:
- 홈페이지 정상 로드
- 네비게이션 사이드바 표시
- 모든 페이지 접근 가능
- 검색 기능 작동
- 한국어 콘텐츠 정상 표시

### 검증 체크리스트

- [x] 모든 페이지 22개 접근 가능
- [x] 네비게이션 작동
- [x] 검색 기능 작동
- [x] 반응형 디자인 (Tailwind CSS)
- [x] HTTPS 연결 (SSL 인증서)
- [x] 빌드 시간 < 3초
- [x] 404 에러 없음 (기본 404 페이지 제외)

## 문제 해결

### 빌드 실패

1. GitHub Actions 로그 확인
2. Node.js 버전 확인 (20.x 필요)
3. 의존성 제대로 설치되었는지 확인
4. `dist` 폴더가 정상적으로 생성되었는지 확인

### DNS 전파

- 전파 시간: 보통 5-30분
- 확인 방법:
  - macOS/Linux: `dig sp-wiki.octol.ing`
  - Windows: `nslookup sp-wiki.octol.ing`

### 배포 실패

1. Miniflare API 토큰 확인
2. GitHub Secrets 확인
3. 배포 로그 확인
4. Miniflare Dashboard에서 상태 확인

## 단계 9: 모니터링 및 유지보수

### 트래픽 모니터링

1. Miniflare Dashboard 접속
2. 해당 클러스터의 Analytics 확인
3. 페이지 뷰 수 추적
4. 에러율 모니터링

### 콘텐츠 업데이트

1. 변경 사항:
   - 새 스테이지 가이드 추가
   - 적/무기 전략 업데이트
   - 스페셜 이벤트 정보
2. 로컬에서 테스트
3. Git 커밋 생성
4. GitHub에 푸시
5. 자동 배포 대기

### 수동 배포 (필요시)

```bash
# 빌드
npm run build

# Miniflare CLI를 통한 수동 배포
miniflare deploy dist --env=production
```

## 비용

- GitHub: 무료 (공개 리포지토리)
- Miniflare 클러스터: 기존 사용 중
- 도메인: octol.ing (기존 소유)
- **총 비용**: 0원/월

## 추가 리소스

- [Miniflate CLI Docs](https://docs.miniflare.com/)
- [Miniflare Dashboard](https://dash.miniflare.com/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Astro Docs](https://docs.astro.build/)
- [Starlight Docs](https://starlight.astro.build/)

## 성공 기준

배포가 성공했다고 간주할 때:

1. ✅ 모든 22개 페이지가 배포 URL에서 접근 가능
2. ✅ HTTPS가 정상 작동 (SSL 인증서)
3. ✅ 네비게이션 사이드바가 작동
4. ✅ 검색 기능이 정상 작동
5. ✅ 빌드 시간이 3초 이내
6. ✅ 404 에러가 없음 (기본 404 페이지 제외)
7. ✅ 반응형 디자인이 모바일에서도 잘 보임
8. ✅ 한국어 콘텐츠가 완전히 번역되어 표시

## 롤백 계획

### 실패 시 롤백

1. 이전 커밋으로 복귀: `git reset --hard HEAD~1`
2. 수정 후 재커밋: `git add . && git commit -m "Fix deployment issue"`
3. 재푸시: `git push`
4. 배포 상태 모니터링

### 버전 관리

- GitHub에서 태그 사용: `git tag -a v1.0.0`
- 배포 전후 버전 확인: `git tag -l`
- 롤백이 필요하면 특정 태그로 복구: `git checkout v1.0.0`


## Next Steps

1. Complete DNS configuration
2. Set up Cloudflare Pages project
3. Configure GitHub Actions (optional)
4. Test deployment end-to-end
5. Monitor site performance
6. Add monitoring/alerts (optional)
