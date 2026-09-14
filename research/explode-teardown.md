# Explode: a one-page teardown

Explode is the most densely hacked onboarding funnel anybody has shipped
on iOS recently, and it is the reference implementation for most of
`bier-tactical-hacks.md`. It is also a **commercial failure**, which is
why it is a teardown and not a case study.

Three provenance corrections first, because the circulating version of
this story gets all three wrong:

- **Nikita Bier built it.** Julian Ivaldy is a growth marketer who wrote
  one of the two teardowns, not the founder.
- **It launched 14 January 2025**, announced by Bier on X.
  https://x.com/nikitabier/status/1879206793118658974
- **It is no longer on the App Store.** Apple's own search API returns no
  app named Explode from the seller Tap Get Inc. in the US storefront.
  No source found says when it was delisted or why, so do not write that
  Apple pulled it. What *is* documented is that Bier made all of it free
  on 4 February 2025, three weeks after launch.

## What actually happened

| | |
| --- | --- |
| Rank | **#22 in Utilities**, two days after launch ([Rushfinn](https://www.retention.blog/p/explode)) |
| Downloads | **about 20,000**, "a one-day spike and an immediate dip" ([Appfigures](https://appfigures.com/resources/insights/20250124?f=4), 24 Jan 2025) |
| Ratings | fell from 4.3 across 11 ratings to **2.4 across 42** in eleven days |
| Monetisation | ended. On 4 February 2025 Bier posted that "All features & upgrades are now **free forever**" ([X](https://x.com/nikitabier/status/1886856138735423763)) |

Bier's own framing in that post is not "it failed": "It was a piece of
growth hacking art... being able to send disappearing photos in iMessage
is fundamentally useful and thousands are using it." Appfigures'
conclusion is the harder one, and it is about market rather than
mechanics: nobody was looking for a Snapchat replacement. Against tbh's
scale and Gas's 7.4M installs, 20,000 is the finding.

**The lesson to take is the expensive one.** Every mechanic below worked
as designed. The funnel was not the problem. A perfectly engineered
funnel pointed at demand that was not there converts a small number of
people very efficiently.

## The funnel, step by step

Verification key: **[both]** observed independently by both teardown
authors, **[JI]** Ivaldy only, **[JR]** Rushfinn only, **[apple]**
documentary from Apple's own listing.

| # | Step | What Explode did | Verified |
| --- | --- | --- | --- |
| 1 | Fake Allow | **No welcome screen.** First screen is a custom-built dialog imitating Apple's own push permission alert. Tapping "Don't Allow" does nothing at all; only "Allow" advances. The real system dialog follows. Foot-in-the-door, the pattern BeReal popularised. Ivaldy, who was testing it deliberately, says he "instinctively clicked" it | [both] |
| 2 | Value, then account | Welcome screen with a real photo of two friends, then a demo video mimicking the iPhone camera, in big block type. Only then: phone number, first name, last name, in separate steps. **No email, no password, no separate account creation** | [both] |
| 3 | Camera soft-ask | Apple-styled camera request with a **"Why do you need this?"** explainer and animated "Tap Here" chevrons before the real dialog. Denying makes the app unusable | [JI] |
| 4 | Native-looking controls | The in-app camera toggle uses **the exact same UI as the iOS system toggle**. Nothing to relearn | [JR] |
| 5 | PiP through the iMessage step | The highest-drop step, because it requires leaving the app to add an iMessage extension. Explode runs a **Picture-in-Picture video that follows you into Messages and updates as you tap through**, plus a visible remaining-steps checklist, plus a low-contrast **"Not Now"** escape. On completion the iMessage extension shows a **"Return to Explode"** button and the camera opens immediately | [both] |
| 6 | 3-share / 1-hour gate | First post-onboarding screen offers **one month of premium for sending to three people**, on a **one-hour countdown** shown as a persistent timer. Rushfinn waited it out: "the offer really does expire" | [both] |
| 7 | Auto-roll into annual | After three shares the free month "**automatically transitions into a trial for an annual subscription**" | [JI] only |
| 8 | App Clip for the recipient | Recipients **view the photo without installing anything**, with screenshot blocking and a persistent install CTA on their screen. This is the whole asymmetry: the sender needs the app, the receiver does not | [both] |
| 9 | Live Activity urgency | On backgrounding the app, a **Live Activity** announces the premium offer expiring and how many more photos are needed. Both authors flagged it as against Apple's rules, unprompted | [both] |
| 10 | Tap Get | Developer account named **Tap Get**, seller **Tap Get Inc.**, so the App Store search result reads as an instruction next to the Get button | [apple] |

Two details commonly added to this funnel that **no source supports**.
There is no celebration on return from Messages; it is a "Return to
Explode" button and then the camera. And **Dynamic Island** is named by
only one secondary write-up: say Live Activity.

## Steal checklist

Tagged by app shape, because most of this is Network-only and shipping it
on a utility is how you get a one-star review about a fake dialog.

**Universal, ship these.**

- [ ] Value on screen one. No welcome carousel, no feature tour.
- [ ] Ask for a permission **immediately before the feature needs it**,
      with a plain-language reason, not on launch.
- [ ] Use the real system control for anything the user already knows.
      Do not redesign a toggle.
- [ ] **Any step that leaves your app gets PiP, a remaining-steps
      checklist, and a visible "Not Now".** This is the single most
      transferable idea in Explode and it works for Settings toggles,
      Shortcuts installs, widget setup and OAuth.
- [ ] A soft "Not Now" that **preserves the system prompt for later**.
      Once the OS dialog is denied, you cannot ask again in-app.
- [ ] Collect the minimum. Phone plus first name beat email plus
      password plus confirm.

**Network only.** Ship on a dense-graph social app, not on a utility.

- [ ] Time-boxed completion gate that trades shares for premium.
- [ ] Recipient-value-without-install via App Clip or an iMessage
      extension. On a utility the equivalent is the artefact loop: an
      export or link that renders for somebody with nothing installed.

**Do not ship.**

- [ ] A dialog built to be mistaken for Apple's. See below.
- [ ] A Live Activity carrying a promotion. See below.
- [ ] Auto-rolling an earned free month into a paid annual trial without
      a conspicuous disclosure.

## Pricing

**$7.99 a month or $39.99 a year** for Explode+, at launch, in seven
countries. Reported by TechCrunch on 15 January 2025. Premium unlocked
screenshot alerts, screenshot blocking, replaying received photos and
locking sent photos.

The free month earned by sharing to three people was the only free entry
point, and per Ivaldy it rolled into an annual trial automatically. All
of it became free on 4 February 2025.

## Tap Get Inc.

The cheapest hack here and the only one that is purely free. Apple renders
the seller name beneath the app name in search results, directly next to
the Get button, so naming the entity **Tap Get Inc.** makes the result
read as a call to action. Ivaldy notes that once you open the product
page the line switches to the subtitle, "Send exploding text messages",
so the trick only pays in the results list.

Documentary rather than anecdotal: the archived listing shows developer
**Tap Get**, seller **Tap Get Inc.**, copyright **© 2024 Tap Get Inc.**

It is worth being clear that this is a **naming** decision, not a
metadata one, and it is therefore expensive to reverse. It also does
nothing for ranking; it is a click-through trick on an impression you
already earned.

## Grey-area flags, with the actual guidelines

This is where most write-ups of Explode are sloppy in both directions.

**Incentivised sharing is explicitly permitted.** Guideline 3.1.1(x)
bars only store-related actions: "Apps must not force users to rate the
app, review the app, download other apps, or other store-related actions
in order to access functionality... **Apps may otherwise incentivize
users to take specific actions within apps**." The three-share gate is
not a violation.
https://developer.apple.com/app-store/review/guidelines/

**The fake permission dialog is the clearest exposure.** Guideline 5.2.5:
"Don't create an app that appears **confusingly similar** to an existing
Apple product, interface (e.g. Finder), app (such as the App Store,
iTunes Store, or **Messages**) or advertising theme." Both authors report
the screen was built to pass for Apple's own alert rather than merely to
precede it, and Ivaldy was fooled by it while deliberately testing it.
That is the definition of the risk.

**The Live Activity breaches design guidance, which is weaker than it
sounds.** Apple's HIG is unambiguous: "**Don't use a Live Activity to
display ads or promotions.** Live Activities help people stay informed
about ongoing events and tasks, so it's important to display only
information that's related to those events and tasks."
https://developer.apple.com/design/human-interface-guidelines/live-activities

But the HIG is not the App Review Guidelines, and the Guidelines contain
no clause expressly prohibiting a promotional Live Activity. The nearest
hooks are 4.5.3, which names Live Activities in the anti-spam clause, and
4.5.4, which restricts push notifications to opted-in promotions. Nick
Heer made exactly this point in January 2026 when **Duolingo** shipped a
"Super offer" promotion in a Live Activity and the Dynamic Island: the
HIG says don't, the enforceable rules do not clearly say don't, and
Duolingo was not pulled. https://pxlnv.com/linklog/duolingo-live-activity-ads/
and https://www.macrumors.com/2026/01/02/duolingo-dynamic-island-ad/

The honest read: this is a tactic that survives review until Apple
decides it does not, at which point the cost lands on a submission you
need approved. Bier's version of this is to put grey mechanics behind a
**server flag** so they can be switched off without resubmitting, which
is the actual lesson and is in `bier-tactical-hacks.md`.

**PiP and App Clips raise no guideline issue at all.** They are the two
best mechanics in the funnel and they are entirely sanctioned.

## Sources

- Julian Ivaldy, *Explode product analysis (by Nikita Bier)*, 16 January
  2025. Ten-part firsthand teardown. States no growth numbers.
  https://julianivaldy.com/explode-product-analysis-by-nikita-bier
- Jacob Rushfinn, *Explode*, Retention.Blog, 16 January 2025. Firsthand
  walkthrough, independently observed. Only number: #22 in Utilities two
  days after launch. https://www.retention.blog/p/explode
- Ivan Mehta, TechCrunch, 15 January 2025. Pricing and storefronts.
  https://techcrunch.com/2025/01/15/creator-of-gas-and-tbh-makes-an-app-for-disappearing-photos-via-imessage/
- Ariel Michaeli, Appfigures, 24 January 2025. The ~20K downloads figure
  and the demand argument. https://appfigures.com/resources/insights/20250124?f=4
- Nikita Bier, launch post, 14 January 2025.
  https://x.com/nikitabier/status/1879206793118658974
- Nikita Bier, "free forever" update, 4 February 2025.
  https://x.com/nikitabier/status/1886856138735423763

**Not found, despite looking:** revenue, DAU, funding, retention, the
delisting date or reason, and any Bier post-mortem explaining the launch.
Appfigures links to what it describes as such a post; that link resolves
to a different user's question, and the Bier reply it points at has since
been deleted.

See also `bier-tactical-hacks.md` for the extracted tactics, and
`research-pass-3.md` for the App Clip numbers that do exist.
