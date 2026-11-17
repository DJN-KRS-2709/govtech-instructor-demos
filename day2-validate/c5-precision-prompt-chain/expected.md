# Expected · C5 Your Prompt Chain (made up data)

## Lands on
After prompt 1: a partner check view is added after the dashboard. The dashboard stays the anchor and is unchanged.
After prompt 2: after 30 seconds the partner check asks "Which reply would you change?" It counts partners who name one. Five made-up answers go in: 3 name a change, 2 do not. The count is 3 of 5. The success signal is 4 of 5, so not yet. The kill switch (fewer than 3 of 5) holds.
After prompt 3: the audit names the 2 biggest gaps on the partner check: the kill switch line is easy to miss, and the timer has no label. It fixes only the top one (the kill switch line, .kill-line).
Then Claude saves the three prompts and their checks to day2-validate/PROMPTS.md, logs toy or tool: tool in build-log.md, and merges both on main.

Line to say: add behavior, never rebuild. Could a teammate rerun this from your three prompts alone?

## Fallback
If the audit ranks the gaps in a different order, say so out loud: the point is "audit first, then a scoped fix", not which one it picks. Or play the C5 Prompt Chain video.
