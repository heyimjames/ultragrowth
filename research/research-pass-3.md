# Research pass 3: firsthand iOS growth numbers

Third pass against the brief in `NEXT-RESEARCH-PROMPT.md`. Primary sources
only. Every claim below carries a number and a URL, or it is filed under
"still empty" instead.

Two things to read before the findings. First, this pass **broke the
longest-standing gap in the skill**: there is now a named app with a
published iOS widget adoption figure. Second, it **corrected four claims
the skill or the brief was making**, listed at the bottom under
"corrections". Those matter more than the new numbers.

Tags used throughout: **[dev]** published by the developer who earned it,
**[vendor]** published by a company selling the thing being measured,
**[apple]** published by Apple, **[press]** journalism.

---

## 1. Firsthand iOS widget numbers

### The gap is now partly filled

- **Glow, an iOS affirmations app: 80.7% of users install at least one
  widget**, lock screen widgets most popular. **[dev]**
  https://expo.dev/blog/how-to-implement-ios-widgets-in-expo-apps
  Written by Arthur Spalanzani as a guest post on Expo's blog. Expo
  promoted it on 12 January 2026, which is the best available date; the
  post itself carries none.

  **Read this figure carefully.** Glow is a widget-first app: the post's
  own framing is "what if the widget is the app". No sample size, no
  timeframe, no measurement method and no widget-versus-non-widget
  comparison are published. It is a **ceiling case, not a benchmark**, and
  it is the number a product gets when the widget *is* the product, which
  is the pattern the skill already identifies via Sindre Sorhus.

- **Overcast: "over 10,000 people who have it installed, who have a
  widget configured"**, about two weeks after shipping its iOS 14 widget,
  with no press push. **[dev]** Marco Arment, Under the Radar #227,
  29 September 2021. https://www.relay.fm/radar/227 (transcript at
  timestamp 00:08:10: https://podsearch.david-smith.org/episodes/5216)

  An absolute count with **no denominator**, so it cannot be turned into
  an adoption rate. Still the only first-party iOS configured-widget
  count found in three passes.

- **Widgetsmith: "around 131 million downloads"** at five years.
  **[dev]** David Smith, 18 September 2025.
  https://david-smith.org/blog/2025/09/18/widgetsmith-at-five/
  This is **Widgetsmith alone**, not his portfolio. Earlier milestone at
  100M: https://david-smith.org/blog/2023/03/08/new-post

- **Locket: over 80 million total downloads, more than 9 million daily
  active users, more than 10 billion photos shared.** **[press]**,
  company-claimed, TechCrunch, 6 August 2025.
  https://techcrunch.com/2025/08/06/photo-sharing-app-locket-is-banking-on-a-new-celebrity-focused-feature-to-fuel-its-growth/

  The widely repeated **"100M+ downloads" is an interviewer's framing**,
  not a figure Matt Moss stated, in
  https://asseenonbyochuko.substack.com/p/gen-alphas-post-algorithm-social
  (10 April 2026). Use 80M+ and 9M DAU. Locket is another widget-as-the-
  product case, not a widget-as-retention-feature case.

### The retention delta is still empty, and the attempt to refute it failed

No named iOS developer has published retention for widget users against
non-widget users. The closest three findings are all instructive:

- **Android, not iOS:** Gratitude saw **25% higher retention for widget
  users**, with **10% of total DAU** having adopted the widget.
  Google-published, developer-reported, correlational, no holdout.
  https://developer.android.com/blog/posts/gratitude-saw-25-higher-retention-for-widget-users
- **Shopify built the instrumentation and published no numbers.** Its
  engineering post says it added widget telemetry specifically to
  "better understand adoption and retention of widgets" via
  `WidgetKit.getCurrentConfigurations`, and contains no percentages at
  all. https://shopify.engineering/lessons-building-ios-widgets
