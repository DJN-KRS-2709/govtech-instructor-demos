#!/usr/bin/env python3
"""Seed every demo folder with its made-up data. Deterministic: same seed, same bytes.
Run from the repo root with: python3 tools/seed.py  (maintainer step, not part of the live run sheet)."""
import csv, io, os, random, shutil

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


def remove_stale():
    stale = [
        "day2-validate/c5-context-injection/day2-validate/validation-brief.md",
        "day2-validate/c5-context-injection/day2-validate/data",
        "day2-validate/c5-context-injection/day2-validate/prototype/draft.html",
        "day2-validate/c5-context-injection/day2-validate/prototype/result.html",
        "day2-validate/c5-precision-prompt-chain/day2-validate/data/sample-enquiries.csv",
        "day2-validate/c5-precision-prompt-chain/day2-validate/prototype/partner-check.html",
        "day2-validate/c5-precision-prompt-chain/day2-validate/prototype/dashboard.html",
        "day2-validate/c6-exterior-vs-hood",
    ]
    for rel in stale:
        p = os.path.join(ROOT, rel)
        if os.path.isdir(p):
            shutil.rmtree(p)
        elif os.path.isfile(p):
            os.remove(p)

# Shared Scenario A officer-dashboard assets (made up). Used by C5 and C6.
METRICS_HEADER = ["officer", "category", "closed_30d", "reopened", "top_reason"]
METRICS_ROWS = [
    ("OFF-07", "Parking", 22, 7, "missed next step"),
    ("OFF-07", "Permits", 14, 2, "wrong form linked"),
    ("OFF-07", "Drains", 9, 1, "duplicate report"),
    ("OFF-07", "Noise", 11, 2, "outcome disputed"),
    ("OFF-07", "Payments", 16, 9, "missed next step"),
    ("TEAM", "all", 412, 99, "missed next step"),
]
ONE_PAGER = f"""# One Pager (made up for this demo)

{MADE_UP}

## Scenario
Scenario A, ServiceSG enquiry response. Made-up sample only.

## Problem
Residents reopen 1 in 4 enquiries within 30 days.

## Who it is for
Officers on the enquiry desk, so they can see their own reopened enquiries by category.

## Proposal
An officer dashboard of made-up sample metrics.

## Risks (market, technical, team)
To be filled in after Show and Swap.
"""
BUILD_LOG_M4 = f"""# Build log (made up for this demo)

{MADE_UP}

## Module 4
Built the officer dashboard. Toy or tool: toy.
"""
BUILD_LOG_M5 = BUILD_LOG_M4 + """
## Module 5: riskiest assumption
Officers who see their own reopened enquiries will change how they reply.
Risk type: market. Will officers act on their numbers?
Kill switch: if fewer than 3 of 5 partners name a reply they would change, stop. Test the templates theory.
Success signal: 4 of 5 partners name one reply to change after 30 seconds on the dashboard.
"""
BUILD_LOG_END_M5 = BUILD_LOG_M5 + """
## Module 5: prompt chain
Toy or tool: tool. The partner check runs against the kill switch.
"""
DASH_CSS = """*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,Helvetica,Arial,sans-serif;background:#f4f5f7;color:#16181d;min-height:100vh}
a{color:#3046c8;text-decoration:none;font-weight:600}
.wrap{max-width:1120px;margin:0 auto;padding:22px 24px 40px}
.dh{display:flex;align-items:center;gap:14px;margin-bottom:18px}
.logo{width:38px;height:38px;border-radius:9px;background:#5b5bf6;flex:none}
.tt{font-size:24px;font-weight:700;letter-spacing:-.02em}
.st{font-size:14px;color:#6b6f78;margin-top:2px}
.sb{margin-left:auto;font:600 11px ui-monospace,SFMono-Regular,monospace;color:#9a6a00;background:#fdf2d0;padding:5px 10px;border-radius:5px;letter-spacing:.06em;text-transform:uppercase}
nav{display:flex;gap:16px;margin:0 0 16px;font-size:14px}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:12px}
.card{background:#fff;border-radius:10px;padding:14px 16px;border:1px solid #e3e4e8}
.k{font-size:12px;font-weight:700;letter-spacing:.08em;color:#5d616b;text-transform:uppercase}
.v{font-size:34px;font-weight:700;letter-spacing:-.02em;line-height:1.25;margin-top:2px}
.v.sm{font-size:22px;line-height:1.45}
.s{font-size:13px;color:#6b6f78;margin-top:2px}
.red{color:#d03a3a}.org{color:#d9772b}
.lower{display:grid;grid-template-columns:1.55fr 1fr;gap:12px}
.panel{background:#fff;border-radius:10px;border:1px solid #e3e4e8;padding:14px 16px 16px;min-height:280px;display:flex;flex-direction:column}
.bars{display:flex;align-items:flex-end;gap:22px;height:200px;padding:28px 6px 0}
.bar{flex:1;background:linear-gradient(180deg,#6d5cf6,#4f46e5);border-radius:4px 4px 0 0;position:relative;min-height:8px}
.bar .bv{position:absolute;top:-24px;left:0;right:0;text-align:center;font-weight:700;font-size:16px;color:#333}
.bar.sig{background:linear-gradient(180deg,#f6a35c,#e2742c);box-shadow:0 0 0 3px rgba(240,150,90,.35)}
.sigtag{position:absolute;top:-52px;left:50%;transform:translateX(-50%);font:700 11px ui-monospace,SFMono-Regular,monospace;background:#e2742c;color:#fff;padding:3px 8px;border-radius:4px;letter-spacing:.06em;white-space:nowrap}
.blabels{display:flex;gap:22px;margin-top:8px;padding:0 6px}
.blabels span{flex:1;text-align:center;font-size:13px;color:#555}
.li{display:flex;align-items:center;gap:12px;font-size:15px;min-height:40px;border-bottom:1px solid #eee}
.li:last-child{border-bottom:0}
.li b{font:600 13px ui-monospace,SFMono-Regular,monospace;width:70px}
.pt{margin-left:auto;font:700 11px ui-monospace,SFMono-Regular,monospace;padding:3px 8px;border-radius:4px;letter-spacing:.04em;white-space:nowrap}
.pt.r{background:#fde2e2;color:#c03030}.pt.o{background:#fde9d6;color:#b85e17}.pt.g{background:#dcfce7;color:#15803d}
.lab{font-size:11px;font-weight:700;letter-spacing:.1em;color:#7a7e88;text-transform:uppercase;margin-top:10px}
.tx{font-size:15px;line-height:1.4;color:#1d2027;margin-top:3px}
.sigline{background:#fff4ea;border:1.5px solid #f2b583;border-radius:8px;padding:7px 10px}
.btn{background:#3046c8;color:#fff;border:0;border-radius:8px;padding:10px 14px;font-weight:600;font-size:14px;cursor:pointer}
#ai-out{margin-top:10px;min-height:24px;font-size:15px;color:#1d2027}
.kill-line{font-size:20px;font-weight:700;color:#15803d}
.count{font-size:44px;font-weight:700;letter-spacing:-.02em;line-height:1.1;margin:6px 0}
@media(max-width:860px){.cards,.lower{grid-template-columns:1fr 1fr}.wrap{padding:16px}}
"""

