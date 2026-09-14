# Widgets, Live Activities, App Intents and Controls

These get recommended constantly and measured almost never. This file is
what can actually be shown, which is less than the internet claims, and
what can be argued from Apple's own documentation, which is more useful.

## First, the honest position on widgets

An earlier version of this skill said: if you build one thing, build the
widget. That was overclaimed and here is the correction.

- **There is still no iOS widget retention study.** Apple has never
  published a retention number. RevenueCat's State of Subscription Apps,
  2023 through 2026, contains nothing on widgets at all. No named iOS
  developer has published retention for widget users against non-widget
  users.
- **The only retention case study is Android**: Google's DevRel wrote up
  Gratitude at **25% higher retention for widget users**, with **10% of
  DAU adopting the widget**. It is correlational with no holdout, and the
  10% is the more useful figure because it bounds the ceiling.
- **Adoption for an ordinary app is low.** A TidBITS reader poll, which
  is a sample of Apple enthusiasts and therefore an upper bound, found
  only **14% use iPhone widgets heavily**, and "don't use" was the single
  most common answer for the Home Screen, the Lock Screen and Today View
  alike.
- **Adoption for a widget-first app is a different number entirely.**
  Glow, an affirmations app whose own framing is "what if the widget is
  the app", published **80.7% of users installing at least one widget**.
  Self-reported, no sample size, and a ceiling rather than a benchmark.
  The gap between 14% and 80.7% is the whole point: **adoption is a
  function of whether the widget carries the value, not of whether you
  shipped one.**

So: a widget is worth building, and the reason is not a retention
percentage. It is that a widget is one of very few ways to be present
without being opened, and for a visual app it is the artefact loop. If
the widget is incidental, build it for the 10 to 14% who will use it and
accept that it is a minority. If the widget can be where the value
actually lives, the ceiling is far higher, and that is the play worth
choosing deliberately.

Every number you will find asserting otherwise is in
`numbers-that-are-not-real.md`, because several of them are invented.

## The measurement problem, which explains the absence

App Store Connect Analytics has **no share-extension-source dimension, no
Spotlight-origin dimension and no control-adoption dimension.**
`ControlCenter.currentControls()` reports only to the owning app, so
control adoption is unknowable across apps by construction.

**Widgets are the exception, and this corrects an earlier version of this
file.** Apple ships a **Home Screen Widget Installs** analytics report,
with data available from iOS 17.4, alongside
`WidgetCenter.getCurrentConfigurations`. So widget adoption *is*
measurable, and every developer shipping a widget can see their own
number.

Almost none publish it. Two do: Glow at **80.7% of users installing at
least one widget**, which is a widget-first app and therefore a ceiling
case, and Overcast at **over 10,000 configured widgets** two weeks after
shipping, with no denominator given. Nobody has published a retention
comparison at all.

Note also that the "~10%" widget figure attributed to Apple is not a
statistic. It is boilerplate arithmetic in that report's documentation,
where 10 and 100 are placeholder device counts, and the identical
sentence appears on unrelated report pages.

So for the other surfaces there is no data because almost nobody can see
whether they work. For widgets there is no data because almost nobody
says. **Argue all of them from documented mechanism, never from a
retention percentage.**

## The honest argument for all of them

iOS push notification opt-in for Utilities is **51.6%** (Games 20.6%).
About half your users will never grant push.

Widgets, Live Activities, App Shortcuts and Controls are the only
re-engagement surfaces that **do not require a permission**. That is the
real case, and it does not need a made-up number.

## Widget Suggestions: the documented free real estate

The one genuine discovery mechanism here, and Apple documents it:

> if someone hasn't configured a matching widget in a Smart Stack, the
> system can automatically suggest your widget... This process increases
> the visibility of your widget

You get it by donating `PredictableIntent` app intents. Two hard traps:

- A `TimelineEntryRelevance` score of **0 or lower means WidgetKit will
  never rotate your widget to the top**. A default you did not set is a
  widget nobody sees.
- **iPhone and iPad Smart Stacks ignore the `relevance()` callback
  entirely.** That is watchOS only. Plenty of code has been written
  against it that does nothing.

## App Shortcuts work before first launch

The strongest discovery claim on the platform, and it is Apple's own:
App Shortcuts are **"available immediately when installation finishes"**
and are **"featured prominently when searching in Spotlight"**. Cap of
ten per app.

That is a surface where your app does something for somebody who has
never opened it.

**Three rules that silently exclude your intent from Spotlight**, any one
of which is enough:

1. The parameter summary omits a required parameter that has no default
2. `isDiscoverable` is false, or `assistantOnly` is true
3. It is a widget-configuration intent with no perform method

Most apps that believe they have "adopted App Intents" are invisible for
one of those three, and nothing warns you.

Note also that iOS 26 shifts the recommended path from individual App
Shortcuts towards **app schema domains**, which let Siri surface features
contextually without adopting shortcuts one by one. The Mail, Clock and
Messages domains are all-or-nothing; Xcode fails the build otherwise.

## Live Activities

- **The only measured outcome anywhere is Uber's**: 2.26% fewer driver
  cancellations, 2.13% fewer rider cancellations, 1.06% fewer pickup
  defects. Uber also documents that Live Activities have **no native
  analytics** and that they had to build regression baselines to see
  anything at all.
- **One Live Activity ships to seven surfaces**: Lock Screen, Home
  Screen, Dynamic Island, StandBy, the Mac menu bar, the Watch Smart
  Stack and the CarPlay Dashboard. That leverage is the argument.
- **Apple forbids using them for growth**, in as many words: "Don't use a
  Live Activity to display ads or promotions." They are for something
  happening now, with an end.

## Control Center controls

Be sceptical. Two years on there is **zero public telemetry** from Apple,
any vendor, or any developer. Apple's own attention is receding: an
eighteen minute session at WWDC24, ninety seconds at WWDC25, and no
mention at all in the WWDC26 WidgetKit session. The Human Interface
Guidelines page for Controls has one changelog entry: "New page."

And they cannot be an acquisition channel by construction. Adoption is
entirely user-initiated, there is no gallery search or ranking, and the
HIG explicitly says to avoid content that repeats the guidance already in
Settings for the Action button.

Build one if it genuinely helps your users. Do not build one for growth.

## The share sheet, which does have a documented lever

Donate `INSendMessageIntent` from **both the app and the extension**. The
share sheet "suggests conversations with people in apps that a person
interacts with frequently", and providing an image of at least 360px
improves how your entry presents.

Spotlight has exactly one developer-controlled ranking lever:
`associateAppEntity(_:priority:)`. Apple says "Spotlight elevates items
with higher priority values." That is the entire published surface area.