- **David Smith, who ships more widgets than almost anybody, has still
  never published an adoption share or a retention delta** for any of his
  apps, despite publishing download totals, OS version splits and paywall
  conversion. Checked his blog, his own podcast transcript archive and
  his Mastodon. That absence is the strongest single piece of evidence
  the skill has.

  One trap: in Under the Radar #227 Smith says "The WidgetSmith adoption
  rate, 50%." That is **iOS 15 operating-system adoption** among
  Widgetsmith users, not widget adoption. Do not repurpose it.

### Apple's "~10%" widget figure is not a statistic

Worth stating precisely, because it is the kind of number that becomes a
fact by repetition. Apple's **Home Screen Widget Installs** analytics
report page contains this:

> if your app performed an action detailed in this report on 10 unique
> devices on a specific day, and the App Sessions Context report shows
> there were 100 unique devices running your app that day, then you can
> approximate that 10% of the devices running your app performed that
> action

https://developer.apple.com/documentation/analytics-reports/home-screen-widget-installs

It is **boilerplate arithmetic, not measurement**. The identical sentence
appears verbatim on unrelated report pages, for instance
https://developer.apple.com/documentation/analytics-reports/shortcuts-actions-usage
The 10 and the 100 are placeholder device counts. There is no Apple
statement of a real measured widget install rate.

---

## 2. Share sheet, exports, App Clips and Universal Links

### App Clips: the first honest firsthand datapoint is a zero

- **Singapore Buses: the App Clip "since September it's been used a grand
  total of zero times"**, about six months after shipping. The developer
  is removing it. **[dev]** Stuart Breckenridge, 12 March 2026.
  https://stuartbreckenridge.net/2026-03-12-app-clip-usage/
  The original implementation post, where he says "I'm interested to see
  how (or if) it affects download statistics":
  https://stuartbreckenridge.net/2025-09-16-singapore-buses-v2026/
  Caveat: he does not say whether zero came from App Store Connect's App
  Clip metrics or his own telemetry.

- **Footprint, an identity-verification vendor, publishes the only real
  App Clip funnel numbers found.** Doc scan completion went from
  **70 to 80% to about 92%**; full App Clip flow completion from **about
  75% to about 86%**; passkey success **78%**; overall conversion
  including passkey-skippers **96%**. **[vendor]**, 6 July 2025.
  https://footprint-blog.ghost.io/app-clip-improvements-how-we-built-best-in-class-doc-scanning/
  **Badly confounded**: they redesigned the UI *and* rewrote the App Clip
  from React Native to native Swift in the same change, so neither cause
  is isolable. Their own hedge: the "dataset is still early". Note the
  canonical marketing URL at onefootprint.com 404s; cite the Ghost one.

- **Apple has published no App Clip adoption, conversion or install-rate
  figure, 2020 to now.** It publishes metric *definitions* only:
  https://developer.apple.com/help/app-store-connect-analytics/acquisition/app-clips/
  and https://developer.apple.com/documentation/analytics-reports/app-clip-usage

- Useful as evidence *for* the absence: operators decline to give
  numbers. Lime's senior product manager said of App Clip rides "we also
  see a relatively high download conversion rate" and **"declined to
  provide conversion rates"**. **[press]**
  https://techcrunch.com/2021/03/24/lime-launches-app-less-rides-and-no-fee-reservations-to-get-more-people-riding/

### Share-to-install and Universal Links: still empty

No named developer has published what share of their installs came from
somebody receiving a shared artefact or export, and nobody has published
a **Universal Link versus bare App Store link** install-rate test for a
shared artefact.

The closest near-miss explicitly refuses the number: Kiyo's "Made with
Kiyo" watermark write-up says shared watermarked exports "drove more
installs than any paid campaign we'd run", measured by correlating App
Store impressions with sharing spikes, and **publishes no percentage**.
https://fillbyte.com/blog/how-kiyo-reached-one-million-downloads

---

## 3. Activation rates for utilities

