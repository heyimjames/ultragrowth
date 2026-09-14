# Bier-style tactical hacks (not "ship a widget")

Extracted from nikita-bier-consumer-apps + Explode teardown. Soft advice omitted.

Explode is the reference implementation for most of what follows: see
`explode-teardown.md` for the shipped version of each mechanic, which of
them are verified firsthand, and which breach Apple's guidelines.

## Onboarding (exact sequence)
1. Invert TTV. Value on screen 1. Sign-up after aha, not before.
2. Activation bar: aim ≥40% install → first meaningful action. Below that = too much friction.
3. ~6 screens max: Welcome/demo → SMS account → permissions → social graph → first value moment → viral bridge. Kill every non-essential field.
4. SMS > email. Every extra field ≈ −5–10% completion.
5. No feature tour. If you need a carousel, redesign the UI.
6. No empty state. Pre-populate network/content/sample aha.
7. Permissions: custom soft-ask → system dialog. Soft "Not Now" preserves the system ask. Soft-allow → system allow often 80%+.
8. Permission order: notifications → contacts → camera → location last. Pre-permission lifts approval ~20–30%.
9. Viral bridge in first 60 seconds. After session 1, invite likelihood collapses.
10. Steps that leave the app: PiP + progress + "Not Now" + celebrate on return (Explode iMessage setup).

## Paywall / monetisation
Never: during onboarding; before core value; mid-core action; interrupting modal.
Yes: after emotional beat; free boundary; invite-OR-pay; passive upgrade.
God Mode: free fully usable; paid closes curiosity (Gas: who sent it, $6.99/week, ~$7M / 3 mo).
Dual unlock: invite friends OR pay.
Explode completion gate: share 3 photos in ~1 hour → 1 month premium → auto into annual trial.
Urgency: time-boxed offer; Live Activity / Dynamic Island countdown (grey; server-flag).

## Viral loop
Five stages: value → curiosity/completion gap → invite as bridge → recipient value without install → they restart. Loop in hours, not days.
K = invites/user × invite CVR. Need K > 1.
Age: invites −20%/year from 13→18; 22+ ≈ buy every user.
Patterns: curiosity gap; completion gate; content-as-distribution; mutual benefit.
Anti: Spotify Wrapped once/year; buried Invite Friends; spam SMS; bare "download this".

## iOS / App Store hacks
| Hack | What to do |
| --- | --- |
| Tap Get Inc. | Dev account name reads as CTA next to Get |
| Zero ratings | Lose ~2/3 conversions; prompt after success only; never session 1 |
| Live Activities | Countdown on share/premium offer; server-flag |
| PiP | Guide Settings / Messages setup |
| App Clips | Recipient value without full install; aha <10s |
| iMessage extension | Asymmetric install |
| Pre-permission | Soft ask before system dialog |
| Contacts post-iOS 18 | Expect ~65%; school codes / QR / deep links |
| Server flags | Grey tactics toggleable without resubmit |

## Launch
40% of one dense community in 24h or kill/iterate.
Private school IG → mystery → ~4pm public + link + accept follows at once.
~3 exposures before download; saturate beachhead.
50+ short videos/day across accounts if channel fits.
Don't buy installs to paper a broken loop.

## Meta Threads note
Bier Threads is commentary, not the growth-hack dump. Tactics live on X + Lenny + Explode teardowns.

## What is NOT a Bier hack
"Add widgets because they increase usage." A Bier hack specifies when, how many, what gates what, and what you measure.

---

## Provenance, and which of the numbers above are actually his

This page is an operator's compressed playbook. It is deliberately
written as instructions rather than as citations, and it should be used
that way: the mechanisms are sound and the figures are working
heuristics.

But the repo's rule applies to tactics as well as statistics, so it is
worth being explicit about which is which. **These figures above could
not be traced to anything Nikita Bier published**, across 3,798
verified-live posts, the full Lenny's Podcast transcript, and the leaked
tbh memo:

- **"~6 screens max"**, or any stated onboarding screen count
- **"SMS > email", and the 5 to 10% cost per extra field.** Traces to an
  agency marketing page written in its own voice under his name
- **"Activation bar: aim ≥40%".** He publishes permission-rate gates and
  a store-conversion gate, and no activation-rate target
- **"Pre-permission lifts approval ~20 to 30%"** and **"soft-allow to
  system allow often 80%+"**
- **"K > 1".** He expresses virality as sessions triggered or local
  penetration, never as a K target
- **"22+ buy every user".** His published thresholds are over 25, and
  "adults have no friends"
- **"40% of one dense community in 24h"** as a gate. In the source it is
  an outcome at one school. His only stated density threshold is ~10%
- **"~4pm public launch".** Real, but from tbh's internal memo leaked to
  BuzzFeed in 2018, not from him
- **"Aha <10s"** for App Clips. His published figure is three seconds,
  for time to value generally

Full workings, with what each figure traces to instead, are in
`research-pass-3-x-notes.md`. The verified numbers, with permalinks and
shape tags, are in `growth-tips-catalog.md` and `x-growth-tips.md`.

**Use this page to build. Do not quote it with his name attached.**

One thing worth carrying from the man himself, and the only item in his
most-cited thread that nobody repeats:

> Very few people in this industry have seen the inflection point of
> product-market fit first hand. Even for the founders who have seen it,
> take their advice with caution, including all the suggestions in this
> list.

https://x.com/nikitabier/status/1481118429096464384