def dash_html(title, body, css_inline=True, extra_script=""):
    css = f"<style>\n{DASH_CSS}</style>" if css_inline else '<link rel="stylesheet" href="styles.css">'
    return f"""<!doctype html>
<!-- {MADE_UP} -->
<html lang="en"><head><meta charset="utf-8"><title>{title} (made up)</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
{css}
</head><body>
{body}
{extra_script}
</body></html>
"""

def data_js():
    rows = ",\n  ".join(
        '{{officer:"{o}", category:"{c}", closed_30d:{cl}, reopened:{r}, top_reason:"{t}"}}'.format(
            o=o, c=c, cl=cl, r=r, t=t
        )
        for o, c, cl, r, t in METRICS_ROWS
    )
    return f"""// {MADE_UP}
// Copied from data/sample-officer-metrics.csv. No fetch, no validation, no error handling.
var METRICS = [
  {rows}
];
"""

def sample_data_js():
    return f"""// {MADE_UP}
// Hard-coded sample numbers. No assumption, no CSV, no test.
var SAMPLE = {{
  open: 128,
  reopenRate: 24,
  firstReplyDays: 2.1,
  mine: 17
}};
"""

def m4_dashboard():
    bars = [
        ("Parking", 83, False),
        ("Permits", 50, False),
        ("Drains", 66, False),
        ("Noise", 42, False),
        ("Payments", 73, False),
    ]
    bar_html = "".join(f'<div class="bar" style="height:{h}%"></div>' for n, h, _ in bars)
    labels = "".join(f"<span>{n}</span>" for n, h, _ in bars)
    week = [
        ("E-1031", "Parking", "REOPENED TWICE", "r"),
        ("E-1027", "Payments", "REOPENED", "o"),
        ("E-1019", "Drains", "REOPENED", "o"),
        ("E-1012", "Permits", "CLOSED", "g"),
    ]
    lis = "".join(f'<div class="li"><b>{i}</b>{c}<span class="pt {k}">{t}</span></div>' for i, c, t, k in week)
    body = f"""<div class="wrap">
<div class="dh"><div class="logo"></div><div><div class="tt">Officer dashboard</div><div class="st">Enquiry desk &middot; this month</div></div><span class="sb">Sample data, made up</span></div>
<div class="cards">
<div class="card"><div class="k">Open enquiries</div><div class="v">128</div><div class="s">across 5 categories</div></div>
<div class="card"><div class="k">Reopened in 30 days</div><div class="v red">24%</div><div class="s">1 in 4</div></div>
<div class="card"><div class="k">First reply</div><div class="v">2.1 days</div><div class="s">median</div></div>
<div class="card"><div class="k">My enquiries</div><div class="v">17</div><div class="s">assigned to me</div></div>
</div>
<div class="lower">
<div class="panel"><div class="k">Reopened by category</div><div class="bars">{bar_html}</div><div class="blabels">{labels}</div></div>
<div class="panel"><div class="k">Reopened this week</div>{lis}</div>
</div>
</div>
<script src="sample-data.js"></script>
<!-- Hard-coded sample numbers. No assumption, no CSV, no test. -->
"""
    return dash_html("Officer dashboard", body)

