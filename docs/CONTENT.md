# Wedding content inventory

The active page is `download/www.missingpieceinvites.com/demos/city-2-local.html`; the page-specific bundle is `download/framerusercontent.com/sites/3bR6R2YrHoycodLqL6z8ep/rnnTUOxVq8PHuNJnW02Z-QNi-QQMH82osuPTQxAKcn0.q7vHoL6S.mjs`. The table records current content from the user-provided handoff and static inspection. Desktop/tablet/phone SSR repeats some HTML copy. Component prop/instance locations are listed where provided by the audit; verify before editing.

| Content | Current page value | Source location / status |
|---|---|---|
| Couple | SHIVANI / weds / KETAN; title case forms also appear | HTML hero variants and page-instance bundle props. Old template names may remain in non-visible Framer layer names. |
| Bride's blessing | “With the blessings of the late Dadasaheb Patil, the late Pramila Patil & the late Pandurang Chandwade” | Instance `NTi5RD_EY`; props `rEqxinV9x`, `KhId2_Z78`, `SwyWMQuoO`; HTML text and MJS. |
| Bride's parents | Mrs. Rupali & Mr. Nitin Chandwade | Same bride-side instance; HTML and MJS. |
| Groom's parents | “Son of” Mrs. Hemlata & Mr. Mohan Mohite | Instance `YV8c7Qylc`; props `sKFuJb5xa`, `PF8ftF8Ur`; HTML and MJS. |
| Wedding | Friday, November 27th 2026, 12:24pm | Event card; source of truth says 12:24 PM. |
| Haldi | Thursday, November 26th 2026, 7pm Onwards | **Incorrect:** source of truth is 7:00 AM. |
| Sakharpuda | Thursday, November 26th 2026, 5pm Onwards | Matches supplied schedule. Former template title was Engagement. |
| Mehendi | Friday, March 9th 2026, 6pm Onwards | Template placeholder; date/time awaiting confirmation. |
| Cocktail | Friday, March 10th 2026, 6pm Onwards | Template placeholder; date/time awaiting confirmation. |
| Reception | Friday, March 17th 2026, 6pm Onwards | Template placeholder; date/time pending groom-side confirmation. |
| Event-card venue | GMK Banquets & Lawns, Ravet, Pune | All six cards; full supplied address: Katraj-Dehu Road Bypass, Ravet, Pimpri-Chinchwad, Pune, Maharashtra. |
| Countdown | `2026-11-27T06:54:00.000Z`, `pickTime: 6` | Page-instance props; 06:54 UTC is 12:24 PM IST. Component uses `setUTCHours(pickTime)`; live countdown correctness has not been browser-tested. |
| Hashtag | `#ShivKetan` | Two HTML copies and one page prop per supplied audit. `#BadriKiDulhania` also remains in export source; visibility is unverified. |
| WhatsApp | `wa.me/918888823338` | Replaced template placeholder; target not click-tested. |
| Map | `https://share.google/t3Uf17DTRMBksyH7F` | Prop `Ze39EmOzQ` (event cards) and location CTA prop `i9HrUZDnv`, instance `mpz3MRaNl`; HTML opens new tab. Destination was not resolved/verified. |
| Instagram | “Click to open our Instagram page” | Target still points to Missingpiece in two HTML copies and one MJS prop; decision pending. |
| Music | `framerusercontent.com/assets/sajiri-gojiri.mp3` | Local audio is present; prior handoff says a body script tries autoplay and listens for first user gesture if blocked. Actual playback is untested. |
| Weather / stay | “mostly sunny” up to 28 degrees; Bhola Bhawan staff-hotel copy | Generic/template copy requiring Pune-specific confirmation or removal. |

## Responsive/source editing notes

The active HTML has duplicated responsive variants; counts of repeated strings are not counts of unique event cards. The user-provided source says edits were made in both HTML and page-instance props, while shared defaults were generally left intact. A prior audit also found a CSS order correction removed in favor of changing the content arrangement. Check all instances and breakpoints, then make a reviewable diff before editing.

## Website gallery functionality

The active page bundle includes the existing `SlideShow` module and photo-highlight/gallery functionality. This is part of the website; its browser behavior has not been tested in this audit.
