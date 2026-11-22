# Shivani and Ketan Wedding Invitation

A locally served copy of Missing Piece's Framer wedding invitation template, personalized for **Shivani Chandwade weds Ketan Mohite**. Missing Piece template attribution and the current sharing restrictions are documented in [Asset and licence notes](docs/IMAGES.md#licensing-and-sharing).

## Run locally

Requires Python 3 (the server uses only the standard library; Python 3.12 is sufficient). From a terminal:

```bash
cd download
python3 serve.py
```

Open <http://127.0.0.1:8000/demos/city-2> or the direct file URL <http://127.0.0.1:8000/www.missingpieceinvites.com/demos/city-2-local.html>. Do not open the HTML through `file://`; browser module imports need an HTTP origin. After any file change, hard-reload with **Cmd+Shift+R** because the browser caches MJS modules and audio. If port 8000 is busy, `lsof -ti :8000 | xargs kill` stops the process listening there.

## Static production build

The version-controlled build in `scripts/build_site.py` writes a Vercel-ready site to `dist/`. It normalizes Framer query-string filenames, rewrites HTML and module asset references, and emits `/` and `/demos/city-2/` routes.

```bash
python3 scripts/build_site.py
python3 scripts/check_site.py
```

Vercel uses the committed `vercel.json` to build and serve the static output directly. Production hosting does not run `download/serve.py` or another Python web server. `dist/` is generated and ignored by Git.

## Project map

| Path | Contents |
|---|---|
| `download/www.missingpieceinvites.com/demos/` | Active personalized page, original reference export, and older export snapshots. |
| `download/framerusercontent.com/sites/` | Framer runtime modules and the active page bundle. |
| `download/framerusercontent.com/images/` | Local site images, responsive size variants, originals, and clean PNG variants. |
| `download/framerusercontent.com/assets/` | Fonts and audio tracks. |
| `download/serve.py` | Local-only Python HTTP server and asset routing. |
| `scripts/build_site.py` | Reproducible static production build. |
| `scripts/check_site.py` | Generated route, asset reference, and localhost checks. |
| `vercel.json` | Vercel build, route, and cache configuration. |
| `download/PROJECT_HANDOFF.md` | Earlier technical audit and source-of-truth findings. |
| `module-urls.txt` | Captured Framer module URL inventory. |
| `docs/` | Architecture, content, image/licence, status, and contributor handoff. |

## Documentation

Start with [project status](docs/PROJECT_STATUS.md), [context for AI agents](docs/PROJECT_CONTEXT_FOR_AI.md), and [working rules](docs/WORKING_WITH_AI_AGENTS.md). GitHub currently reports the supplied repository as public. The Vercel project has SSO protection enabled for deployments.

## Repository safety

The owner has confirmed permission to include and share `sajiri-gojiri.mp3` for this intended project arrangement; this does not establish unrestricted public redistribution rights. The separate Missing Piece template licence remains unresolved; see [Asset and licence notes](docs/IMAGES.md#licensing-and-sharing).
