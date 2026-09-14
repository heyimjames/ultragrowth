# ultragrowth

A growth playbook for iOS apps that are **not** viral teen social apps.

<p align="center">
  <a href="#install"><img src="https://img.shields.io/badge/install-npx%20skills%20add%20heyimjames%2Fultragrowth-000?style=for-the-badge&logo=npm&logoColor=white" alt="Install with npx skills"></a>
  <a href="https://github.com/heyimjames/ultragrowth/stargazers"><img src="https://img.shields.io/github/stars/heyimjames/ultragrowth?style=for-the-badge&color=000&logo=github&logoColor=white&label=Star" alt="Star this repo"></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-000?style=flat-square" alt="MIT"></a>
</p>

---

## The problem this exists for

Almost all published app-growth advice is about one kind of app: a free
social product for teenagers, whose value comes from other people being
on it. That advice is excellent, and it is *specific*.

Applied to a paid utility, a professional tool, or a game, it is not
merely useless. It is actively misleading, because it tells you to
optimise a loop your product does not have. You end up building invite
mechanics nobody uses while the thing that would actually work — being
findable in a search — goes untouched.

## The idea

Brian Balfour's point, which this hangs on: you need **product-channel
fit**, and the channel is not a free choice. It follows from how people
naturally discover, evaluate and buy a thing like yours.

So the skill starts with one question:

> **Where does the value come from, the first time somebody opens it?**

| Answer | Shape | Growth actually comes from |
| --- | --- | --- |
| Other people already being there | Network | Invitations |
| It doing a job, alone, immediately | **Utility** | App Store search, overwhelmingly |
| A library to read or watch | Content | The open web |
| Making somebody better at their work | Professional | The trade's own channels |
| Play | Game | Paid acquisition and creators |

Everything after that is organised by shape, with the tells for having
guessed wrong.

## What is in it

Numbers rather than vibes. Every benchmark is cited:

- The default App Store product page converts at about **1.6%**
- Custom Product Pages lift that by around **156%**, and you get **70** of them
- **65%+** of downloads begin with a store search
- Zero ratings costs roughly **two thirds** of your conversions
- Hard paywalls convert about **5x** freemium, with similar long-term retention
- Median subscription app grew MRR **5.3%** year on year. The top decile grew **306%**
- New subscription apps launched per month went from ~2,000 to **~15,000** in three years

That last one is the whole argument. Being good is table stakes now.
Being *findable* is the work.

## The loop a utility actually has

The usual conclusion about non-social apps is that they have no growth
loop and must buy every user forever. That is wrong, and the correction
is the most useful idea in the skill:

> **A utility's loop is not an invitation. It is an artefact.**
>
> The app makes something that leaves the app, and that thing is seen by
> somebody who does not have the app.

A widget on a Home Screen is seen by everybody who looks at that phone,
and it costs the user nothing, because the distribution is a side effect
of the product working. An export that carries its origin. A shared link
that renders something real for somebody who has installed nothing.

Which is also why the advice is: build the widget, and make it look like
nothing else. A widget that looks like every other widget is not an
artefact, it is furniture.

## And the half nobody writes down

Every ASO guide tells you what to put in the fields. None of them mention
that most of the time you cannot put anything in the fields at all:
keywords and subtitles are only writable while a version sits in
`PREPARE_FOR_SUBMISSION`, so ASO is gated on your release cycle rather
than on when you feel like doing it.

`references/operating-the-listing.md` is that half. How to probe whether
a field is writable without risking anything. Why a subtitle change on a
multi-platform app can fold itself into a review happening on a platform
you were not thinking about. Why adding a locale costs you a screenshot
set forever. And why "you are ranked" is the wrong sentence, because you
are ranked for a term, in a storefront, and the two disagree.

## Install

```bash
npx skills add heyimjames/ultragrowth
```

Or copy `skills/ultragrowth-ios/` into `~/.claude/skills/`.

## Use

Ask any question about growing an app and the skill will work out which
shape you have before answering. Or invoke it directly:

```
/ultragrowth-ios
```

It is most useful pointed at a real listing: give it your App Store ID
and ask what is wrong.

## It also tells you which numbers are made up

App-growth writing is an SEO battleground and a lot of its statistics are
laundered. One reference file exists only to list the ones that were
chased to their supposed source and are not there: "widget users have 15%
higher retention" (the cited page contains no figures at all), "0.3%
Spotlight click-through" attributed to a company whose two posts on the
subject contain no statistics, "apps need 4.5 stars to be featured",
which Apple has never said.

It also separates those from numbers that are real but far weaker than
their reputation, and from places where credible sources simply disagree
by a factor of two.

The habit it argues for: before planning around a number, find the
primary source, check the sample and the year, and check whether whoever
published it sells the thing the number recommends.

## Sources

- Brian Balfour, [*Four Fits for $100M+ Growth*](https://brianbalfour.com/four-fits-growth-framework)
- RevenueCat, [*State of Subscription Apps 2026*](https://www.revenuecat.com/state-of-subscription-apps) — 115,000 apps, $16B revenue
- Apple, [*Custom product pages*](https://developer.apple.com/app-store/custom-product-pages)
- Nikita Bier, for the Network shape, which this skill deliberately does not duplicate

## Licence

MIT. Do what you like with it.
