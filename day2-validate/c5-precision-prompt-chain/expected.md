# Expected · C5 Precision Prompt Chain (made up data)

## Lands on
After prompt 1: 3 screens become 5 (Enquiry list, Enquiry detail, Draft reply, Partner check, PM dashboard). The list stays the anchor. Nothing is torn down.
After prompt 2: loading, empty and error states with the text in day2-validate/PROMPTS.md ("No enquiries right now." / "New enquiries will appear here." / "Try again"), and the line "Drafts are never sent automatically. An officer reviews and sends each one."
After prompt 3: the audit names the 3 gaps seeded in the list screen: the header is too small (14px), the main button looks disabled (opacity .45), row spacing is tight (2px). It fixes only the first two.
Then Claude saves the 3 prompts to day2-validate/PROMPTS.md.

Line to say: could a teammate reproduce this from your three prompts alone? After today, yes.

## Fallback
If the audit ranks the gaps in a different order, say so out loud: the point is "audit first, then a scoped fix", not which two it picks. Or play the C5 HyperFrames video.
