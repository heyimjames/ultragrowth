# Actually changing the listing

Every ASO guide tells you what to put in the fields. None of them tell
you that most of the time you cannot put anything in the fields at all.
This is the part you only learn by trying, usually on the afternoon you
had set aside for something else.

## You cannot edit metadata without an editable version

Keywords, subtitle, name, description and screenshots all hang off an App
Store **version**, and a version is only writable while it is in
`PREPARE_FOR_SUBMISSION`. If everything you own is live
(`READY_FOR_SALE`) or queued (`WAITING_FOR_REVIEW`), every write is
refused:

```
Attribute 'keywords' cannot be edited at this time
The field 'subtitle' can not be modified in the current state
```

So ASO is **gated on your release cycle**. You cannot decide on a Tuesday
to fix your keywords. You create the next version, change the metadata as
part of it, and it goes through review with the build.

Plan for it: keep a staged file of the keyword and subtitle strings you
intend to use, rule-checked and character-counted, so that the moment a
version opens it is a paste rather than an afternoon.

## Probe before you write

To find out whether a field is writable without risking anything, PATCH
it with **its own current value**. A no-op write returns either success,
which tells you the field is open, or the exact error, which tells you
why it is not. Nothing changes either way.

Do this before any bulk edit. It costs one request and saves discovering
the state halfway through a sequence of writes.

## AppInfo is app-wide, not per-platform

The **name, subtitle and category** live on an `AppInfo` record that is
shared across iOS, macOS and tvOS. The per-version localisation carries
keywords, description and screenshots.

The consequence is nasty and easy to miss: if any platform has a
submission in review, it is holding the editable `AppInfo`, and editing
your subtitle folds a metadata change into **that review**. A multi
platform app therefore cannot safely change its name or subtitle while
any one of its platforms is queued.

Check every platform's state before touching `AppInfo`, not just the one
you are thinking about.

## Adding a locale costs screenshots

The advice everywhere, including elsewhere in this skill, is to fill the
`en-GB`, `en-AU` and `en-CA` keyword fields because they are separate
indexes and usually empty. True, and the cost is never mentioned:

**Screenshot sets hang off the version localisation.** Create an `en-GB`
localisation and you must upload or copy a screenshot set for it, or the
version fails submission validation. Three new locales is three new
screenshot sets to keep in step forever.

So it is usually right to add **en-GB only**, and only then the others if
the data justifies it. Which brings us to:

## en-GB is much bigger than Great Britain

`en-GB` is the fallback for most non-US English storefronts: Ireland,
India, Singapore, South Africa, New Zealand and more. `en-AU` and `en-CA`
cover one country each.

If you are going to maintain exactly one extra English locale, it is
`en-GB`, and it is not close.

## Measure rank per term per storefront

You are not ranked. You are ranked *for a term, in a storefront*, and the
two can disagree wildly. A real example from a six-day-old app:

| Term | US | GB |
| --- | --- | --- |
| split flap | 37 | 15 |
| the brand name | not found | 16 |
| departure board | not found | 93 |
| flip clock | not found | not found |

Three separate lessons in one table. The app was doing far better in GB
than the US, which is an argument for where to spend the one extra
locale. It did not rank for its own brand name in the US, which for a
six-day-old app usually means the index is still settling rather than
that anything is wrong. And **"flip clock" ranked nowhere in either
storefront** for an app that does exactly that, which is the most
valuable line in the table: an uncontested term you already deserve.

Run this before writing keywords, not after. The gaps are the brief.

## The subtitle is 30 characters and most of them get wasted

Common failure, seen in the wild: an app named "Clack Board" with the
subtitle "A split-flap board, on screen".

Six of thirty characters go on *board*, which is already in the name and
therefore already indexed. "A" and "on" are filler that index nothing.
Nearly a third of the field is doing no work.

Replacing it with "Split-flap departure display" frees those characters
and buys *departure* and *display*, which then combine with the *board*
already in the name to give "departure board", "flap display" and "split
flap display" without spending anything further.

Rules, then:

- Never repeat a word from the name
- No articles, no prepositions, no punctuation you do not need
- Prefer nouns people type over adjectives that describe you
- Remember Apple builds phrases across name, subtitle and keywords, so
  every word you place is also every combination it can form
