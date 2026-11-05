# Project status

Last updated: 2026-11-05. Repository root: `<project-root>`.

## Seven-step handoff

| Step | Status | Evidence / next action |
|---|---|---|
| 1. Inspect | Complete | Project-local `.git` was absent. The prior Git root from the project was `$HOME`; this project now has its own repository. Project root verification is recorded in the final handoff. |
| 2. `.gitignore` | Complete | Project-specific ignore file added. Clean PNGs and website/audio source are not ignored. Backup files and local mask review artifacts are excluded. |
| 3. Tooling | Deferred by current strict scope | Original prompt requested `tools/`, copied scripts and `check_assets.py`; the continuation allowed only Git metadata, `.gitignore` and requested documentation. No scripts/helper created or copied; `check_assets.py` was not run. |
| 4. Documentation | Complete | README and requested architecture, content, changelog, known issues, image, AI-agent, contribution, context and status docs added. |
| 5. Git commits | Not done by instruction | No application files staged; no commits created. |
| 6. Push | Not configured in this handoff | The intended workflow is private GitHub collaboration with the owner's brother; no remote or push exists yet. This status is not a prohibition or licensing gate for private collaboration. |
| 7. Verification | Partial | Local repo root/status and asset counts checked. Original clone test and helper comparison are impossible because there is no commit/remote and helper was deferred. No app files were changed in this task. |

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
4. The local repository currently has no commits, remote, or checked-in source files; site files remain untracked. These are current repository-state facts, not a prohibition on the intended private collaboration.
5. The current code still contains stale event and destination details listed in `KNOWN_ISSUES_AND_TODO.md`.
