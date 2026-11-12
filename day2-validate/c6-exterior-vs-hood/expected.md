# Expected · C6 Exterior vs Hood (made up data, Scenario B, ICA)

## Lands on
A long list against a screen that looks finished. The seeded gaps it should find:
- Data handling: the uploaded document name is kept in the browser (localStorage); no rule on what is stored or for how long.
- Error paths: no handling for a missing file, a wrong file type or a failed check.
- Access rules: no sign-in; anyone can see the made-up application record.
- Tests: none.
- AI step: callModel() returns a fixed string. No real call, no timeout, no fallback, no logging.

Line to say: a polished exterior with a thin hood is the most common prototype risk. Who can see an applicant's documents?

## Fallback
If the list is short, ask: "What happens if the upload fails, and who can see this file?" Both gaps are in the code.
