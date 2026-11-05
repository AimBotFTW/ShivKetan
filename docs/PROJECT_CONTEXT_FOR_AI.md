# Project context for AI agents

## Purpose and source of truth

This is Shivani Chandwade and Ketan Mohite's wedding invitation, made from a Missing Piece Framer template export. Preserve the existing design. The local active page is `download/www.missingpieceinvites.com/demos/city-2-local.html`; the custom bundle and local server are described in [ARCHITECTURE.md](ARCHITECTURE.md). Read [CONTENT.md](CONTENT.md), [IMAGES.md](IMAGES.md), and [KNOWN_ISSUES_AND_TODO.md](KNOWN_ISSUES_AND_TODO.md) before related work.

Confirmed core event facts: Haldi Thursday 26 November 2026 at 7:00 AM; Sakharpuda that day at 5:00 PM; wedding Friday 27 November 2026 at 12:24 PM; venue GMK Banquets & Lawns, Katraj-Dehu Road Bypass, Ravet, Pimpri-Chinchwad, Pune, Maharashtra. Reception details are pending. Mehendi/Cocktail and Reception card content in the export is stale template content and must not be treated as confirmed.

Bride's parents: Nitin and Rupali Chandwade. Groom's parents: Mohan and Hemlata Mohite. The active copy also includes late Dadasaheb Patil, late Pramila Patil and late Pandurang Chandwade in the bride-side blessing line.

## Website gallery functionality

The active page bundle includes the existing slideshow/photo-highlight functionality. Keep it as part of the wedding website. The static dependency audit found the `SlideShow` module, but gallery behavior has not been browser-tested.

## Assets and sharing

Eight clean image families and all 22 clean variants are present locally and referenced in the active HTML and custom MJS. The 22 original non-clean variants are retained as source/history assets, not dependencies of the active personalized page. Do not confuse the front-facing blue Mercedes and black vintage car with the previously cleaned rear and angled-front Mercedes.

The five watermark scripts live in the user's home directory and are documented in `IMAGES.md`; they were deliberately not copied here. `$HOME/lama-env` is external and must stay out of Git. Do not edit HTML/MJS, images, audio, or backups unless the task explicitly authorizes that file class.

The owner has confirmed permission to include and share `sajiri-gojiri.mp3` for the intended project arrangement; that does not grant unrestricted public redistribution rights. The intended workflow is local development and commits, then private GitHub collaboration with the owner's brother. Public distribution and public hosting are not currently intended. The local repository currently has no remote. For the separate Missing Piece template terms, see [IMAGES.md](IMAGES.md#licensing-and-sharing); do not infer broader rights from the MP3 permission or private-repository purpose.
