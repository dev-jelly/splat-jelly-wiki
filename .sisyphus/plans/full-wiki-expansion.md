# Plan: Expand Splat Jelly Wiki to Full Splatoon 3 Coverage

## Requirements Summary

- Expand current Salmon Run-focused wiki (21 pages) to cover all Splatoon 3 content
- Target: 500-800+ pages from https://wikiwiki.jp/splatoon3mix/
- Maintain existing Astro 5.0 + Starlight 0.30.6 + Tailwind CSS infrastructure
- Implement i18n for Japanese source → Korean translation
- Support future English localization
- Daily update sync with Japanese wiki

## Scope & Constraints

### In Scope
- All Japanese wiki content categories translated to Korean
- Infrastructure enhancements for i18n support
- Automated translation workflow setup
- Content maintenance and update system
- SEO optimization for Korean audience

### Out of Scope
- Rebuilding from scratch (leverage existing infrastructure)
- Image hosting (continue using existing CDN approach)
- Community features (comments, forums)
- User accounts/login system
- Real-time data synchronization (batch updates only)

### Technical Constraints
- Current: 22 HTML pages, 21 MDX files
- Target: 500-800+ pages (20-40x scale)
- Must maintain Starlight documentation theme
- Build time under 60 seconds
- Static site generation (no backend)

## Implementation Steps

### Phase 1: Infrastructure & i18n Setup (Week 1-2)

#### 1.1 Configure Astro i18n Routing
**File**: `astro.config.mjs`

```javascript
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://sp-wiki.octol.ink',
  integrations: [
    starlight({
      title: 'Splat Jelly Wiki',
      description: '스플래툰 3 공략 & 번역 사이트',
      defaultLocale: 'ko', // Korean as primary
      locales: ['ko', 'ja', 'en'], // Support for future expansion
      lastUpdated: true,
      customCss: ['./src/styles/custom.css'],
      sidebar: [
        {
          label: '기본 정보',
          items: [
            { label: '스플래툰 3 소개', link: '/ko/basic/intro' },
            { label: '시스템', link: '/ko/basic/system' },
            // ... more items
          ],
        },
        // ... other sections
      ],
    }),
  ],
});
```

**Action**: Update `astro.config.mjs` with locale configuration

#### 1.2 Create Multi-Language Content Structure
```
src/content/
  docs/
    ko/ (Korean - primary)
      index.mdx
      basic/
      online/
      stages/
      weapons/
      gear/
    ja/ (Japanese - source reference)
      index.mdx
      basic/
      online/
      stages/
    en/ (Future English support)
```

**Action**: Reorganize existing content into `ko/` directory, create `ja/` structure

#### 1.3 Setup Starlight i18n Configuration
**File**: `src/content/config.ts`

```typescript
import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema(),
  }),
};
```

**Action**: Keep existing config, ensure it supports multi-language content

#### 1.4 Create UI Translation Files
**Files**: `src/i18n/ko.json`, `src/i18n/ja.json`

```json
{
  "search.label": "검색",
  "selectLanguage": "언어 선택",
  "sidebar.menu": "메뉴",
  "page.edit": "편집",
  "page.history": "편집 내역",
  "theme.toggle": "테마 전환"
}
```

**Action**: Create translation dictionaries for Starlight UI elements

### Phase 2: Content Translation Strategy (Week 3-12)

#### 2.1 Translation Priority Matrix

| Priority | Category | Pages | Est. Words | Rationale |
|----------|----------|--------|------------|-----------|
| P0 | Online Battle Modes | ~50 pages | 50,000 | Core gameplay, highest traffic |
| P0 | Weapons (all 181) | ~200 pages | 120,000 | Most searched content |
| P1 | Stages (25 stages) | ~100 pages | 80,000 | Visual content, popular |
| P1 | Gear System | ~60 pages | 40,000 | Meta-game important |
| P1 | Salmon Run (updates) | ~30 pages | 20,000 | Already done, need sync |
| P2 | Offline Modes | ~40 pages | 30,000 | Story content, DLC |
| P2 | Events | ~20 pages | 15,000 | Time-limited content |
| P3 | Glossary/Reference | ~30 pages | 10,000 | Reference material |
| P4 | Wiki Management | ~10 pages | 5,000 | Meta content |

