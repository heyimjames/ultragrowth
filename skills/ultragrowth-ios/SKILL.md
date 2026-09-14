---
name: ultragrowth-ios
description: Growth for iOS apps that are not viral teen social apps. Picks the playbook from the product's shape rather than applying one formula to everything, and covers App Store search, the product page, ratings, pricing, retention surfaces and launch with current, cited benchmarks.
---

# The app growth playbook, for the other kinds of app

Most published app-growth advice is about one kind of app: a free social
product for teenagers whose value comes from other people being on it.
That advice is excellent and it is specific. Applied to a paid utility, a
professional tool or a game, it is not merely useless but actively
misleading, because it tells you to optimise a loop your product does not
have.

**Read `nikita-bier-consumer-apps` when the product is a dense-network
social app.** This skill is for everything else, and for working out
which one you have.

---

## THE FIRST QUESTION: WHAT SHAPE IS IT

Brian Balfour's point, and the one this whole skill hangs on: a company
needs *product-channel fit*, and the channel is not a choice you make
freely. It follows from how people naturally discover, evaluate and buy a
thing like yours. Pick the wrong channel for the shape and you will work
very hard for nothing.

Answer this before anything else:

> **Where does the value come from, the first time somebody opens it?**

| Answer | Shape | Where growth actually comes from |
| --- | --- | --- |
| From other people already being there | **Network** | Invitations. Bier's playbook. |
| From it doing a job, alone, immediately | **Utility** | App Store search, overwhelmingly |
| From a library of things to read or watch | **Content** | Web search and the open internet |
| From it making somebody better at their work | **Professional** | The trade's own channels: communities, newsletters, word of mouth |
| From play | **Game** | Paid acquisition and creator content |

Everything below is organised by shape. A product can move between them
over time, and a few genuinely straddle two, but on any given day it is
mostly one and you should know which.

### The tell that you have guessed wrong

- You built invite mechanics and nobody uses them → you are not a Network
- You are buying installs for a £3 app → your LTV cannot support paid, you
  are a Utility and belong in search
- You are doing ASO for something nobody searches for by name or need →
  you may be Content, and your channel is the open web, not the store

---

## UTILITY: THE ONE MOST PEOPLE ACTUALLY HAVE

A utility is a thing somebody wants to do, alone, now. Weather, notes,
scanning, timers, boards, converters, trackers. There is no viral loop
because using it well does not require anybody else. Stop looking for one.

**Over 65% of app downloads begin with a store search.** For a utility
with no ad budget, that is not one channel among several. It is the
channel, and everything else is a rounding error until it is working.

### Before any of it: you probably cannot edit the fields

Keywords, subtitle, name and screenshots hang off an App Store **version**
and are only writable while that version is in `PREPARE_FOR_SUBMISSION`.
If your app is live and nothing is queued, every write is refused:

```
Attribute 'keywords' cannot be edited at this time
```

ASO is therefore gated on your release cycle. You cannot decide on a
Tuesday to fix your keywords; you fix them as part of the next version,
and they go through review with the build. Keep the strings staged,
rule-checked and counted, so that when a version opens it is a paste
rather than an afternoon.

And on a multi-platform app, the name and subtitle live on an app-wide
record. If **any** platform is in review it is holding that record, and
editing the subtitle folds a metadata change into that review. See
`references/operating-the-listing.md`, which is the half of ASO nobody
writes down.

### The search stack, in the order it pays

1. **Name and subtitle.** Apple indexes both. The name is your strongest
   keyword field. "Clack" ranks for nothing; "Clack: Split-Flap Board"
   ranks for the thing people actually type. Put the *category noun* in
   the name, not only the brand.
2. **The 100-character keyword field.** Comma separated, no spaces, no
   plurals (Apple stems), never repeat a word already in the name or
   subtitle, never use a competitor's trademark.
3. **Category.** Pick the one where you can plausibly rank top 10, not
   the one that describes you best. Ranking 3rd in a small category beats
   80th in a big one.
