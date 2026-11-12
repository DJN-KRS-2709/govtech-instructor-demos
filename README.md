# GovTech instructor demos · run sheet (made up data)

Every instructor demo in the 12 GovTech Curriculum decks, ready to run live in the Claude desktop app, Code tab. All data is made up. Scenarios: A ServiceSG, B ICA, C MOE.

## How to run a demo

1. In the Claude desktop app, open the Code tab and select the demo's folder (for example `day4-measure/c12-read-product-data`) as the folder Claude works in.
2. Open the demo's `prompt.md` and paste the prompts in order. `expected.md` has the answer it should land on and one fallback.
3. To reset after a run, ask Claude in the Code tab: `restore this demo folder to the last commit`.
4. Five demos also have a HyperFrames video on the slide (C4, C5 twice, C7, C8). If a live run stalls, play the video.

No Terminal steps. The Claude desktop app and the browser are all you need.

## Day 2 · Validate

### C4 · The Triple-Threat Build · 4 min · `day2-validate/c4-triple-threat-build/`

Slide: "The Triple-Threat Build" (Instructor-Led Demo, Scenario A). Also on video: `c4-triple-threat-build.mp4`.
```
Build a dashboard so officers can see their own reopened enquiries by category. Use made-up sample data. Save it in day2-validate/prototype/.
```

Then: `Which of the three theories in GROUP.md does this dashboard test?`

Lands on: it only built the loudest guess.

### C5 · Demo · Context Injection · 5 min (agenda 4) · `day2-validate/c5-context-injection/`

Slide: "Demo · Context Injection" (Instructor-Led Demo · 5 Minutes). Also on video: `c5-context-injection.mp4`. Attach `day2-validate/validation-brief.md` and `day2-validate/data/sample-enquiries.csv` first.
```
Use the brief and the CSV. Rebuild the inbox with the real enquiries and a draft reply each, then add the partner check from the brief.
```

Then: `Read day2-validate/data/partner-check-results.csv. Against the kill switch in day2-validate/validation-brief.md, does it fire?`

Lands on: 2 of 5 partners missed the urgent enquiry, so the kill switch fires.

### C5 · Demo · The Precision Prompt Chain · 6 min (agenda 4) · `day2-validate/c5-precision-prompt-chain/`

Slide: "Demo · The Precision Prompt Chain" (Instructor-Led Demo · 6 Minutes). Also on video: `c5-precision-prompt-chain.mp4`.
```
Prompt 1, Expand: add an enquiry detail view and a draft reply view, in that order. Keep the list as the anchor.
```
```
Prompt 2, Behavior: add loading, empty and error states with the exact text in PROMPTS.md. Drafts are never sent automatically.
```
```
Prompt 3, Refine: audit the list screen for its 3 biggest visual gaps. Then fix only the top two.
```

Lands on: 3 screens become 5, states added, the audit names the header, the disabled-looking button and the row spacing, and fixes two.

### C6 · Exterior vs Hood · inside the 4 min slide · `day2-validate/c6-exterior-vs-hood/`

Slide: "Exterior vs hood" (Lecture; the live demo is in the speaker note, Scenario B).
```
Open day2-validate/prototype/index.html. List what's missing before this could go to production: data handling, error paths, access rules, tests, and how the AI step is called.
```

Lands on: a long list against a screen that looks finished.

## Day 3 · Build

### C7 · Instructor Demo · Run Your Agent · 5 min of the 15 min lab · `day3-build/c7-run-your-agent/`

Slides: "Instructor Demo · Run Your Agent" and "Run Your Agent in the Code tab". Also on video: `c7-run-your-agent.mp4`. Attach `day3-build/agent-spec.md` and `day3-build/agent-control-panel.md` first.
```
Create day3-build/CLAUDE.md from agent-spec.md and agent-control-panel.md
```
```
add 3 made-up inputs to day3-build/agent-run-log.md: one to complete, one to escalate, one to refuse
```
```
Run each of the 3 inputs with day3-build/CLAUDE.md. Show what you would do.
```
```
Note where it broke a rule in day3-build/agent-run-log.md.
```
```
Save day3-build/agent-run-log.md and day3-build/CLAUDE.md on main.
```

Lands on: the complete case breaks rule 4 (no policy page named).

### C8 · Instructor Demo · Connected to Secured · 8 min (agenda 12) · `day3-build/c8-connected-to-secured/`

Slide: "Instructor Demo · Connected to Secured" (Demo · 8 min). Also on video: `c8-connected-to-secured.mp4`.
```
Add a data schema to sample-app/ for enquiries. Use synthetic records only.
```
```
Add a simple sign-in so the app knows who is asking. Test accounts only.
```
```
Add row level access rules: each user sees only their own records.
```
```
Run a security check, then deploy to a local test environment.
```

Lands on: each officer sees only their own 3 made-up records; the check warns sign-in is test accounts only.

## Day 4 · Measure and decide

### C12 · Read Your Product Data · 2 min demo before the 7 min lab · `day4-measure/c12-read-product-data/`

Slide: "Lab · Read Your Product Data" ("Instructor demo, 2 minutes").
```
read day4-measure/data/synthetic-usage.csv and name the one biggest signal against day4-measure/metrics-plan.md
```

Lands on: officers rewrite most drafts on one enquiry type, Permits (78 of 100), past the stop line in the metrics plan.

## No demo on Day 1
Curriculum 1 to 3 have no instructor demo slide.

## Files
- `demos/INVENTORY.md`: every demo with module, slide, minutes, what the instructor does, prompts, files and the outcome.
- `tools/seed.py`: writes all made-up data, deterministic. `tools/verify.py`: checks each expected signal is really in the data. Maintainer steps, not part of the live run.
- `preview/index.html`: this run sheet in the browser, with links to every demo file.
