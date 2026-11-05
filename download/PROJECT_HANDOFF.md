# Shivani and Ketan Wedding Website — Project Handoff (Superseded Historical Audit)

Audit date: 2 November 2026 (Asia/Kolkata). Scope: read-only inspection of `city-2-offline/download`; this document is the only file created by this audit. No app files, images, backups, or scripts were changed.

> **Superseded:** This is a historical snapshot of findings as of 2 November 2026. Its counts and unresolved items below describe that audit date, not the current project state. The dependency audit and documentation review superseded this snapshot on 5 November 2026. Current state:
>
> - The image directory has 82 local files, including eight clean families with 22 clean PNG variants. All eight families and all 22 variants are referenced in the active HTML and custom MJS, and all 22 files exist locally. Twenty-two original non-clean variants remain as source/history assets; they are not active personalized-page dependencies.
> - The two additional cleaned vehicles are `T1dORVl8kMLXNd7ShMJWzCpoHtM` (front-facing blue Mercedes) and `O07fRruEj5em3moPWz2blxIGqRI` (black vintage car). The WtUt URL is a missing remote default icon in the `Hashtag` component, not an identified vehicle.
> - There are 58 files in `assets/`, 20 active MJS modules plus four MJS backups in `sites/`, nine backups total, eight non-runtime watermark-review files, and eleven Markdown documents across root, `docs/` and `download/`.
> - `city-2-local.html` is active. `city-2-original.html` is a reference snapshot with remote dependencies and unverified pristine status. `city-2.html` is obsolete, not selected by the active route, and a candidate for eventual Git exclusion; it remains present.
> - An independent local Git repository was initialized at the project root on 4 November 2026. It has no commits or remote; 177 paths are untracked. The outer `$HOME` repository was not modified.
> - The owner confirmed permission to include/share `sajiri-gojiri.mp3` for the intended project arrangement; unrestricted public redistribution rights are not implied. The private GitHub collaboration purpose is documented in current project docs; public distribution/hosting are not currently intended. See `docs/IMAGES.md` for the separate template-term note.
> - Browser hydration, remote network behavior and full browser QA remain unverified.
>
> Older findings below are retained as historical evidence. In particular, the 79-image/19-clean-variant counts, the recommendation to identify and clean two remaining cars, and the pre-initialization Git status are superseded. The T1d and O07f vehicles were later identified and cleaned; current active HTML/MJS references use their clean variants.

## A. Executive summary

This is a downloaded Framer site, not a source project built from a package manager. Its active local page is `www.missingpieceinvites.com/demos/city-2-local.html`; SSR HTML carries much of the visible page and embeds responsive desktop/tablet/phone variants, while a Framer-generated module graph hydrates interactions and includes a large page-specific bundle. The custom page bundle is `framerusercontent.com/sites/3bR6R2YrHoycodLqL6z8ep/rnnTUOxVq8PHuNJnW02Z-QNi-QQMH82osuPTQxAKcn0.q7vHoL6S.mjs`.

As of the 2 November 2026 audit (historical): the local page contained the couple's names, Pune venue, parents and specified blessings, wedding and Sakharpuda dates, and clean references for six then-identified image families. Confirmed content errors at that time included: Haldi says 7pm (source of truth is 7am), and Mehendi/Cocktail/Reception show March 2026 dates although dates/times are awaiting confirmation or groom-side confirmation. Parking content remains in HTML but local CSS hides it. The exact two watermarked car images described in the prior screenshot cannot both be proven from filenames alone. The active page and custom MJS reference a distinct car image `T1dORVl8kMLXNd7ShMJWzCpoHtM.png` (629×431, plus 512w derivative); it is not either of the two cleaned Mercedes IDs. Another MJS image reference `WtUtKiZfYvFe6ob7yo3S6KaxT4.png` has no local image file and cannot be classified from available local evidence. Visual inspection of those image contents/screenshots is needed before asserting which corresponds to which vehicle.

## B. Project architecture

