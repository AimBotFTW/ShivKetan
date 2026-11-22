# Wedding content inventory

The active page is `download/www.missingpieceinvites.com/demos/city-2-local.html`; the page-specific bundle is `download/framerusercontent.com/sites/3bR6R2YrHoycodLqL6z8ep/rnnTUOxVq8PHuNJnW02Z-QNi-QQMH82osuPTQxAKcn0.q7vHoL6S.mjs`. The table records current content from the user-provided handoff and static inspection. Desktop/tablet/phone SSR repeats some HTML copy. Component prop/instance locations are listed where provided by the audit; verify before editing.

| Content | Current page value | Source location / status |
|---|---|---|
| Couple | SHIVANI / weds / KETAN; title case forms also appear | HTML hero variants and page-instance bundle props. Old template names may remain in non-visible Framer layer names. |
| Bride's blessing | “With the blessings of the late Dadasaheb Patil, the late Pramila Patil & the late Pandurang Chandwade” | Instance `NTi5RD_EY`; props `rEqxinV9x`, `KhId2_Z78`, `SwyWMQuoO`; HTML text and MJS. |
| Bride's parents | Mrs. Rupali & Mr. Nitin Chandwade | Same bride-side instance; HTML and MJS. |
| Groom's parents | “Son of” Mrs. Hemlata & Mr. Mohan Mohite | Instance `YV8c7Qylc`; props `sKFuJb5xa`, `PF8ftF8Ur`; HTML and MJS. |
| Wedding | Friday, November 27th 2026, 12:24 PM | Event card; source of truth says 12:24 PM. |
| Haldi | Thursday, November 26th 2026, 7:00 AM | Updated in SSR HTML and page-instance props. |
| Sakharpuda | Thursday, November 26th 2026, 5:00 PM | Matches supplied schedule. Former template title was Engagement. |
| Mehendi | Old March 2026 placeholder | Card hidden pending confirmed event details; no replacement invented. |
| Cocktail | Old March 2026 placeholder | Card hidden pending confirmed event details; no replacement invented. |
| Reception | Old March 2026 placeholder | Card hidden pending confirmed date/time; no replacement invented. |
| Event-card venue | GMK Banquets & Lawns, Dehu Road Bypass, Ravet, Pimpri-Chinchwad, Pune | Shown on the three confirmed cards. |
| Countdown | `2026-11-27T06:54:00.000Z`, `pickTime: 6` | Page-instance props; 06:54 UTC is 12:24 PM IST. Component uses `setUTCHours(pickTime)`; live countdown correctness has not been browser-tested. |
| Hashtag | `#ShivKetan` | Two HTML copies and one page prop per supplied audit. `#BadriKiDulhania` also remains in export source; visibility is unverified. |
| WhatsApp | `wa.me/918888823338` | Unconfirmed; CTA hidden pending owner confirmation. |
| Map | `https://share.google/t3Uf17DTRMBksyH7F` | Destination not verified; map CTAs hidden pending owner confirmation. |
| Instagram | Couple account not supplied | Vendor destination removed/disabled; CTA hidden pending owner confirmation. |
| Music | Local `sajiri-gojiri.mp3` | Autoplay removed; playback begins on a user gesture. Browser check changed the control to pause; duplicate rendered players are paused by the controller and the track loops. |
| Weather / stay | No confirmed details supplied | Template weather and staff-stay copy removed from the active page. |

## Responsive/source editing notes

The active HTML has duplicated responsive variants; counts of repeated strings are not counts of unique event cards. The user-provided source says edits were made in both HTML and page-instance props, while shared defaults were generally left intact. A prior audit also found a CSS order correction removed in favor of changing the content arrangement. Check all instances and breakpoints, then make a reviewable diff before editing.

## Website gallery functionality

The active page bundle includes the existing `SlideShow` module and photo-highlight/gallery functionality. This is part of the website; its browser behavior has not been tested in this audit.
