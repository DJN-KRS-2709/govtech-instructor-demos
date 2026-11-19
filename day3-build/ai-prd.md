# AI PRD · enquiry reply assistant (made up)

Made up for a live demo. Synthetic data, no real people, no real records. A learner-style file so the M12 Final Presentation Builder can load this repo.

## Problem and user

Officers on the enquiry desk spend their time finding the right policy page for each resident enquiry, and residents reopen 1 in 4 enquiries within 30 days. The assistant drafts a cited first reply so the officer reviews instead of searching.

## Instructions

day3-build/CLAUDE.md, built from agent-spec.md and agent-control-panel.md: never send, escalate, refuse, name the policy page.

## Tools

Read the policy pages listed in agent-spec.md. Write a draft reply. No sending.

## Context and memory

One resident enquiry at a time. No memory between enquiries.

## Permissions

| Tool | Tier | Setting |
|---|---|---|
| Read policy pages | read | auto |
| Draft a reply | draft | auto |
| Hand off to an officer | write | confirm, signed off by the enquiry desk lead |
| Send a reply | send | block |

## Human checkpoints

An officer reads every draft before anything goes to a resident.

## Stop conditions

Stop and hand off when the enquiry is a complaint, has personal data, or comes from a vulnerable resident, or when no policy page fits.

## Logs

day3-build/agent-run-log.md: each input, what the assistant did, and any rule it broke.

## Business rules

- If no policy page fits, then hand the enquiry to an officer.
- If the enquiry asks for another person's details, then refuse and point to the official process.

## What engineering decides

Hosting, the model version and how policy pages are kept up to date.

## Open decisions

Who signs off a new policy page before the assistant may cite it.
