# Working with AI agents

Use Codex, Antigravity, Cursor or another agent as a careful pair-programmer. Give it one bounded task, require evidence before edits, and keep people in control of ambiguous content.

## Task rules

- Ask for a find/report pass first. If wording, link target, event detail, image identity, or source file is ambiguous, the agent must stop before editing and show the ambiguity.
- Never print whole HTML or MJS files. MJS is minified; use `grep -c`, `rg -o` with short context, or line-limited excerpts.
- Before an edit, make a backup or a small Git commit and inspect the diff. Do not delete existing backups. Never claim a check passed unless it was actually run.
- The active Framer page has SSR HTML and MJS props, with repeated responsive variants. Check both sources and all breakpoints when editing user-facing text.
- No browser/server checks inside a restricted agent sandbox. The owner performs visual review and browser/network checks. If a task asks for runtime verification, report exactly what could not be tested.
- Run `node --check` on any changed MJS file. Run only checks requested by the task or needed to substantiate claims.
- Preserve originals. Do not rerun LaMa, overwrite clean images, or adjust masks without explicit task direction and review of the full-resolution assets.
- Keep private family photographs outside the repository unless the project owner explicitly authorizes their inclusion. Do not add large media without checking rights and asking first.

## Branch and review workflow

Use one feature branch per bounded change, for example `feature/event-cards`. Keep diffs small and commits descriptive. Review the diff and complete manual QA before merging to `main`. The intended workflow is local development and commits, then private GitHub collaboration with the owner's brother. Keep the repository private; public distribution and public hosting are not currently intended. The local repository currently has no remote. See `IMAGES.md` for the separate template-term note; do not infer public distribution rights from private collaboration.

## Manual QA checklist

- Desktop 1440px, tablet 1000px and phone 390px.
- Hero order, parents and grandparents, event-card copy and images, countdown, hashtag.
- Map and WhatsApp links point to approved destinations.
- Song starts after the first tap/click when autoplay is blocked, loops, and respects pause.
- No Buy Now button, no Parking card, and no visible watermark overlays or baked-in marks in day/night scenes and cars.
- No shifted layout, clipped text, broken images, or red rows in the Network panel.
- Check console/hydration behavior, keyboard/focus, contrast, image alternatives and duplicate IDs.
- Confirm every check was run and record any remaining failure or uncertainty.
