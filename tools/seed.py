#!/usr/bin/env python3
"""Seed every demo folder with its made-up data. Deterministic: same seed, same bytes.
Run from the repo root with: python3 tools/seed.py  (maintainer step, not part of the live run sheet)."""
import csv, io, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20261112
MADE_UP = "Made up for a live demo. Synthetic data, no real people, no real records."

def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", newline="\n") as f:
        f.write(text if text.endswith("\n") else text + "\n")

def csv_text(header, rows):
    buf = io.StringIO()
    buf.write("# " + MADE_UP + "\n")
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue()

def page(title, scenario, body, style=""):
    return f"""<!doctype html>
<!-- {MADE_UP} -->
<html lang="en"><head><meta charset="utf-8"><title>{title} (made up)</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{{font-family:system-ui,Helvetica,Arial,sans-serif;margin:0;background:#f4f5f8;color:#111}}
header{{display:flex;justify-content:space-between;align-items:center;padding:18px 28px;background:#fff;border-bottom:1px solid #e3e5ea}}
.badge{{font:600 11px ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;background:#fff4d6;color:#7a4b00;padding:4px 8px;border-radius:4px}}
main{{max-width:880px;margin:24px auto;padding:0 20px}}
.card{{background:#fff;border:1px solid #e3e5ea;border-radius:10px;padding:16px 18px;margin-bottom:12px}}
nav a{{margin-right:14px;color:#3046c8;text-decoration:none;font-weight:600}}
{style}
</style></head><body>
<header><div><strong>{title}</strong><div style="font-size:13px;color:#666">{scenario}</div></div><span class="badge">Made up</span></header>
<main>
{body}
</main></body></html>
"""

# ---------- Day 2 · C4 Triple-Threat Build (Scenario A, ServiceSG) ----------
D = "day2-validate/c4-triple-threat-build"
write(f"{D}/GROUP.md", f"""# GROUP.md (made up for this demo)

{MADE_UP}

## Scenario A · ServiceSG enquiry replies

Residents reopen 1 in 4 enquiries within 30 days.

## Three leaders, three theories, zero data

- Director, Service Operations: "It's the replies. Our templates are too long."
- Head of Product: "Residents can't find the right FAQ page."
- Chief Executive: "Build a dashboard so officers see their own numbers."

## Data we have

None yet. Nobody has measured which theory is true.

## Where builds go

Save prototypes in day2-validate/prototype/.
""")
write(f"{D}/day2-validate/prototype/README.md", f"# day2-validate/prototype/ (made up)\n\n{MADE_UP}\n\nEmpty on purpose. Claude builds the dashboard here during the demo.\n")

# ---------- Day 2 · C5 Context Injection (Scenario A, ServiceSG) ----------
D = "day2-validate/c5-context-injection"
ENQ = [("E-2041", "Fallen tree blocking a footpath", "Roads", "urgent"),
       ("E-2042", "Streetlight flickering on my block", "Lighting", "routine"),
       ("E-2043", "Question about a parking fine", "Parking", "routine"),
       ("E-2044", "How do I renew a permit?", "Permits", "routine"),
       ("E-2045", "Noise from a renovation next door", "Noise", "routine")]
write(f"{D}/day2-validate/data/sample-enquiries.csv", csv_text(["id", "subject", "category", "urgency"], ENQ))
write(f"{D}/day2-validate/validation-brief.md", """# Validation brief (made up for this demo)

## Hypothesis
Officers spot the urgent enquiry from the list alone,
in under 10 seconds.

## Test
5 partners look at the inbox. Which enquiry is urgent?

## Kill switch
If more than 1 of 5 partners miss the urgent enquiry,
redesign the list before building anything else.
""")
PARTNERS = [("Partner 1", "E-2041"), ("Partner 2", "E-2042"), ("Partner 3", "E-2041"), ("Partner 4", "E-2045"), ("Partner 5", "E-2041")]
write(f"{D}/day2-validate/data/partner-check-results.csv", csv_text(["partner", "picked_as_urgent", "seconds"],
      [(p, e, s) for (p, e), s in zip(PARTNERS, (6, 11, 8, 14, 7))]))
write(f"{D}/day2-validate/data/officer-quotes.md", f"""# Officer quotes (made up for this demo)

{MADE_UP}

- "I open every enquiry to find the urgent one. The list doesn't tell me."
- "A fallen tree and a noisy neighbour look the same in the inbox."
- "If I could see urgency first, I'd clear the queue faster."
""")
rows = "\n".join(f'<div class="card row"><span class="id">E-000{i}</span> <em>Enquiry subject goes here</em> <span class="tag">TAG</span> <a href="#">Draft reply &rsaquo;</a></div>' for i in range(1, 6))
write(f"{D}/day2-validate/prototype/index.html", page("Enquiry inbox", "Scenario A · officer view",
      f'<nav><a href="index.html">Inbox</a><a href="draft.html">Draft reply</a><a href="result.html">Result</a></nav>\n<div class="card"><strong>Hypothesis</strong> <em>Hypothesis goes here.</em></div>\n{rows}\n<div class="card"><strong>Next steps</strong> <em>Add success criteria later.</em></div>',
      ".row{display:flex;gap:14px;align-items:center}.id{font:12px ui-monospace,monospace;color:#666}.tag{margin-left:auto;font:11px ui-monospace,monospace;background:#eceef3;padding:2px 6px;border-radius:4px}"))