- `www.missingpieceinvites.com/demos/city-2-local.html`: local page with SSR markup, inline Framer CSS, custom local URL rewrites, and head metadata. Responsive SSR variants duplicate text/content in desktop, tablet and phone branches; do not mistake repeated strings for repeated distinct events.
- `www.missingpieceinvites.com/demos/city-2-original.html`: original-domain export snapshot; assets point to hosted Framer resources.
- `www.missingpieceinvites.com/demos/city-2.html`: another export snapshot; appears template content, not the active personalized local page.
- `framerusercontent.com/sites/3bR6R2YrHoycodLqL6z8ep/`: Framer runtime, React, motion, page and component modules. The main page module imports the custom page bundle; the latter supplies components/content and references assets. SSR HTML lets the initial design render before hydration; JS supplies React hydration, interactive components, animations and client behavior. Images are loaded through Framer-style `src`/`srcSet` URLs, which the local server maps to filenames containing the query string.
- Historical 2 November count, superseded on 5 November: `framerusercontent.com/images/` contained 79 local image/SVG files including query-string variants; `assets/` contained 52 files (50 WOFF2 fonts, two MP3 tracks). No standalone CSS file, local video file, package manifest, or installed app build pipeline was found within the download tree. Styling is largely embedded in HTML; some styles are emitted by Framer modules.
- `serve.py`: Python standard-library HTTP server with CORS headers, byte-range responses, query-string-aware local asset lookup, and a route alias from `/demos/city-2` to the local HTML file.
- `module-urls.txt`: module URL inventory.

There are no separate authored route files. The canonical route is served by the Python handler; the direct local HTML URL also works. Internal navigation includes page anchors/sections and route buttons, but a complete browser click-through was not conducted.

## C. Directory structure (historical 2 November snapshot)

```text
city-2-offline/
├── module-urls.txt
└── download/
    ├── serve.py (+ serve.py.bak)
    ├── PROJECT_HANDOFF.md (this audit)
    ├── framerusercontent.com/
    │   ├── assets/ (fonts and audio)
    │   ├── images/ (79 image/SVG files and size variants)
    │   └── sites/3bR6R2YrHoycodLqL6z8ep/ (runtime and page MJS modules)
    └── www.missingpieceinvites.com/demos/
        ├── city-2-local.html (+ .bak, .bak-wm, .bak-wm2)
        ├── city-2-original.html
        └── city-2.html
```

Tree omits individual generated Framer modules and asset files; see the inventories below. Full module listing is obtainable with `find framerusercontent.com/sites -type f -maxdepth 2` from the download root.

## D. Technical stack and development tools

- Static HTML/CSS + React/Framer runtime as exported by Framer; ECMAScript modules (`.mjs`). Runtime modules include `react`, `motion`, `framer`, `SlideShow`, `SmoothScroll_Prod`, `Badge`, `script_main`, `siteMetadata`, and supporting hashed modules.
- Local serving uses Python 3 standard library (`http.server`, `urllib.parse`, `pathlib`, `re`); no dependency installation is needed to start it.
- Assets include WOFF2 fonts (font-face definitions include Cormorant family variants, Gotu, Manrope, Yaldevi, Aboreto, Inter and others), SVGs, PNG/JPEG images, and MP3 audio. Some Google Fonts URLs remain external as well as local WOFF2 URLs.
- Python image tooling (Pillow) was not available to the audit's active Python interpreter (`ModuleNotFoundError`). The user reports a separate `$HOME/lama-env`, IOPaint and Big LaMa tooling, but their current install/model state was not independently verified. No node package manifest was found in the project.

## E. Asset inventory and watermark mapping (historical 2 November findings; current counts superseded)

The image directory has 79 files (many are distinct `?width=...` or `?scale-down-to=...` variants). 19 files have `-clean.png` in their names: 4 day-palace, 4 night-palace, 7 rear-Mercedes and 4 angled-front-Mercedes variants. Thus the reported total of 19 is verified; it is 19 local files/variants, not 19 unique source images.

