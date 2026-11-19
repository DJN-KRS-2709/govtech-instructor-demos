# Living PRD · officer dashboard (made up)

Made up for a live demo. Synthetic data, no real people, no real records. A learner-style file so the M12 Final Presentation Builder can load this repo.

- Solid: officers found their own reopened enquiries by category in under 30 seconds.
- Fragile: every number is a fixed sample in the page; there is no data source, sign in or error handling.
- Surprise: 3 of 5 partners named one reply they would change, so the kill switch held but the success signal (4 of 5) was not reached.

## Product overview

An officer dashboard of made-up sample metrics. Each officer sees their own reopened enquiries by category, and their top reason for a reopen.

## Problem and riskiest assumption

Residents reopen 1 in 4 enquiries within 30 days. Riskiest assumption: officers who see their own reopened enquiries will change how they reply.

## User flow and screen map

One screen: pick an officer (OFF-07 in the sample), see reopened enquiries by category, then the top reason (missed next step, 16 of 21).

## Success metrics

Reopen rate for OFF-07 is 29% against a team rate of 24%. Success signal: 4 of 5 partners name a reply to change after 30 seconds on the dashboard.

## Technical reality

A single HTML page with a made-up CSV. No error handling, no sign in, no access rules, no tests. The AI step is a fixed string.

## Assumptions and risks

Market risk: will officers act on their own numbers? Kill switch: fewer than 3 of 5 partners name a reply they would change.

## In and out of scope

In: one officer view of reopened enquiries. Out: live data, sending replies, any resident data.

## Engineering recommendation

Keep prototyping. Add a real data source, access rules and error handling before any pilot.
