# GovTech instructor demos · run sheet (made up data)

Every instructor demo in the 12 GovTech Curriculum decks, ready to run live in the Claude desktop app, Code tab. All data is made up. Scenarios: A ServiceSG, B ICA, C MOE.

## How to run a demo

1. In the Claude desktop app, open the Code tab and select the demo's folder (for example `day4-measure/c12-read-product-data`) as the folder Claude works in.
2. Open the demo's `prompt.md` and paste the prompts in order. `expected.md` has the answer it should land on and one fallback.
3. To reset after a run, ask Claude in the Code tab: `restore this demo folder to the last commit`.
4. Five demos also have a HyperFrames video on the slide (C4, C5 twice, C7, C8). If a live run stalls, play the video.

No Terminal steps. The Claude desktop app and the browser are all you need.

## Day 2 · Validate

Every Day 2 demo runs on one Scenario A thread: ServiceSG enquiry response, made-up data. Module 4 builds the officer dashboard. Module 5 aims it at an assumption, then adds a partner check. Module 6 opens that same dashboard and asks what is missing for production.

### C4 · The Triple-Threat Build · 4 min · `day2-validate/c4-triple-threat-build/`

Slide: "The Triple-Threat Build" (Instructor-Led Demo, Scenario A). Also on video: `c4-triple-threat-build.mp4`.
```
Build a dashboard so officers can see their own reopened enquiries by category. Use made-up sample data. Save it in day2-validate/prototype/.
```

Then: `Which of the three theories in GROUP.md does this dashboard test?`

Lands on: it only built the loudest guess.

### C5 · Demo · Context Injection · 3 min · `day2-validate/c5-context-injection/`

Slide: "Demo · Context Injection" (Instructor-Led Demo). Also on video: `c5-context-injection.mp4`. Starts from the Module 4 officer dashboard, plus `one-pager.md` and `day2-validate/build-log.md`.
```
Read one-pager.md and day2-validate/build-log.md. Plan first. Then add my riskiest assumption: officers who see their own reopened enquiries will change how they reply, its risk type, a kill switch and a success signal to day2-validate/build-log.md, update day2-validate/prototype/ to test it using made-up sample data labelled as made up, and save both on main (open the pull request and merge it).
```

Lands on: the same dashboard now tests an assumption, with a made-up CSV and one marked signal.

### C5 · Demo · Your Prompt Chain · 3 min · `day2-validate/c5-precision-prompt-chain/`

Slide: "Demo · Your Prompt Chain" (Instructor-Led Demo · 6 Minutes). Also on video: `c5-precision-prompt-chain.mp4`. Starts from the end of Context Injection.
```
Prompt 1, Expand: add a partner check view after the dashboard, in that order. Keep the dashboard as the anchor.
```
```
Prompt 2, Behavior: after 30 seconds, ask "Which reply would you change?" Count partners who name one. Fewer than 3 of 5 fires the kill switch.
```
```
Prompt 3, Refine: audit the partner check for its 2 biggest gaps. Fix only the top one.
```

Then: `Save the chain and its checks to PROMPTS.md, log toy or tool in build-log.md, and save both on main.`

Lands on: a partner check on the same dashboard, answers counted against the kill switch, one scoped fix, prompts saved on main.

### C6 · Demo vs code · inside the 8 min slide block · `day2-validate/c6-demo-vs-code/`

Slide: "Demo vs code" (Lecture; the live demo is in the speaker note, Scenario A). In the Claude desktop app, Code tab, select `day2-validate/c6-demo-vs-code`.
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
