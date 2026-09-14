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
4. **Localisation.** Even English-only apps should fill in en-GB, en-AU
   and en-CA keyword fields; they are separate indexes and mostly empty.

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

## WHAT TO DO FIRST

In order, for an app that is already built and not growing:

1. **Name and subtitle** carry the category noun somebody would type
2. **Keyword field** filled properly, and filled in every English locale
3. **First two screenshots** captioned so they work as an argument
4. **Ratings prompt** moved to a moment of success
5. **One custom product page** per reason people want it
6. **Product Page Optimization** turned on, which is free
7. **A widget**, if the app has anything worth glancing at
8. **Pitch Apple editorial** on the next release

Most of that is an afternoon, and most apps have done none of it while
worrying about a viral loop they were never going to have.

---

## REFERENCES

| Topic | File |
| --- | --- |
| Store search, keywords, category, locales | `references/app-store-search.md` |
| Product page, screenshots, CPPs, PPO | `references/product-page.md` |
| Pricing, paywalls, trials | `references/pricing.md` |

## SOURCES

- Brian Balfour, *Four Fits for $100M+ Growth*, brianbalfour.com/four-fits-growth-framework
- RevenueCat, *State of Subscription Apps 2026*, 115,000 apps and $16B of revenue
- Apple, *Custom product pages*, developer.apple.com/app-store/custom-product-pages
- Nikita Bier, for the Network shape. See the `nikita-bier-consumer-apps` skill
- David Barnard / RevenueCat and Appfigures, on indie and utility app growth
