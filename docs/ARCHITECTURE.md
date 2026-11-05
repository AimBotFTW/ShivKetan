# Architecture

## What is running

This directory is a downloaded Framer export, not a package-managed source project. The active page is `download/www.missingpieceinvites.com/demos/city-2-local.html`. It contains server-rendered markup and embedded styles, then hydrates through Framer's React/runtime MJS graph. The page-specific bundle is `download/framerusercontent.com/sites/3bR6R2YrHoycodLqL6z8ep/rnnTUOxVq8PHuNJnW02Z-QNi-QQMH82osuPTQxAKcn0.q7vHoL6S.mjs`. The server is `download/serve.py`.

Visible copy exists in the HTML's responsive SSR variants and in page-instance properties/defaults in MJS. The handoff's static audit found that edits to personalized instance content may need matching changes in both places; otherwise hydration can re-render a different value. Confirm the exact instance and all breakpoint variants before changing text. Shared component defaults may affect other instances.

The template's generated layer structure is hydrated after initial HTML rendering. Existing removals (watermark overlay, Buy Now stack, and Parking card) are implemented with CSS hiding rules so the runtime does not restore deleted nodes. Generated `.framer-*` classes are export-specific and may change on re-export.

## Important files and routes

| File | Role |
|---|---|
| `download/www.missingpieceinvites.com/demos/city-2-local.html` | Active personalized local page. |
| `download/framerusercontent.com/sites/3bR6R2YrHoycodLqL6z8ep/rnnTUOxVq8PHuNJnW02Z-QNi-QQMH82osuPTQxAKcn0.q7vHoL6S.mjs` | Page-specific content and component props. |
| `download/serve.py` | Local Python server. |
| `download/www.missingpieceinvites.com/demos/city-2-original.html` | Reference snapshot with remote Framer dependencies. Whether it is pristine is unverified. |
| `download/www.missingpieceinvites.com/demos/city-2.html` | Obsolete older page, not selected by the active route. It remains in the repository as a candidate for exclusion from the eventual Git repository; it has not been removed. |

The canonical local alias is `/demos/city-2`; the direct file route is `/www.missingpieceinvites.com/demos/city-2-local.html`. `serve.py` serves the `/framerusercontent.com/...` tree, sends CORS headers, uses HTTP/1.1, supports byte ranges (needed for MP3 seeking), and maps the alias to the active HTML. Local image filenames include URL query strings literally, for example `asset.png?width=...&height=...`; references may encode the question mark as `%3F` or ampersands as `&amp;` in HTML. Do not normalize these names without changing and checking the server's lookup behavior.

## Runtime and dependencies

The active page has 20 local MJS modules, including React/Framer runtime, motion, smooth scrolling, slideshow and other generated modules. There are four MJS backup files in the module directory; they are not runtime modules. No `package.json` or install/build workflow was found in the download tree. Local serving uses Python's standard library. The active HTML/MJS still reference remote Framer/CDN assets and Google-hosted fonts. Browser hydration and network behavior are unverified; the locally served site still depends on remote resources and has not been browser-tested.

The active HTML also references a missing local Apple touch icon (`crQk5UzfRd9W9n54FdrUY2WUTU.png`) and missing Open Graph/Twitter image (`7LPUQldg1w5B1Zrz0pCfh0AeQw.png`). The custom page MJS contains a missing remote WtUt asset as the `Hashtag` component's default icon. The active HTML does not reference WtUt directly; whether hydration requests that default is unverified.

## Backups

Several `.bak*` snapshots remain on disk and are intentionally ignored by Git. Preserve them. Once source files are tracked, reviewable Git history can provide change history; it is not a reason to delete existing backups. Compare a backup before relying on it as pristine because the earlier audit found backups differ from current files.
