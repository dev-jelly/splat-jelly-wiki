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
					label: '연어런 공략',
					items: [
						{ label: '연어런 NEXT WAVE', link: '/' },
						{
							label: '스테이지',
							autogenerate: { directory: 'stages' },
						},
						{
							label: '적',
							autogenerate: { directory: 'enemies' },
						},
						{
							label: '무기',
							autogenerate: { directory: 'weapons' },
						},
						{
							label: '특수 상황',
							autogenerate: { directory: 'special-situations' },
						},
						{
							label: '이벤트',
							autogenerate: { directory: 'events' },
						},
					],
				},
			],
		}),
	],
});
