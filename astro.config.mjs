// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
	site: 'https://sp-wiki.octol.ing',
	trailingSlash: 'always',
	prefetch: {
		prefetchAll: true,
		defaultStrategy: 'hover'
	},
	i18n: {
		defaultLocale: 'ko',
		locales: ['ko'],
	},
	integrations: [
		starlight({
			title: 'Splat Jelly Wiki',
			description: '스플래툰 3 새먼 런 공략 & 번역 사이트',
			lastUpdated: true,
			defaultLocale: 'ko',
			customCss: ['./src/styles/custom.css'],
			social: {
				github: 'https://github.com/dev-jelly/splat-jelly-wiki',
			},
			head: [
				{
					tag: 'meta',
					attrs: { property: 'og:type', content: 'website' },
				},
				{
					tag: 'meta',
					attrs: { property: 'og:locale', content: 'ko_KR' },
				},
				{
					tag: 'meta',
					attrs: { property: 'og:site_name', content: 'Splat Jelly Wiki' },
				},
				{
					tag: 'meta',
					attrs: { property: 'og:image', content: 'https://sp-wiki.octol.ing/og-main.png' },
				},
				{
					tag: 'meta',
					attrs: { name: 'twitter:card', content: 'summary_large_image' },
				},
				{
					tag: 'meta',
					attrs: { name: 'twitter:image', content: 'https://sp-wiki.octol.ing/og-main.png' },
				},
				{
					tag: 'meta',
					attrs: { name: 'theme-color', content: '#f5a623' },
				},
			],
			sidebar: [
				{
					label: '새먼 런 가이드',
					items: [
						{ label: '홈 (기본 룰)', link: '/' },
						{ label: '고급 테크닉', link: '/guides/techniques/' },
						{ label: '연어의 종류', items: [
							{ label: '적 목록', link: '/enemies/' },
							{ label: '거물 연어 공략', link: '/enemies/boss-salmon/' },
							{ label: '조무래기 연어 가이드', link: '/enemies/small-fry/' },
						]},
						{ label: '무기 및 기어', items: [
							{ label: '전체 요약', link: '/weapons/' },
							{ label: '슈터', link: '/weapons/shooters/' },
							{ label: '블래스터', link: '/weapons/blasters/' },
							{ label: '차저', link: '/weapons/chargers/' },
							{ label: '롤러 & 붓', link: '/weapons/rollers-brushes/' },
							{ label: '슬로셔', link: '/weapons/sloshers/' },
							{ label: '스피너', link: '/weapons/splatlings/' },
							{ label: '마뉴버', link: '/weapons/dualies/' },
							{ label: '쉘터', link: '/weapons/brellas/' },
							{ label: '스트링거 & 와이퍼', link: '/weapons/stringers-wipers/' },
						]},
						{ label: '특수 상황', link: '/special-situations/' },
						{ label: '이벤트 (빅 런)', link: '/events/' },
					],
				},
				{
					label: '일반 스테이지 (상시)',
					items: [
						{ label: '스테이지 목록', link: '/stages/' },
						{ label: '셰케나 댐', link: '/stages/spawning-grounds/' },
						{ label: '연어말이 요새', link: '/stages/sockeye-station/' },
						{ label: '뫼니 엘 해양 발전소', link: '/stages/gone-fission-hydroplant/' },
						{ label: '난파선 돈・브라코', link: '/stages/marooners-bay/' },
						{ label: '연어알젓 교차로 옛터', link: '/stages/jammin-salmon-junction/' },
						{ label: '사계절 훈제 공방', link: '/stages/salmonid-smokeyard/' },
						{ label: '연어 심장 투기장', link: '/stages/bonerattle-arena/' },
					],
				},
				{
					label: '빅 런 스테이지 (이벤트)',
					items: [
						{ label: '초밥 월드', link: '/stages/wahoo-world/' },
						{ label: '해녀 미술 대학', link: '/stages/inkblot-art-academy/' },
						{ label: '맛조개 방수로', link: '/stages/undertow-spillway/' },
						{ label: '남플라 유적', link: '/stages/umami-ruins/' },
						{ label: '대구 포트 쇼핑 파크', link: '/stages/barnacle-and-dime/' },
						{ label: '메기 지구', link: '/stages/eeltail-alley/' },
						{ label: '대치 시장', link: '/stages/crableg-capital/' },
					],
				},
			],
		}),
		sitemap(),
	],
});