| Source image ID (description from prior audit context) | Source dimensions from Framer URLs | Clean local variants | Active page/bundle refs |
|---|---:|---:|---|
| `fLGamlH2btcCdaNTj1Bd4kvcjXQ` — day palace landscape | 1350×1056 | 3 `-clean.png` files | Clean refs only in local HTML and custom MJS |
| `d1VXMMgvaZ3QWPbqrWb5gAkZPU` — day palace portrait | 1024×1536 | 2 | Clean refs only |
| `EdGEU12grE10PHMcGr2JDkUcYU` — night palace landscape | 2752×1536 | 4 | Clean refs only |
| `Gg2XUucIOzXx6jPzqnFhZnpkFY` — night palace portrait | 1696×2528 | 3 | Clean refs only |
| `0VfGPTieZBqRnGtOTVKFd5d6t0` — rear Mercedes | 2059×1403 | 4 | Clean refs only |
| `SSy3qmt0CmquDCHvdD4yQabgeMI` — angled-front Mercedes | 1528×1009 | 3 | Clean refs only |

Source dimensions are the dimensions declared by Framer in the page's asset URLs. The downloaded clean variants retain the corresponding requested pixel dimensions; scale-down derivatives are intentionally smaller (512, 1024 or 2048 px on their constrained edge). Transparency preservation was **not** established with an image decoder in this environment, so do not assume alpha-channel equivalence. `sips` confirmed dimensions for sampled local variants, including the car image below; it is not a full visual quality review.

The HTML and the active custom MJS reference `-clean.png` variants for each of the six known families. No original filename reference for those six families was found in either active file. Original copies still exist locally as archival assets; that is not evidence they are active page references. Variant sizes/filenames for each known family can be enumerated with `find framerusercontent.com/images -name '<ID>*'`.

### Newly spotted vehicle leads (2 November findings; superseded 5 November)

| Candidate | Exact local path / dimensions | Reference | Assessment |
|---|---|---|---|
| `T1dORVl8kMLXNd7ShMJWzCpoHtM.png` | `framerusercontent.com/images/T1dORVl8kMLXNd7ShMJWzCpoHtM.png?width=629&height=431` (629×431), and `...?scale-down-to=512&width=629&height=431` (512×351) | Active local HTML around line 696; custom page MJS around line 24, two responsive background declarations | At the time, it was an uncleaned lead whose identity was unverified. Superseded 5 November: identified as the front-facing blue Mercedes, cleaned, and referenced using clean variants.
| `WtUtKiZfYvFe6ob7yo3S6KaxT4.png` | Referenced with 1024×1024 and 512×512 variants, but **no local file** found | Custom page MJS default component asset reference; no active HTML filename hit | Cannot establish whether vehicle or unrelated image; cannot inspect local dimensions/content. This may be dynamically hosted if used, and is a likely offline broken asset.

Historical 2 November conclusion, superseded 5 November: no second vehicle was identified in that audit, and it recommended further visual investigation. The later audit identified O07f as the black vintage car and verified both additional vehicle families are cleaned and referenced in active HTML/MJS. Browser appearance remains unverified.

### Watermark-removal process (history, not reproduced)

Historical notes state image cleaning used Python, IOPaint and Big LaMa, with model `$HOME/.cache/torch/hub/checkpoints/big-lama.pt`, environment `$HOME/lama-env`, car script `$HOME/wm_lama_cars.py`, and workspace `$HOME/lama-cars/`. The handoff context reports 12 palace and 7 car clean variants. The local image variant count at the time of that historical audit was 19 `-clean` files across six families; this is superseded by the current 22 clean variants across eight families. No cleaning was performed in this audit. Current external tool/model paths, masks, exact commands, and visual quality were not verified.

## F. HTML, MJS, backups and asset swaps

| File | Original references | Clean references | Backup exists | Status |
|---|---|---|---|---|
| `www.missingpieceinvites.com/demos/city-2-local.html` | None for six known families in active file | Yes, all six known families | `.bak`, `.bak-wm`, `.bak-wm2` | Swaps applied for known IDs; contains personalized page and CSS hiding parking. Also has unrelated uncleaned T1d car reference. |
| `framerusercontent.com/sites/.../rnnTUOxVq8PHuNJnW02Z-QNi-QQMH82osuPTQxAKcn0.q7vHoL6S.mjs` | None for six known families in active bundle | Yes, all six known families | `.bak`, `.bak-wm`, `.bak-wm2` | Swaps applied for known IDs; also references T1d car and missing local WtUt image. |
| `city-2-original.html` | Template image references; not the customized local variant | None expected | No matching backup found | Hosted/original export snapshot; do not treat as active customized page. |
| `city-2.html` | Template image references; not the customized local variant | None expected | No matching backup found | Another export snapshot; Jaipur/template text remains. |

