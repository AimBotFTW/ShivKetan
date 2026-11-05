# Shivani and Ketan Wedding Invitation

A locally served copy of Missing Piece's Framer wedding invitation template, personalized for **Shivani Chandwade weds Ketan Mohite**. Missing Piece template attribution and the current sharing restrictions are documented in [Asset and licence notes](docs/IMAGES.md#licensing-and-sharing).

## Run locally

Requires Python 3 (the server uses only the standard library; Python 3.12 is sufficient). From a terminal:

```bash
cd download
python3 serve.py
```

Open <http://127.0.0.1:8000/demos/city-2> or the direct file URL <http://127.0.0.1:8000/www.missingpieceinvites.com/demos/city-2-local.html>. Do not open the HTML through `file://`; browser module imports need an HTTP origin. After any file change, hard-reload with **Cmd+Shift+R** because the browser caches MJS modules and audio. If port 8000 is busy, `lsof -ti :8000 | xargs kill` stops the process listening there.

## Project map

| Path | Contents |
|---|---|
| `download/www.missingpieceinvites.com/demos/` | Active personalized page, original reference export, and older export snapshots. |
| `download/framerusercontent.com/sites/` | Framer runtime modules and the active page bundle. |
| `download/framerusercontent.com/images/` | Local site images, responsive size variants, originals, and clean PNG variants. |
| `download/framerusercontent.com/assets/` | Fonts and audio tracks. |
| `download/serve.py` | Local-only Python HTTP server and asset routing. |
| `download/PROJECT_HANDOFF.md` | Earlier technical audit and source-of-truth findings. |
| `module-urls.txt` | Captured Framer module URL inventory. |
| `docs/` | Architecture, content, image/licence, status, and contributor handoff. |

## Documentation

Start with [project status](docs/PROJECT_STATUS.md), [context for AI agents](docs/PROJECT_CONTEXT_FOR_AI.md), and [working rules](docs/WORKING_WITH_AI_AGENTS.md). The intended workflow is local development followed by collaboration with the owner's brother through a private GitHub repository. A public repository and public deployment are not currently intended. The website is locally served with Python's HTTP server; remote Framer/CDN and Google font dependencies remain, so network access may be needed.

## Repository safety

The repository is intended to remain private for collaboration between the owner and his brother; public distribution and public hosting are not currently intended. The owner has confirmed permission to include and share `sajiri-gojiri.mp3` for this intended project arrangement; this does not establish unrestricted public redistribution rights. The separate Missing Piece template licence is unresolved; see [Asset and licence notes](docs/IMAGES.md#licensing-and-sharing) for the concise factual note. The local repository currently has no remote.
