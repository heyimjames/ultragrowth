# What nobody has measured

Three research passes went looking for firsthand numbers on the things
this skill recommends. Most of them came back empty, and that emptiness
is worth writing down, because the alternative is quoting one of the
invented figures in `numbers-that-are-not-real.md`.

If you find one of these, it is genuinely new information.

## Widget adoption: two real numbers now exist. Retention is still empty

The two halves of this have to be kept apart, because the third pass
filled one of them and not the other.

**Adoption, which is now partly answered.**

- **Glow, an iOS affirmations app: 80.7% of users install at least one
  widget.** Published by its developer, Arthur Spalanzani, as a guest
  post on Expo's blog. Read it as a **ceiling case, not a benchmark**:
  the post's own framing is "what if the widget is the app", no sample
  size or timeframe is given, and it is the number you get when the
  widget *is* the product. Which is the pattern below.
- **Overcast: "over 10,000 people who have it installed, who have a
  widget configured"**, two weeks after shipping, with no press push.
  Marco Arment, Under the Radar #227, September 2021. An absolute count
  with **no denominator**, so it cannot be turned into a rate.

**Retention, which is still completely empty.** No named iOS developer
has ever published retention for widget users against non-widget users.
Checked: Charlie Chapman, Andy Allen, David Smith, Curtis Herbert, which
is close to the complete set of indie developers who publish numbers at
all, plus every podcast and conference source reachable.

Three things sharpen the gap rather than closing it:

- **Chapman published a full public analytics post for Dark Noise** with
  monthly actives, daily actives, the Mac share of sessions and OS
  version spread, and **said nothing about widgets**, despite having
  shipped them since iOS 14.
- **David Smith has published 131 million Widgetsmith downloads and
  still no widget adoption share or retention delta**, for any of his
  apps, which is the strongest single piece of evidence here given he
  ships more widgets than anybody.
- **Shopify built the instrumentation specifically to measure it and
  published nothing.** Its engineering write-up says it added telemetry
  to "better understand adoption and retention of widgets" and contains
  no percentages at all.

The only retention figure anywhere is **Android**: Gratitude at 25%
higher retention for widget users with 10% of DAU adopting. Google
published it, it is correlational, and it has no holdout.

**Two corrections worth carrying.** Apple *does* now ship a **Home
Screen Widget Installs** analytics report, with data from iOS 17.4, so
this is no longer unmeasurable: it is measured privately by every
developer and published by almost none. And the "~10%" widget figure
attributed to Apple is **boilerplate arithmetic** from that report's
documentation, where 10 and 100 are placeholder device counts, not a
statistic. The identical sentence appears on unrelated report pages.

**So the honest position is:** build widgets for reasons of mechanism,
and for the adoption ceiling Glow demonstrates when the widget carries
real value. Anyone quoting you an iOS widget *retention* percentage is
quoting something invented.

### The widget play that is commercially proven is different

Sindre Sorhus runs 63 apps over eleven years, six million users, 33 of
them one-time purchase and no subscriptions. Several of those apps **are
widgets, sold as the entire product**: a photo widget, a favourites
widget, a memo widget.

That is the demonstrated commercial pattern. Not "ship a widget to retain
users", but **"ship a widget as the product"**, for a job somebody wants
done on their Home Screen and nowhere else.

## Nobody has published a share sheet or export-to-install number

The skill argues that a utility's growth loop is an artefact that leaves
the app. No developer has published what share of their installs came
from somebody receiving one.

Plinky, a save-links utility whose primary input *is* the share sheet,
published its pricing, its free-tier limits and its email tactics, and no
share-sheet origination figure.

The closest anybody has come explicitly declines to give the number.
Kiyo's "Made with Kiyo" watermark write-up says shared exports "drove
more installs than any paid campaign we'd run", measured by correlating
App Store impressions with sharing spikes, and publishes **no
percentage**.

**Be precise about why.** App Store Connect has no
share-**extension**-source dimension, so you cannot isolate your shared
artefact. But a share does not vanish: Apple's source types are App Store
search, App Store browse, **App referrer** and web referrer, and App
referrer "Includes Apple apps, such as Messages". So a link shared into
Messages and tapped does appear, attributed to Messages, subject to a
privacy minimum-volume threshold below which referrers do not display at
all. What is impossible is telling your artefact apart from any other
link in that app. Argue the loop from mechanism. Do not attach a
percentage to it.