**Total**: ~540 pages, ~370,000 words

#### 2.2 Translation Workflow Setup

**Stack**: DeepL API + Weblate + Glossary Enforcement

**Tools Configuration**:
```
src/scripts/translation/
  ├── glossary/               # Terminology management
  │   ├── core-terms.json  # 100+ existing terms
  │   ├── weapons.json      # Weapon-specific terms
  │   └── abilities.json    # Ability names, effects
  ├── mt-config.json          # DeepL API settings
  └── qa-rules.js           # Quality control rules
```

**Workflow**:
1. **Fetch**: Script downloads updated pages from Japanese wiki
2. **Extract**: Extract content, preserve formatting, images
3. **Pre-translate**: Apply terminology glossary
4. **Machine Translate**: DeepL API with glossary enforcement
5. **Post-edit**: Manual review in Weblate
6. **Validate**: QA checks (terminology, formatting, links)
7. **Commit**: Merge to main branch → auto-deploy

#### 2.3 Expand Terminology Dictionary

**File**: `japanese-korean-terminology-expanded.json`

Add new categories:
```json
{
  "weapons": {
    "シューター": "슈터",
    "マニューバー": "매뉴버",
    "ブラスター": "블래스터",
    "ローラー": "롤러",
    "フデ": "붓",
    "チャージャー": "차저",
    "スピナー": "스피너",
    "スロッシャー": "슬로셔",
    "シェルター": "쉘터",
    "ストリンガー": "스트링거",
    "ワイパー": "와이퍼"
  },
  "battle_modes": {
    "ナワバリバトル": "터레인 배틀",
    "バンカラマッチ": "앵커리 매치",
    "フェスマッチ": "페스 매치",
    "トリカラバトル": "트리컬러 배틀",
    "レギュラーマッチ": "레귤러 매치",
    "プライベートマッチ": "프라이빗 매치",
    "Xマッチ": "X 매치"
  },
  "gear_powers": {
    "インク効率アップ(メイン)": "잉크 효율 업(메인)",
    "インク効率アップ(サブ)": "잉크 효율 업(서브)",
    "ヒト移動速度アップ": "히트 이동속도 업",
    "スペシャル増加量アップ": "스페셜 증가량 업"
  },
  "stage_features": {
    "インクレール": "잉크 레일",
    "スポンジ": "스펀지",
    "シフト": "시프트",
    "ガチエリア": "가치 에어리어",
    "ガチヤグラ": "가치 야그라",
    "ガチホコバトル": "가치 호코 배틀",
    "ガチアサリ": "가치 아사리"
  }
}
```

**Action**: Expand dictionary to 500+ terms covering all game categories

#### 2.4 Category-Specific Translation Plans

##### 2.4.1 Online Battle Modes (Priority P0)

**Pages to Create** (~50 pages):

**Core Structure**:
```
src/content/docs/ko/online/
  index.mdx                    # Overview of all modes
  regular-match/
    index.mdx                # Regular Match guide
  turf-war/
    index.mdx                # Turf War rules, strategies
  anarchy-match/
    index.mdx                # Anarchy Match overview
    areas/index.mdx           # Ranked Areas
    rainmaker/index.mdx        # Ranked Rainmaker
    clam-blitz/index.mdx       # Ranked Clam Blitz
    tower-control/index.mdx     # Ranked Tower Control
  x-match/
    index.mdx                # X Match details
  private-match/
    index.mdx                # Private Match setup
```

