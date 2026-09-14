# Research brief: firsthand app growth numbers, all shapes

Paste this into any AI with web access. It is self-contained.

---

You are researching for a public skill called **ultragrowth**
(github.com/heyimjames/ultragrowth), about growing apps. **Three research
passes are done. Your job is the fourth.**

## The scope changed, and this is the most important instruction

The first three passes deliberately excluded viral teen social apps,
because that is the one kind of app the published literature already
covers well. **That exclusion is now lifted.** This pass covers all three
shapes, and the comparison between them is the point:

- **Network.** Value comes from other people already being there. Dense
  graph, invitations, teen social. Nikita Bier's territory.
- **Utility.** Value comes from the app doing a job, alone, immediately.
  Tools, trackers, converters, professional apps, paid apps.
- **Hybrid.** A solo-value product with a manufactured social edge
  bolted on, or a social product with a real single-player mode. This is
  where most 2025 and 2026 consumer AI apps actually sit, and it is the
  least documented of the three.

**Tag every finding with the shape it came from.** A number measured on a
teen social app is not a benchmark for a scanner, and a number measured
on a paid utility says nothing about invite rates. Most bad app-growth
advice is a real number applied to the wrong shape. Do not reproduce
that error; the tagging is how you avoid it.

Where a tactic is **actively harmful** if carried across shapes, say so
explicitly. That is the highest-value output of this pass. See
`growth-tips-catalog.md` for worked examples: the "70% contacts or dead
on arrival" rule, the age curves, and the local-density thresholds are
all real, all measured, and all destructive if applied to a utility.

## The standard, which matters more than the coverage

- **Primary sources only.** A developer's own blog, their own podcast
  appearance, their own conference talk, their own App Store Connect
  screenshot, their own X post with a live permalink. Not an agency
  summarising one, not an SEO listicle, not "studies show".
- **Every claim needs a number and a URL.** A claim without a number is
  not a finding. A number without a URL is not a finding either. If you
  cannot produce a working URL, report the claim as not found rather than
  publishing the number.
- **"Nothing found" is a valuable result.** Say it plainly and move on.
  Two of the repo's files exist to record emptiness honestly, and adding
  to them is worth more than a soft claim.
- **Flag fabrications by name.** If a widely-repeated statistic traces
  back to a page containing no figures, say so and give the URL. Previous
  passes found a dozen and this remains the single most valued output.
- **Note conflicts of interest.** Most app data comes from vendors,
  because vendors have the aggregate. That does not make it wrong. Note
  which direction the error would run if there were one.
- **Density over prose.** It goes straight into a skill file.

### The bar for a tactic, not just for a statistic

New in this pass, and it changes what counts as an answer.

Read `bier-tactical-hacks.md` in this repo, and the
`nikita-bier-consumer-apps` skill if you have it. Those are the standard
for what a **tactic** has to specify before it is worth writing down:

> A tactic must say **when** it fires, **how many** of something, **what
> gates what**, and **what you measure**.

"Ship a widget because widgets increase usage" is not a tactic. "Put the
viral bridge in the first 60 seconds, because after session 1 invite
likelihood collapses" is one, because it names a window, a mechanism and
an observable. Prefer five tactics at that resolution over fifty pieces
of advice.

**And apply the same scepticism to tactics that the repo applies to
statistics.** `research-pass-3-x-notes.md` documents an agency marketing
page that is the traceable origin of at least three numbers now
circulating under an operator's name, each written in the page's own
voice. Tactical advice launders exactly like ASO statistics do. A
percentage attached to an onboarding tactic with no permalink is a
percentage somebody made up.

## Already covered. Do NOT re-research any of this