All seven `.bak*` files discovered (3 for HTML, 3 for main MJS, 1 for `serve.py`) differ byte-for-byte from the current corresponding file. They are snapshots, but the exact state/timing they represent and whether any is a faithful pristine original cannot be confirmed by hashes alone. The original HTML backup is present, but its intactness as the true untouched export was not provable. No `*.bak-cars` file was present. The HTML `.bak-wm2` exists; the MJS `.bak-wm2` exists. Do not restore or overwrite without comparing content and making a separate backup.

The swap workflow is therefore evidenced in active HTML and MJS, not by a Git history. Repeated responsive references are expected; no duplicate/inconsistent known-family clean/original mixture was found in the two active files.

## G. Wedding content and schedule

Source of truth provided with the audit request:

- Wedding: Friday, 27 November 2026, muhurat 12:24 PM.
- Venue: GMK Banquets & Lawns, Dehu Road Bypass, Ravet, Pimpri-Chinchwad, Pune.
- Bride's parents: Nitin and Rupali Chandwade.
- Haldi: Thursday, 26 November 2026, 7:00 AM.
- Sakharpuda: Thursday, 26 November 2026, 5:00 PM.
- Mehendi and Cocktail: dates/times awaiting confirmation.
- Reception: date/time awaiting groom-side confirmation.

Active page content verified in local HTML:

- Bride `Shivani`; groom `Ketan`; groom's parents `Mrs. Hemlata & Mr. Mohan Mohite`.
- Blessings: “the late Dadasaheb Patil, the late Pramila Patil & the late Pandurang Chandwade”, followed by “Mrs. Rupali & Mr. Nitin Chandwade”.
- Event cards show Haldi Thursday, November 26th 2026 at `7pm Onwards` (incorrect vs 7 AM); Sakharpuda Thursday, November 26th 2026 at `5pm Onwards`; Wedding Friday, November 27th 2026 at `12:24pm`.
- Mehendi reads Friday, March 9th 2026 at 6pm; Cocktail Friday, March 10th 2026 at 6pm; Reception Friday, March 17th 2026 at 6pm. All three dates/times must be confirmed or removed/hidden rather than inferred from source of truth. Venue on cards is shortened to “GMK Banquets & Lawns, Ravet, Pune”.
- Hashtag currently `#ShivKetan`.
- Weather copy says mostly sunny, up to 28 degrees; hotel copy names Bhola Bhawan; neither contains Jaipur in active local copy. These are generic claims requiring confirmation. Template `city-2.html` does still contain Rambagh, Jaipur and old template content.

## H. Feature implementation status

This table reports code/content presence; only static inspection was performed unless noted.

| Feature | Status | Evidence / limit |
|---|---|---|
| Invitation landing / names | Implemented; SSR content present | Names appear in desktop/tablet/phone variants. No screenshot review in this audit. |
| Parents and blessings | Implemented | Bride's blessing order/wording matches supplied context; groom parents shown. Grandparents beyond named blessings not found. |
| Event cards | Implemented, content partly incorrect | Six card types; dates/times above. Responsive markup duplicates the cards. |
| Haldi/Sakharpuda | Partly correct | Dates and Sakharpuda time match; Haldi says 7pm instead of 7am. |
| Mehendi/Cocktail/Reception | Incorrect/unconfirmed | March 2026 values remain, despite source-of-truth details being pending. |
| Countdown | Implemented; correctness unverified | HTML contains timer component and SSR placeholder `00:00:00:00`; event date exists elsewhere. Need live runtime/date/timezone test. |
| Palace backgrounds | Implemented; clean refs | Six known image families point to clean versions in active HTML/bundle. Visual output not reviewed here. |
| Vintage cars (2 November status; superseded 5 November) | Watermark status incomplete at that time | Later identified as T1d and O07f; both are cleaned, and clean variants are referenced in active HTML/MJS. Browser appearance remains unverified. |
| Sliders/galleries | Implemented in bundle | `SlideShow` module included. Runtime behavior not tested. |
| Music | Implemented, first-tap behavior unverified | Local page references `sajiri-gojiri.mp3`, loop/autoplay attributes and audio controls. Browsers commonly gate autoplay; no interaction test. Original page references `q8x7...mp3`. |
| Maps | Implemented, destination unverified | Cards include “See the route”; map CTA points to `https://share.google/t3Uf17DTRMBksyH7F`. No external destination validation or click test. |
| Parking card removal | CSS-hidden, not removed | CSS targets `.framer-au7054-container[data-framer-name="Parking"]`; parking content remains in DOM, so CSS-disabled/changed layouts may expose it. |
| Instagram | CTA implemented; target unknown | Copy says “Click to open our Instagram page”; grep found no Instagram URL literal in page or custom bundle. Likely component/default override; actual target not established. |
| Mobile responsiveness | Responsive variants implemented | HTML contains desktop/tablet/phone variant classes; no mobile browser visual QA. |
| Animations/transitions | Implemented | Framer motion/runtime, appear attributes, scroll transforms and smooth-scroll module. Hydration/runtime behavior not tested. |
| External scripts/API | Present | Framer events script, Google Fonts references, Google tag `G-VCMPQ02N6E`, PixelFlow event/script references, and `share.google` map link. Network/privacy/availability not tested. |