**Template**: Each mode page includes:
- Mode rules and objectives
- Stage selection (25 stages)
- Win/loss conditions
- Scoring system
- Strategy guides
- Team composition tips
- Update history

**Estimation**: 50 pages × 1,000 words = 50,000 words

##### 2.4.2 Weapons (Priority P0)

**Pages to Create** (~200 pages for 181 weapons):

**Structure**:
```
src/content/docs/ko/weapons/
  index.mdx                    # Weapons overview
  shooters/
    index.mdx                # Shooters category
    wakaba-shooter.mdx       # Individual weapons
    bold-marker.mdx
    sharp-marker.mdx
    promodeler.mdx
    spla-shooter.mdx
    .52-galon.mdx
    n-zap.mdx
    prime-shooter.mdx
    .96-galon.mdx
    jet-sweeper.mdx
    # ... 28 total shooters
  rollers/
    index.mdx                # Rollers category
    spla-roller.mdx
    dynamo-roller.mdx
    carbon-roller.mdx
    variable-roller.mdx
    wide-roller.mdx
  chargers/
    index.mdx                # Chargers category
    spla-charger.mdx
    squiffer.mdx
    e-liter.mdx
    # ... 16 total chargers
  sloshers/
  splatters/
  splatlings/
  blasters/
  brushes/
  stringers/
  wipers/
  specials/
    index.mdx                # Special weapons overview
    ultra-shot.mdx
    great-barrier.mdx
    ink-storm.mdx
    multi-missile.mdx
    # ... 20 specials
  subs/
    index.mdx                # Sub weapons
    splat-bomb.mdx
    curling-bomb.mdx
    splash-bomb.mdx
    # ... 14 subs
```

**Template**: Each weapon page includes:
- Weapon stats (damage, range, fire rate, mobility)
- Sub weapon and special weapon
- Playstyle
- Recommended gear builds
- Stage performance
- Counter strategies
- Update history

**Estimation**: 181 weapons × 600 words = 108,600 words

##### 2.4.3 Stages (Priority P1)

**Pages to Create** (~100 pages for 25 stages):

**Structure**:
```
src/content/docs/ko/stages/
  index.mdx                    # Stage list overview
  # Splatsville stages (13)
  yunohana-canyon.mdx
  gonzi-district.mdx
  yagara-market.mdx
  mate-gami-waterway.mdx
  namero-metal.mdx
  masaba-highway-bridge.mdx
  kinmei-museum.mdx
  mahi-mahi-resort.mdx
  # ... more stages
  # Inkopolis stages (12)
  masaba-channel.mdx
  kinmei-art-museum.mdx
  mahi-mahi-resort-spa.mdx
  # ... more stages

  # Each stage has:
  stage-name/
    index.mdx                # Overview
      turf-war.mdx           # Turf War layout
      ranked-modes.mdx        # Ranked variations
      images/                 # Screenshots per mode
```

**Template**: Each stage page includes:
- Stage overview (size, layout, symmetry)
- Mode-specific maps (Turf War, Ranked)
- Key positions (spawns, objectives, chokepoints)
- Stage-specific strategies
- Image gallery per mode
- Update history

**Estimation**: 25 stages × 4 modes × 800 words = 80,000 words

##### 2.4.4 Gear (Priority P1)

**Pages to Create** (~60 pages):

**Structure**:
```
src/content/docs/ko/gear/
  index.mdx                    # Gear system overview
  gear-powers/
    index.mdx                # All 30 gear powers
    ink-efficiency-main.mdx
    ink-efficiency-sub.mdx
    movement-speed-up.mdx
    special-charge-up.mdx
    # ... 26 more powers
  brands/
    index.mdx                # Brand system
    ami.mdx                  # Gear brands (30 brands)
    cuttleg.mdx
    forge.mdx
    inkline.mdx
    # ... more brands
  gear-sets/
    index.mdx                # Recommended builds
```

