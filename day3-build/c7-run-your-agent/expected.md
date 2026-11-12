# Expected · C7 Run Your Agent (made up data)

## Lands on
day3-build/CLAUDE.md with four rules: never send, escalate, refuse, name the policy page.
IN-1 (complete) breaks rule 4: it drafts a renewal reply but names no policy page. That break is seeded: day3-build/agent-spec.md lists no policy page for parking permit renewals.
IN-2 escalates to an officer, no draft sent. IN-3 refuses and points to the official process.
The log shows 1 break, with a next change such as "Move rule 4 to the top of CLAUDE.md, then re-run IN-1."

Line to say: an assistant with rules, running in the Code tab. Not a production agent runtime. You want to find the break here, before anyone relies on it.

## Fallback
If Claude invents a policy page for IN-1, ask: "Which page in agent-spec.md did that come from?" There is none, so that is the rule 4 break. Or play the C7 HyperFrames video.