## I. Known bugs, quality risks and accessibility

- Confirmed bad event details: Haldi time is PM; Mehendi/Cocktail/Reception use stale March 2026 date/time content.
- Local HTML still contains a visible Buy Now / INR 3999 text node in the export; CSS hides the Buy Now button class. Verify it does not show in current rendering.
- Local map is a short `share.google` link; resolve it and verify it points to GMK Banquets & Lawns before sharing.
- Instagram target is not discoverable as a literal URL in local HTML/custom bundle. Verify actual link and replace if it points to Missingpiece.
- Weather/hotel section uses generic forecast and staff lodging language; no Jaipur string in active personalized page, but local facts are unverified.
- HTML has repetitive SSR variants and duplicate `id="instagram"` hits across variants. Check duplicate-ID behavior in DOM and anchors after hydration; duplicate IDs are a likely markup/accessibility issue, not automatically a user-visible failure.
- Several accessibility concerns need a browser/a11y pass: image `alt` values are frequently empty (decorative status unclear), controls/icons, link names, focus visibility, heading hierarchy, and contrast. Inline SSR provides text but native semantics should be reviewed.
- The page's export title remains “City 2 – Indian Wedding Invitation Website Template”; update title/metadata before public sharing.
- No browser DevTools console/network inspection or desktop/mobile render was performed. React hydration warnings, broken image loads, click behavior, visual crop, layout overflow and actual mobile usability are unknown.
- Query-string filenames and server path mapping are unusual. A static host must serve the literal query-keyed files correctly or rewrite to the actual stored filenames; test deployment. Local absolute `127.0.0.1:8000` paths must not escape into public HTML/MJS.
- Some resources point to externally hosted Framer/Google/PixelFlow services, which can fail offline or be blocked. Custom MJS declares `WtUt...png` remotely but no local copy exists.
- Largest local files are multi-megabyte palace images and long portrait images; image directory totals about 49 MiB. Compression should follow visual and dimension checks.
- JS syntax was not independently parsed/executed; modules are minified/generated and browser runtime was not tested. HTML structural validation, broken-reference full crawl, and syntax checks remain.

## J. Exact local run commands

From the project download directory:

```bash
cd download
python3 serve.py
```

Open either:

```text
http://127.0.0.1:8000/www.missingpieceinvites.com/demos/city-2-local.html
http://127.0.0.1:8000/demos/city-2
```

The server binds specifically to `127.0.0.1:8000`; it is not configured for public network access or deployment. Stop with Ctrl-C. The script has no command-line flags or dependency installation.

## K. Git and backup state (as of 2 November 2026)

At the time of this 2 November audit, the download directory did not have its own Git repository. `git rev-parse --show-toplevel` resolved to `$HOME` (an enclosing user-home repository), branch `master`, with no commits. A separate project-local repository was initialized on 4 November 2026; it has no commits or remote. The outer repository was not modified. Preserve all working files and backups. The audit added only this document to the download tree.

Backup files discovered:

- `serve.py.bak`
- Main bundle `.bak`, `.bak-wm`, `.bak-wm2`
- `city-2-local.html.bak`, `.bak-wm`, `.bak-wm2`
- No `.bak-cars` files found.