4. **Localisation.** Even English-only apps should fill in the en-GB
   keyword field: separate index, usually empty, and it is the fallback
   for Ireland, India, Singapore, South Africa and New Zealand as well as
   the UK. en-AU and en-CA cover one country each.

   The cost nobody mentions: **screenshot sets hang off the version
   localisation**, so every locale you add is a screenshot set you must
   upload and then keep in step forever. Usually right to add en-GB only,
   and the others only if the rank data justifies them.

### The product page is a conversion problem, not a decoration problem

The default App Store product page converts at about **1.6%**. That is
the number to beat and most people never measure it.

- **Custom Product Pages** move it. Apple's own figure is a 2.5 point
  average lift on referred traffic, which is a **156% increase**. You get
  up to 70 of them, and since July 2025 you can assign keywords from your
  keyword field to a specific page. One page per *reason somebody wants
  it*, not one per feature.
- **The first two screenshots** are all most people see. They must answer
  "what is this" and "why would I" without being tapped. Caption them.
  A screenshot of your UI tells somebody it is a screenshot of your UI.
- **Product Page Optimization** is Apple's free A/B test, up to three
  treatments. Most developers never turn it on.

### Check where you rank before writing keywords, not after

You are not "ranked". You are ranked **for a term, in a storefront**, and
the two disagree more than people expect. A real table from a six-day-old
app:

| Term | US | GB |
| --- | --- | --- |
| split flap | 37 | 15 |
| the brand name | not found | 16 |
| departure board | not found | 93 |
| flip clock | not found | not found |

The last row is the most valuable thing on the page: an uncontested term
the app plainly deserved and was not competing for. **The gaps are the
brief.** Run this first, and write the keyword field against what it
tells you rather than against a list of synonyms.

### Ratings are a conversion multiplier, not a vanity metric

Zero ratings costs roughly **two thirds of your conversions**. Nothing
else on this list matters as much for as little work.

- Target **4.4+**. Below 4.0 you are losing installs you already paid for
  in attention.
- Prompt with `SKStoreReviewController`, and prompt **at a moment of
  success**, never during onboarding, never on launch. After the thing
  worked. After the third successful use, not the first.
- Apple allows three prompts a year per user. Use them on people who are
  having a good time, not on everybody.
- Answer every one-star review. It is public, it is permanent, and the
  reply is read by the next person deciding.

---

## CONTENT AND PROFESSIONAL: THE CHANNEL IS NOT THE STORE

If people find you by searching the *web* rather than the store, the app
is the destination and not the funnel. Your growth work is on the open
internet: the thing that ranks, the thing that gets linked, the thing
somebody sends a colleague.

- The store listing still has to convert, but it is the bottom of the
  funnel rather than the top
- A web version, even a read-only one, is usually worth more than another
  month of ASO
- Professional tools grow by being the thing one person in a team brings
  in. Optimise for the demo they will give their colleague, not for a
  first-run tutorial

---

## THE LOOP A UTILITY ACTUALLY HAS

A social app grows because using it requires other people. A utility has
no such requirement, which is why the usual conclusion is that utilities
have no loop and must buy every user forever.

That is wrong, and the correction is the most useful idea in this skill:

> **A utility's loop is not an invitation. It is an artefact.**
>
> The app makes something that leaves the app, and that thing is seen by
> somebody who does not have the app.

Five of them, in rough order of value:

| Loop | What it is |
| --- | --- |
| **The visible surface** | A widget, a Lock Screen, a wallpaper, a Watch face. Seen by everybody who looks at that device, and it costs the user nothing because the distribution is a side effect of the product working. Adoption is a minority, perhaps 10 to 15%; build it for them |
| **The export** | Anything the app makes that can be sent, and whether it carries its origin when it travels |
| **The link that works without the app** | A shared link that renders something real for somebody who has installed nothing is worth an order of magnitude more than one that opens the store |
| **The multiplayer edge** | The single place a second person is natural. Usually small, usually the only loop the product has |
| **The other device** | The same person on a Mac and a Watch. Not new revenue, but retention that looks like growth and it seeds the visible surface elsewhere |
| **The secret** | Unproven, and worth thinking about. A hidden feature is one of very few things people voluntarily tell each other about a utility. Nobody says "get this scanner app"; plenty of people say "tap the version number five times". Android has been getting free word of mouth out of seven taps on a build number for fifteen years |

