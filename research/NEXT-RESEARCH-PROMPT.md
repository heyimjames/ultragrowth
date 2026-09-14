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
Same sources. App Store Connect has no share-extension-source dimension,
so anybody with a number built their own attribution and will probably
say how. Specifically worth chasing:

- Apps whose main input is the share sheet (read-later, save-links,
  clipboard, screenshot tools) and whether any has published where their
  installs come from
- Whether a **watermark or a "made with" mark on an export** measurably
  drives installs, and at what cost in resentment. Everyone has an
  opinion; find somebody who measured
- **App Clips** as the "value before install" version of this, which has
  been shipping for five years with almost no published results
- Whether **Universal Links** versus a bare App Store link changes
  install rate for a shared artefact

**3. Activation rates for utilities.** Install to first successful use,
and what moved it. Two firsthand numbers exist so far. More would make
this section real rather than illustrative.

**4. Apps that grew primarily through App Store search**, with the
before and after. The skill claims search is the channel for utilities
and currently supports that with Apple's own 65% figure rather than with
a developer's story.

**5. Custom Product Pages, from developers rather than vendors.** Every
CPP number in circulation, including the ones in this skill, comes from a
company that sells ASO tooling. Find a named developer who shipped CPPs
and published their own before and after. Also: does anybody use more
than a handful of the 70 available, and what happens to the ones you make
and forget?

**6. Control Centre controls and the Action Button.** Two years after
launch there is **zero public telemetry** on controls from Apple, any
vendor, or any developer, and Apple's own attention is visibly receding.
So the questions are:

- Has **any** developer published a control adoption number, even an
  order of magnitude
- Has anybody measured whether shipping a control changed anything
- Same for the Action Button: is there a single published figure on how
  many users assign a third-party app to it
- If the answer to all of the above is nothing, say so clearly. A
  confident "nobody knows" is a useful thing for a skill to be able to
  say about a feature people keep being told to build

**7. Hidden features and easter eggs as a distribution mechanism.** This
is the most speculative item here and possibly the most interesting,
because almost nobody treats it as growth.

The pattern: a feature you can only find by being told about it. Tapping
a version number several times. A long press that does something
unexpected. A konami code. Android made this canonical by hiding
developer options behind seven taps on the build number, and people still
tell each other how to do it fifteen years later.

The question is whether that is a real loop for a small app. It is
plausible that it is: a secret is one of very few things people
voluntarily tell other people about a utility, and "did you know if
you..." is word of mouth that costs nothing and asks nothing.

What to look for:

- Any developer who has said a hidden feature drove discovery, shares,
  or a Reddit or X thread that produced installs
- Apps where an easter egg was itself covered by press
- Whether anything is measurable at all, given the thing is by definition
  undiscoverable to analytics until somebody finds it
- The counter-argument, honestly: is there evidence that hidden features
  mostly go unfound and are therefore wasted effort
- Adjacent and better documented: **App Store Connect offer codes and
  promo codes shared in communities**, which are the sanctioned version
  of the same "insider" feeling

Expect this one to come back thin. If it does, say so, and say what the
strongest anecdote you found was, because a good anecdote is worth having
even when there is no number behind it.

**8. Non-English and non-US markets.** Almost all of this research is
US and UK. Any firsthand account of localisation producing measurable
growth, and what it cost to maintain.

**9. Recent App Store policy changes that affect discovery**, from 2026
onward: Apple Intelligence and Siri app-schema domains, App Store Tags in
practice, the two-ads-per-query change, anything about apps being removed
for inactivity. Prefer Apple's own words and developers' observed
effects.

## What blocked us, so you do not rediscover it

Two passes hit these walls. If you have a browser, a paid account, or a
transcription tool, you can get past several of them, and that is most of
the remaining value in this brief.

**Hard-blocked to automated fetching:**

| Source | What happened |
| --- | --- |
| `relay.fm` | 403 to fetchers. Hosts Under the Radar, the likeliest single home for indie widget numbers |
| `launched.fm` | Connection refused |
| `david-smith.org` | 403. David Smith ships more widgets than almost anybody and has published 131M lifetime downloads but no widget figure |
| `jordibruin.com` | Connection refused |
| Apple Podcasts episode pages | 404 to fetchers |

**Never attempted, because we could not:**

- **Podcast audio itself.** Every finding so far came from show-note
  writeups, which are summaries written by the host's marketing, not
  transcripts. The numbers developers say out loud in interviews are, as
  far as we can tell, the largest untapped source in this whole field.
  If you can transcribe, start with Under the Radar and Launched.
- **Paywalled newsletters.** Sub Club members' posts, Mobile Dev Memo's
  paid tier, Appfigures' subscriber data.
- **Conference talk video.** Deep Dish Swift, iOSDevUK, NSSpain, Swift
  Island, Do iOS. Slides sometimes carry numbers that never make it into
  a blog post.
- **Private communities.** iOS Folks, Indie Dev Slack, the RevenueCat
  and Superwall Slacks. Numbers get posted there that are never published
  anywhere public. Obviously do not scrape them; but if you are a member,
  it is the place to ask.
- **Just asking.** No pass has tried simply emailing or posting to a
  developer and asking "what share of your users have the widget
  installed?" For a question nobody has answered publicly, that may well
  be cheaper than any amount of searching.

**One budget note:** the second pass exhausted its web-search allowance
and finished on direct URL fetches only, which meant discovery stopped
and it could only follow links it already had. If your tooling has a
similar cap, spend it on discovery early and leave fetching until last.

## Output

Markdown. One section per topic above. Within each, bullets where every
bullet is a specific claim plus the number plus the URL. Then:

- **Nothing found**: the topics that yielded nothing, stated plainly
- **Fabrications traced**: widely-repeated numbers that are not at their
  cited source, named individually with URLs
- **Conflicts**: where credible sources disagree, with both numbers
- **Conflicts of interest**: who published what and what they sell

Under 1,200 words. Fifteen well-sourced specifics beat sixty soft ones.
