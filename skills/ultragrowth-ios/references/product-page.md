# The product page

Default App Store product pages convert at about **1.6%**. Every
improvement here multiplies everything you do upstream.

## Screenshots

- The **first two** are what most people see, in the search results, at
  thumbnail size, without tapping. They are the advert.
- **Caption them.** A bare screenshot of your interface tells somebody
  that it is a screenshot of your interface. A caption tells them why
  they would want it.
- Size the caption for the thumbnail, not for the file you are looking
  at. Text that looks absurdly large in Figma is usually about right.
- Portrait apps: 6.9" and 6.5" are the required sets. Apple scales down.
- The **app preview video** autoplays muted. It must work with no sound
  and be comprehensible in three seconds.

## Custom Product Pages

Up to **70** of them. Apple's own figure: referring people to a CPP gives
a **2.5 percentage point** lift on average, which against a 1.6% baseline
is a **156% increase**.

- One per *reason somebody wants the thing*, not one per feature
- Since July 2025 you can assign keywords from your keyword field to a
  specific CPP, so a search for a specific need lands on the page about
  that need
- Each keyword combination must be unique to one page
- They have their own URLs, so use them for every campaign, newsletter,
  and press link, which also gets you per-source conversion data for free

## Product Page Optimization

Apple's built-in A/B test. Up to three treatments against the default,
free, with real traffic and real significance. Most developers never
enable it. Test the first screenshot before anything else.

## Ratings

- Zero ratings costs about **two thirds** of conversions. Target 4.4+.
- Prompt at a moment of success. Apple's own warning: "people may even be
  more likely to leave negative feedback if they feel an app is asking
  for a rating before they get a chance to use it."
- **StoreKit caps it at three prompts per person per year**, and the cap
  is enforced by the system whether or not you know about it.
- **The trap that wastes your testing**: the request is a **silent no-op
  in TestFlight** and **always fires in debug**. So it never appears
  where you test, and always appears where you develop, which is the
  wrong way round. Instrument "attempted" separately from "shown" or you
  cannot tell what happened in the wild.
- Apple's HIG also asks for **a week or two between requests**, which
  almost nobody implements.
- **The native prompt is a rating machine and an anti-review machine.**
  One study: 13.5% of prompted people left a rating, averaging 4.7 stars,
  and **0.07% left a written review**. One-star raters wrote reviews at
  12.2%; five-star raters at 0.05%. So the prompt lifts your average and
  will not fill your page with words, and the words you do get skew
  angry. Both facts are useful and neither is obvious.
- **Reply to reviews.** Replies are retroactive to any review ever left,
  and Apple notifies the reviewer with an option to update their rating.
  Only **12% of Productivity apps reply**, against 51% in Finance, so it
  is a cheap differentiator as well as the right thing.
- **Never reset your summary rating** as a small app. It does not remove
  written reviews, it stamps a "recently reset" notice on your page, and
  it cannot be undone.
- **Ratings are per-territory.** A US and a UK visitor see different
  averages for the same app.
- The governing guideline is **5.6.1**, which disallows custom review
  prompts. Gating a feature behind a review is **3.2.2(x)**. Manipulating
  ratings is **3.2.2**, and the penalty is expulsion from the Developer
  Program.