If your app produces nothing anybody else ever sees, you do not have a
loop. Stop looking for one and go and be very good at search instead.

The whole of this, plus activation, paywall mechanics and retention
without nagging, is in `references/in-app-growth.md`.

### Activation: the number most small apps never define

Between "downloaded" and "user" there is a specific event. Write the
sentence: **"Somebody is a real user once they have ______, at least
once."** Scanned a document. Written on the board. Got a result.

Measure the share of installs that reach it in the first session. That
number, not downloads, is what onboarding is for. And nothing may stand
between the install and it: not a sign-up, not a permission you do not
need yet, not a paywall, not a tour.

## PRICING, WITH THE CURRENT NUMBERS

From RevenueCat's 2026 report across **115,000 apps and $16B** of revenue:

| Finding | What to do about it |
| --- | --- |
| **Hard paywalls convert about 5x better than freemium**, with similar long-term retention | If you are freemium out of nervousness rather than strategy, test a hard paywall. The retention fear is mostly unfounded |
| Short trials bring revenue forward but cost long-term conversion | Do not shorten the trial to make this quarter look better |
| Median app grew MRR **5.3%** year on year; the top decile grew **306%** | The median is not a target, it is a warning. This market is winner-take-most |
| New subscription apps launched per month went from ~2,000 to **~15,000** in three years | Attention is the scarce thing. Being good is table stakes; being *findable* is the work |

A one-off purchase is still legitimate and is often right for a utility
somebody wants to own rather than rent. Subscriptions suit things with
ongoing cost or ongoing value. Do not subscribe a calculator.

---

## RETENTION SURFACES: THE APPLE FEATURES MOST APPS SKIP

For a utility, retention is not a notification strategy. It is **being
present without being opened**.

| Surface | Why it retains |
| --- | --- |
| **Widgets** | The app is on the Home Screen doing its job. The highest-value retention feature Apple ships, and the most skipped |
| **Live Activities** | For anything with a duration: a timer, a delivery, a match |
| **Shortcuts and App Intents** | Makes you part of somebody's automation, which is very hard to churn out of |
| **Control Center controls / Action Button** | One press from anywhere |
| **Watch and Lock Screen** | Presence at a glance |
| **Share extension** | You are in every other app's share sheet, which is distribution as well as retention |

Notifications: only when there is something worth knowing. "You have not
opened the app" is a message about your needs, not theirs.

---

## LAUNCH, WHEN YOU HAVE NO AUDIENCE

- **Apple editorial is the biggest free lever most apps never pull.** You
  can pitch it directly through App Store Connect. Apple favours apps that
  use new platform features, look native, and have a story. Do it for
  every meaningful release, not once.
- **Ship on a Tuesday or Wednesday**, not a Friday, so a problem does not
  sit unattended over a weekend.
- **Product Hunt, Hacker News and the relevant subreddit** are one-day
  spikes, not channels. Use them to get first ratings, which are the
  thing that compounds.
- **Newsletters in your niche** outperform general tech press for
  utilities, because the reader is already the buyer.

---

## THE HONEST BENCHMARKS

Numbers worth arguing with rather than treating as targets:

| Thing | Rough figure |
| --- | --- |
| Downloads that begin with a store search | 65%+ |
| Default product page conversion | ~1.6% |
| Custom product page lift on referred traffic | +2.5pp, ~156% |
| Cost of having zero ratings | ~2/3 of conversions |
| Ratings target | 4.4+ |
| Median subscription app MRR growth, YoY | 5.3% |
| Top decile | 306%+ |
| New subscription apps per month | ~15,000 |

---

## TWO NUMBERS THAT DECIDE THINGS

**Paid acquisition, for most small apps, does not clear.** Median revenue
per install across subscription apps is $0.23 at day 14 and $0.34 at day
60. Median US cost per install on Search Ads is $2.90 for Utilities and
$3.83 for Health and Fitness. A median app recovers about a quarter of
what it spends in the first year.