- **RocketSim: "only 60% of those who install RocketSim will actually see
  the side window. In other words, 40% of users don't experience
  RocketSim's added value."** **[dev]** Antoine van der Lee, 27 December
  2023. https://www.avanderlee.com/general/swiftlee-2023-a-year-in-review/
  Same post: MRR $4,500, ARR $62,000 including team licences, DAU up
  300%, 43,000 App Actions. This is the cleanest published
  install-to-core-value number for an iOS utility found in three passes.

  Later RocketSim figures, at 100K ARR: churn **3.2%**, conversion to
  paying **8.6%**, initial conversion **14.1%**, LTV **$2.52**, LTV of a
  paying user **$42.00**.
  https://www.linkedin.com/posts/ajvanderlee_major-milestone-rocketsim-just-hit-100k-activity-7287173229230587904-T1Fq
  And on shipping the top-voted feature: **"I saw the active trials going
  from 40 a day to 120 a day."**
  https://www.revenuecat.com/blog/growth/antoine-van-der-lee-rocketsim-launched-podcast-2026

- **Flowvi.be: 320 users reached the Welcome screen, 308 granted library
  access, 246 started the initial sync, 87 reached the core "play a mood"
  action. 87/320 = 27.2%.** **[vendor]** TelemetryDeck, 12 August 2026,
  quoting the developer (Konstantin) and publishing the raw funnel query.
  https://telemetrydeck.com/blog/why-your-app-gets-downloads-but-no-conversions-and-how-to-fix-it/

  **Do not write "320 installs".** 320 is onboarding starts, which
  excludes everybody who installed and never opened, or opened and
  bounced before the Welcome screen. **True install-to-activation is
  lower than 27%, by an unpublished amount.** The period is given only as
  "a recent period".

Two real activation numbers for utilities now exist, from 60% and 27%
denominators that are not the same denominator. Both are worth quoting.
Neither is a benchmark.

---

## 4. Apps that grew primarily through App Store search

- **HabitKit: "About 98% of my users find Habit Kit directly through the
  App Store, Google Play. I literally do no marketing at all besides
  that."** **[dev]** Sebastian Röhl, on Starter Story Build, 2 May 2026.
  https://www.youtube.com/watch?v=I2GG0lyb_RI
  **The 98% is both stores combined**, self-reported verbally. It is not
  an App Store Connect source-type breakdown and it is not iOS-only.

  His own numbers for 2025: **App Store 272,000 downloads, Google Play
  290,000 downloads, total revenue $602,000, MRR $28,000**, and a top-5
  US ranking for "habit tracker".
  https://sebastianroehl.substack.com/p/2025-the-year-that-changed-everything

  His ASO mechanics, which support the skill's advice directly: the app
  is named **"Habit Tracker - HabitKit"** with the subtitle "Streaks &
  Accountability", the category noun in the name exactly as the skill
  recommends. Apple Search Ads run at **$100 a month** and got **40
  installs at about €2.50 each**, which he calls "pretty horrible" and
  says he does not measure.
  https://sebastianroehl.substack.com/p/my-app-store-optimization-strategy

- **FlipperHelper: App Store Search was 143 of 279 product page views, or
  51%**, over 90 days. Full split: Search 143 (51%), web referral 99
  (36%), App Store browse 21 (8%), app referral 14 (5%). Also **81
  first-time downloads at a 29% page-to-download conversion**, and Search
  page views growing from 38 in March to 105 in April. **[dev]**
  Oleksandr Prudnikov, 8 May 2026.
  https://hackernoon.com/53-blog-posts-0-google-clicks-81-downloads-6-weeks-of-marketing-a-free-ios-app
  The metric is **product page views**, not impressions and not
  downloads. The absolute base is tiny (279 views), so this is a real
  number and a thin one.

---

## 5. Custom Product Pages

**Still no named indie developer has published their own before-and-after
CPP result.** Searched developer blogs, X, r/iOSProgramming,
r/AppStoreOptimization, r/AppleSearchAds, IndieHackers, Sub Club,
Launched, Under the Radar and Apple Tech Talks. Nobody has written "I
shipped N custom product pages and my conversion went from X to Y". The
skill's claim stands.