**Template**: Each gear page includes:
- Effect description
- Stack potential
- Compatible builds
- Cost/availability
- Brand bonuses

**Estimation**: 60 pages × 650 words = 39,000 words

##### 2.4.5 Offline Modes (Priority P2)

**Pages to Create** (~40 pages):

**Structure**:
```
src/content/docs/ko/offline/
  index.mdx                    # Offline modes overview
  hero-mode/
    index.mdx                # Hero Mode overview
    stages/                  # Stage guides
    octarians/                # Enemy encyclopedia
    bosses/                  # Boss strategies
  side-order/
    index.mdx                # Side Order overview
    palettes/
    color-chips/
    floors/
  card-battler/
    index.mdx                # Card game guide
```

**Estimation**: 40 pages × 750 words = 30,000 words

### Phase 3: Automation & Tooling (Week 4-8)

#### 3.1 Content Sync Script

**File**: `src/scripts/sync-wiki.mjs`

```javascript
import fetch from 'node-fetch';
import RSS from 'rss-parser';

const RSS_URL = 'https://wikiwiki.jp/splatoon3mix/::cmd/mixirss';

export async function syncJapaneseWiki() {
  const feed = await fetch(RSS_URL).then(r => r.text());
  const parsed = await RSS.parse(feed);

  const updatedPages = parsed.items
    .filter(item => item.pubDate > lastSyncTime)
    .map(item => ({
      title: item.title,
      url: item.link,
      pubDate: item.pubDate
    }));

  console.log(`Found ${updatedPages.length} updated pages`);
  return updatedPages;
}

syncJapaneseWiki().then(pages => {
  // Trigger translation pipeline for each page
});
```

**Action**: Create sync script that polls RSS for changes

#### 3.2 Translation Pipeline Script

**File**: `src/scripts/translate-pipeline.mjs`

```javascript
import DeepL from 'deepl-node';

const deepL = new DeepL({
  authKey: process.env.DEEPL_API_KEY,
  glossaries: process.env.DEEPL_GLOSSARY_ID
});

async function translatePage(japaneseContent) {
  // 1. Extract translatable text
  const text = extractTranslatableContent(japaneseContent);

  // 2. Apply terminology constraints
  const constrained = applyGlossaryConstraints(text);

  // 3. Machine translate
  const translated = await deepL.translateText(constrained, 'ja', 'ko');

  // 4. Post-process formatting
  const formatted = preserveMarkdownFormatting(translated);

  return formatted;
}
```

**Action**: Create translation pipeline with glossary enforcement

#### 3.3 Quality Control Automation

**File**: `src/scripts/qa-check.mjs`

```javascript
export function validateTranslation(koreanContent) {
  const issues = [];

  // Check 1: Terminology compliance
  issues.push(...checkTerminology(koreanContent));

  // Check 2: Markdown formatting
  issues.push(...checkMarkdownSyntax(koreanContent));

  // Check 3: Link integrity
  issues.push(...checkInternalLinks(koreanContent));

  // Check 4: Image references
  issues.push(...checkImageLinks(koreanContent));

  return issues;
}
```

**Action**: Create automated QA checks

#### 3.4 Build Optimization

**Target**: Build time < 60 seconds for 800+ pages

**Strategies**:
1. Incremental builds (only changed pages)
2. Pre-render navigation
3. Optimize image processing
4. Cache compilation artifacts

**File**: `astro.config.mjs`

```javascript
export default defineConfig({
  build: {
    format: 'directory',
    inlineStylesheets: false,
  },
  vite: {
    build: {
      chunkSizeWarningLimit: 1000,
    },
  },
});
```

### Phase 4: SEO & Performance (Week 6-8)

#### 4.1 Multilingual SEO Configuration

**File**: `src/layouts/Layout.astro`

