# Growth loops for apps nobody invites anybody to

A social app grows because using it requires other people. That is a
loop, and it is the only loop most growth writing describes.

A utility has no such requirement. Somebody uses a scanner alone, a
weather app alone, a board on their own desk. So the usual conclusion is
that utilities have no loop and must buy every user forever.

That is wrong, and the correction is the most useful idea in this file:

> **A utility's loop is not an invitation. It is an artefact.**
>
> The app makes something that leaves the app, and the thing it makes is
> seen by somebody who does not have the app.

Everything below is a way of making that artefact, or of making it
travel. If your app produces nothing that anybody else ever sees, you do
not have a loop, and you should stop looking for one and go and be very
good at search instead.

---

## THE FIVE ARTEFACT LOOPS

### 1. The visible surface

The strongest and the most skipped. A widget on a Home Screen, a Lock
Screen complication, a wallpaper, a screen saver, a Watch face, a board
on a desk. These are seen by **everybody who looks at that device**, and
a phone is looked at by other people constantly.

- It costs the user nothing. There is no share action, no decision, no
  moment where they weigh whether to bother. The distribution is a side
  effect of the product working.
- It only works if the surface is **distinctive at a glance**. A widget
  that looks like every other widget is not an artefact, it is furniture.
- Design the widget to be *recognised*, not merely to be useful. Somebody
  has to be able to ask "what is that".

Build the widget, and make it look like nothing else. But be honest about
the size of the prize: **there is no iOS widget retention study at all**,
Apple has never published an adoption number, and the best reader survey
available found only about 14% use widgets heavily. The reason to build
one is not a retention percentage, it is that it is one of very few ways
to be present without being opened. See `platform-surfaces.md`, including
the several invented statistics circulating on this exact topic.

### 2. The export

Anything the app produces that can be sent: an image, a PDF, a file, a
link, a calendar event. The question is not whether you have export, it
is whether the exported thing **carries its origin**.

- A tasteful mark is worth real installs. An ugly watermark is worth
  resentment and a workaround.
- Better than a watermark: make the export *so characteristic* that the
  format is the advertisement. Nobody watermarks a split-flap board.
- Export must be **one action from the thing being exported**, not four
  taps into a menu. Every step halves it.

### 3. The link that works without the app

A shared link that renders something real for somebody who has not
installed anything is worth an order of magnitude more than one that
opens the App Store.

- Give the recipient the **value first** and the install prompt second.
- Open Graph images are the whole of this on the web. A link that unfurls
  into the actual thing is doing your marketing in every group chat it
  lands in.
- Universal Links so the app opens if they have it, the web view if not.

### 4. The multiplayer edge

Most utilities have exactly one place where a second person is natural,
and it is usually small: a shared list, a shared board, a handoff, a
"send this to someone". It is rarely the point of the product and it is
often the only loop it has.

Find that one edge and make it excellent. Do not bolt on a social layer
around a solitary product; nobody wants a feed in their scanner.

### 5. The other device

The same person on a second device is not new revenue, but it is
retention that looks like growth and it seeds the visible surface
elsewhere. Mac plus iPhone plus Watch plus TV, one purchase, syncing
quietly, is a real moat for a small app and a thing big competitors
frequently cannot be bothered to do.

---

### The sixth, which is unproven and worth thinking about anyway

**A secret is one of very few things people voluntarily tell each other
about a utility.**

Nobody says "you should get this scanner app". Plenty of people say "did
you know if you tap the version number five times". Android made this
canonical by hiding developer options behind seven taps on the build
number, and people are still telling each other how to do it fifteen
years later, entirely unprompted, at no cost to Google.

The mechanism is real: a hidden feature converts a user into somebody
with a piece of information worth passing on, which is exactly what an
invitation is, minus the asking.

**Nobody has measured it**, and by its nature it is awkward to measure:
the thing is undiscoverable to your analytics until somebody finds it,
and the telling happens somewhere you cannot see. Treat this as a reason
to make something delightful rather than as a growth tactic with a
number behind it.

If you do it: the secret has to be **findable by a curious person and
invisible to everybody else**, it should reward rather than merely
unlock, and it must never be the only route to something people need.

## ACTIVATION: THE NUMBER MOST SMALL APPS NEVER DEFINE

Between "downloaded" and "user" there is a specific event, and if you
cannot name it you cannot improve it.

Write the sentence: **"Somebody is a real user of this app once they have
______, at least once."** Scanned a document. Written on the board.
Created a project. Got a result.

Then measure the share of installs that reach it in the first session.
That number, and not downloads, is what your onboarding is for.

Two rules that follow:

- **Nothing may stand between the install and the activation event.** Not
  a sign-up, not a permission you do not yet need, not a paywall, not a
  tour. Ask for the camera permission when they tap the camera.
- **Deliver value before asking for investment.** Every source from Bier
  to enterprise PLG agrees on this. They disagree only on how much value.

---

## PAYWALLS, TACTICALLY

The strategy is in `pricing.md`. This is the mechanics.

### Placement

| Pattern | When it is right |
| --- | --- |
| **Hard paywall at launch** | The value is obvious from the store listing. Converts about 5x freemium with similar long-term retention |
| **After activation** | The value has to be felt to be understood. Let them do the thing once, then ask |
| **At the limit** | Metered use: three scans, then pay. Works when the limit is generous enough to prove the thing |
| **Feature gate** | Weakest for a utility. Splits your product into a good one and a worse one, and the worse one is what gets reviewed |

### The mechanics worth getting right

- **Annual on top, monthly below.** The default option is the one most
  people take, and annual is both better revenue and better retention.
- **Show the price.** A paywall that hides the number until the last
  screen is a paywall people leave. Trust converts.
- **One screen.** A paywall carousel is a paywall you are apologising for.
- **Restore purchases must be visible.** Apple requires it, and its
  absence generates one-star reviews that cost more than the design.
- **Trials:** short trials pull revenue forward and cost long-term
  conversion. Do not shorten a trial to make a quarter look better.
- **Ask at the good moment**, the same way you ask for a review: after
  something worked, never after an error and never on launch.

### Offers, which most small apps never use

- **Win-back offers** for lapsed subscribers, configured in App Store
  Connect and shown by the App Store itself
- **Offer codes** for press, newsletters and communities, which are far
  better than free promo codes because they still create a subscriber
  relationship
- **Promotional offers** for people already in the funnel
- **Family Sharing**, which is a conversion feature dressed as a
  technicality: for a household utility it can be the reason somebody
  buys

---

## RETENTION WITHOUT NAGGING

Notifications for a utility should be **events, not reminders**.

- "Your delivery is two stops away" is an event. "You have not opened
  Clack in three days" is a message about your needs, not theirs.
- If you genuinely have nothing timely to say, do not ask for the
  permission at all. An unused notification permission is a prompt spent
  for nothing.
- **Live Activities** for anything with a duration. **App Intents and
  Shortcuts** to become part of somebody's automation, which is very hard
  to churn out of. **Control Center and the Action Button** for one press
  from anywhere.

The best retention for a utility is not a notification. It is being
present without being opened, which is the visible surface again, which
is also the loop. Build the widget.

---

## WHAT TO DO, IN ORDER

1. Name the activation event and measure how many installs reach it
2. Remove whatever stands between the install and that event
3. Build the visible surface, and make it distinctive rather than merely
   useful
4. Make the export one action, and make it carry its origin
5. Make the shared link work for somebody with no app
6. Put the paywall after the activation event, annual first, price shown
7. Turn on win-back offers, which take an afternoon and run forever