def m5_dashboard(link_partner=False, include_ai=False, css_inline=True):
    # Heights relative to Payments = 9 reopens (tallest).
    bars = [
        ("Parking", 7, False),
        ("Permits", 2, False),
        ("Drains", 1, False),
        ("Noise", 2, False),
        ("Payments", 9, True),
    ]
    bar_html = []
    for n, v, sig in bars:
        h = int(round(v / 9 * 88))
        cls = "bar sig" if sig else "bar"
        tag = '<span class="sigtag">SIGNAL</span>' if sig else ""
        bar_html.append(f'<div class="{cls}" style="height:{h}%"><span class="bv">{v}</span>{tag}</div>')
    labels = "".join(f"<span>{n}</span>" for n, v, sig in bars)
    nav = ""
    if link_partner:
        nav = '<nav><a href="index.html">Dashboard</a><a href="partner-check.html">Partner check</a></nav>\n'
    ai = ""
    script = ""
    if include_ai:
        ai = """
<div class="lab">Suggest a reply change</div>
<div class="tx">A stubbed AI step on the Payments signal. Looks finished. The hood is thin.</div>
<p style="margin-top:10px"><button class="btn" type="button" onclick="suggest()">Suggest a reply change</button></p>
<div id="ai-out">Your suggestion appears here.</div>
"""
        script = """<script>
// Thin hood: no error handling, no access rules, no tests, no logging.
function callModel(reason){ return "Most reopens missed the next step. Add the next step to the reply."; }  // AI step: fixed string, no real call, no timeout, no fallback
function suggest(){
  var last = "OFF-07:Missed next step";
  localStorage.setItem("lastSuggestion", last);                     // the officer id and reason sit in the browser
  document.getElementById("ai-out").textContent = callModel(last);
}
</script>
"""
    body = f"""<div class="wrap">
<div class="dh"><div class="logo"></div><div><div class="tt">Officer dashboard</div><div class="st">OFF-07 &middot; last 30 days &middot; data/sample-officer-metrics.csv</div></div><span class="sb">Synthetic data, made up</span></div>
{nav}<div class="cards">
<div class="card"><div class="k">My closed</div><div class="v">72</div><div class="s">last 30 days</div></div>
<div class="card"><div class="k">My reopen rate</div><div class="v red">29%</div><div class="s">team 24%</div></div>
<div class="card"><div class="k">Top reopen reason</div><div class="v sm org">Missed next step</div><div class="s">16 of 21 reopens</div></div>
<div class="card"><div class="k">Success signal</div><div class="v">4 of 5</div><div class="s">target: partners name a change</div></div>
</div>
<div class="lower">
<div class="panel"><div class="k">My reopened by category</div><div class="bars">{''.join(bar_html)}</div><div class="blabels">{labels}</div></div>
<div class="panel"><div class="k">Testing &middot; from build-log.md</div>
<div class="lab">Riskiest assumption</div><div class="tx">Officers who see their own reopens will change how they reply.</div>
<div class="lab">Signal</div><div class="tx sigline">16 of 21 of my reopens missed the next step. Most are in Payments.</div>
<div class="lab">Kill switch</div><div class="tx">Fewer than 3 of 5 partners name a change: stop and test the templates theory.</div>
{ai}</div>
</div>
</div>
<script src="data.js"></script>
<!-- Numbers copied from data/sample-officer-metrics.csv. No validation, no error handling. -->
{script}
"""
    return dash_html("Officer dashboard", body, css_inline=css_inline)