Related and completely unmeasured: **nobody has published whether a
Universal Link beats a bare App Store link** on install rate for a shared
artefact.

## Nobody has published a Custom Product Page result of their own

Every CPP conversion figure in circulation is vendor-published or
Apple-published, including the ones in this skill. No named developer has
written "I shipped five custom product pages and my conversion went from
X to Y." A third pass searched six developer communities and five
podcasts specifically to refute this, and could not.

The numbers may well be right. They have not been independently confirmed
by anybody without a product to sell.

**Apple's own case studies are worth knowing, and worth discounting
correctly.** In its Tech Talk on custom product pages Apple reports
**FunPlus at 33% higher conversion and 14% lower cost per install**, and
**CBS Sports at a 20% conversion uplift with 48% better tournament
signups year over year**. Both customised all five screenshots for a
specific audience. These are large advertisers with dedicated creative
teams, and the mechanism that produced 33% for a game with five bespoke
screenshot sets is not the mechanism available to a one-person utility.
Useful as a ceiling, useless as a forecast.

The only 2026 commentary from a named practitioner rather than a vendor
is Thomas Petit noting that custom product page headers still do not
support full A/B testing flexibility: "it's not the full liberty we have
now, it's somewhere in between." Useful as a caution that the feature is
less finished than the case studies imply.

## Control Centre controls and the Action Button: nothing, and it is structural

No adoption figure exists from Apple, any vendor, or any developer, for
either third-party controls or third-party Action Button assignment.
RevenueCat's 2026 report, 115,000 apps across 338 pages, contains zero
occurrences of "Control Center" or "Action Button".

And it cannot be measured across apps by construction:
`ControlCenter.currentControls()` reports only to the owning app. The
only possible source is a developer volunteering their own number, and
none has.

The closest published figures are reader polls that do not answer the
question. A TidBITS poll of iPhone 15 Pro owners found 33% use the Action
Button for Ring/Silent, 21% Camera, 20% do not use it at all, and **no
third-party-app option was offered**. Do not quote them as adoption.

Apple's own attention is receding on a measurable curve: an entire WWDC24
session on controls, no controls chapter at WWDC25, and the string
"control" appearing zero times in the WWDC26 WidgetKit session.

## Also still missing

- Any developer's before and after numbers for an **Apple Design Award**.
- Per-feature-type download data after 2018.
- Any modern one-off **price elasticity** study. The only systematic one
  is from 2015.
- Any published measurement of **App Intents** driving installs, opens or
  retention.
- Any **easter egg with a number attached after 2009**. There is exactly
  one datapoint, PCalc's day-one sales tripling, and the developer partly
  retracted it in the same post and attributes it to a press release he
  wrote rather than to organic discovery.
- **Localisation with both a delta and a maintenance cost**, from a named
  indie iOS developer. Three partial accounts exist and each is
  confounded, on the wrong store, or twelve years old.

## One gap that closed

- The **Featuring Nominations form** now has a firsthand account. The
  developer of Steptastic reports being "very lucky to get nominated on
  my second time", featured in the German App Store apps and games tab
  for about two weeks. Notable operational detail: the dashboard only
  ever showed the nomination as 'accepted', which "doesn't indicate
  whether it actually WILL be nominated", and he received no App Store
  Connect notification that the app had been featured.

  What it did is the more useful half, and it matches Slopes: **impressions
  went from about 150 a day to about 43,000, and conversion fell from
  about 12% to about 0.1%.** Downloads rose and he published no download
  number. A feature is a spike in impressions before it is a spike in
  anything else.

## Two things widely cited that do not say what people think

- **"Slopes Diaries #19: App Store Review Replies"** is linked everywhere
  as evidence that replying to reviews works. It is entirely qualitative.
  The only figure in it is "around 700 reviews". No rating change, no
  reply count, no outcome.
- **Focus Friend's number one App Store run** is cited as proof of
  organic virality. It was a creator partnership: 20,000 downloads in
  week one, driven by a Hank Green community post, with no paid
  acquisition. A real and repeatable strategy, and not the one it is
  being used to evidence.
