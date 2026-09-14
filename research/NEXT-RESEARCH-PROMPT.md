# Research brief: firsthand iOS growth numbers

Paste this into any AI with web access. It is self-contained.

---

You are researching for a public Claude skill called **ultragrowth**
(github.com/heyimjames/ultragrowth), about growing iOS apps that are
**not** viral teen social apps: utilities, tools, professional apps, paid
apps, indie apps.

Two research passes are already done. Your job is the third, and it is
narrower and harder than the first two, because the easy sources are
exhausted.

## The standard, which matters more than the coverage

- **Primary sources only.** A developer's own blog, their own podcast
  appearance, their own conference talk, their own App Store Connect
  screenshot. Not an agency summarising one, not an SEO listicle, not
  "studies show".
- **Every claim needs a number and a URL.** A claim without a number is
  not a finding.
- **"Nothing found" is a valuable result.** Say it plainly and move on.
  The skill already has a file called `what-nobody-has-measured.md` and
  adding to it honestly is worth more than a soft claim.
- **Flag fabrications by name.** If a widely-repeated statistic traces
  back to a page containing no figures, say so and give the URL. The
  previous passes found several and this is the most valued output.
- **Note conflicts of interest.** Most app data comes from vendors,
  because vendors have the aggregate. That does not make it wrong. Note
  which direction the error would run if there were one.
- **Density over prose.** It goes straight into a skill file.

## Already covered. Do NOT re-research any of this

Apple Search Ads CPI benchmarks by category and the break-even
arithmetic against RevenueCat's revenue-per-install medians. Editorial
featuring criteria, lead times, the Featuring Nominations form limits,
and the Slopes App-of-the-Day numbers. Custom Product Pages, Product Page
Optimization, App Store Tags, keyword-assignable CPPs. Apple's stated
search ranking factors and the fact that promotional text is excluded.
Cross-localisation and which storefronts index which secondary locales.
StoreKit review-prompt caps and behaviour, the native prompt's
rating-versus-review split, reply rates by category. Paid-upfront market
share, lifetime-versus-subscription revenue per install, the Dark Noise
paywall experiment, Halide's revenue split and launch-week share. Widget
adoption being unmeasured on iOS and the Android Gratitude case study.
Live Activities at Uber, Widget Suggestions, App Shortcuts before first
launch, Control Center's absent telemetry. Shot Pattern, Short Circuit,
Sequel, Sindre Sorhus, Natal, Visible, Plinky, Focus Friend.

## What to find, hardest and most valuable first

**1. Firsthand iOS widget numbers.** The single biggest hole. The entire
internet asserts widgets drive retention and no named iOS developer has
ever published adoption share or a retention delta. Two passes have
checked blogs. **The unexplored layer is podcast audio and video**: Under
the Radar, Core Intuition, Launched, Sub Club, Swift over Coffee,
Stacktrace, and conference talks from Deep Dish Swift, iOSDevUK, NSSpain,
Swift Island, Do iOS. Look for transcripts, auto-captions, YouTube
transcripts, and Patreon or member-only show notes. Any developer saying
"X% of our users have the widget installed" is a genuinely new fact.

**2. Share sheet and export-to-install numbers.** What share of a
utility's installs came from somebody receiving an exported artefact.
Same sources. Note that App Store Connect has no share-extension-source
dimension, so anybody with a number built their own attribution and will
probably say so.

**3. Activation rates for utilities.** Install to first successful use,
and what moved it. Two firsthand numbers exist so far. More would make
this section real rather than illustrative.

**4. Apps that grew primarily through App Store search**, with the
before and after. The skill claims search is the channel for utilities
and currently supports that with Apple's own 65% figure rather than with
a developer's story.

**5. Non-English and non-US markets.** Almost all of this research is
US and UK. Any firsthand account of localisation producing measurable
growth, and what it cost to maintain.

**6. Recent App Store policy changes that affect discovery**, from 2026
onward: Apple Intelligence and Siri app-schema domains, App Store Tags in
practice, the two-ads-per-query change, anything about apps being removed
for inactivity. Prefer Apple's own words and developers' observed
effects.

## Output

Markdown. One section per topic above. Within each, bullets where every
bullet is a specific claim plus the number plus the URL. Then:

- **Nothing found**: the topics that yielded nothing, stated plainly
- **Fabrications traced**: widely-repeated numbers that are not at their
  cited source, named individually with URLs
- **Conflicts**: where credible sources disagree, with both numbers
- **Conflicts of interest**: who published what and what they sell

Under 1,200 words. Fifteen well-sourced specifics beat sixty soft ones.