def partner_check_html():
    answers = [
        ("Partner 1", "Payments replies: add the next step", True),
        ("Partner 2", "Not sure", False),
        ("Partner 3", "Parking: link the appeal form", True),
        ("Partner 4", "Payments: say when the refund lands", True),
        ("Partner 5", "Nothing, it looks fine", False),
    ]
    lis = "".join(
        f'<div class="li"><b style="width:100px">{p}</b><span>{a}</span><span class="pt {"g" if n else "r"}">{"NAMED A CHANGE" if n else "NO CHANGE"}</span></div>'
        for p, a, n in answers
    )
    body = f"""<div class="wrap">
<div class="dh"><div class="logo" style="background:#e2742c"></div><div><div class="tt">Partner check</div><div class="st">Asked after 30 seconds on the dashboard</div></div><span class="sb">Synthetic data, made up</span></div>
<nav><a href="index.html">Dashboard</a><a href="partner-check.html">Partner check</a></nav>
<div class="lower">
<div class="panel"><div class="k">Which reply would you change?</div><div style="margin-top:8px">{lis}</div></div>
<div class="panel"><div class="k">Against build-log.md</div>
<div class="lab">Named a change</div><div class="count">3 of 5</div>
<div class="lab">Success signal: 4 of 5</div><div class="tx org" style="font-weight:700">Not yet</div>
<div class="lab">Kill switch</div><div class="tx kill-line">Fewer than 3 of 5: holds</div>
</div>
</div>
</div>
"""
    return dash_html("Partner check", body, css_inline=False)

remove_stale()

# ---------- Day 2 · C5 Context Injection (Scenario A, ServiceSG) ----------
# Starting state: the Module 4 dashboard. Looks finished. Tests nothing.
D = "day2-validate/c5-context-injection"
write(f"{D}/one-pager.md", ONE_PAGER)
write(f"{D}/day2-validate/build-log.md", BUILD_LOG_M4)
write(f"{D}/day2-validate/prototype/sample-data.js", sample_data_js())
write(f"{D}/day2-validate/prototype/index.html", m4_dashboard())

# ---------- Day 2 · C5 Your Prompt Chain (Scenario A, ServiceSG) ----------
# Starting state: the end of Context Injection. Dashboard wired to the CSV. No partner check yet.
D = "day2-validate/c5-precision-prompt-chain"
write(f"{D}/one-pager.md", ONE_PAGER)
write(f"{D}/day2-validate/build-log.md", BUILD_LOG_M5)
write(f"{D}/day2-validate/data/sample-officer-metrics.csv", csv_text(METRICS_HEADER, METRICS_ROWS))
write(f"{D}/day2-validate/prototype/data.js", data_js())
write(f"{D}/day2-validate/prototype/index.html", m5_dashboard(link_partner=False, include_ai=False, css_inline=True))
write(f"{D}/day2-validate/PROMPTS.md", f"""# PROMPTS.md (made up for this demo)

{MADE_UP}

## Prompts used in this build

Claude adds the three demo prompts here at the end of the run.
""")

# ---------- Day 2 · C6 Demo vs code (Scenario A, ServiceSG, end of Module 5) ----------
D = "day2-validate/c6-demo-vs-code"
write(f"{D}/one-pager.md", ONE_PAGER)
write(f"{D}/day2-validate/build-log.md", BUILD_LOG_END_M5)
write(f"{D}/day2-validate/data/sample-officer-metrics.csv", csv_text(METRICS_HEADER, METRICS_ROWS))
write(f"{D}/day2-validate/prototype/data.js", data_js())
write(f"{D}/day2-validate/prototype/styles.css", f"/* {MADE_UP} */\n{DASH_CSS}")
write(f"{D}/day2-validate/prototype/index.html", m5_dashboard(link_partner=True, include_ai=True, css_inline=False))
write(f"{D}/day2-validate/prototype/partner-check.html", partner_check_html())
write(f"{D}/day2-validate/PROMPTS.md", f"""# PROMPTS.md: run in this order

{MADE_UP}

## 1 Expand
Add a partner check view after the dashboard.
Check: dashboard unchanged.

## 2 Behavior
After 30 seconds ask "Which reply would you change?"
Count named changes. Fewer than 3 of 5 fires the kill switch.
Check: 5 made-up answers, count is right.

## 3 Refine
Audit for the 2 biggest gaps. Fix only the top one.
Check: only .kill-line changed.
""")
write(f"{D}/day2-validate/prototype/README.md", f"""# day2-validate/prototype/ (made up)

{MADE_UP}

Scenario A officer dashboard at the end of Module 5. A polished screen with a thin hood, for the Demo vs code live run.
""")

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