And the firsthand accounts point somewhere else entirely. Of the indie
apps that have published real numbers, **not one grew through Apple
Search Ads.** One spent $100 and abandoned the channel. Another hit **a
$0.80 cost per install on Meta against a $4 thirty-day LTV**, which is a
fifth of what Search Ads charges for the same category. Two firsthand
non-social accounts, both pointing away from Apple's own ad product as an
indie's first paid channel, against a vendor benchmark literature that
exists to sell campaign management. See `references/what-actually-worked.md`.

**A feature is a spike in downloads, not in users.** The best firsthand
account, Slopes as App of the Day, is 19,000 downloads in a day against
120,000 in the entire preceding year. **Only about 5,500 of those 19,000
ever launched the app.** If your first run cannot turn a curious tap into
an activation, a once-in-a-lifetime event becomes a rounding error.

## WHAT TO DO FIRST

In order, for an app that is already built and not growing:

1. **Name and subtitle** carry the category noun somebody would type
2. **Keyword field** filled properly, and filled in every English locale
3. **First two screenshots** captioned so they work as an argument
4. **Ratings prompt** moved to a moment of success
5. **One custom product page** per reason people want it
6. **Product Page Optimization** turned on, which is free
7. **A widget**, distinctive rather than merely useful. Not for a
   retention statistic, since no iOS one exists, but because it is one of
   the few ways to be present without being opened and about half your
   users will never grant push. Note also that the commercially proven
   widget play is **the widget as the product**, not the widget as a
   retention feature: one developer runs a portfolio of sixty-three apps,
   several of which are simply widgets people buy
8. **Name the activation event** and measure how many installs reach it
9. **Pitch Apple editorial** on the next release

Most of that is an afternoon, and most apps have done none of it while
worrying about a viral loop they were never going to have.

---

## REFERENCES

| Topic | File |
| --- | --- |
| Store search, keywords, category, locales | `references/app-store-search.md` |
| Actually changing the listing, and why you cannot | `references/operating-the-listing.md` |
| Product page, screenshots, CPPs, PPO | `references/product-page.md` |
| Pricing, paywalls, trials | `references/pricing.md` |
| Loops, activation, paywall mechanics, retention | `references/in-app-growth.md` |
| Widgets, Live Activities, App Intents, Controls | `references/platform-surfaces.md` |
| Search Ads arithmetic, and getting featured | `references/paid-acquisition-and-editorial.md` |
| Statistics in this field that are invented | `references/numbers-that-are-not-real.md` |
| Firsthand results, with the developers' own numbers | `references/what-actually-worked.md` |
| What nobody has measured, and the gaps to respect | `references/what-nobody-has-measured.md` |

## HOW TO READ A NUMBER IN THIS FIELD

App-growth content is an SEO battleground and a lot of its statistics are
laundered: a vendor's 2017 sample becomes "the industry average", or a
figure is attributed to a source that never published it. Several of the
most-repeated claims about widgets in particular were traced to pages
containing no figures at all.

Before planning around any number: find the primary source, check the
sample and the year, and check whether whoever published it sells the
thing the number recommends. `references/numbers-that-are-not-real.md`
lists the ones already chased down.

## SOURCES

- Brian Balfour, *Four Fits for $100M+ Growth*, brianbalfour.com/four-fits-growth-framework
- RevenueCat, *State of Subscription Apps 2026*, 115,000 apps and $16B of revenue
- Apple, *Custom product pages*, developer.apple.com/app-store/custom-product-pages
- Nikita Bier, for the Network shape. See the `nikita-bier-consumer-apps` skill
- Apple, *Getting featured*, *Discoverability*, and the Human Interface Guidelines
- AppTweak, for Search Ads cost benchmarks. Use medians, never the global average
- Curtis Herbert on Slopes, Ben Dodson on Music Library Tracker, Lux on Halide, and Charlie Chapman on Dark Noise: the indie developers who actually publish their numbers
- David Barnard, Phil Carter and Reid DeRamus on pricing and paywalls
- Ariel Michaeli / Appfigures on the ranking algorithm and the case against paid-upfront
