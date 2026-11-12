#!/usr/bin/env python3
"""Verify the made-up demo data: each expected signal is really in the data, every file is labelled
made up, no dashes, no real contact details, seeding is reproducible. Maintainer step, not part of the live run."""
import csv, glob, hashlib, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
P = []; OK = []
def check(name, cond, detail=""):
    (OK if cond else P).append(f"{name}{': ' + detail if detail else ''}")
def rd(p): return open(p, encoding="utf-8").read()
def rows(p): return list(csv.DictReader(l for l in open(p, encoding="utf-8") if not l.startswith("#")))
FILES = sorted(f for f in glob.glob("**/*", recursive=True) if os.path.isfile(f) and not f.startswith(".git") and "__pycache__" not in f)
TEXT = [f for f in FILES if f.endswith((".md", ".csv", ".html", ".py", ".txt"))]
DEMOS = sorted(os.path.dirname(p) for p in glob.glob("day*/*/prompt.md"))

# 1 reproducible seeding
h = lambda: {f: hashlib.sha256(open(f, "rb").read()).hexdigest() for f in FILES}
before = h(); subprocess.run([sys.executable, "tools/seed.py"], check=True, capture_output=True); after = h()
check("seed.py is deterministic (rerun gives identical bytes)", before == after, str([f for f in before if before[f] != after.get(f)][:5]))
# 2 labels and rules on every file
for f in TEXT:
    s = rd(f)
    check(f"labelled made up: {f}", re.search(r"made up|made-up", s, re.I) is not None)
    check(f"no em or en dash: {f}", "\u2013" not in s and "\u2014" not in s)
    check(f"no LMS: {f}", re.search(r"\bLMS\b", s) is None or f == "tools/verify.py")
    em = [e for e in re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", s) if not e.endswith("@example.test")]
    check(f"emails only on example.test: {f}", not em, str(em[:3]))
    check(f"no phone numbers: {f}", re.search(r"(\+65[\s-]?)?\b[689]\d{3}[\s-]?\d{4}\b", s) is None)
# 3 run sheet: no Terminal steps, every README prompt is in a prompt.md
R = rd("README.md")
check("README has no Terminal steps", all("Terminal" not in l or l.startswith("No Terminal steps") for l in R.splitlines()))
allp = "\n".join(rd(f"{d}/prompt.md") for d in DEMOS)
for blk in re.findall(r"```\n(.*?)\n```", R, re.S) + re.findall(r"Then: `([^`]+)`", R):
    check(f"README prompt is in a prompt.md: {blk[:50]}", blk in allp)
for d in DEMOS:
    check(f"{d} has expected.md with a fallback", os.path.exists(f"{d}/expected.md") and "## Fallback" in rd(f"{d}/expected.md"))
    check(f"{d} listed in README and INVENTORY", d + "/" in R and d + "/" in rd("demos/INVENTORY.md"))

# 4 signals
D = "day2-validate/c4-triple-threat-build"; g = rd(f"{D}/GROUP.md")
check("C4 GROUP.md: 1 in 4 reopen, three theories, no data", "1 in 4" in g and g.count('- ') >= 3 and "None yet" in g)

D = "day2-validate/c5-context-injection"
e = rows(f"{D}/day2-validate/data/sample-enquiries.csv"); urgent = [r["id"] for r in e if r["urgency"] == "urgent"]
pr = rows(f"{D}/day2-validate/data/partner-check-results.csv"); miss = sum(r["picked_as_urgent"] != urgent[0] for r in pr)
brief = rd(f"{D}/day2-validate/validation-brief.md")
check("C5 CI: 5 enquiries, exactly one urgent (E-2041)", len(e) == 5 and urgent == ["E-2041"])
check("C5 CI: kill switch fires (more than 1 of 5 partners miss)", len(pr) == 5 and miss > 1 and "more than 1 of 5" in brief, f"miss={miss}")
check("C5 CI: expected.md says 2 of 5 missed", f"{miss} of 5 missed" in rd(f"{D}/expected.md"))
check("C5 CI: seeded inbox is placeholder only", rd(f"{D}/day2-validate/prototype/index.html").count("goes here") >= 6)

D = "day2-validate/c5-precision-prompt-chain"
scr = sorted(glob.glob(f"{D}/day2-validate/prototype/*.html")); body = "".join(rd(f) for f in scr)
check("C5 PC: first build has 3 screens", len(scr) == 3, str(scr))
check("C5 PC: no loading, empty or error state yet", not re.search(r"Loading|No enquiries|Try again", body))
ix = rd(f"{D}/day2-validate/prototype/index.html")
check("C5 PC: 3 seeded visual gaps on the list screen", "font-size:14px" in ix and "opacity:.45" in ix and "padding:2px" in ix)
pm = rd(f"{D}/day2-validate/PROMPTS.md")
check("C5 PC: PROMPTS.md carries the state text", all(t in pm for t in ("No enquiries right now.", "New enquiries will appear here.", "Try again", "Drafts are never sent automatically.")))

D = "day2-validate/c6-exterior-vs-hood"; c6 = rd(f"{D}/day2-validate/prototype/index.html")
check("C6: no error handling", not re.search(r"\btry\b|catch|onerror|\.catch\(", c6))
check("C6: no sign-in or access rules", not re.search(r"(?i)sign.?in|login|password|role", c6))
check("C6: no tests", not glob.glob(f"{D}/**/*test*", recursive=True))
check("C6: document kept in the browser, AI step is a fixed string", "localStorage.setItem" in c6 and re.search(r"function callModel\([^)]*\)\{ return \"", c6) is not None)

D = "day3-build/c7-run-your-agent"; spec = rd(f"{D}/day3-build/agent-spec.md")
pol = spec.split("## Policy pages")[1].split("There is no")[0]
check("C7: no policy page for parking permits (rule 4 break is seeded)", not re.search(r"(?i)parking|permit", pol))
check("C7: control panel has the 4 rules", all(k in rd(f"{D}/day3-build/agent-control-panel.md") for k in ("Never send", "Escalate", "Refuse", "policy page")))

D = "day3-build/c8-connected-to-secured"; r8 = rows(f"{D}/sample-app/data/enquiries.csv")
own = {}
for r in r8: own.setdefault(r["owner_email"], []).append(r["id"])
check("C8: 6 made-up rows, 2 test owners with 3 each", len(r8) == 6 and sorted(len(v) for v in own.values()) == [3, 3], str(own))
ex8 = rd(f"{D}/expected.md")
check("C8: expected.md officer split matches the data", all(", ".join(v[:2]) in ex8 for v in own.values()))
check("C8: sample app has no sign-in or access rules yet", not re.search(r"(?i)<form|password|policy", rd(f"{D}/sample-app/index.html")))

D = "day4-measure/c12-read-product-data"; u = rows(f"{D}/day4-measure/data/synthetic-usage.csv"); ex = rd(f"{D}/expected.md")
by = {}
for r in u: by.setdefault(r["enquiry_type"], []).append(r)
rw = {t: sum(r["officer_action"] == "rewritten" for r in v) for t, v in by.items()}
ro = {t: sum(r["reopened_30d"] == "yes" for r in v) / len(v) for t, v in by.items()}
top = max(rw, key=lambda t: rw[t] / len(by[t]))
others = [rw[t] / len(by[t]) for t in by if t != top]
check("C12: one enquiry type has most drafts rewritten (Permits)", top == "Permits" and rw[top] / len(by[top]) > 0.5 and max(others) < 0.3)
check("C12: expected.md numbers match (rewrites)", f"{rw[top]} of {len(by[top])}" in ex and f"{round(min(others)*100)}% to {round(max(others)*100)}%" in ex)
plan = rd(f"{D}/day4-measure/metrics-plan.md")
check("C12: Permits crosses the stop line in metrics-plan.md", "more than 40%" in plan and rw[top] / len(by[top]) > 0.4)
rest = [v for t, v in ro.items() if t != "Noise"]
check("C12 fallback: Noise reopen rate stands out", ro["Noise"] > 0.25 and max(rest) < 0.16 and f"{round(ro['Noise']*100)}%" in ex and f"{round(min(rest)*100)}% to {round(max(rest)*100)}%" in ex)
ov = sum(r["reopened_30d"] == "yes" for r in u) / len(u)
check("C12 fallback: overall reopen under the 15% target", ov < 0.15 and f"{ov*100:.1f}%" in ex, f"{ov:.3f}")

print(f"checks passed {len(OK)}, problems {len(P)}")
for p in P: print("PROBLEM", p)
sys.exit(1 if P else 0)