**Passes 1 and 2.** Apple Search Ads CPI benchmarks by category and the
break-even arithmetic against RevenueCat's revenue-per-install medians.
Editorial featuring criteria, lead times, the Featuring Nominations form
limits, and the Slopes App-of-the-Day numbers. Custom Product Pages,
Product Page Optimization, App Store Tags, keyword-assignable CPPs.
Apple's stated search ranking factors and the exclusion of promotional
text. Cross-localisation and which storefronts index which secondary
locales. StoreKit review-prompt caps and behaviour, reply rates by
category. Paid-upfront market share, lifetime-versus-subscription revenue
per install, the Dark Noise paywall experiment, Halide's revenue split.
Live Activities at Uber, Widget Suggestions, App Shortcuts before first
launch. Shot Pattern, Short Circuit, Sequel, Sindre Sorhus, Natal,
Visible, Plinky, Focus Friend.

**Pass 3, all of it in `research-pass-3.md`.** Glow's 80.7% widget
install rate, Overcast's 10,000 configured widgets, Widgetsmith's 131M
downloads, Locket's 80M downloads and 9M DAU, and the fact that Apple's
"~10%" widget figure is boilerplate arithmetic rather than a statistic.
The Singapore Buses App Clip at zero uses, Footprint's App Clip
completion lifts, and the absence of any Apple App Clip figure.
RocketSim's 60% install-to-core-value and Flowvi.be's 27%
activation-per-onboarding-start. HabitKit's 98% store-sourced downloads
and FlipperHelper's 51% search share of product page views. Apple's own
FunPlus and CBS Sports CPP case-study numbers. The WWDC session-time
decline on Controls across WWDC24 to WWDC26, and the TidBITS and
MacRumors Action Button polls. PCalc's tripled day-one sales in 2009.
Steptastic's featuring impressions and its Featuring Nominations
account. Kittehface, Itemlist and MindSea on localisation. App Store
Tags being US-only, Siri app schema domains, the "additional ads" change,
Guideline 4.3(b), the new age ratings, and Apple's 2026 search ranker
paper.

**The Bier corpus, in `x-growth-tips.md` and `growth-tips-catalog.md`.**
The January 2022 thread in full with permalinks, his permission-rate
gates, the age curves, the 10% density threshold, the tbh and Gas launch
mechanics, the Dupe, VYBE and Death Clock single-player tactics, and his
X tenure figures. Also the chase list in
`research-pass-3-x-notes.md`: do not spend time re-confirming that "6
screens", "K > 1", "22+", the 40% activation bar or the pre-permission
lift cannot be traced to him. They cannot.

**Explode, in `explode-teardown.md`.** The funnel, the pricing, the Tap
Get Inc. naming trick, the ~20,000 downloads, and the guideline analysis.
The one open question there is listed below.

## The still-empty gaps. Start here

Five gaps have now survived three passes and a deliberate attempt to
refute each one. **Filling any single one of these is worth more than
everything else in this brief.**

1. **The widget retention delta.** Adoption is now partly filled: Glow at
   80.7%, Overcast at 10,000 configured, and the Android Gratitude case
   at 25% higher retention with 10% DAU adoption. **No named iOS
   developer has ever published retention for widget users against
   non-widget users.** Shopify built the instrumentation specifically to
   measure it and published no numbers. David Smith, who ships more
   widgets than anybody, has never published it either.

   Note the newly relevant fact: Apple *does* ship a **Home Screen Widget
   Installs** analytics report, with data from iOS 17.4. So developers
   can see their own adoption. The question is who will say what theirs
   is, and whether anybody has cohorted retention against it.

2. **Share sheet or export to iOS install, as a percentage.** What share
   of a utility's installs came from somebody receiving an exported
   artefact. Apps whose main input *is* the share sheet are the best
   candidates. The closest near-miss explicitly refuses the number: Kiyo
   says watermarked exports "drove more installs than any paid campaign
   we'd run" and publishes no percentage.

3. **Universal Links against a bare App Store link**, install rate for a
   shared artefact. No published test exists. The only adjacent figure is
   an eleven-year-old vendor beta range.

