# Expected · C5 Context Injection (made up data)

## Lands on
Before: the Module 4 officer dashboard looks finished. The numbers are hard-coded (128 open, 24% reopened). build-log.md only has the Module 4 entry. It tests nothing.
After: Claude plans first, then adds the riskiest assumption to day2-validate/build-log.md: officers who see their own reopened enquiries will change how they reply. Risk type: market. Kill switch: if fewer than 3 of 5 partners name a reply they would change, stop and test the templates theory. Success signal: 4 of 5 partners name one reply to change after 30 seconds on the dashboard.
It writes day2-validate/data/sample-officer-metrics.csv, labelled as made up: 6 rows, officer OFF-07, 72 closed and 21 reopened in 30 days (29% reopen rate, team 24%), top reason "missed next step" (16 of 21), with Payments at 9 reopens as the marked signal.
The same dashboard is wired to that data. Both the build log and the prototype are merged on main.

Line to say: same dashboard, same look. Now it tests an assumption.

## Fallback
If the rebuild is slow, open day2-validate/build-log.md and the CSV from the Files list and walk the room through the assumption, the kill switch and the Payments signal. Or play the C5 Context Injection video.