write(f"{D}/day2-validate/prototype/draft.html", page("Draft reply", "Scenario A · officer view", '<nav><a href="index.html">Inbox</a><a href="draft.html">Draft reply</a><a href="result.html">Result</a></nav>\n<div class="card"><em>Draft reply goes here.</em></div>'))
write(f"{D}/day2-validate/prototype/result.html", page("Result", "Scenario A · officer view", '<nav><a href="index.html">Inbox</a><a href="draft.html">Draft reply</a><a href="result.html">Result</a></nav>\n<div class="card"><em>Result goes here.</em></div>'))

# ---------- Day 2 · C5 Precision Prompt Chain (Scenario A, ServiceSG) ----------
D = "day2-validate/c5-precision-prompt-chain"
write(f"{D}/day2-validate/data/sample-enquiries.csv", csv_text(["id", "subject", "category", "urgency"], ENQ))
GAPS = ("h1{font-size:14px;font-weight:600;margin:0 0 6px}"            # gap 1: header too small
        ".btn{background:#3046c8;color:#fff;border:0;border-radius:6px;padding:8px 14px;opacity:.45}"  # gap 2: main button looks disabled
        ".row{padding:2px 8px;border-bottom:1px solid #eee;display:flex;gap:12px}")  # gap 3: row spacing tight
nav = '<nav><a href="index.html">Enquiry list</a><a href="partner-check.html">Partner check</a><a href="dashboard.html">PM dashboard</a></nav>'
lst = "\n".join(f'<div class="row"><span>{i}</span><span>{s}</span><span style="margin-left:auto">{c}</span></div>' for i, s, c, u in ENQ)
write(f"{D}/day2-validate/prototype/index.html", page("Enquiries", "Scenario A · officer view",
      f'{nav}\n<div class="card"><h1>Open enquiries</h1>\n{lst}\n<p><button class="btn">Open enquiry</button></p></div>', GAPS))
write(f"{D}/day2-validate/prototype/partner-check.html", page("Partner check", "Scenario A · partner view",
      f'{nav}\n<div class="card"><h1>Which enquiry is urgent?</h1><p>Each partner picks one.</p></div>', GAPS))
write(f"{D}/day2-validate/prototype/dashboard.html", page("PM dashboard", "Scenario A · PM view",
      f'{nav}\n<div class="card"><h1>PM dashboard</h1><p>5 open enquiries (made up).</p></div>', GAPS))
write(f"{D}/day2-validate/PROMPTS.md", f"""# PROMPTS.md (made up for this demo)

{MADE_UP}

## State text to use, word for word

- Loading: "Loading enquiries..."
- Empty: "No enquiries right now." Subline: "New enquiries will appear here."
- Error: "We couldn't load the enquiries." Button: "Try again"
- Every draft screen: "Drafts are never sent automatically. An officer reviews and sends each one."

## Prompts used in this build

Claude adds the three demo prompts here at the end of the run.
""")

# ---------- Day 2 · C6 Exterior vs Hood (Scenario B, ICA) ----------
D = "day2-validate/c6-exterior-vs-hood"
write(f"{D}/day2-validate/prototype/index.html", page("Passport renewal for a child · pre-submission check", "Scenario B · applicant view",
"""<div class="card"><h2 style="margin-top:0">Upload your child's photo and documents</h2>
<p>We check your documents before you submit, so fewer applications come back.</p>
<input type="file" id="doc"> <button class="btn" onclick="check()">Check my documents</button></div>
<div class="card" id="out">Your check result appears here.</div>
<script>
// Exterior only: no error handling, no access rules, no tests, no logging.
var applications = [{ref:"APP-0001", child:"Child A (made up)", status:"Draft"}];
function callModel(file){ return "Photo looks fine. Birth certificate looks fine."; }  // AI step: fixed string, no real call, no timeout, no fallback
function check(){
  var f = document.getElementById('doc').files[0];
  localStorage.setItem('lastUpload', f.name);                     // the document name sits in the browser
  document.getElementById('out').textContent = callModel(f);
}
</script>""", ".btn{background:#3046c8;color:#fff;border:0;border-radius:8px;padding:10px 16px;font-weight:600}"))
write(f"{D}/day2-validate/prototype/README.md", f"# day2-validate/prototype/ (made up)\n\n{MADE_UP}\n\nA polished screen with a thin hood, for the Exterior vs hood demo.\n")