What does exist is Apple's own case-study session, which is worth quoting
precisely because it is Apple talking about large customers:

- **Apple Tech Talks, "Make the most of custom product pages", 28
  February 2023.** **[apple]**
  https://developer.apple.com/videos/play/tech-talks/110361/
  - **FunPlus** (State of Survival, RPG audience segments, all five
    screenshots customised): **33% higher conversion rate and 14% lower
    cost per install.**
  - **CBS Sports** (March Madness seasonal page for mobile web visitors,
    all five screenshots customised): **20% uplift in conversion rate and
    48% improvement in tournament signups year over year.**
  - Two Search Ads ad-variation results from the same session: **Baidu
    +10% install rate**, **Otto +12% install rate** against their default
    ad.

  No methodology, no absolute numbers, no confidence intervals. These are
  large advertisers with dedicated creative teams, and the mechanism that
  produced 33% for a game with five bespoke screenshot sets is not
  available to a one-person utility.

- Vendor-published, for completeness and with the conflict noted:
  AppTweak reports **+58% conversion and 39% lower CPI for SoundCloud**,
  and benchmarks of **+6.6% for apps, up to +8% for games**. AppTweak
  sells ASO tooling.
  https://www.reddit.com/r/AppleSearchAds/comments/1kbgpva/the_strategy_behind_our_58_increase_in/

---

## 6. Control Centre controls and the Action Button

**Nothing. Confirmed by attempting to refute it.** No adoption figure
exists from Apple, any analytics vendor, or any named developer, for
either controls or third-party Action Button assignment.

- RevenueCat's *State of Subscription Apps 2026*, 115,000+ apps and 338
  pages, contains **zero occurrences of "Action Button" or "Control
  Center"**. Widgets appear once, in a developer quote about Flutter.
  https://www.revenuecat.com/state-of-subscription-apps-2026-utilities/
- Apple's API is scoped so that this cannot be measured across apps:
  `ControlCenter.currentControls()` reports only to the owning app.
  https://developer.apple.com/documentation/widgetkit/controlcenter
- Sensor Tower and Appfigures are store-scrape and panel businesses with
  no system-UI telemetry product.

**Apple's own attention, measured by session allocation.** This is now
verifiable rather than impressionistic:

| Year | Session | Controls coverage |
| --- | --- | --- |
| WWDC24 | *Extend your app's controls across the system* (10157) | Entire session, six chapters |
| WWDC25 | *What's new in widgets* (278) | No controls chapter; a sub-segment on new macOS and watchOS placements, redirecting viewers to WWDC24 |
| WWDC26 | *WidgetKit foundations* (277) | The string "control" appears **zero** times across the description, four chapters and full transcript |

https://developer.apple.com/videos/play/wwdc2024/10157/ ·
https://developer.apple.com/videos/play/wwdc2025/278/ ·
https://developer.apple.com/videos/play/wwdc2026/277/

**The closest published figures do not answer the question**, and should
not be quoted as if they did. A TidBITS reader poll of iPhone 15 Pro
owners, 16 September 2024, on Action Button use: **33% Ring/Silent, 21%
Camera, 20% do not use it at all, 11% a Shortcut, 9% flashlight.** No
third-party-app category was offered at all.
https://tidbits.com/2024/09/16/do-you-use-it-iphone-15-pro-action-button-struggles-to-find-its-purpose/
A MacRumors X poll of about 7,000 respondents, April 2024: **50.6% "often
forget it exists", 12.6% "game changer".** Both are opt-in reader polls
of Apple enthusiasts, not telemetry.

A confident "nobody knows, and here is why it cannot be known" is the
correct output for this section.

---

## 7. Hidden features and easter eggs as distribution

This came back thinner than hoped and with **one genuinely good number**,
which is more than the brief expected.

