# Known issues and TODO

## Content and links

1. Confirm Reception date/time and venue details with the groom's family. Replace or remove the stale March 2026 Mehendi, Cocktail and Reception cards once final details arrive; confirm their images and text.
2. Supply the real event-card images and final copy. The user wants actual imagery in the cards; required images/copy are not yet provided.
3. Correct Haldi from 7pm to the supplied 7:00 AM.
4. Replace or hide weather and staff-stay copy that still appears Jaipur-oriented; confirm the Bhola Bhawan reference.
5. Change the Instagram CTA from Missingpiece to the couple's approved account.
6. Resolve and verify the map link points to GMK Banquets & Lawns.
7. Check whether `#BadriKiDulhania` appears in the rendered page.
8. Confirm the WhatsApp destination and run a user-gesture test of song playback/looping.

## Runtime, presentation and accessibility

- Investigate React hydration recoverable errors #418/#422 and the “Throttling navigation” warning. The earlier handoff hypothesized a mismatch between server markup and props; root cause is unverified.
- Earlier reported console messages: PixelFlow analytics 401 and “Framer On-Page Editing unavailable.” These were called harmless in the supplied history, but were not independently reproduced here.
- Verify countdown timing and timezone in a browser.
- Review mobile/tablet layout, image loads, visual crops, keyboard access, focus, contrast, image alt text, heading hierarchy and duplicate IDs.
- Confirm no Buy Now/parking UI appears at desktop/tablet/phone; the parking markup remains and is CSS-hidden.
- Check that there are no broken network requests, localhost URLs or incorrect external links before any hosting.
- Compress large clean images only after visual comparison; do not alter originals or clean references without review.

## Sharing and project hygiene

- The owner has confirmed permission to include and share `sajiri-gojiri.mp3` for the intended project arrangement; that confirmation does not grant unrestricted public redistribution rights.
- The Missing Piece template's published terms include restrictions on redistribution/sharing, third-party use and watermark alteration. The intended use is private GitHub collaboration with the owner's brother; public distribution and public hosting are not currently intended. See [IMAGES.md](IMAGES.md#licensing-and-sharing) for the concise licensing note.
- Do not add private family photographs to Git without project authorization.
- The project-local repository is intended for private collaboration with the owner's brother. It currently has no remote; local development and commits are distinct from private GitHub collaboration and from public distribution or hosting.
- The active HTML and custom MJS now reference all eight clean image families and all 22 locally present clean variants. The older `city-2.html` is not selected by the active route and remains a candidate for exclusion from the eventual Git repository; it has not been removed.
