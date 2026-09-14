# Store search

65%+ of downloads begin here. For a utility with no ad budget this is not
a channel, it is the channel.

## What Apple actually says it ranks on

Apple's complete stated list, from the discoverability page:

> text relevance (matches for the app's **title, keywords, and primary
> category**) and customer behaviour (**downloads and the number and
> quality of ratings and reviews**)

That is the whole of it. Worth noticing what is **not** named: subtitle,
description, retention, crash rate, uninstalls. Most ASO writing asserts
several of those confidently. Apple does not.

So:

1. **App name** (30 chars). Named by Apple. Brand alone ranks for the
   brand alone; `Brand: Category Noun` ranks for what people type.
2. **Keyword field** (100 chars). Named by Apple. Not shown to anybody.
   Comma separated, **no space after commas**, singular only (Apple
   stems), no competitor trademarks.
3. **Primary category.** Named by Apple, and the one people forget is a
   ranking input at all rather than just a shelf.
4. **Subtitle** (30 chars). Widely believed to be indexed and widely
   observed to behave as if it is. Apple has never said so. Write it as
   though it counts, because the evidence suggests it does, but do not
   build a strategy that only works if it does.

**Promotional text is not a ranking field and Apple says so outright:**
"Promotional text doesn't affect your app's search ranking so it should
not be used to display keywords." It is a conversion asset you can change
without a new version. Use it that way.

The description is a conversion asset too. Apple's own two pages are
inconsistent about whether it is indexed at all, and Apple separately
warns against stuffing it. Write it for a human who is already half
convinced.

## Repetition: within, not between

The rule is **repetition is bad within a localisation, not between
them**. Do not spend a keyword on a word already in your name in the same
locale. Do repeat freely across locales, because each is a separate
index.

## Combinations are free

Apple builds phrases across your fields. If the name has "Split-Flap" and
the keyword field has "departure", you rank for "split flap departure"
without spending characters on it. So never repeat, and choose words that
combine.

## Category

Pick where you can rank, not what describes you. Top 10 in a narrow
category beats 80th in a broad one, because category browsing converts
and page 4 does not exist.

## Locales are separate indexes, and they stack

English-only apps should still fill the **en-GB** keyword field. It is a
separate index, usually empty, and it is the fallback for most non-US
English storefronts: Ireland, India, Singapore, South Africa and New
Zealand, not only the UK.

Better than that: **storefronts index secondary locales as well as their
own.** The US storefront indexes nine secondary locales (es-MX, ru,
zh-Hans, zh-Hant, ar, fr, pt-BR, vi, ko) on top of en-US, which is 160
indexable characters per locale of extra surface. The UK's secondary
locale is **en-AU**; Australia's is **en-GB**. So for an English-only
indie app, filling en-GB and en-AU is the version of cross-localisation
with **no conversion risk**, because nobody ever sees a listing in a
language they do not read.

The one limit: **phrases only form within a single locale.** Apple will
combine your words into search phrases inside en-GB, but it will not
build a phrase from one word in en-GB and another in en-AU. Each locale
has to make sense on its own.

The cost, which the usual advice omits: screenshot sets hang off the
version localisation, so each locale you add is a screenshot set you must
upload and keep in step. Add en-GB, then add others only if the rank data
justifies the maintenance.

## Measuring it

App Store Connect → Analytics → Acquisition shows impressions and
conversion split by **search vs browse vs referral**. If search
impressions are low, that is a keyword problem. If they are high and
conversion is low, that is a product page problem. They are different
problems and mixing them up wastes months.
