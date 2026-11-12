# Expected · C8 Connected to Secured (made up data)

## Lands on
Start: sample-app/ shows all 6 made-up enquiries to everyone (owners officer.a and officer.b on example.test, a test domain).
Step 1: a schema for enquiries plus 6 synthetic rows.
Step 2: a sign-in page and 2 test accounts.
Step 3: a row level rule, so Officer A sees E-3001, E-3002, E-3005 and Officer B sees E-3003, E-3004, E-3006.
Step 4: a security check that confirms access rules are on, Officer A cannot read Officer B's rows, no keys or passwords in the code, 0 real records, and warns that sign-in uses test accounts only. Then a local test deploy.

Line to say: a demo of the pattern on made-up data, not a production setup. A real service goes through GovTech's own security and deployment processes.

## Fallback
If the local deploy stalls, stop after step 3 and show the two officer views. Or play the C8 HyperFrames video.
