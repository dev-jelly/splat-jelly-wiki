// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://sp-wiki.octol.ing',
	integrations: [
		starlight({
			title: 'Splat Jelly Wiki',
			description: '스플래툰 3 연어런 공략 & 번역 사이트',
			lastUpdated: true,
			customCss: ['./src/styles/custom.css'],
			sidebar: [
				{
					label: '연어런 가이드',
					items: [
						{ label: '홈 (기본 룰)', link: '/' },
						{ label: '고급 테크닉', link: '/guides/techniques/' },
						{ label: '연어의 종류', items: [
							{ label: '적 목록', link: '/enemies/' },
							{ label: '대물 연어 공략', link: '/enemies/boss-salmon/' },
							{ label: '일반 연어 가이드', link: '/enemies/small-fry/' },
						]},
						{ label: '무기 및 기어', link: '/weapons/' },
						{ label: '특수 상황', link: '/special-situations/' },
						{ label: '이벤트 (빅 런)', link: '/events/' },
					],
				},
				{
					label: '일반 스테이지 (상시)',
					items: [
						{ label: '스테이지 목록', link: '/stages/' },
						{ label: '셰케나 댐', link: '/stages/spawning-grounds/' },
						{ label: '아라마키 요새', link: '/stages/sockeye-station/' },
						{ label: '무니 엘 해양 발전소', link: '/stages/gone-fission-hydroplant/' },
						{ label: '난파선 돈 브라코', link: '/stages/marooners-bay/' },
						{ label: '스지코 정션 터', link: '/stages/jammin-salmon-junction/' },
						{ label: '토키라즈 이부시 공방', link: '/stages/salmonid-smokeyard/' },
						{ label: '돈피코 투기장', link: '/stages/bonerattle-arena/' },
					],
				},
				{
					label: '빅 런 스테이지 (이벤트)',
					items: [
						{ label: '스메시 월드', link: '/stages/maho-mahi-resort/' },
						{ label: '해녀 미술 대학', link: '/stages/undam-burger/' },
						{ label: '타라포트 쇼핑 파크', link: '/stages/stageworks/' },
						{ label: '곤즈이 지구', link: '/stages/familys-bend/' },
						{ label: '쇼어사이드 스크랩 야드', link: '/stages/shoreside-scrapyard/' },
						{ label: '뉴 앨배코어 호텔', link: '/stages/new-albacore-hotel/' },
					],
				},
			],
		}),
	],
});
