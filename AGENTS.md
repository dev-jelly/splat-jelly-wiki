# PROJECT KNOWLEDGE BASE

**Generated:** 2026-01-14
**Commit:** 86a3650
**Branch:** main

## OVERVIEW

Splatoon 3 Salmon Run wiki/guide site built with Astro Starlight. Korean docs site deployed to GitHub Pages at `sp-wiki.octol.ing`.

## STRUCTURE

```
splat-jelly-wiki/
├── src/
│   ├── content/docs/     # MDX content (stages, enemies, weapons, events)
│   ├── components/       # Astro components (Search, Sidebar)
│   ├── layouts/          # Page layouts
│   ├── styles/           # CSS (custom.css loaded by Starlight)
│   └── utils/            # search.ts - client-side search
├── scripts/              # DNS setup/verification bash scripts
├── astro.config.mjs      # Starlight config, sidebar structure
├── tailwind.config.js    # Theme colors (salmon-*)
└── dist/                 # Build output (gitignored in prod)
```

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Add new stage guide | `src/content/docs/stages/*.mdx` | Auto-added to sidebar |
| Add new enemy guide | `src/content/docs/enemies/*.mdx` | Auto-added to sidebar |
| Modify sidebar structure | `astro.config.mjs` | `sidebar.items` array |
| Change site metadata | `astro.config.mjs` | `title`, `description`, `site` |
| Custom styling | `src/styles/custom.css` | Loaded via `customCss` config |
| Theme colors | `tailwind.config.js` | `salmon.*` color palette |
| Search functionality | `src/utils/search.ts` | Static index, client-side filter |
| Homepage | `src/content/docs/index.mdx` | Large file (~38KB) |
| DNS/deployment scripts | `scripts/` | `setup-dns.sh`, `verify-dns.sh` |

## CONVENTIONS

### Content (MDX)
- Korean language content
- Frontmatter: `title`, `description` (Starlight schema)
- Each content directory has `index.mdx` as section landing
- Starlight `autogenerate: { directory: 'X' }` populates sidebars

### Styling
- CSS variables in `custom.css` (--color-primary: #f5a623)
- Tailwind for MDX content only (see `content` path in config)
- Korean fonts: 'Noto Sans KR' fallback

### Search
- Static search index in `src/utils/search.ts`
- Manually maintained (not auto-generated)
- Exposed as `window.salmonRunSearch.search()`

## ANTI-PATTERNS (THIS PROJECT)

- **DO NOT** add Tailwind to components/layouts (only MDX content)
- **DO NOT** modify search URLs without updating `src/utils/search.ts` manually
- **DO NOT** use `src/pages/` for content (use Content Collections in `src/content/docs/`)

## UNIQUE STYLES

- `tailwind.config.js` has duplicate `darkMode` keys (line 19-20) - harmless but unusual
- Homepage `index.mdx` is unusually large (~38KB) - contains full guide content
- Search index is hardcoded, not dynamically built from content

## COMMANDS

```bash
npm run dev      # Start dev server
npm run build    # Production build
npm run preview  # Preview production build

# DNS verification (after deployment)
bash scripts/setup-dns.sh
bash scripts/verify-dns.sh
```

## NOTES

- Site URL: `https://sp-wiki.octol.ing` (requires DNS CNAME to `dev-jelly.github.io`)
- GitHub Pages deployment via GitHub Actions
- No test suite
- TypeScript minimal (only `src/utils/search.ts`, `src/content.config.ts`)
- `.sisyphus/plans/` contains AI planning artifacts (ignore)