Each backup differs from the current corresponding file. Their naming suggests successive snapshots, but exact chronology and pristine-original status are unknown.

## L. Recommended roadmap (historical 2 November recommendations; superseded where noted)

1. **Superseded 5 November 2026:** identify and clean the two remaining watermarked cars. The cars were later identified as T1d (front-facing blue Mercedes) and O07f (black vintage car), cleaned, and their clean references are present in active HTML/MJS.
2. Confirm missing event details with family. Change Haldi to 7:00 AM; replace or suppress Mehendi/Cocktail/Reception placeholders until dates/times are confirmed.
3. Verify all names, parent/grandparent wording/order and `#ShivKetan` with the family.
4. Test first-tap music, map destination, countdown date/time/timezone, and parking visibility in live browser behavior.
5. Confirm Pune weather/hotel copy or remove it; confirm the Instagram destination and remove any template/vendor target.
6. Inspect browser console for hydration warnings and repair only after understanding expected Framer SSR behavior.
7. Compress large images after visual comparison; reduce duplicate size variants only if references remain complete.
8. Test desktop and mobile, all internal links, accessibility basics, console/network errors, and missing local resources.
9. **Historical optional deployment recommendation; not current intent (5 November 2026):** remove local-only origins/URLs and validate query-string paths only if deployment is later requested. Public deployment is not currently intended.
10. **Superseded 4 November 2026:** establish a project-scoped Git repository. The independent project repository was initialized on that date.

## M. Important cautions for the next assistant

- Treat the family-provided schedule as source of truth; do not invent pending times/dates.
- This audit did not alter images or content. Do not assume that the six clean source families cover the separate `T1d...` car asset.
- Do not restore a `.bak*` file based only on its suffix. Compare it first; backups differ from current state and may contain earlier edits.
- Do not deploy the local page as-is: it contains localhost URLs, stale event content, and external services; perform a deployment-path audit first.
- **Historical status as of 2 November 2026:** the two screenshot-reported watermarks had not been identified; that finding is superseded as described above. Alpha preservation, exact map/Instagram targets, autoplay, countdown correctness, hydration messages and mobile rendering were not established by that audit.

## N. Verified and unverified facts

Historical verification as of 2 November 2026 (superseded 5 November): expected paths and serving script existed; active personalized HTML and custom MJS existed; 79 local image/SVG files and 19 `-clean.png` files were counted; six then-known image families referenced clean versions in active HTML/MJS; exact currently displayed event/name/blessing/hashtag/weather/staff/parking text is present in SSR HTML; map URL is present; audio paths and bundle graph exist; backup inventory and hash differences; no dedicated project Git repo existed at that time; no `.bak-cars` found.

Not verified in the 2 November audit: live browser appearance, screenshot identity of both watermarked cars (superseded 5 November), WtUt image contents, full image alpha preservation, actual audio playback or first-tap behavior, countdown accuracy, map/Instagram destination, browser console/hydration errors, mobile layout, all accessibility behavior, deployment success, external API responses, and current state of the separate user-level LaMa environment/model/scripts.

## O. Short handoff for another AI (historical; superseded 5 November 2026)

Audit the personalized Framer export at `<project-root>/download`; active page is `www.missingpieceinvites.com/demos/city-2-local.html`. Keep the design. The page already names Shivani and Ketan, shows the requested blessings, Pune venue, Sakharpuda at 5pm and wedding at 12:24pm. Fix Haldi from 7pm to 7am only after preparing a reviewable change; obtain dates before altering Mehendi/Cocktail/Reception, currently stale March 2026 placeholders. At the time of this 2 November handoff, six known palace/rear-car IDs had clean refs (19 clean variants); it recommended investigating T1d and a second screenshot car. **Superseded 5 November:** there are eight clean families and 22 clean variants; T1d and O07f are the two identified additional vehicles, and their clean files are referenced in active HTML/MJS. Test music, map, countdown, Instagram, parking CSS, hydration, accessibility and mobile rendering. `serve.py` runs locally with `python3 serve.py`. At the time of this 2 November handoff, no independent project Git repository existed; one was initialized on 4 November. Preserve backups.