4. **An indie-owned Custom Product Page before-and-after.** Every CPP
   number in circulation is published by an ASO vendor or by Apple about
   a large advertiser. Nobody has written "I shipped N custom product
   pages and my conversion went from X to Y." Pass 3 searched six
   communities and five podcasts for this and found nothing.

5. **Control Centre and Action Button third-party adoption.** No figure
   from Apple, any vendor, or any developer, for either. Note that
   `ControlCenter.currentControls()` reports only to the owning app, so
   this is structurally unknowable across apps: the only possible source
   is a developer volunteering their own number.

Also still empty, and lower priority: any before-and-after for an Apple
Design Award; any modern price-elasticity study, the only systematic one
being from 2015; any measurement of App Intents driving installs, opens
or retention; localisation with **both** a delta and a maintenance cost
from a named indie iOS developer; and any easter-egg number after 2009.

## What else to find, by shape

### Network and teen social, newly in scope

The literature here is good on strategy and thin on verifiable numbers,
because the operators post on X and then delete. Concretely:

- **Contacts permission after iOS 18, measured.** Bier's position is that
  friend-based contact sync is "dead on arrival" post-iOS 18 and that the
  approval rate "nose-dived". **Nobody has published the before and
  after.** A single named app with a contacts-approval rate on iOS 17
  against iOS 18 would be a genuinely new fact.
- **The alternatives to contact sync**, with numbers: school codes, QR
  codes, deep links, invite links. Anybody who replaced contact sync and
  published what it cost them.
- **Any 2025 or 2026 teen social launch with published funnel numbers.**
  Not commentary, numbers. Preferably one that failed: failure post
  mortems with figures are rarer and more useful than wins.
- **Push approval rates, firsthand.** There is a claimed "proven 85%" and
  a claimed 51.6% Utilities category average from a vendor. A named app
  publishing its own opt-in rate, with the prompt design described, would
  settle a lot.
- **Whether the age curve is real outside tbh and Gas.** The "invites
  fall 20% per year of age from 13 to 18" figure has one source and one
  author. Anybody else measuring invite propensity by age.

### Hybrid, the least documented and most current

This is where the new work is, and almost nothing is written down.

- **Consumer AI apps that went viral then churned, with the numbers.**
  The pattern Bier describes for VYBE is: viral spike, churn within days,
  then rescue by finding the one retained sub-behaviour. He claims
  retention "nearly 4x" and gives no absolutes. **Find anybody who
  published the actual cohort curves for a spike-and-churn AI app.**
- **Manufactured shareable artefacts on solo tools**, measured. Death
  Clock's shareable death-date projection is the stated example and the
  only figure is "cost of acquisition down to pennies". Somebody must
  have real numbers on an artefact bolted onto a single-player app.
- **Safari extensions and keyboard extensions as retention mechanisms.**
  The VYBE claim is that once the extension is enabled the user is
  "essentially retained for life". That is a very strong claim with no
  published data behind it. Anybody measured it?
- **Commission or affiliate monetisation replacing subscription** on a
  consumer app, with the revenue comparison.

### Utility, continuing

- **More activation numbers.** Two exist, with different denominators:
  RocketSim's 60% install-to-core-value and Flowvi.be's 27%
  activation-per-onboarding-start. A third, stated precisely enough to
  know what the denominator is, would make this section real.
- **Apps that grew primarily through App Store search, with before and
  after.** HabitKit and FlipperHelper are the two firsthand accounts and
  both have caveats: HabitKit's 98% is both stores combined, and
  FlipperHelper's 51% sits on a base of 279 product page views.
- **The artefact loop, measured.** Anything where an export, a widget, a
  shared link or a distinctive format produced installs, with a number.

### Platform and policy, 2026 onward

- **Guideline 4.3(b) enforcement.** In June 2026 Apple added the power to
  remove *already-published* apps that "are not updated, improved, or do
  not attract customers", naming dating, flashlight, sound effects,
  wallpaper, simple timers and fortune telling. Apple has defined nothing
  numerically and published no changelog entry. **Has anybody actually
  been removed under it?** A single confirmed case would matter a lot.
