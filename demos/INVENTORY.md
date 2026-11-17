# Instructor demo inventory (made up data)

Read from the 12 GovTech Curriculum instructor decks (`Curriculum N - Slides.html`, Nov 12 build in `govtech-sg/takeaway-stories/out/`). A slide counts when its body says "Instructor demo", its tag says Demo, or its speaker note describes a live demo. Prompts for the 5 HyperFrames demos were read off the videos' on-screen chat, because those slides show no prompt.

| Day | Module | Slide (deck index) | Demo | Minutes | Folder |
|---|---|---|---|---|---|
| 2 | C4 | The Triple-Threat Build | Build the loudest guess, then ask if it helps | 4 | `day2-validate/c4-triple-threat-build/` |
| 2 | C5 | Demo · Context Injection | Module 4 dashboard, one prompt, assumption in build-log.md, made-up CSV | 3 | `day2-validate/c5-context-injection/` |
| 2 | C5 | Demo · Your Prompt Chain | Expand, Behavior, Refine on the same dashboard | 3 (tag 6) | `day2-validate/c5-precision-prompt-chain/` |
| 2 | C6 | Demo vs code | Ask Claude what's missing for production on the end-of-M5 dashboard | inside the 8 min block | `day2-validate/c6-demo-vs-code/` |
| 3 | C7 | Instructor Demo · Run Your Agent (#14) and Run Your Agent in the Code tab (#15) | Instruction file, 3 inputs, run, log the break, save on main | 5 of the 15 min lab | `day3-build/c7-run-your-agent/` |
| 3 | C8 | Instructor Demo · Connected to Secured (#12) | Schema, sign-in, access rules, check and deploy | 8 (agenda 12) | `day3-build/c8-connected-to-secured/` |
| 4 | C12 | Lab · Read Your Product Data (#11) | Read a seeded dataset, name one signal | 2 (before the 7 min lab) | `day4-measure/c12-read-product-data/` |

HyperFrames videos on the slide: C4, C5 Context Injection, C5 Your Prompt Chain, C7, C8. All 5 can also run live from this repo. Day 2 is one Scenario A thread.

## Details

### C4 · The Triple-Threat Build
- Tag: Instructor-Led Demo. Speaker note: "Planned: 4 min". Scenario A, made up.
- Instructor: shows three leaders with three theories and no data, sends one simple prompt, Claude writes the files and starts a local preview, then asks whether the dashboard is helpful.
- Prompt (video): `Build a dashboard so officers can see their own reopened enquiries by category. Use made-up sample data. Save it in day2-validate/prototype/.`
- Files: `GROUP.md` (the video shows Claude reading it), `day2-validate/prototype/`.
- Outcome: it built only the Chief Executive's guess; neither other theory is tested.

### C5 · Demo · Context Injection
- Tag: Instructor-Led Demo. Agenda: 3 min. Scenario A, made up.
- Instructor: opens the Module 4 officer dashboard (it looks finished and tests nothing), pastes one lab prompt. Claude plans, writes the assumption into `day2-validate/build-log.md`, makes a made-up CSV, wires the dashboard, and merges on main.
- Prompt (video): `Read one-pager.md and day2-validate/build-log.md. Plan first. Then add my riskiest assumption: officers who see their own reopened enquiries will change how they reply, its risk type, a kill switch and a success signal to day2-validate/build-log.md, update day2-validate/prototype/ to test it using made-up sample data labelled as made up, and save both on main (open the pull request and merge it).`
- Files: `one-pager.md`, `day2-validate/build-log.md` (Module 4 entry only), `day2-validate/prototype/` (Module 4 dashboard).
- Outcome: same dashboard, now testing the assumption, with OFF-07's made-up metrics and a marked Payments signal (29% reopen rate, top reason missed next step).

### C5 · Demo · Your Prompt Chain
- Tag: Instructor-Led Demo · 6 Minutes. Agenda: 3 min. Scenario A, made up.
- Instructor: runs three prompts in order on the Context Injection result, without rebuilding the dashboard.
- Prompts (video): Prompt 1 Expand, Prompt 2 Behavior, Prompt 3 Refine, then save to PROMPTS.md (full text in `prompt.md`).
- Files: `one-pager.md`, `day2-validate/build-log.md` (assumption already logged), `day2-validate/data/sample-officer-metrics.csv`, `day2-validate/prototype/` (dashboard only; no partner check yet), stub `day2-validate/PROMPTS.md`.
- Outcome: partner check added, 5 made-up answers counted (3 of 5 name a change, kill switch holds), one scoped fix on `.kill-line`, prompts and toy-or-tool: tool saved on main.

### C6 · Demo vs code
- Tag: Lecture. The live demo is in the speaker note. Part of the 8 min Module 6 block. Scenario A, made up.
- Instructor: in the Claude desktop app, Code tab, selects `day2-validate/c6-demo-vs-code`, opens the end-of-Module-5 officer dashboard, and asks what is missing for production.
- Prompt: none on the slide; `prompt.md` turns the note into one prompt.
- Files: `day2-validate/prototype/index.html` (Scenario A dashboard, polished with a thin hood), `partner-check.html`, `styles.css`, `data.js`, `data/sample-officer-metrics.csv`.
- Outcome: gaps in data handling, error paths, access rules, tests and the AI step, against a screen that looks finished.

### C7 · Instructor Demo · Run Your Agent
- #14 tag: Instructor Demo, no Planned line. #15 body: "Instructor demo 5 minutes, then 10 minutes on your own agent." #15 note: "Planned: 15 min (agenda: 10 min)".
- Instructor: creates the instruction file, writes 3 made-up inputs, runs them, logs the break, saves on main.
- Prompts: slide steps on #14 and #15 plus the video chat (full text in `prompt.md`).
- Files: `day3-build/agent-spec.md`, `day3-build/agent-control-panel.md`, `day3-build/agent-run-log.md`, creates `day3-build/CLAUDE.md`.
- Outcome: IN-1 (complete) breaks rule 4, no policy page named.

### C8 · Instructor Demo · Connected to Secured
- Tag: Demo · 8 min. Note: "Planned: 8 min (agenda: 12 min)", "on my own sample repo, in Claude Code, with made-up data only".
- Instructor: four prompts, one per step.
- Prompts (video): schema, sign-in, row level access rules, security check and local test deploy.
- Files: `sample-app/` (index.html, data/enquiries.csv with 6 made-up rows on example.test test accounts).
- Outcome: each officer sees only their own records; the check passes and warns sign-in is test accounts only.

### C12 · Lab · Read Your Product Data
- Body: "Instructor demo, 2 minutes: read a seeded synthetic dataset in the Claude desktop app, Code tab and name one signal." Note: "Planned: 7 min, after a 2 min demo from me".
- Prompt: the slide has none for the instructor; `prompt.md` adds one, plus the learner prompt word for word.
- Files: `day4-measure/data/synthetic-usage.csv` (the learner path on the slide), `day4-measure/metrics-plan.md`, `day4-measure/iteration.md`.
- Outcome: officers rewrite most drafts on one enquiry type (Permits, 78 of 100), past the stop line.

## Slide and speaker note disagreements
1. C5 Your Prompt Chain: 6 min on the tag, 3 min in the Module 5 agenda.
2. C7: the Run Your Agent slides and the video run 3 inputs and find a rule 4 break on the complete case; one speaker note says the demo runs "one made-up example that should escalate. Watch where it stops."
3. C7: the lab body and Instructor Guide give 5 min of demo; one note says "under a minute" (the video).
4. C8: 8 min on the tag and note, 12 min in the agenda and Instructor Guide.
5. C12: the subtitle says "Ten minutes on a seeded synthetic dataset"; the timer is 7 min and the note gives 2 + 7 = 9.
6. C6: the note describes a live demo, but the slide is tagged Lecture.

## Looked at, not counted
- C9 "Role Clarity and Team Shape": instructor led, takes learners' scenarios as live examples; no Code tab demo.
- C12 "Final Presentations": learners demo their own prototypes.
- C2, C4, C6, C11 slides that use "demo" as a word ("only impress in a demo", "A working demo doesn't prove quality"): not demos.
