# Prompts · C5 Demo · Your Prompt Chain (made up data)

Source: the three prompts typed on screen in the C5 Prompt Chain video (`c5-precision-prompt-chain.mp4`). The slide names the chain but shows no prompts.
The starting state is the end of the Context Injection demo: the Module 4 dashboard is already wired to day2-validate/data/sample-officer-metrics.csv, and the assumption is in day2-validate/build-log.md. There is no partner check yet.

## Prompt 1, Expand

```
Prompt 1, Expand: add a partner check view after the dashboard, in that order. Keep the dashboard as the anchor.
```

## Prompt 2, Behavior

```
Prompt 2, Behavior: after 30 seconds, ask "Which reply would you change?" Count partners who name one. Fewer than 3 of 5 fires the kill switch.
```

## Prompt 3, Refine

```
Prompt 3, Refine: audit the partner check for its 2 biggest gaps. Fix only the top one.
```

## Then paste this to save

```
Save the chain and its checks to PROMPTS.md, log toy or tool in build-log.md, and save both on main.
```
