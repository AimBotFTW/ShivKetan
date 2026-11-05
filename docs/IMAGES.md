# Images, watermark processing and licensing

## Clean image families

The image directory contains **eight clean image families and 22 `-clean.png` variants**, verified by filename count. All eight families and all 22 clean variants are referenced in both the active HTML and custom page MJS, and all 22 files exist locally. The 22 original non-clean variants are retained as source/history assets; they are not runtime dependencies of the active personalized page. The obsolete `city-2.html` still references original variants. Query strings are part of the disk filename.

| Image family | Master dimensions | Clean variants | Processing / notes |
|---|---:|---:|---|
| `fLGamlH2btcCdaNTj1Bd4kvcjXQ` day palace landscape | 1350×1056 | 3 | LaMa/IOPaint; six logo boxes on reference size. |
| `d1VXMMgvaZ3QWPbqrWb5gAkZPU` day palace portrait | 1024×1536 | 2 | LaMa/IOPaint; five boxes. |
| `EdGEU12grE10PHMcGr2JDkUcYU` night palace landscape | 2752×1536 | 4 | LaMa/IOPaint; seven boxes on 2048×1143 reference. |
| `Gg2XUucIOzXx6jPzqnFhZnpkFY` night palace portrait | 1696×2528 | 3 | LaMa/IOPaint; nine boxes on 1373×2048 reference. |
| `0VfGPTieZBqRnGtOTVKFd5d6t0` rear Mercedes | 2059×1403 | 4 | OpenCV Telea inpainting; reference box `(1050,696,222,41)` on 2048×1395. |
| `SSy3qmt0CmquDCHvdD4yQabgeMI` angled-front Mercedes | 1528×1009 | 3 | OpenCV Telea inpainting; reference box `(772,441,164,26)` on 1528×1009. |
| `T1dORVl8kMLXNd7ShMJWzCpoHtM` front-facing blue Mercedes | 629×431 | 2 | Approved mask, Big LaMa/IOPaint; 512×351 derivative also present. Separate clean family; not the earlier cleaned rear/angled cars. |
| `O07fRruEj5em3moPWz2blxIGqRI` black vintage car | 520×779 | 1 | Approved mask, Big LaMa/IOPaint. |

The first six IDs contribute 19 clean variants and the two vehicle IDs contribute three more. The 22 original non-clean variants remain alongside them. The eight local watermark-mask review files are in `download/watermark_masks/` and are ignored by `.gitignore`; clean PNGs remain active website assets.

### Processing scripts and dependencies (home-directory copies)

The five existing scripts were inspected in `$HOME`; they were **not copied into this repository** under the current strict file-creation limit. No virtual environment or model was copied. Their imports and behavior are:

| Script | Actual role | Dependencies / effects |
|---|---|---|
| `wm_inpaint.py` | Finds PNG variants for the two original car IDs, maps the reference boxes with 20px padding, selects near-white nontransparent logo pixels, dilates the mask, runs OpenCV Telea inpainting, restores source alpha, writes `-clean` PNGs and previews. | Python stdlib `os`; NumPy; OpenCV (`cv2`); Pillow. Writes into the project image tree and `$HOME/wm-preview`. |
| `wm_palace.py` | Finds a local logo template; searches high-pass grayscale regions around configured box locations; template-matches logos with a bright-area fallback, dilates masks, inpaints, and writes clean copies and previews for four palaces. | `os`, NumPy, OpenCV, Pillow (`Image`, `ImageDraw`). Writes into the project image tree and `$HOME/wm-preview-palace`. |
| `wm_lama_prep.py` | Builds masks and RGB input for four palace masters, using logo-template matching with box fallback, and writes mask-check previews. | `os`, NumPy, OpenCV, Pillow. Writes under `$HOME/lama/{in,mask,check,out}`. |
| `wm_lama_finish.py` | Reads IOPaint outputs, resizes to each original local variant, restores original alpha/transparency where present, carries DPI metadata when available, and writes `-clean` PNGs for each palace variant. | `os`, NumPy (imported), Pillow. Reads/writes project assets and `$HOME/lama/out`. |
| `wm_palace2.py` | Discarded experiment: makes tighter masks, attempts copied-patch Poisson blending and falls back to Telea inpainting; creates preview sheets. The result was judged worse. | `os`, NumPy, OpenCV, Pillow. Writes into the project image tree and `$HOME/wm-preview-palace2` if run. |

The original six image process used reference-coordinate boxes recorded above and in the two scripts' `JOBS` tables. The T1d/O07f workflow used separately approved masks and `$HOME/lama-remaining-cars/` plus cached `$HOME/lama-env/bin/iopaint`; no reusable project-local script for that two-car run was verified. Do not rerun processing without reviewing source/mask alignment, alpha handling and outputs. **LaMa has not been rerun for this documentation task.**

## Source fidelity and QA limits

Original PNGs are kept beside clean variants. The two historic car scripts explicitly preserve alpha; the palace finish script restores input alpha/transparency when detected. The new two-car workflow saved original alpha separately and restored it per the user-requested workflow. A byte-for-byte alpha-channel equivalence audit across all 22 variants was not run for this documentation task. Visual defects and responsive rendering require browser/image review. Never clean the already-clean rear/angled Mercedes again.

The active page has 20 local MJS modules. Its HTML/MJS still contain remote Framer/CDN and Google font references; browser hydration and network behavior are unverified, so do not describe the site as independent of remote resources or browser-tested. The active HTML points to a missing local Apple touch icon (`crQk5UzfRd9W9n54FdrUY2WUTU.png`) and missing Open Graph/Twitter image (`7LPUQldg1w5B1Zrz0pCfh0AeQw.png`). The custom MJS has a WtUt image URL as the `Hashtag` component's default icon, but the asset is not local and its runtime use is unverified.

Do not commit private family photographs without project authorization. `.gitignore` has named private-photo directory patterns but does not blanket-ignore image formats because actual website imagery must remain trackable.

## Licensing and sharing

This project includes the Missing Piece template and its logo/artwork, plus the local `sajiri-gojiri.mp3` recording. The owner has confirmed permission to include and share the MP3 for the intended project arrangement. That confirmation is limited to that arrangement and does not grant unrestricted public redistribution rights.

The Missing Piece template licence remains unresolved. Its published [Terms](https://www.missingpieceinvites.com/terms) describe restrictions on redistribution/sharing, third-party use and watermark alteration; the [licence page](https://www.missingpieceinvites.com/privacy-policy) describes a non-transferable, single-use personal-event licence. The owner's intended private collaboration does not itself establish what use is permitted under those terms. Public distribution and public hosting are not currently intended. Do not infer broader rights from the MP3 confirmation.

The local audio filename identifies “Sajiri Gojiri.” Public song credits attribute the film version to lyricist Omkar Mangesh Datt, singers Sahil Kulkarni and Rupali Moghe, composer Pankaj Padghan, and label Video Palace ([song credits](https://www.marathifilm.in/2017/05/sajiri-gojiri-song-lyrics-sahil.html)). The owner's permission applies to the intended project arrangement only; it does not establish unrestricted public redistribution rights. The Missing Piece template restriction remains separate. No remote is configured and nothing has been pushed.