# ---------- Day 3 · C7 Run Your Agent (Scenario A, ServiceSG) ----------
D = "day3-build/c7-run-your-agent"
write(f"{D}/day3-build/agent-spec.md", f"""# agent-spec.md · enquiry reply assistant (made up)

{MADE_UP}

## Job
Draft replies to resident enquiries for an officer to review.

## Inputs
One resident enquiry, as text.

## Output
A draft reply, or a hand-off to an officer, or a refusal.

## Policy pages the assistant may cite (made up)
- Bin collection schedule page
- Park repairs page
- Lift repairs page
- Road repairs page

There is no policy page for parking permit renewals in this list.
""")
write(f"{D}/day3-build/agent-control-panel.md", f"""# agent-control-panel.md (made up)

{MADE_UP}

| Control | Setting |
|---|---|
| Sending | Never send a reply. An officer sends it. |
| Escalate | Complaints, personal data or a vulnerable resident. |
| Refuse | Requests for another person's details. |
| Citing | Name the policy page each answer comes from. |
""")
write(f"{D}/day3-build/agent-run-log.md", f"# agent-run-log.md (made up)\n\n{MADE_UP}\n\nEmpty on purpose. The demo adds 3 made-up inputs and logs the run here.\n")

# ---------- Day 3 · C8 Connected to Secured (Scenario A, ServiceSG) ----------
D = "day3-build/c8-connected-to-secured"
REC = [("E-3001", "officer.a@example.test", "Bin not collected"), ("E-3002", "officer.a@example.test", "Broken bench in the park"),
       ("E-3003", "officer.b@example.test", "Lift out of service"), ("E-3004", "officer.b@example.test", "Pothole near the bus stop"),
       ("E-3005", "officer.a@example.test", "Overgrown grass verge"), ("E-3006", "officer.b@example.test", "Blocked drain after rain")]
write(f"{D}/sample-app/data/enquiries.csv", csv_text(["id", "owner_email", "subject", "status"], [r + ("open",) for r in REC]))
cards = "\n".join(f'<div class="card"><code>{i}</code> {s} <small style="color:#666">owner {o}</small></div>' for i, o, s in REC)
write(f"{D}/sample-app/index.html", page("Enquiries · sample app", "Scenario A · connected, nothing secured yet",
      f"<p>Every record is visible to everyone. No sign-in, no access rules, no schema yet. Test accounts only (example.test).</p>\n{cards}"))
write(f"{D}/sample-app/README.md", f"# sample-app (made up)\n\n{MADE_UP}\n\nConnected but nothing secured: no schema, no sign-in, no access rules, no security check.\nOwners are test accounts on example.test, a domain reserved for testing.\n")

# ---------- Day 4 · C12 Read Your Product Data (Scenario A, ServiceSG) ----------
D = "day4-measure/c12-read-product-data"
rng = random.Random(SEED)
TYPES = [("Parking", 20), ("Permits", 18), ("Roads", 16), ("Lighting", 14), ("Noise", 16), ("Waste", 16)]
REWRITE = {"Permits": 0.72}
REOPEN = {"Noise": 0.31}
pool = [t for t, w in TYPES for _ in range(w)]
rows = []
for n in range(600):
    t = rng.choice(pool)
    week = 1 + n // 150
    r = rng.random()
    pr = REWRITE.get(t, 0.14)
    action = "rewritten" if r < pr else ("light_edit" if r < pr + (1 - pr) * 0.35 else "sent_as_is")
    mins = {"sent_as_is": rng.randint(2, 6), "light_edit": rng.randint(5, 10), "rewritten": rng.randint(12, 22)}[action]
    reopened = "yes" if rng.random() < REOPEN.get(t, 0.11) else "no"
    rows.append((f"Q-{n + 1:04d}", f"2026-W{40 + week}", t, rng.choice(["web form", "app", "email"]), action, mins, reopened))
write(f"{D}/day4-measure/data/synthetic-usage.csv", csv_text(["enquiry_id", "week", "enquiry_type", "channel", "officer_action", "minutes_to_send", "reopened_30d"], rows))
write(f"{D}/day4-measure/metrics-plan.md", f"""# metrics-plan.md · Scenario A, ServiceSG (made up)

{MADE_UP}

## Goal
Fewer residents come back with the same enquiry.

## Baseline
1 in 4 enquiries (25%) reopened within 30 days.

## Target
15% or fewer reopened within 30 days by the end of the pilot.

## Guardrail
Officers rewrite fewer than 30% of drafts, for every enquiry type.

## Stop line
If more than 40% of drafts on one enquiry type are rewritten, pause drafts for that type.
""")
write(f"{D}/day4-measure/iteration.md", f"# iteration.md (made up)\n\n{MADE_UP}\n\n## Signals I confirmed\n\n(empty, filled in during the demo)\n")
print("seeded")
