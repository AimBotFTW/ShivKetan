# Changelog

Dates are recorded only where supported by the handoff. Earlier edits are “undated, before first commit”; this repository has no commits yet.

## Undated, before first commit — personalized Framer export

- Replaced template couple names with Shivani and Ketan in the local active page and page-instance bundle.
- Added family names, blessing copy, venue and core event details; changed Sakharpuda/Engagement and Wedding/Shaadi labels.
- Added the countdown date/time, `#ShivKetan`, WhatsApp number, and GMK map link. The map target and countdown runtime still need testing.
- Swapped the page music reference from the template track to `sajiri-gojiri.mp3`; added a script that attempts autoplay and retries after a user gesture. Browser behavior is unverified.
- Added CSS hides for the Missingpiece overlay, Buy Now stack and Parking card rather than deleting hydrated Framer markup.
- Updated local HTML/MJS image references for six known cleaned asset families. A separate earlier audit noted a remaining T1d vehicle image and an unresolved WtUt remote reference; later work cleaned two additional families but did not swap references as of that image-processing handoff.
- Used successive `.bak*` snapshots around edits; exact snapshot chronology and pristine status are not established.

## Before this documentation task — watermark cleanup

- Two car families were cleaned with OpenCV inpainting by `wm_inpaint.py`; four palace families were processed with LaMa via IOPaint using `wm_lama_prep.py` and `wm_lama_finish.py`. Detailed source sizes, reference boxes and per-script behavior are in [IMAGES.md](IMAGES.md).
- `wm_palace2.py` tested a patch-copy/Poisson-blending approach; it was judged worse and discarded.
- Two additional vehicle families, T1d and O07f, were later prepared with approved masks and processed through the Big LaMa / IOPaint workflow. The clean variants were generated locally; references were deliberately not changed in that processing task.
- Result: eight clean families and 22 clean PNG variants are present. This count was verified from filenames; visual/runtime review is not implied.

## 2026-11-04 — repository handoff documentation

- Created an independent project-local Git repository at `city-2-offline/.git`, initialized on `main`; no remote, staging, commit or push.
- Added project `.gitignore` and documentation. Application files and existing backups were not edited by this task.

## 2026-11-04 — dependency audit reconciliation

- Verified that all eight clean image families and all 22 clean PNG variants are referenced in the active HTML and custom MJS; all 22 files exist locally. The 22 original non-clean variants remain as source/history assets.
- Counted 20 active MJS modules, four MJS backups in the site module directory, nine backups project-wide, eight non-runtime watermark-review files, 82 local images, 58 asset files and eleven Markdown documents.
- Confirmed page roles: `city-2-local.html` is active; `city-2-original.html` is a remote-dependent reference snapshot with unverified pristine status; `city-2.html` is obsolete and a candidate for eventual Git exclusion, not removed.
- Owner confirmed permission to include/share `sajiri-gojiri.mp3` for the intended project arrangement. Missing Piece template terms remain a separate factual consideration; see `IMAGES.md`.
- Browser hydration and network behavior remain unverified. The earlier processing entry records that the two newer car references were not swapped at that processing handoff; this audit verifies that the active HTML/MJS now use their clean files.

## 2026-11-05 — final documentation consistency

- Clarified that the project is a locally served Framer export intended for local development and private GitHub collaboration between the owner and his brother. Public repository distribution and public hosting are not currently intended.
- Retained the MP3 permission as limited to the intended project arrangement and summarized the separate template-term concern in `IMAGES.md`; browser hydration and network behavior remain unverified.