- **The "additional ads" rollout**, live since 3 March 2026. Any measured
  effect on organic search traffic. Apple named no cap.
- **App Store Tags outside the US.** Currently US-only and generated from
  `en_US` metadata. Any expansion, and any measured ranking effect.
- **Siri app schema domains and the Spotlight semantic index.** Mechanism
  documented, zero adoption or install figures. Anybody shipped them and
  measured anything.
- **App Clips, five years in.** Apple has never published a single
  adoption or conversion figure. The only disinterested developer number
  found is zero uses in six months.

### One open question on Explode

`explode-teardown.md` is complete except for this: **the app is no longer
on the App Store and no source found says when it was delisted or why.**
Apple's search API returns nothing for the seller Tap Get Inc. Do not
assert that Apple pulled it without a source. If you can date the
delisting, or find the deleted Bier reply that Appfigures linked to
(best candidate status `1883628269662240783`, 26 January 2025), that
closes the file.

## What blocked previous passes

**Two walls came down in pass 3, and one of them is the best source in
this whole field:**

- **`podsearch.david-smith.org` is a searchable full-text index of Under
  the Radar.** It is how the Overcast configured-widget figure was
  finally recovered after two passes failed on show notes. **Start
  there.** Previous briefs did not know it existed.
- **`david-smith.org` now fetches fine.** It had 403'd previously.

**Still hard-blocked to automated fetching:**

| Source | What happens |
| --- | --- |
| `relay.fm` | 403 to fetchers, but see podsearch above, which indexes it |
| `launched.fm` | Connection refused |
| `jordibruin.com` | Connection refused |
| Apple Podcasts episode pages | 404 to fetchers |
| Reddit | IP-blocked from some environments. Pass 3 recovered a comment via three independent search queries but could not load the thread |
| `emrldlabs.com` | CAPTCHA-walled |
| X guest search and conversation endpoints | Shut down. Individual posts resolve via `cdn.syndication.twimg.com/tweet-result`; **replies and search do not** |

**Still never attempted:**

- **Podcast and conference audio.** Every finding so far came from show
  notes or from the one searchable transcript archive. Deep Dish Swift,
  iOSDevUK, NSSpain, Swift Island and Do iOS talks are unexamined, and
  slides often carry numbers that never reach a blog post.
- **Paywalled newsletters.** Sub Club members' posts, Mobile Dev Memo's
  paid tier, Appfigures' subscriber data.
- **Private communities.** iOS Folks, Indie Dev Slack, the RevenueCat and
  Superwall Slacks. Do not scrape them. If you are a member, ask.
- **Just asking.** No pass has tried emailing a developer to ask "what
  share of your users have the widget installed?" For a question nobody
  has answered publicly, and which Apple now gives every developer the
  report for, that is probably cheaper than any amount of searching.

**One budget note:** pass 2 exhausted its web-search allowance and
finished on direct URL fetches only, which stopped discovery dead. Spend
search on discovery early and leave fetching until last.

## Output

Markdown. One section per topic above. Within each, bullets where every
bullet is a specific claim, plus the number, plus the URL, plus the
**shape tag**. Then:

- **Nothing found**: the topics that yielded nothing, stated plainly
- **Fabrications traced**: widely-repeated numbers that are not at their
  cited source, named individually with URLs
- **Tactics that do not survive a shape change**: anything real that
  would be harmful applied to a different shape, and why
- **Conflicts**: where credible sources disagree, with both numbers
- **Conflicts of interest**: who published what and what they sell
- **Corrections**: anything in this repo that your pass shows to be
  wrong. Pass 3 produced four. This is not a failure mode, it is the
  point

Under 1,500 words. Fifteen well-sourced specifics beat sixty soft ones.
