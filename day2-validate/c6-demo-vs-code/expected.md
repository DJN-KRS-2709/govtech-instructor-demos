# Expected · C6 Demo vs code (made up data, Scenario A, ServiceSG)

## Lands on
A long list against a screen that looks finished. The seeded gaps it should find:
- Data handling: the metrics are copied into data.js and the page from a made-up CSV, with no validation; the last AI suggestion is kept in the browser (localStorage); no rule on what is stored or for how long.
- Error paths: no handling if the data file is missing, a row is bad, or the AI step fails.
- Access rules: no sign-in; anyone can see officer OFF-07's numbers.
- Tests: none.
- AI step: callModel() returns a fixed string. No real call, no timeout, no fallback, no logging.

Line to say: a polished demo with thin code is the most common prototype risk. Who can see an officer's numbers?

## Fallback
If the list is short, ask: "What happens if the data file is missing, and who can see these numbers?" Both gaps are in the code. Or point at the Suggest a reply change button and ask how the AI step is called.