```html
<link rel="alternate" hreflang="ko" href={`https://sp-wiki.octol.ink${currentPath}`} />
<link rel="alternate" hreflang="ja" href={`https://sp-wiki.octol.ink/ja${currentPath}`} />
<link rel="alternate" hreflang="en" href={`https://sp-wiki.octol.ink/en${currentPath}`} />
<link rel="alternate" hreflang="x-default" href={`https://sp-wiki.octol.ink${currentPath}`} />

<meta name="description" content={description} />
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
<meta property="og:url" content={`https://sp-wiki.octol.ink${currentPath}`} />
<meta property="og:type" content="article" />
```

**Action**: Implement proper hreflang and canonical tags

#### 4.2 Sitemap Generation

**File**: `astro.config.mjs` (already has `@astrojs/sitemap`)

Ensure sitemap includes:
- All Korean pages (`/ko/**`)
- All Japanese pages (`/ja/**`)
- Proper `lastmod` timestamps
- Proper priority values (weapons: 0.9, stages: 0.8, guides: 0.7)

#### 4.3 Core Web Vitals Optimization

**Target**: Lighthouse score > 90

**Actions**:
1. Lazy load images
2. Optimize images (WebP, responsive sizes)
3. Minify CSS/JS
4. Implement code splitting
5. Cache static assets

### Phase 5: Deployment Strategy (Week 7-8)

#### 5.1 Update CI/CD Pipeline

**File**: `.github/workflows/deploy.yml`

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]
    paths:
      - 'src/content/**'
      - 'src/i18n/**'
      - 'astro.config.mjs'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Build site
        run: npm run build
        timeout-minutes: 10

      - name: Run Lighthouse CI
        uses: treosh/lighthouse-ci-action@v10
        with:
          urls: |
            https://sp-wiki.octol.ink
            https://sp-wiki.octol.ink/ko/weapons/
          uploadArtifacts: true

      - name: Deploy to Miniflare
        uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.MINIFLARE_API_TOKEN }}
          accountId: ${{ secrets.MINIFLARE_ACCOUNT_ID }}
          command: deploy --env=production
```

**Action**: Update deployment pipeline with performance checks

#### 5.2 Rollback Strategy

**Mechanism**:
1. Keep last 5 deployments in Miniflare
2. GitHub Actions retains build artifacts
3. DNS TTL: 3600s (1 hour)

**Procedure**:
```bash
# Rollback to previous version
git revert HEAD~1
git push
# GitHub Actions auto-deploys
```

### Phase 6: Content Maintenance (Ongoing)

#### 6.1 Weekly Sync Schedule

**Monday**: Sync Japanese wiki updates
**Tuesday**: Translate new/updated pages
**Wednesday**: QA review
**Thursday**: Deploy to production
**Friday**: Analytics review

#### 6.2 Update Monitoring

**Metrics to Track**:
- Pages translated vs. Japanese wiki total
- Average time lag (Japanese update → Korean update)
- Search traffic per category
- User feedback (quality issues, missing content)

**Dashboard**: Create simple tracking in PROJECT_STATUS.md

#### 6.3 Community Integration

**Feedback Mechanisms**:
1. GitHub Issues for content requests
2. Discussion tab for strategy sharing
3. Pull requests for community translations
4. Wiki talk pages (future)

### Phase 7: English Support (Future - Phase 8)

**Placeholder Structure**:
```
src/content/docs/en/
  basic/
  online/
  stages/
  weapons/
  # Mirror of Korean structure
```

**Timeline**: After Korean completion (Month 4-6)

## Acceptance Criteria

- [ ] **Phase 1**: i18n routing configured, multi-language structure created
- [ ] **Phase 2**: 500+ pages translated (P0+P1 categories complete)
- [ ] **Phase 3**: Automated translation pipeline operational
- [ ] **Phase 4**: SEO configuration complete, Lighthouse > 90
- [ ] **Phase 5**: CI/CD pipeline updated, < 10min deploy time
- [ ] **Phase 6**: Weekly sync schedule established
- [ ] **Performance**: Build time < 60s, First Contentful Paint < 1.8s
- [ ] **Quality**: Terminology consistency > 95%, broken links < 1%
- [ ] **Coverage**: All Japanese wiki P0+P1 content translated

## Risk Mitigations

| Risk | Impact | Probability | Mitigation |
|------|---------|--------------|-------------|
| Translation quality issues | High | Medium | Glossary enforcement + human review workflow |
| Japanese wiki format changes | Medium | Low | Abstracted content extraction + format normalization |
| DeepL API limits/costs | Medium | Medium | Caching + rate limiting + alternative MT provider |
| Build time explosion | Medium | Low | Incremental builds + build optimization |
| Content updates overwhelm team | High | High | PRIORITY system (P0 > P1 > P2) |
| Terminology drift | High | Medium | Centralized glossary + automated checks |
| Broken links/404s | Low | High | Automated link checker in CI |
| SEO duplicate content | Medium | Low | Proper hreflang + canonical tags |

## Verification Steps

### 1. Infrastructure Verification
```bash
# Test i18n routing
npm run dev
# Visit /ko/ (should work)
# Visit /ja/ (should show Japanese)
# Visit /en/ (should show placeholder)

# Test build
npm run build
# Verify < 60s build time
# Verify all 500+ pages generated
```

### 2. Content Quality Verification
```bash
# Run terminology check
node src/scripts/qa-check.mjs

# Run link checker
npm run check-links

# Sample manual review
# Review 10 random pages for:
# - Translation quality
# - Formatting consistency
# - Image references
# - Internal links
```

### 3. Performance Verification
```bash
# Run Lighthouse CI
npx lighthouse https://sp-wiki.octol.ink --view

# Check core web vitals
# - LCP < 2.5s
# - FID < 100ms
# - CLS < 0.1
```

### 4. Deployment Verification
```bash
# Deploy to production
git push origin main

# Wait for GitHub Actions
# Check build logs

# Verify production site
curl -I https://sp-wiki.octol.ink
curl -I https://sp-wiki.octol.ink/ko/weapons/

# Check sitemap
curl https://sp-wiki.octol.ink/sitemap-index.xml
```

### 5. SEO Verification
```bash
# Test search console
# Google Search Console index status

# Test robots.txt
curl https://sp-wiki.octol.ink/robots.txt

# Test canonicals
curl https://sp-wiki.octol.ink/ko/weapons/ | grep canonical

# Test hreflang
curl https://sp-wiki.octol.ink/ko/weapons/ | grep hreflang
```

## Timeline and Resource Estimates

### Phase 1: Infrastructure (2 weeks)
- Week 1: i18n config, content structure reorganization
- Week 2: UI translation files, basic templates
- **Resource**: 1 developer (full-time)
- **Milestone**: Multi-language site builds successfully

### Phase 2: Core Content Translation (10 weeks)
- Weeks 3-4: Online Battle Modes (50 pages)
- Weeks 5-7: Weapons (200 pages) - PRIORITY
- Weeks 8-9: Stages (100 pages)
- Weeks 10-12: Gear (60 pages)
- **Resource**: 1 translator + 1 reviewer (full-time)
- **Milestone**: P0+P1 content complete (300+ pages)

### Phase 3: Automation (4 weeks, parallel with Phase 2)
- Weeks 4-5: Translation pipeline scripts
- Weeks 6-7: QA automation
- Week 8: Sync scripts
- **Resource**: 1 developer (part-time)
- **Milestone**: Automated translation operational

### Phase 4: SEO & Performance (3 weeks, parallel)
- Weeks 6-7: SEO configuration
- Week 8: Performance optimization
- **Resource**: 1 developer (part-time)
- **Milestone**: Lighthouse > 90, build < 60s

### Phase 5: Deployment (2 weeks)
- Weeks 7-8: CI/CD updates, rollback procedures
- **Resource**: 1 DevOps (part-time)
- **Milestone**: Reliable < 10min deploys

### Phase 6: Maintenance (ongoing)
- Starting Week 9: Weekly sync schedule
- Ongoing: Update monitoring, feedback collection
- **Resource**: 1 maintainer (part-time)
- **Milestone**: Consistent updates, < 7-day lag

### Total Project Timeline: **12-14 weeks (3-4 months)**

### Cost Estimates

| Item | Monthly Cost | Notes |
|------|--------------|-------|
| DeepL API | $50-$100 | Depends on volume (free tier: 500k chars/month) |
| GitHub Actions | $0 | Public repo, free tier |
| Miniflare | $0 | Already paid |
| Domain | ~$10/year | octol.ink already owned |
| **Total Monthly** | **$50-$100** | Primarily translation API |
| **Total Project** | **$150-$300** | 3-4 month project |

### Human Resource Summary

| Role | Time Commitment | Notes |
|------|-----------------|-------|
| Developer (Infrastructure) | 8 weeks full-time | Phases 1, 3, 4, 5 |
| Translator | 10 weeks full-time | Phase 2 content translation |
| Reviewer | 10 weeks full-time | Phase 2 quality review |
| Maintainer | Ongoing part-time | Phase 6 updates |
| **Total Effort** | ~30 person-weeks | Spread across 3-4 months |

## Next Steps

### Immediate (This Week)
1. **Review and approve plan** with stakeholders
2. **Set up DeepL API account** and get API key
3. **Initialize i18n structure** in repository
4. **Create translation glossary** expansion (500+ terms)
5. **Set up Weblate** or alternative translation platform

### Week 1-2 Priorities
1. **Configure Astro i18n** routing
2. **Create Korean content structure** (`src/content/docs/ko/`)
3. **Migrate existing content** to `ko/` directory
4. **Create UI translation files** (`src/i18n/*.json`)
5. **Test multi-language builds**

### Week 3-4 Priorities
1. **Start Online Battle Modes translation** (P0 priority)
2. **Build translation pipeline script**
3. **Implement RSS sync mechanism**
4. **Create 50 online mode pages**

### Month 2 Priorities
1. **Complete Weapons translation** (P0 priority, 200 pages)
2. **Automate terminology enforcement**
3. **Implement QA checks**
4. **SEO configuration (hreflang, sitemap)**

### Month 3-4 Priorities
1. **Complete Stages translation** (P1 priority, 100 pages)
2. **Complete Gear translation** (P1 priority, 60 pages)
3. **Performance optimization** (build time, Core Web Vitals)
4. **Production deployment**
5. **Establish weekly sync schedule**

### Success Metrics

**Content Coverage**:
- Korean pages: 500+ (vs. Japanese 800+)
- Coverage rate: > 60% of Japanese wiki
- Update lag: < 7 days average

**Quality Metrics**:
- Terminology consistency: > 95%
- User-reported issues: < 5/month
- Translation accuracy: > 90% (human-reviewed)

**Performance Metrics**:
- Build time: < 60s
- Lighthouse score: > 90
- First Contentful Paint: < 1.8s
- Time to Interactive: < 3.5s

**SEO Metrics**:
- Indexed pages: 400+ (Google Search Console)
- Organic traffic growth: +20% month-over-month
- Average position: Top 10 for "스플래툰 3 공략" queries

**Engagement Metrics**:
- Monthly unique visitors: > 5,000
- Average pages per session: > 3
- Bounce rate: < 50%
- Return visitor rate: > 30%

## Appendix

### A. Japanese Wiki Category Mapping

| Japanese Category | Korean Translation | Page Count | Priority |
|------------------|---------------------|--------------|----------|
| 基本情報 | 기본 정보 | 20 | P2 |
| オンライン対戦 | 온라인 대전 | 50 | P0 |
| ステージ | 스테이지 | 100 | P1 |
| サーモンラン | 연어런 | 30 | P1 |
| ブキ | 무기 | 200 | P0 |
| ギア | 기어 | 60 | P1 |
| イベント | 이벤트 | 20 | P2 |
| オフラインモード | 오프라인 모드 | 40 | P2 |
| その他 | 기타 | 30 | P3 |
| 当Wikiについて | 위키 정보 | 10 | P4 |
| **Total** | | **560** | |

### B. Technology Stack

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| Static Site Generator | Astro | 5.0.0 | Core framework |
| Documentation Theme | Starlight | 0.30.6 | UI/components |
| Styling | Tailwind CSS | 3.4.19 | Custom styles |
| Language | TypeScript | 5.7.2 | Type safety |
| Package Manager | npm | 20+ | Dependency management |
| Deployment | Miniflare | Latest | Hosting |
| CI/CD | GitHub Actions | Latest | Automation |
| Translation API | DeepL | Latest | Machine translation |
| Translation Management | Weblate or OmegaT | Latest | Human review |
| Quality Assurance | Custom scripts | - | Terminology checks |

### C. File Structure (Final)

```
splat-jelly-wiki/
├── src/
│   ├── content/
│   │   └── docs/
│   │       ├── ko/           # Korean (primary)
│   │       │   ├── index.mdx
│   │       │   ├── basic/
│   │       │   ├── online/
│   │       │   ├── stages/
│   │       │   ├── salmon-run/
│   │       │   ├── weapons/
│   │       │   ├── gear/
│   │       │   ├── events/
│   │       │   ├── offline/
│   │       │   └── other/
│   │       ├── ja/           # Japanese (reference)
│   │       └── en/           # Future English
│   ├── i18n/                # UI translations
│   │   ├── ko.json
│   │   ├── ja.json
│   │   └── en.json
│   ├── layouts/              # Astro layouts
│   ├── components/           # Vue/Svelte components
│   ├── scripts/              # Automation
│   │   ├── sync-wiki.mjs
│   │   ├── translate-pipeline.mjs
│   │   ├── qa-check.mjs
│   │   └── glossary/
│   └── styles/
├── public/                 # Static assets
├── astro.config.mjs          # i18n config
├── tailwind.config.js
├── tsconfig.json
├── package.json
├── japanese-korean-terminology-expanded.json
├── PROJECT_STATUS.md         # Updated with i18n status
├── DEPLOYMENT.md
└── EXPANSION_PLAN.md       # This document
```

### D. Translation Workflow Diagram

```
Japanese Wiki
    ↓ [RSS Feed]
Sync Script
    ↓ [Fetch Updated Pages]
Content Extractor
    ↓ [Normalize Format]
Glossary Applier
    ↓ [Enforce Terms]
DeepL API
    ↓ [Machine Translate]
Format Preserver
    ↓ [Markdown Fix]
Weblate
    ↓ [Human Review]
QA Checks
    ↓ [Terminology, Links]
Merge to Main
    ↓ [Git Push]
GitHub Actions
    ↓ [Build + Deploy]
Miniflare
    ↓
Production Site
```

### E. Glossary Categories

**Core Terms (100+)**:
- Game modes, UI elements, basic mechanics
- Enemy types, weapon categories
- Stage features, special conditions

**Weapons (150+)**:
- All weapon names, sub/special weapons
- Ability names, effect descriptions
- Brand names, gear powers

**Gear (100+)**:
- 30 gear powers
- 30 brand names
- Gear slot terminology

**Stages (50+)**:
- 25 stage names
- Mode-specific terms
- Map features (ink rails, sponges)

**Battle (100+)**:
- Ranked mode names
- Victory/loss conditions
- Scoring terminology

**Total**: 500+ terms

---

**Plan Version**: 1.0
**Created**: 2026-01-13
**Author**: Prometheus AI
**Status**: Draft - Pending Approval