- **PCalc: "Sales of the full PCalc tripled on the first day and have
  slowly now returned to normal just over a week later. Downloads of the
  free version increased more than tenfold."** **[dev]** James Thomson,
  TLA Systems, 12 October 2009.
  https://tla.systems/blog/2009/10/12/going-viral/

  **Two caveats that must travel with this number**, because the
  circulating version drops both. The driver was **a satirical press
  release Thomson wrote about the easter egg**, not organic discovery of
  the egg. And he deflates it himself in the same post: "it didn't
  actually do a whole lot", and it was "slightly worse in terms of
  numbers than what happened with the release of PCalc 1.7, which was
  just a normal release... and no huge fanfare". It is a multiplier with
  no absolute figures. The egg was PCalc 1.8's joke where `5318008`
  flipped upside down became "Censored!".

- **Strongest anecdote with no number**, labelled as such: PCalc's About
  screen grew from a physics toy into a driving game with a worldwide
  leaderboard and a physical trophy, and was covered by press *as an
  easter egg* at least twice, by MacStories
  (https://www.macstories.net/reviews/pcalcs-delightfully-insane-about-screen/)
  and by TechRadar when it span out as the free standalone *About by
  PCalc* in March 2022. Notably, on https://pcalc.com/thirty Thomson
  attributes a separate sales bump to **Apple featuring**, not to the
  egg: "the publicity caused such a sales bump that I could buy a Retina
  5K iMac and have a nice vacation." No figure.

The honest position: the mechanism is real and is evidenced exactly once,
in 2009, with a press release doing most of the work. Build the secret
because it is delightful. Do not forecast from it.

---

## 8. Localisation

No named indie iOS developer has published both a delta attributable to
localisation **and** an ongoing maintenance cost. Three partial sources,
in descending order of rigour:

- **Best-controlled, but Android and 2014.** Kittehface Software, 15
  April 2014. Six languages by native speakers at **$0.09 per word,
  about $1,000 total**. After translating the Play **listings only**:
  average install change **+94.8% for free versions against −1.2% for an
  unmodified control**, and **+10.5% for paid against −16.35% for
  unmodified paid**. Per app: Thunderstorm Free **+268%**, Galactic Core
  Free **+104%**, Koi Paid **+42.7%**. **[dev]**
  https://www.kittehface.com/2014/04/product-localization-and-results-thereof.html
  Unusually good methodology, with a control group. Wrong store, and
  twelve years old.
- **iOS, named app, confounded, no cost figure.** Itemlist by dabo.dev,
  30 September 2024. Seven languages added end of July 2024. August
  against July: revenue **$974 to $985 (+1.13%)**, MRR **$233 to $261
  (+12.02%)**, active subscribers **118 to 135 (+14.41%)**. He publishes
  a downloads-by-country graph with Germany leading and **no download
  number**. **[dev]** https://dabo.dev/indie-dev-diary-6-august-2024
  Same month he also hit top 5 for "home inventory" in the US and shipped
  an iOS 18 update, so attribution is not clean and he does not claim it
  is.
- **Has the cost discussion, headline number confounded.** MindSea,
  Etchings 1.5, seven languages, December 2012: English-country downloads
  **4.44x higher** in the 17 days after against the 17 days before, but
  the same update added iPad support, hi-res export and new filters, and
  the app had a worldwide free promo as part of iTunes 12 Days of Gifts.
  They say plainly that "localization was not a slam dunk". Their cost
  discussion is qualitative and the most honest found: you commit to a
  language for the app's lifetime, including new-feature strings, store
  metadata, permanent QA and non-English support.
  https://mindsea.com/blog/app-localization-case-study-etchings-goes-global/

Rejected as sources, all with an interest in the answer: hoettler.com's
"212% more downloads with 4 languages" is arithmetic on reachable-market
share (32% to 100%), not a measured lift, published by the founder of a
localisation service. blog.sparrowapps.io changed name, icon and
localisation simultaneously and the author sells a localisation tool.
localepack.app's "400% international traffic growth" is about a website.

---

## 9. Editorial featuring, and the Featuring Nominations form

### The Featuring Nominations gap is closed

The skill said no firsthand account existed of the nominations form
producing a feature. **That is now refuted.**

- **Steptastic: "I sent nominations once or twice, very lucky to get
  nominated on my second time. I was featured in the German App Store in
  the apps and games tab for about 2 weeks."** He adds that the dashboard
  only ever showed the nomination as **'accepted'**, which "doesn't
  indicate whether it actually WILL be nominated, but it moves to the
  next stage", and that he **received no App Store Connect notification**
  that the app had been featured. **[dev]** Thomas Redway, u/Tom42-59,
  r/iOSProgramming, April 2025.
  https://www.reddit.com/r/iOSProgramming/comments/1k1lo0b/has_anyone_had_success_with_the_app_store/

### What the feature did, stated correctly

- **Impressions went from about 150 a day to about 43,000. Conversion
  rate went from about 12% to about 0.1%.** Downloads increased, and he
  **gives no download number**.

  **Both figures are impressions.** The brief for this pass asked for
  "~150 downloads/day rising to ~43k impressions", which compares two
  different metrics and invents a downloads baseline he never published.
  The conversion collapse is the more useful half and matches the
  skill's existing line that a feature is a spike in downloads, not in
  users.

- **Emrld Labs: pre-feature baseline of roughly 110 to 140 downloads per
  day in the US; day-zero downloads about 38x baseline and revenue about
  22x; after 30 days, daily downloads about 1.6x and daily revenue about
  1.9x pre-feature baseline.** Today tab, US storefront, spillover in the
  UK and Australia. **[dev]**, 19 April 2026.
  https://emrldlabs.com/blog/revenue-impact-apple-app-store-feature/

  **Weak enough that it should be quoted only with its caveats.** The
  post never names which of their apps was featured, gives no date for
  the feature, and says the day-by-day figures are "normalized so you can
  see the shape rather than absolute numbers". The only absolute figure is
  the 110 to 140 baseline. No named app means nobody can check it. The
  *shape* it reports, a large day-zero spike settling to a small
  multiple, is consistent with Slopes and with Steptastic, which is the
  only reason to keep it.

---

## 10. App Store policy and discovery, 2025 into 2026

- **App Store Tags are United States only.** Apple: "Currently, tags are
  only supported and displayed to users across the App Store in the
  United States", generated from `en_US` metadata, and "Deselecting all
  tags may affect your discoverability." **[apple]**
  https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags
  Announced at WWDC25 session 328.

- **Siri and Apple Intelligence app schema domains: mechanism
  documented, no numbers.** Adopting schemas puts actions into "the app
  toolbox, which Apple Intelligence draws on to service requests", and
  entities must also enter the **Spotlight semantic index** to be matched
  at runtime. **[apple]**
  https://developer.apple.com/documentation/appintents/app-schema-domains
  No adoption or install figures published.

- **More ads in search results, and "two ads per query" is wrong.**
  Apple said "additional ads", with no stated cap: "Early next year,
  we'll begin running additional ads in search results, where 65% of
  downloads start." **[apple]**, 17 December 2025.
  https://ads.apple.com/news Placement mechanics, including that existing
  campaigns are automatically eligible and there is no position bidding:
  https://ads.apple.com/app-store/help/ad-placements/0082-search-results
  Rollout began 3 March 2026, UK and Japan first, all markets by end of
  March, iOS and iPadOS 26.2 and later. That date came via developer
  email, so it rests on secondary reporting.

- **Removal for inactivity, plus a materially new 2026 clause.**
  Long-standing App Store Improvements criteria: no update in three
  years plus a minimal download threshold over a rolling twelve months,
  90 days to fix. https://developer.apple.com/support/app-store-improvements
  Apple's own scale figure: "almost **2.8 million apps**" removed over six
  years. https://developer.apple.com/news/?id=gi6npkmf Apple's 2025
  transparency report shows 166,899 apps removed, of which 72,271 under
  Guideline 4.0 are footnoted as outdated-app cleanup.
  https://www.apple.com/legal/app-store/transparency/2025/

  New in the June 2026 guidelines update, **Guideline 4.3(b) now permits
  removing already-published apps**: "We may remove these apps from the
  App Store going forward if they are not updated, improved, or do not
  attract customers." Named categories include dating, flashlight, sound
  effects, wallpaper, simple timers and fortune telling.
  https://developer.apple.com/app-store/review/guidelines/
  Caveat worth carrying: Apple has not defined "attract customers"
  numerically, published no changelog entry for the edit, and confirmed
  no removals under it.

- **New age ratings.** 13+, 16+ and 18+ added to 4+ and 9+, replacing 12+
  and 17+, all apps auto-reassigned, questionnaire responses required by
  31 January 2026. **[apple]**, 24 July 2025.
  https://developer.apple.com/news/?id=ks775ehf

- **Today tab or organic ranking changes:** nothing announced in this
  window.

### Apple's 2026 ranker paper, and what it does not say

*Scaling Search Relevance: Augmenting App Store Ranking with
LLM-Generated Judgments*, Christakopoulou et al., Apple Machine Learning
Research, February 2026.
https://machinelearning.apple.com/research/augmenting-app
(preprint https://arxiv.org/abs/2602.23234)

The ranker trains against two label sources: **behavioural relevance**,
described as "downloads and clicks from aggregated App Store search
logs", and **textual relevance**, human judges plus millions of
fine-tuned-LLM labels. A worldwide A/B test gave a **+0.24% conversion
rate lift**, conversion defined as "the proportion of search sessions
with at least one app download", beating production in **89% of
storefronts**, with the largest gains on tail queries.

**A literal string search across the full paper returns zero occurrences
of "retention", "crash", "uninstall" or "churn".** The only behavioural
inputs named anywhere are clicks and downloads.

One precision note. The paper documents two *training objectives*, not an
exhaustive feature list. The defensible phrasing is "the paper names only
clicks and downloads and is silent on retention", **not** "Apple
confirmed retention is not a ranking factor".

---

## Still empty after three passes

These are the gaps to hand to pass 4. Each has now survived a deliberate
attempt to refute it.

1. **The widget retention delta.** Adoption is now partly filled by Glow
   at 80.7% and Overcast at 10,000 configured. No iOS developer has ever
   published retention for widget users against non-widget users. The
   only such number anywhere is Android.
2. **Share-sheet or export to iOS install, as a percentage.** No
   developer has published one.
3. **Universal Links against a bare App Store link**, install rate for a
   shared artefact. No published test.
4. **An indie-owned Custom Product Page before-and-after.** Every CPP
   number in circulation is vendor-published or Apple-published.
5. **Control Centre and Action Button third-party adoption.** No figure
   from Apple, any vendor, or any developer, and Apple's API is scoped so
   that nobody can measure it across apps.
6. **Localisation, with both a delta and a maintenance cost**, from a
   named indie iOS developer.
7. **An easter egg with a number, after 2009.** One datapoint, sixteen
   years old, and the developer who published it partly retracted it.
8. **Any before-and-after for an Apple Design Award.**
9. **Any modern price-elasticity study.** The only systematic one is
   still 2015.
10. **Any published measurement of App Intents driving installs, opens or
    retention.**

---

## Fabrications traced in this pass

The most valuable output of the previous passes, continued. Each of these
was chased to its cited source and is not there.

- **"App Clip invocations grew 34% year over year" and "fewer than 5% of
  apps have registered a clip experience"**, both attributed by an ASO
  vendor to Apple's *WWDC 2025 Platforms State of the Union*. **The
  attribution is false.** The string "clip" appears **zero times** in the
  full transcript of that session, checked at
  https://developer.apple.com/videos/play/wwdc2025/102/ and Apple's own
  upload. The same post's other figures carry bracketed source tags that
  link nowhere. Source of the false claim:
  https://trysonar.app/blog/app-clips-when-they-help
- **A family of iOS widget retention numbers with no developer behind
  any of them**: "5 to 10% range", "15% higher retention", "3.2x higher
  retention after 90 days", "Todoist D1 retention 34% to 58%", "28%
  retention boost". Found on trysonar.app, fanana.io, johal.in,
  proofingroom.tortastudios.com and emrldlabs.com. Several describe
  companies that do not exist; one miscites a Sensor Tower report. None
  names a real developer publishing real cohort data.
- **"20 to 35% of installs from referrals (AppsFlyer)" and
  "share-to-install 12 to 20% (Branch)"**, circulating on aggregator
  pages such as growsurf.com with no URL to any underlying study. No
  primary AppsFlyer or Branch publication containing either figure could
  be located.
- **"97.9% WidgetKit coverage"** on ioscompatibility.com is an **iOS
  version share**, not widget or control adoption. Flagged because it is
  one rewrite away from becoming a widget adoption statistic.
- A general note for pass 4: the top of search results on all of these
  topics is now substantially generated content with no named author and
  no verifiable data. Several domains above pattern-match to it. The
  filter that worked was: name the developer, or discard the number.

---

## Conflicts of interest in this pass

- **Expo** hosts the Glow widget post but did not measure it. The author
  is a guest, the app is his, and the figure is self-reported.
- **Footprint** and **Reactiv** both publish App Clip conversion figures
  and both sell App Clip implementations. Treat as favourable-case
  marketing.
- **TelemetryDeck** publishes the Flowvi.be funnel and sells analytics.
  The raw query is included, which is better disclosure than most.
- **AppTweak** publishes CPP lifts and sells ASO tooling.
- **RevenueCat** publishes the best subscription dataset available and
  sells subscription infrastructure. Its silence on widgets and controls
  is therefore informative: it has no product interest in them either
  way.
- **Emrld Labs** publishes featuring multipliers and does not name the
  featured app.

---

## Corrections this pass forces on the skill

Filed explicitly, because the point of the repo is not repeating things
that turn out to be untrue.

1. **`platform-surfaces.md` says App Store Connect Analytics has "no
   widget-install dimension". That is now wrong.** Apple ships a **Home
   Screen Widget Installs** report, with data available from iOS 17.4.
   https://developer.apple.com/documentation/analytics-reports/home-screen-widget-installs
   The correct statement is that the dimension exists and **nobody
   publishes what it says**, which is a different and more damning fact.

2. **The share-sheet claim should be narrowed.** It is true that there is
   no *share-extension* source dimension. It is not true that a share
   leaves no trace: Apple's source types are App Store search, App Store
   browse, **App referrer** and web referrer, and App referrer "Includes
   Apple apps, such as Messages". So a link shared into Messages and
   tapped does appear, attributed to Messages. What is impossible is
   isolating *your shared artefact* from any other link in that app, and
   there is a privacy minimum-volume threshold below which referrers do
   not display at all.
   https://developer.apple.com/help/app-store-connect-analytics/acquisition/acquisition

3. **`what-nobody-has-measured.md` listed the Featuring Nominations form
   as having no firsthand account. It now has one**, Steptastic, above.

4. **"Two ads per query" should not be used.** Apple said "additional
   ads" and named no cap.

---

## Method note for pass 4

Web search plus direct fetches. Every URL in this file returned HTTP 200
on the day it was written. Where a source was reachable only through a
search index rather than a live fetch, that is stated inline.

The walls listed in the previous brief still stand, with two exceptions
worth recording: **david-smith.org fetched fine** this pass, and his own
podcast transcript archive at `podsearch.david-smith.org` turned out to
be a searchable full-text index of Under the Radar, which is how the
Overcast figure was finally recovered. That archive is the single most
productive source found in this pass and the previous brief did not know
it existed. Start there.
