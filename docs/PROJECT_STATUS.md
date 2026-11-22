# Project status

Last updated: 2026-11-22. Repository root: `<project-root>`.

## Production-readiness pass

| Area | Status | Evidence / remaining work |
|---|---|---|
| Static build | Implemented | `scripts/build_site.py` generates `dist/`, normalizes query-bearing asset filenames, and writes `/` and `/demos/city-2/`. |
| Asset checks | Implemented | `scripts/check_site.py` checks both routes, local Framer references, module imports, query-free output names, and localhost references. |
| Wedding content | Updated | Haldi, Sakharpuda, wedding date/time and full venue address match supplied details. Unconfirmed March events are hidden; weather/staff copy is removed. |
| Outbound destinations | Pending confirmation | Map, WhatsApp and Instagram CTAs are hidden until their destinations are confirmed. |
| Browser review | Partial | Isolated browser confirmed hydration, content, countdown, music activation on click, and gallery rendering. Console/network logs and requested viewport matrix remain untested. |
| Deployment | READY | Preview created from `fix/production-readiness`; an anonymous HTTP request redirects to Vercel SSO. No production promotion was made. |
| Repository visibility | Finding | GitHub reports `AimBotFTW/ShivKetan` as public, despite older docs describing it as private. |
| Licensing | Unresolved | Missing Piece template terms remain unresolved. |

The repository is on `fix/production-readiness`; changes are reviewable on that feature branch. No changes were made to original assets or backups.

## Verified asset inventory

- The project tree is about 62 MB; no individual file exceeds 50 MB. The largest items are clean palace PNG variants, the local song, and large portrait/landscape PNGs. No large file was excluded from this local checkout.
- `download/framerusercontent.com/images/`: 82 local files. Eight clean image families have 22 clean PNG variants total (fLGaml 3, d1VX 2, EdGE 4, Gg2X 3, 0VfGPT 4, SSy3 3, T1dOR 2, O07f 1); every family and variant is referenced in active HTML and custom MJS, and all 22 clean files exist locally. Twenty-two original non-clean variants remain as source/history assets, not active personalized-page dependencies.
- `download/framerusercontent.com/assets/`: 58 files, including `sajiri-gojiri.mp3` and the older template MP3.
- `download/framerusercontent.com/sites/`: 20 active MJS modules and four MJS backup files; the backups are not runtime modules.
- There are nine backups across the project and eight non-runtime watermark review files. Eleven Markdown documents exist across the root, `docs/` and `download/`.
- Demo pages: `city-2-local.html` is active and personalized; `city-2-original.html` is a reference snapshot with remote dependencies and unverified pristine status; `city-2.html` is obsolete, not selected by the active route, and a candidate for eventual Git exclusion. It has not been removed.
- The active page still references remote Framer/CDN resources and Google fonts. The Apple touch icon and Open Graph/Twitter image references are missing locally. The custom MJS has the missing WtUt asset in the `Hashtag` component's default icon. Browser hydration and network behavior remain unverified; the page still depends on remote resources and has not been browser-tested.
- The demos directory has three HTML files. Backup inventory includes the earlier `.bak`, `.bak-wm` and `.bak-wm2` snapshots plus later `.bak-finalcars` snapshots; all are ignored and preserved. No backup was deleted.

## Collaboration and sharing status

1. The intended workflow is local development and commits, then private GitHub collaboration with the owner's brother. Public distribution and public hosting are not currently intended.
2. The owner confirmed permission to include and share `sajiri-gojiri.mp3` for the intended project arrangement; this does not establish unrestricted public redistribution rights.
3. The Missing Piece template terms include restrictions on redistribution/sharing, third-party use and watermark alteration. See [IMAGES.md](IMAGES.md#licensing-and-sharing) for the concise factual note; do not infer broader rights from private collaboration.
4. GitHub currently reports the supplied repository as public. The project Vercel settings show SSO protection enabled for deployments.
5. The active page hides unconfirmed outbound destinations and unconfirmed event cards; see `KNOWN_ISSUES_AND_TODO.md`.
