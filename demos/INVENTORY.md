# Instructor demo inventory (made up data)

Read from the 12 GovTech Curriculum instructor decks (`Curriculum N - Slides.html`, Nov 12 build in `govtech-sg/takeaway-stories/out/`). A slide counts when its body says "Instructor demo", its tag says Demo, or its speaker note describes a live demo. Prompts for the 5 HyperFrames demos were read off the videos' on-screen chat, because those slides show no prompt.

| Day | Module | Slide (deck index) | Demo | Minutes | Folder |
|---|---|---|---|---|---|
| 2 | C4 | The Triple-Threat Build (#4) | Build the loudest guess, then ask if it helps | 4 | `day2-validate/c4-triple-threat-build/` |
| 2 | C5 | Demo · Context Injection (#2) | Shiny shell, then brief + data, partner check, kill switch | 5 (agenda 4) | `day2-validate/c5-context-injection/` |
| 2 | C5 | Demo · The Precision Prompt Chain (#7) | Expand, Behavior, Refine on one build | 6 (agenda 4) | `day2-validate/c5-precision-prompt-chain/` |
| 2 | C6 | Exterior vs hood (#4) | Ask Claude what's missing for production | inside the 4 min slide | `day2-validate/c6-exterior-vs-hood/` |
| 3 | C7 | Instructor Demo · Run Your Agent (#14) and Run Your Agent in the Code tab (#15) | Instruction file, 3 inputs, run, log the break, save on main | 5 of the 15 min lab | `day3-build/c7-run-your-agent/` |
| 3 | C8 | Instructor Demo · Connected to Secured (#12) | Schema, sign-in, access rules, check and deploy | 8 (agenda 12) | `day3-build/c8-connected-to-secured/` |
| 4 | C12 | Lab · Read Your Product Data (#11) | Read a seeded dataset, name one signal | 2 (before the 7 min lab) | `day4-measure/c12-read-product-data/` |

HyperFrames videos on the slide: C4, C5 Context Injection, C5 Precision Prompt Chain, C7 (#14), C8. All 5 can also run live from this repo.

## Details

### C4 · The Triple-Threat Build
- Tag: Instructor-Led Demo. Speaker note: "Planned: 4 min". Scenario A, made up.
- Instructor: shows three leaders with three theories and no data, sends one simple prompt, Claude writes the files and starts a local preview, then asks whether the dashboard is helpful.
- Prompt (video): `Build a dashboard so officers can see their own reopened enquiries by category. Use made-up sample data. Save it in day2-validate/prototype/.`
- Files: `GROUP.md` (the video shows Claude reading it), `day2-validate/prototype/`.
- Outcome: it built only the Chief Executive's guess; neither other theory is tested.

### C5 · Demo · Context Injection
- Tag: Instructor-Led Demo · 5 Minutes. Note: "Planned: 5 min (agenda: 4 min)".
- Instructor: opens a polished inbox that tests nothing, feeds it context, rebuilds, runs a partner check.
- Prompt (video): `Use the brief and the CSV. Rebuild the inbox with the real enquiries and a draft reply each, then add the partner check from the brief.` Added for the live run: read `day2-validate/data/partner-check-results.csv` against the kill switch.
- Files: `day2-validate/validation-brief.md`, `day2-validate/data/sample-enquiries.csv`, `day2-validate/data/partner-check-results.csv`, `day2-validate/data/officer-quotes.md` (optional), `day2-validate/prototype/`.
- Outcome: 2 of 5 partners miss the urgent enquiry (E-2041), so the kill switch fires.

### C5 · Demo · The Precision Prompt Chain
- Tag: Instructor-Led Demo · 6 Minutes. Note: "Planned: 6 min (agenda: 4 min)".
- Instructor: runs three prompts in order on one build without rebuilding.
- Prompts (video): Prompt 1 Expand, Prompt 2 Behavior, Prompt 3 Refine (full text in `prompt.md`).
- Files: `day2-validate/prototype/` (3 screens seeded), `day2-validate/PROMPTS.md` (state text), `day2-validate/data/sample-enquiries.csv`.
- Outcome: 5 screens, loading, empty and error states, never-send line, audit of 3 seeded visual gaps with 2 fixed, prompts saved to PROMPTS.md.

### C6 · Exterior vs hood
- Tag: Lecture. Note: "Planned: 4 min (12 min with the next two slides)" and "Let me show you on one prototype. I'll open the screen in Claude Code, and then ask Claude to list what's missing for production."
- Prompt: none on the slide; `prompt.md` turns the note into one prompt.
- Files: `day2-validate/prototype/index.html` (Scenario B, ICA, polished with a thin hood).
- Outcome: gaps in data handling, error paths, access rules, tests and the AI step.

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
1. C5 Context Injection: the tag says 5 Minutes and the note says 5 min (agenda 4), but the slide's "Next" card says "What you'll have in 7 min" and the note says "In about seven minutes".
2. C5 Context Injection: the slide and note promise "real user quotes" and "domain metrics"; the video only uses a brief and a CSV. The note's example is ICA (parents renewing for a child, 17% come back); the video is Scenario A, ServiceSG.
3. C5 Precision Prompt Chain: 6 min on the tag and note, 4 min in the agenda.
4. C7: #14 and the video run 3 inputs and find a rule 4 break on the complete case; the #15 note says the demo runs "one made-up example that should escalate. Watch where it stops."
5. C7: the #15 body and Instructor Guide give 5 min of demo; #14 has no Planned line and the note says "under a minute" (the video).
6. C8: 8 min on the tag and note, 12 min in the agenda and Instructor Guide.
7. C12: the subtitle says "Ten minutes on a seeded synthetic dataset"; the timer is 7 min and the note gives 2 + 7 = 9.
8. C6: the note describes a live demo, but the slide is tagged Lecture and the Instructor Guide lists no demo for C6.

## Looked at, not counted
- C9 "Role Clarity and Team Shape": instructor led, takes learners' scenarios as live examples; no Code tab demo.
- C12 "Final Presentations": learners demo their own prototypes.
- C2, C4, C6, C11 slides that use "demo" as a word ("only impress in a demo", "A working demo doesn't prove quality"): not demos.
